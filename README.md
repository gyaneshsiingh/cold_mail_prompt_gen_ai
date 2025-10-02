#Cold Mail Generator

Cold Mail Generator is a Streamlit web application that automates the process of generating personalized cold emails for job opportunities. The app extracts job descriptions from career pages, identifies required skills, and generates tailored cold emails highlighting your company’s capabilities and portfolio.

Features

URL Input: Provide a link to a job posting (e.g., Amazon Jobs).

Job Extraction: Automatically extracts job role, required skills, experience, and description from the webpage.

Portfolio Integration: Queries your portfolio of projects to suggest relevant work in the email.

Cold Email Generation: Generates professional cold emails tailored to the job requirements.

Streamlit Interface: Easy-to-use web interface for generating emails quickly.

Tech Stack

Frontend: Streamlit

Backend / LLM: Groq’s ChatGroq LLM via LangChain Groq integration

Vector Database: ChromaDB for portfolio project storage and retrieval

Data Processing: Pandas for CSV management

Web Scraping: LangChain WebBaseLoader

Environment Management: Python + .env configuration

Installation

Clone the repository

git clone https://github.com/yourusername/cold-mail-generator.git
cd cold-mail-generator


Create a virtual environment and activate it

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Set environment variables in .env file:

GROQ_API_KEY=your_valid_groq_api_key
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36


Create your portfolio CSV at Resources/my_portfolio.csv:

Techstack,Links
Python,https://github.com/yourrepo/python
React,https://github.com/yourrepo/react

Usage

Run the Streamlit app:

python -m streamlit run main.py


Open the app in your browser (default URL: http://localhost:8501).

Enter a job URL (e.g., Amazon Jobs).

Click Submit to generate cold emails.

The app will display the generated emails in Markdown format.

Project Structure
cold-mail-generator/
│
├─ main.py                # Streamlit app entry point
├─ chains.py              # LLM chain for job extraction & email generation
├─ portfolio.py           # Portfolio vector storage & query using ChromaDB
├─ utils.py               # Utility functions (e.g., clean_text)
├─ Resources/
│   └─ my_portfolio.csv   # Portfolio CSV (Techstack + links)
├─ vectorstore/           # ChromaDB persistent storage
└─ .env                   # Environment variables (API key, USER_AGENT)

Notes

Ensure your Groq API key has access to the model used (llama-3.3-70b-versatile or a valid accessible model).

If you see a USER_AGENT warning, set it in .env as shown above.

If my_portfolio.csv is missing, create it as shown above.

License

This project is licensed under the MIT License.
