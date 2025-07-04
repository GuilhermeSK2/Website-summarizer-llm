# Sumarizador de Sites com LLM Local e Docling

Este projeto Python demonstra uma pipeline para resumir o conteúdo de uma página web utilizando um Large Language Model (LLM) executado localmente via Ollama. Ele integra `requests` e `BeautifulSoup` para extração de conteúdo, `Docling` para conversão de documentos e `TokenCount` para estimativa de tokens, antes de enviar o texto para sumarização pelo LLM.

## Visão Geral

Sumarizar conteúdo da web de forma automatizada pode ser muito útil para rapidamente entender o principal de um site. Este projeto aborda essa tarefa com os seguintes passos:
1.  **Extração de Conteúdo:** Faz uma requisição HTTP para obter o HTML de um site.
2.  **Limpeza e Análise:** Usa `BeautifulSoup` para extrair o texto limpo da página HTML.
3.  **Contagem de Tokens:** Estima o número de tokens no texto extraído, o que é útil para gerenciar custos e limites de LLMs.
4.  **Conversão de Documento (Docling):** Converte o conteúdo do site em um formato Markdown estruturado, o que pode melhorar a qualidade da sumarização pelo LLM.
5.  **Sumarização com LLM Local:** Envia o texto processado para um LLM (Llama3:8b via Ollama) para gerar um resumo conciso.

## Estrutura do Projeto

* `html_test.py`: O script Python principal que orquestra todas as etapas.
* `.env`: Arquivo para variáveis de ambiente (necessário para `load_dotenv`, embora não seja explicitamente usado no exemplo fornecido para API keys).

## Tecnologias Utilizadas

* **Python 3**
* **`requests`**: Para fazer requisições HTTP.
* **`BeautifulSoup` (`bs4`)**: Para parsing e extração de dados de HTML.
* **`docling`**: Para conversão e estruturação de documentos.
    * `Docling Document Converter`: Uma biblioteca externa que precisa ser instalada.
* **`langchain-ollama`**: Integração do LangChain com LLMs executados via Ollama.
* **`python-dotenv`**: Para carregar variáveis de ambiente.
* **Ollama**: Servidor local para execução de LLMs.
* **Llama3:8b**: Modelo de linguagem grande (LLM) executado via Ollama.
* `token_count`: (Assumido como uma biblioteca auxiliar ou local para contagem de tokens, pois `gpt-3.5-turbo` é referenciado no seu código como `model_name` para `TokenCount`).

## Pré-requisitos

1.  **Instale o Ollama:** Siga as instruções de instalação em [https://ollama.com/](https://ollama.com/).
2.  **Baixe o modelo Llama3:8b:** Abra seu terminal e execute:
    ```bash
    ollama pull llama3:8b
    ```
    Certifique-se de que o servidor Ollama esteja em execução em segundo plano.
3.  **Instale a biblioteca `Docling`:** Para instalar a biblioteca `Docling`, você pode precisar de um token de acesso ou seguir as instruções de instalação específicas fornecidas pelo Docling. Geralmente, seria algo como:
    ```bash
    pip install docling
    # Ou siga as instruções no site oficial do Docling para instalação.
    ```

## Saída Esperada

O script imprimirá:
* O número de tokens estimado para o conteúdo do site.
* O resumo gerado pelo LLM (Llama3:8b) do site especificado na variável `source`.

## Configuração

* **`source`**: Altere a URL na variável `source` no arquivo `html_test.py` para o site que você deseja resumir.
* **`model_name`**: Na linha `llm = OllamaLLM(model="llama3:8b")`, você pode mudar `llama3:8b` para qualquer outro modelo que esteja executando no seu Ollama (e.g., `mistral`, `gemma:2b`).
* **`prompt`**: Modifique o prompt para o LLM para ajustar o formato ou o comprimento do resumo.
