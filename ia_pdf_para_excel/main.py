import os
from llama_parse import LlamaParse


os.environ["LLAMA_CLOUD_API_KEY"] = "suachaveaqui"


documentos = LlamaParse(
  result_type="markdown",
  parsing_instruction="this file contains text and tables, I'd like to get only the tables from the text."
).load_data("resultado.pdf")


for i, pagina in enumerate(documentos):
  with open(f"meu_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
    arquivo.write(pagina.text)


# print(len(documentos))

# https://cloud.llamaindex.ai/project/d1ddc6d2-47b4-4a28-902f-aad148e03463/api-key
