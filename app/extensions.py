# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-3-19 上午9:57
@Desc :
'''
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor
from flask_moment import Moment
from flask_share import Share

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
share = Share()
