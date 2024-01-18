from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from helpers.text_scraper import scrape_text
from helpers.web_search import web_serach
from helpers.utils import collapse_list_of_lists
from prompts.summary_prompt import summary_prompt
from prompts.search_prompt import search_prompt
from prompts.report_prompt import research_report_prompt
import json

load_dotenv()

scrape_and_summarize_chain = RunnablePassthrough.assign(
    summary=RunnablePassthrough.assign(text=lambda x: scrape_text(x["url"])[:10000])
    | summary_prompt
    | ChatOpenAI(model="gpt-3.5-turbo-1106")
    | StrOutputParser()
) | (lambda x: f"URL: {x['url']}\n\nSUMMARY: {x['summary']}")

web_search_chain = (
    RunnablePassthrough.assign(urls=lambda x: web_serach(x["question"]))
    | (lambda x: [{"question": x["question"], "url": url} for url in x["urls"]])
    | scrape_and_summarize_chain.map()
)

search_question_chain = (
    search_prompt
    | ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
    | StrOutputParser()
    | json.loads
)

full_research_chain = (
    search_question_chain
    | (lambda x: [{"question": q for q in x}])
    | web_search_chain.map()
)

report_chain = (
    RunnablePassthrough.assign(
        research_summary=full_research_chain | collapse_list_of_lists
    )
    | research_report_prompt
    | ChatOpenAI(model="gpt-3.5-turbo-1106")
    | StrOutputParser()
)
