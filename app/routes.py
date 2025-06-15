from flask import render_template, request, flash, redirect, url_for
from app import app
import re


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/about')
def about():
    return render_template('about.html', title='О нас')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        errors = False

        if not name:
            flash('Пожалуйста, введите ваше имя', 'error')
            errors = True
        if not email:
            flash('Пожалуйста, введите ваш email', 'error')
            errors = True
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Пожалуйста, введите корректный email', 'error')
            errors = True
        if not message:
            flash('Пожалуйста, введите ваше сообщение', 'error')
            errors = True

        if not errors:
            flash('Ваше сообщение успешно отправлено!', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html', title='Контакты')