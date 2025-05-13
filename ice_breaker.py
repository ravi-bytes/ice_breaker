import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("Hello from Langchain!")
    # print(os.environ["OPENAI_API_KEY"])

    summary_template = """
    Given the LinkedIn information {information} about a person, I want you to generate:
    1. A short summary of the person
    2. Two interesting facts about the person
    3. A question to ask the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # llm = ChatOpenAI(
    #     temperature=0,
    #     model="gpt-3.5-turbo",
    # )
    # llm = ChatOllama(model="llama3")
    llm = ChatOllama(model="mistral")

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/raviiyer/", mock=True)
    print("--" * 20)
    # print(linkedin_data)
    print("--" * 20)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
    # if isinstance(res, AIMessage):
    #     content = res.content
    #     parts = content.split('\n\n')
    #     for part in parts:
    #         print(part.strip())
    #         print("-" * 20)
    #         print()
    # else:
    #     print(f"Error: 'res' is not an AIMessage object. Its type is: {type(res)}")
    #     print(f"The object itself is: {res}")
