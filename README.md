# CHAT GPT SERVICE
Project is a bot GPT for build learning path.
You can use AI bot of Open AI build some your favorite

Prerequisites

Before you continue, ensure you meet the following requirements:

* You have installed the version 3.11 of python.
* You are using a Linux or Mac OS machine. Windows with wsl or docker.
* You have a basic understanding of python, fastapi, chatgpt, g4f.
## Development with venv
1. Install python version 3.11 (recommend 3.11.6)

2. Run script create venv
```cmd
python3.11 -m venv venv
```
3. Active venv
```cmd
# activate
source ./venv/bin/activate
```
```cmd
# deactivate
deactivate
```

4. Run app
```cmd
make dev
```

## Development with docker
1. Build docker and library
```cmd
make build
```

2. Run app
```cmd
make run
```
