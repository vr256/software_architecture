from abc import ABCMeta, abstractmethod
from typing import List, Union
from .. import *
from ...connector import IConnection

class IUser_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection : IConnection) -> List[User]:
        '''
        Should return list of users
        '''

    @abstractmethod
    def find_by_login(self, connection : IConnection, login : str) -> Union[User, bool]:
        '''
        Should return user with given login 
        or False if no such user found
        '''

    @abstractmethod
    def find_by_email(self, connection : IConnection, email : str) -> Union[User, bool]:
        '''
        Should return user with given email 
        or False if no such user found
        '''

    @abstractmethod
    def insert(self, connection : IConnection, users : List[User]):
        '''
        Should insert given list of users
        '''

    @abstractmethod
    def update(self, connection : IConnection, users : List[User]):
        '''
        Should update given list of users
        '''

    @abstractmethod
    def delete(self, connection : IConnection, users : List[User]):
        '''
        Should delete given list of users and 
        '''