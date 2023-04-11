import logging
import re

from flask import current_app as app
from ..tools import encrypt, singleton, Connection_Factory, DAO_Factory
from ..properties import LOG_FORMAT, LOG_PATHES, ROLES, VALIDATORS, ERRORS
from ..models import User

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class AuthService:
    def get_role(sefl, role_id : int):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_role = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('role')
                role = dao_role.find_by_id(cnx, role_id)
                return role.name_role
        except Exception:
            logging.exception('')

    def get_by_creds(self, credentials : str):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                user_by_login = dao_user.find_by_login(cnx, credentials)
                user_by_email = dao_user.find_by_email(cnx, credentials)
                if user_by_login:
                    return user_by_login
                return user_by_email
        except Exception:
            logging.exception('')

    def get_last(self):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                return dao_user.find_last(cnx)
        except Exception:
            logging.exception('')

    def check_password(self, password : str, user : User):
        return encrypt(password, user.login) != user.password
    
    def check_accessibility(self, login : str, email : str):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                user_by_login = dao_user.find_by_login(cnx, login)
                user_by_email = dao_user.find_by_email(cnx, email)
                if user_by_login:
                    return 'REG_NAME'
                if user_by_email:
                    return 'REG_EMAIL'
        except Exception:
            logging.exception('')

    def sign_up(self, login : str, email : str, password: str):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                current_id = self.get_last().user_id
                user = User(user_id=current_id + 1, login=login, email=email, \
                            password=encrypt(password, login), role_id=ROLES['user'])
                dao_user.insert(cnx, [user])
                return user
        except Exception as e:
            print(e)
            logging.exception('')

    def validate_data(self, data : str, dtype : str):
        is_valid = re.fullmatch(VALIDATORS[f'{dtype}'], data)
        return True if is_valid else ERRORS[f'INVALID_{dtype.upper()}']
    
    def check_data(self, login : str, email : str, password: str):
        login_validity = self.validate_data(login, 'login')
        if login_validity != True:
            return login_validity
        
        email_validity = self.validate_data(email, 'email')
        if email_validity != True:
            return email_validity
        
        password_validity = self.validate_data(password, 'password')
        if password_validity != True:
            return password_validity
        
        return True
