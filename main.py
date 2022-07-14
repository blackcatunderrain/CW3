import logging
from flask import Flask
from view import main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

logging.basicConfig(filename='basiclog.log', level=logging.INFO)

app.run()
