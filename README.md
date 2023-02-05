## Setting up the env

### Requirements

- Python 3.10
- Poetry

### Installing Dependencies

Note: Activate your custom virtual environment before running the below command. Otherwise poetry will automatically
create one.

```bash
poetry install
```

### Setting up pre-commit

[What is pre-commit?](https://pre-commit.com/)

```bash
pre-commit install --hook-type pre-push
pre-commit install --hook-type pre-commit
```

### Running the app

Run this at the repo root after activating the virtual env with the installed dependencies.
Make sure to make a `.env` file or populate the required Environment Variables.

```bash
python -m ango_auth
```
