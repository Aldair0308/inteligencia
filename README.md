# inteligencia

# comandos a ejecutar para echar a andar el proyecto en local:

# Prepara tu bash cli:

- sudo apt update
- sudo apt install python3-venv
- pip install Flask
- pip install mysql-connector-python
- pip install bcrypt

# Crear el entorno virtual

- python3 -m venv venv

# Activar el entorno virual

- source venv/bin/activate

# Exporta la aplicacion

- export FLASK_APP=todo/**init**.py

# Asignalo como development

- export FLASK_ENV=development

# Activa el debug mode

- export FLASK_DEBUG=1
