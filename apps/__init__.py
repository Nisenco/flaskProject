from flask import Flask

import settings

from apps.user import user_bp
from ext import db


def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevConfig)
    db.init_app(app)  # 将 SQLAlchemy 与 app 关联
    # 注册用户登录蓝图
    app.register_blueprint(user_bp)
    return app
