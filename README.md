##  Como Rodar o Backend Localmente (Passo a Passo)

Siga os comandos abaixo no terminal (utilizando Git Bash ou terminal de sua preferência) para preparar o ambiente e rodar a API.

### 1. Navegação de Pastas
Para garantir que você está executando os comandos no lugar certo, acesse a pasta do backend a partir da raiz do projeto:
```bash
cd back

source ../.venv/Scripts/activate

pip install -r requirements.txt

pip install python-dotenv

uvicorn app.main:app --reload

Resultado final deve ser proximo a isso:
Quando o terminal exibir a mensagem INFO: Application startup complete, a API estará online e respondendo em:

URL Local: http://127.0.0.1:8000

Documentação Swagger (Testar Rotas): http://127.0.0.1:8000/docs
