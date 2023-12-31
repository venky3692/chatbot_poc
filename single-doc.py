from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader

load_dotenv('.env')

pdf_loader = PyPDFLoader('./docs/LS-28591 Memo.pdf')
documents = pdf_loader.load()

chain = load_qa_chain(llm=OpenAI())
query = 'Who is the Gokul and where is he from?'
response = chain.run(input_documents=documents, question=query)
print(response)