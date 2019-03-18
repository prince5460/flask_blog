# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/3/18 下午10:00
@Desc :
'''
import os

from flask import Flask

from flask_blog.blueprints.admin import admin_bp
from flask_blog.blueprints.auth import auth_bp
from flask_blog.blueprints.blog import blog_bp
from flask_blog.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    app = Flask('flask_blog')
    app.config.from_object(config[config_name])

    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
