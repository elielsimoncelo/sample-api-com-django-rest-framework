# sample-api-com-django-rest-framework

### Instalação
- [python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

### Ambiente virtual

#### Criando o ambiente virtual
```sh
cd sample-api-com-django-rest-framework
python -m venv ./venv
```

#### Ativar o ambiente virtual
- MAC e Linux
```sh
source venv/bin/activate
```

- Windows (prompt)
```sh
venv\Scripts\activate.bat
```

#### [INFO] DESATIVAR o ambiente virtual
- MAC e Linux
```sh
deactivate
```

- Windows (prompt)
```sh
deactivate
```

### O projeto

#### Instalação das bibliotecas
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

### Iniciar o projeto localmente
```sh
cd sample-api-com-django-rest-framework
python ./src/manage.py runserver
```

### [INFO] Comandos utilizados no projeto

#### Comando utilizado para criar o projeto com django
```sh
cd sample-api-com-django-rest-framework
django-admin startproject setup .
```

#### Comando utilizado para criar uma nova aplicação com django
```sh
cd sample-api-com-django-rest-framework
python manage.py startapp app
```
