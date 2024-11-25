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

    # Clave de OpenAI

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    
        
    @app.route('/')
    def welcome():
        return render_template('welcome.html')
    
    @app.route('/inicio')
    def inicio():
        return render_template('inicio.html', current='home')
    
    @app.route('/ingresar')
    def hola():
        return render_template('base.html', current='ingresar')
    
    @app.route('/ajustes')
    def ajustes():
        return render_template('ajustes.html', current='ajustes')
    
    @app.route('/sopa')
    def sopa():
        return render_template('sopa.html', current='sopa')
    
    @app.route('/imagen')
    def imagen():
        return render_template('imagen.html', current='imagen')
    

    return app
