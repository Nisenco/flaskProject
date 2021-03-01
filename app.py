from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.model import User

from apps import creat_app
from ext import db

app = creat_app()
manager = Manager(app)
# 命令工具
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


@manager.command
def init():
    print('初始化')


if __name__ == '__main__':
    manager.run()
