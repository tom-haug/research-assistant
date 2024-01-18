from langchain.utilities import DuckDuckGoSearchAPIWrapper

RESULTS_PER_QUESTION = 3

ddg_search = DuckDuckGoSearchAPIWrapper()

def web_serach(query: str, num_results: int = RESULTS_PER_QUESTION):
  results = ddg_search.results(query, max_results=num_results)
  return [result["link"] for result in results]
