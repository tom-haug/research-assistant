from langchain.prompts import ChatPromptTemplate

SUMMARY_TEMPLATE = """{text}

---

Using the above text, answer in short the following question:

> {question}

---

if the question cannot be answered using the text, imply summarize the text. Include all factual information, numbers, stats etc.
"""

summary_prompt = ChatPromptTemplate.from_template(SUMMARY_TEMPLATE)