from flask import render_template, request, redirect
from apps.user import user_bp
from apps.user.model import User
from ext import db

users = []


@user_bp.route('/')
def user():
    return render_template('user/show.html', users=users)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'


@user_bp.route('/logout')
def logout():
    return 'logout'


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            for item in users:
                if item.username == username:
                    return render_template('user/register.html', msg='用户已存在')
            user = User()
            user.username = username
            user.password = password
            user.phone = phone

            db.session.add(user)
            db.session.commit()
            return redirect('/')
    return render_template('user/register.html')
