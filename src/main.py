from web_researcher import report_chain

if __name__ == "__main__":
  output = report_chain.invoke({
    "question": "What is the difference between Langsmith and langchain?"
  })

  print(output)
