import os.path as op
import requests
from flask_sqlalchemy import SQLAlchemy
from app.blueprints.blueprint import blueprint_api
from config import app_config
from flask import Flask, render_template

db = SQLAlchemy()


def create_app(app_name):
    root_path = op.join(op.dirname(__file__), '../')
    static_folder = op.join(root_path, 'static')
    template_folder = op.join(root_path, 'templates')

    app = Flask(app_name, root_path=root_path, static_folder=static_folder, template_folder=template_folder)

    app.config.from_object(app_config[app_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_pyfile('config.py')

    db.init_app(app)

    app.register_blueprint(blueprint_api, url_prefix='/api')

    @app.route('/', methods=['GET'])
    def main(**kwargs):
        """ Test Phase 2 """

        try:
            u = 'https://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey=%s&chart_name=top'
            response = requests.get(u % '445d6196c08dc2b7490929f18149d684')

            kwargs.update({'tracks': response.json().get('message').get('body').get('track_list')})

            return render_template('main.html', **kwargs)

        except AttributeError:
            raise Exception('Key Error', 406)
        except Exception:
            raise Exception('Error', 500)

    return app
