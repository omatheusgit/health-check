# Desafio DevOps: Health Check

Este projeto foi criado para resolver um desafio de conhecimento e testar habilidades.

A ideia é simples: utilizando Health Check Automático com Python e GitHub Actions, desenvolva uma automação cujo objetivo é:

> Criar um script em Python que verifica a saúde de serviços (HTTP) e que pode ser executado manualmente ou testado via GitHub Actions.

---

## Como usar

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/health-check-devops.gitcd health-check-devops
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Edite o arquivo `.env` e adicione suas URLs:

```
URLS=https://alura.com.br,https://github.com
```

4. Execute o script:

```
python check_health.py
```

O resultado será exibido no terminal e gravado no arquivo `log.txt`.

---

## GitHub Actions

O projeto inclui um workflow (`.github/workflows/healthcheck.yml`) que pode ser executado manualmente via GitHub.
Existe também uma linha comentada que permite configurar a execução automática (por exemplo, a cada 1 hora), caso deseje ativar no futuro.

---

## Observações

- O arquivo `.env` está incluído de propósito, pois contém apenas URLs públicas.
- O `log.txt` é gerado localmente. Você pode ignorá-lo no versionamento, se quiser.
