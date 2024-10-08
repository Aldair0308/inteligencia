import os
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # Configuración con valores por defecto en el código
    app.config.from_mapping(
        SECRET_KEY='mykey',
        DATABASE_HOST='localhost',
        DATABASE_PASSWORD='',
        DATABASE_USER='root',
        DATABASE='todo',
    )

    app.config['DEBUG'] = True  # Ahora puedes configurar el modo de depuración


    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/hola')
    def hola():
        return 'Esto es un mensaje para Axel'
    
    @app.route('/welcome')
    def welcome():
        return render_template('welcome.html')

    return app
