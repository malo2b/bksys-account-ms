# bksys_account_ms

Account Micro Service

## Setup project

requirements:
- python 3.11
- poetry

### Install dependencies and load environment
```
poetry install && poetry shell
```

### Run application for development
```
uvicorn bksys_account_ms:app --reload --port 8082
```

## Lint project
```
poetry run flake8
```