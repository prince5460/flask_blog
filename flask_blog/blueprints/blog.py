# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/3/18 下午10:05
@Desc :
'''
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/about')
def about():
    return 'The about page'


@blog_bp.route('/category/<int:category_id>')
def category(category_id):
    return 'The category page'
