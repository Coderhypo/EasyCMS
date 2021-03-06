# coding=utf-8

from ..models import User

# 根据ID获取用户
def get_user_by_id(userId):

    user = User.query.filter_by(user_id=userId).first()
    return user

# 根据邮箱获取用户
def getUserByEmail(Email):

    user = User.query.filter_by(user_email=Email).first()
    return user

# 根据登录名获取用户
def getUserByLoginName(loginName):

    user = User.query.filter_by(user_login=loginName).first()
    return user

# 根据权限获取用户组
def getUsersByRule(userRule):

    user = User.query.filter_by(user_rule=userRule).all()
    return user

# 获取全部用户
def get_all_user(page=1, num=5):

    pagination = User.query.paginate(
        page, per_page=num
    )
    return pagination
