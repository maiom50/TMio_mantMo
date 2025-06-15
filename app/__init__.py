from flask import Flask

app = Flask(__name__)
app.secret_key = 'ваш_очень_сложный_секретный_ключ_тут'

from app import routes