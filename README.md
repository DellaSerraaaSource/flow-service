# 🚀 Flow-Service

API construída com **FastAPI** e **Poetry**, projetada para extrair ações de fluxos da plataforma **BLiP**, permitindo a visualização de ações de entrada, saída e conteúdo.  
A resposta pode ser formatada opcionalmente de acordo com o protocolo **MCP (Message Context Protocol)**, facilitando a integração com LLMs e agentes inteligentes.

---

## 📦 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [Poetry](https://python-poetry.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- JSON-RPC 2.0 (padrão MCP)

---

## 📁 Estrutura do projeto

```
flow-service/
├── pyproject.toml
├── README.md
└── src/
    └── app/
        ├── core/             # Armazena o fluxo atual em memória
        ├── models/           # Schemas Pydantic
        ├── services/         # Extração de ações e formatação MCP
        ├── routes/           # Rotas: /import, /leaving, /entering, /content
        └── main.py           # Instância FastAPI
```

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/flow-service.git
   cd flow-service
   ```

2. Instale com Poetry:
   ```bash
   poetry install
   ```

---

## ▶️ Execução local

Inicie a API com reload automático:

```bash
poetry run uvicorn app.main:app \
  --reload \
  --app-dir src \
  --reload-dir src/app
```

Acesse em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📮 Endpoints

### POST `/import`

Importa o fluxo BLiP (em formato JSON):

```bash
curl -X POST http://localhost:8000/import \
  -H "Content-Type: application/json" \
  -d @fluxo.json
```

---

### GET `/leaving/{action}`  
### GET `/entering/{action}`  
### GET `/content/{action}`

Retorna todas as ações de determinado tipo:

```bash
curl http://localhost:8000/leaving/SetVariable
```

Com resposta MCP:

```bash
curl "http://localhost:8000/leaving/SetVariable?mcp=true&id=abc123"
```

---

## 📦 Formato da resposta MCP

```json
{
  "jsonrpc": "2.0",
  "id": "abc123",
  "method": "flow.leaving.SetVariable",
  "params": {
    "data": [ ... ]
  }
}
```

---

## 🧪 Exemplo de fluxo JSON (`fluxo.json`)

```json
{
  "flow": {
    "bloco1": {
      "$title": "Bloco de Teste",
      "$leavingCustomActions": [
        {
          "type": "SetVariable",
          "settings": {
            "variable": "email",
            "value": "teste@example.com"
          }
        }
      ]
    }
  }
}
```

---

## 🤝 Contribuições

1. Fork este repositório
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'feat: adiciona nova funcionalidade'`
4. Push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é distribuído sob a licença MIT.  
Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---
