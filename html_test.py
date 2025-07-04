from bs4 import BeautifulSoup
import requests
from token_count import TokenCount
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
# Docling
from docling.document_converter import DocumentConverter


source = "https://www.guilhermesk2.site/"

# Faz a a requisição HTTP para obter o conteúdo da página
response = requests.get(source)

response.content

soup = BeautifulSoup(response.content, 'html.parser')
tc = TokenCount(model_name="gpt-3.5-turbo")
print(tc.num_tokens_from_string(soup.get_text()))



converter = DocumentConverter()
result = converter.convert(source)

load_dotenv()
llm = OllamaLLM(model="llama3:8b")

prompt = """
    Resuma este site para mim, em até 100 caracteres, em português.
    {text}
"""

docling_txt = result.document.export_to_markdown()
print(llm.invoke(prompt.format(text=docling_txt)))
