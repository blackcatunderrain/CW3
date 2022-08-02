import logging
from flask import Flask
from posts.views import posts

logging.basicConfig(filename='basiclog.log', level=logging.INFO)


def create_and_config_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(posts)
    app.config.from_pyfile(config_path)
    return app


app = create_and_config_app("config.py")

if __name__ == "__main__":
    app.run()
