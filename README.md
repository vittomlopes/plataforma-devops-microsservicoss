# 🚀 Plataforma DevOps Microsserviços

Este repositório contém uma arquitetura base de microsserviços desenvolvida em Python (Flask) para fins de demonstração de práticas de DevOps, CI/CD e conteinerização.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Framework:** Flask
* **Testes:** Pytest
* **CI/CD:** GitHub Actions
* **Conteinerização:** Docker & Docker Compose

## 📁 Estrutura do Projeto

O projeto está dividido nos seguintes diretórios e serviços:

* **`.github/workflows/`**: Configurações de automação do pipeline de CI.
* **`order-service/`**: Microsserviço responsável pelo gerenciamento de pedidos.
* **`product-service/`**: Microsserviço responsável pelo catálogo de produtos.
* **`user-service/`**: Microsserviço responsável pela gestão de usuários.

---

## 🚀 Como Executar o Projeto

### 🐳 Via Docker Compose (Recomendado)

Para subir todos os microsserviços simultaneamente de forma isolada, execute:

```bash
docker-compose up --build
```

### 💻 Execução Local (Manual)

Se preferir rodar um serviço específico localmente:

1. Acesse a pasta do serviço desejado:
   ```bash
   cd user-service
   ```
2. Instale as dependências:
   ```bash
   pip install -r ../requirements.txt
   ```
3. Inicie a aplicação:
   ```bash
   python app.py
   ```

---

## 🧪 Como Rodar os Testes

O pipeline de Integração Contínua (CI) valida os testes automaticamente a cada push na `main`. Para rodar localmente:

```bash
pytest
```

---

## 👥 Contribuidores

* **Vitor Lopes** ([@vittomlopes](https://github.com))
