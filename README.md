# OpenAI Assistant FastAPI

First create the new virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then install the requirements:

```bash
pip install -r requirements.txt
```

## Add the environment variables

Use `.env.example` as a template to create a `.env` file

```bash
cp .env.example .env
```

Then edit the `.env` file and add the required values.


## Run the server

```bash
python main.py --env local --debug
```
## Formatting with Black

```bash
black .
```

## Linting with Pylint

Install extension for VSCode: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylint

Linting with Pylint CLI
```bash
pylint src
```
