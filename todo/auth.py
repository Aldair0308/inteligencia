import functools
from flask import (
    Blueprint, flash, render_template, request, session, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash


from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Encriptar la contraseña antes de guardarla en la base de datos
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        db, c = get_db()
        c.execute(
            'INSERT INTO user (username, password) VALUES (%s, %s)',
            (username, hashed_password.decode('utf-8'))
        )
        db.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')



import bcrypt
from flask import request, render_template, redirect, url_for, flash
from .db import get_db  # Asumiendo que tienes get_db en otro archivo

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None

        # Verifica si el usuario existe
        sql = "SELECT * FROM user WHERE username = %s"
        c.execute(sql, (username,))
        user = c.fetchone()

        if user is None:
            error = "Usuario no encontrado."
        else:
            # Obtener el hashed password desde la base de datos
            hashed_password = user['password']

            # Verificar la contraseña usando bcrypt
            if bcrypt.checkpw(password.encode(), hashed_password.encode()):
                # Contraseña correcta, puedes iniciar sesión
                flash('Inicio de sesión exitoso')
                return redirect(url_for('index'))  # Cambia esto según tu lógica de redirección
            else:
                error = "Contraseña incorrecta."

        if error:
            flash(error)

    return render_template('auth/login.html')




