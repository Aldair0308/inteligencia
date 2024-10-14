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

<!-- PLANTILLA DE SCREENS DE HTML -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenido</title>

    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">

</head>
<body>
    <div class="container">
        {% include 'drawer.html' %}
        <div class="content">
            <div>
                <h1>Bienvenido al Panel de Control</h1>
                <p>Selecciona una opción del menú para ver el contenido aquí.</p>
            </div>
        </div>
    </div>
</body>
</html>
