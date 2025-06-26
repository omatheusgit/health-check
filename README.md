# Health Check DevOps

Este projeto foi criado para resolver um desafio de conhecimento e testar habilidades em:

- Python
- Leitura de variáveis com `.env`
- Organização de código em módulos
- Registro em log (`log.txt`)
- Automatização com GitHub Actions

A ideia é simples: verificar se determinadas URLs estão online e registrar o resultado.

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
