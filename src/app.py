from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="not-needed-for-local"
)

def perguntar_ao_modelo(prompt: str):
    try:
        response = client.chat.completions.create(
            model="qwen-local-model",
            messages=[
                {"role": "system", "content": "Você é um assistente sênior de engenharia de dados e backend."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro de conexão: {e}"

if __name__ == "__main__":
    print(perguntar_ao_modelo("Explique as vantagens de usar SQLAlchemy com FastAPI."))