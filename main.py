import logging
from flask import Flask
from api.views import bp_api
from exceptions.exceptions import DataSourceError
from posts.views import posts

logging.basicConfig(filename='basiclog.log', level=logging.INFO)


def create_and_config_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(posts)
    app.register_blueprint(bp_api, url_prefix="/api")
    app.config.from_pyfile(config_path)
    return app


app = create_and_config_app("config.py")


@app.errorhandler(404)
def page_error_404(error):
    return f"No such page, {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"Error on server side - {error}", 500


@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f"Error on site broken data", 500


if __name__ == "__main__":
    app.run()
