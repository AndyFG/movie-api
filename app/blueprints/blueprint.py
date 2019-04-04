from flask import Blueprint
from flask_restless import APIManager


class BlueprintAPI(Blueprint):
    def register(self, app, options, first_registration=False):
        from app.models import Movie, Artist, Genre, db

        super(BlueprintAPI, self).register(app, options, first_registration)

        api_manager = APIManager(app=app, flask_sqlalchemy_db=db)

        api_manager.create_api(
            model=Movie,
            collection_name='movie',
            methods=['POST', 'GET', 'DELETE', 'PATCH']
        )

        api_manager.create_api(
            model=Artist,
            collection_name='artist',
            methods=['POST', 'GET', 'DELETE', 'PATCH']
        )

        api_manager.create_api(
            model=Genre,
            collection_name='genre',
            methods=['POST', 'GET', 'DELETE', 'PATCH']
        )


blueprint_api = BlueprintAPI('blueprint_api', __name__)
