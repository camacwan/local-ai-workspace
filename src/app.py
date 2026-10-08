from openai import OpenAI

# Configura o cliente apontando para o servidor local do LM Studio / llama.cpp
# O LM Studio roda na porta 1234 por padrão e simula a API da OpenAI
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed-for-local"
)

def perguntar_ao_modelo(prompt: str):
    print(sending... f"Enviando prompt para a IA local: '{prompt}'\n")
    try:
        response = client.chat.completions.create(
            model="qwen-local-model", # Nome livre ou o modelo carregado no LM Studio
            messages=[
                {"role": "system", "content": "Você é um assistente sênior de engenharia de dados e backend."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro de conexão: Certifique-se de que o servidor local está rodando. Detalhes: {e}"

if __name__ == "__main__":
    pergunta_teste = "Explique em 3 tópicos práticos por que utilizar FastAPI em projetos de backend voltados a dados."
    
    resposta = perguntar_ao_modelo(pergunta_teste)
    
    print("=== Resposta da IA Local ===")
    print(resposta)