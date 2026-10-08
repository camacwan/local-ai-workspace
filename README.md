# Local AI Workspace: Rodando, Otimizando e Integrando LLMs no Hardware Pessoal

Guia prático e arquitetural para configurar um ambiente de Inteligência Artificial totalmente local, garantindo **privacidade de dados, zero custo com APIs e controle total de infraestrutura**.

---

## Stack Tecnológica
* **Motor de Inferência / Servidor:** LM Studio / `llama.cpp` (compatível com a API da OpenAI).
* **Modelos Base:** Qwen (Série 2.5 / 1.5) otimizados via quantização (GGUF).
* **Integração Backend:** Python, `openai` client (configurado para localhost) e FastAPI.
* **Hardware de Teste:** Otimizado para GPUs dedicadas com boa alocação de VRAM.

---

## Arquitetura da Solução

```text
[ Sua Aplicação Python / FastAPI ]
              │
              ▼ (Requisição HTTP via OpenAI Client)
     [ http://localhost:1234/v1 ]
              │
              ▼
    [ LM Studio / llama.cpp (Servidor Local) ]
              │
              ▼
   [ Hardware Pessoal (GPU VRAM + RAM) ]