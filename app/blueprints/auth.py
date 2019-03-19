# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/3/18 下午10:05
@Desc :
'''
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'The login page'


@auth_bp.route('/logout')
def logout():
    return 'logout'
