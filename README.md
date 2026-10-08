
```
# Local AI Workspace: Rodando, Otimizando e Integrando LLMs no Hardware Pessoal

Guia prático, arquitetural e avançado para configurar um ambiente de Inteligência Artificial totalmente local, garantindo **privacidade de dados, zero custo com APIs e controle total de infraestrutura**.

---

## Stack Tecnológica & Ecossistema

- **Motor de Inferência / Servidor:** LM Studio / `llama.cpp` (expondo uma API REST compatível com o padrão OpenAI).
- **Modelos Base:** Família **Qwen** (Série 2.5 / 1.5) otimizados para código, lógica e língua portuguesa.
- **Backend & Interface:** Python, SDK `openai` (cliente HTTP local), FastAPI e **Streamlit** (para interfaces de chat web).
- **Hardware & Otimização:** Configurações focadas em maximizar o uso de VRAM de GPUs dedicadas (ex: arquiteturas NVIDIA RTX com suporte a CUDA/Tensor Cores).
-** Spec Usada:** Ryzen 7 5700x | 32GB RAM | RTX 3080 12GB

---

## Arquitetura da Solução

``` Estrutura
[ Interface Web (Streamlit) ou Script Python ]
                    │
                    ▼ (Requisição HTTP via OpenAI Client)
           [ http://localhost:1234/v1 ]
                    │
                    ▼
          [ LM Studio / llama.cpp (Servidor Local) ]
                    │
                    ▼
         [ Hardware Pessoal (GPU VRAM + RAM) ]

```

---

## Passo a Passo de Configuração

### 1. Configurando o Servidor Local (LM Studio)

* **1.1** Instale o LM Studio na sua máquina.
* **1.2** Na aba de busca, baixe um modelo eficiente da família Qwen em formato GGUF.
* **1.3** **Otimização de VRAM (GPU Offload):** Ajuste o slider para descarregar o máximo de camadas na placa de vídeo, garantindo alta velocidade de geração (tokens/sec).
* **1.4** Inicie o servidor local na porta padrão `http://localhost:1234`.

---

## 2. Estrutura do Projeto

```
local-ai-workspace/
├── .gitignore
├── README.md
├── requirements.txt
└── src/
    ├── app.py          # Script de automação via terminal
    └── web_chat.py     # Interface de chat interativa no navegador

```

---

## 3. Códigos de Exemplo (src/app.py)

```
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

```


---

## Criando um Chat no Navegador com Streamlit (src/web_chat.py)

Para rodar uma interface visual de chat no seu navegador:

```
import streamlit as st
from openai import OpenAI

st.title("💬 Meu ChatGPT Local (Privado & Offline)")
st.caption("Rodando com Qwen via LM Studio & OpenAI SDK")

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Olá! Como posso te ajudar hoje?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = client.chat.completions.create(
        model="qwen-local-model",
        messages=st.session_state.messages
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

```

> **Para rodar no navegador, execute no terminal:**
> `streamlit run src/web_chat.py`

---

## Aprofundamento: Otimização, Quantização e Fine-Tuning

* **Quantização GGUF:** Comprime os pesos do modelo para rodar em placas de vídeo comuns sem perder capacidade lógica.
* **Fine-Tuning Local:** Abordagens como QLoRA (usando bibliotecas como Unsloth ou PEFT) permitem adaptar modelos utilizando bases de dados proprietárias diretamente na VRAM do seu computador.

