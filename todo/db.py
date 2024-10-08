import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

def get_db():
    if 'db' not in g:
        try:
            g.db = mysql.connector.connect(
                host=current_app.config['DATABASE_HOST'],
                user=current_app.config['DATABASE_USER'],
                password=current_app.config['DATABASE_PASSWORD'],
                database=current_app.config['DATABASE'],            
            )
            g.c = g.db.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            raise

    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db, c = get_db()

    try:
        for instruction in instructions:
            c.execute(instruction)
        
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error executing instructions: {err}")
        db.rollback()  # Revert any changes if an error occurs

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
