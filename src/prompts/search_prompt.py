from langchain.prompts import ChatPromptTemplate

search_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "user",
            "Write 3 google search queries to search online that form an "
            "objective opinion from the following: {question}\n"
            "You must respond with a list of strings in the following format: "
            '["query 1", "query 2", "query 3"].',
        )
    ]
)