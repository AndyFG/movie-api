# -*- coding: utf-8 -*-
from flask_script.commands import Server
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db, models

app = create_app('development')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("runserver", Server(threaded=True))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
