from flask import render_template, request, redirect, url_for
from models.user import User, db

class UserController:
    # A chamada para esse método seria feita diretamente pela classe, sem a necessidade de criar um objeto (uma instância):
    @staticmethod
    def list_users():
        users = User.query.all()
        return render_template('users.html', users=users)

    @staticmethod
    def create_user():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            # validações simples: se usuário já existe no db, etc

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('list_users'))

        return render_template('create_user.html')