import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=api_key,
            model_name="llama-3.3-70b-versatile"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of website.
            Extract the job postings and return them in JSON format 
            containing the following keys: `role`, `experience`, `skills`, and `description`.
            Only return valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke({"page_data": cleaned_text})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")

        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Mohan, a business development executive at AtliQ. AtliQ is an 
            AI & Software Consulting company dedicated to automation and efficiency. 

            Write a cold email to the client regarding the job, describing AtliQ's capability.  
            Add the most relevant ones from the following links to showcase AtliQ's portfolio: {links_list}

            Remember: You are Mohan, BDE at AtliQ.  
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "links_list": links})
        return res.content
