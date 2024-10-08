from abc import ABCMeta, abstractmethod
from typing import List, Union
from ...entities import Activity

class IActivity_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection) -> List[Activity]:
        '''
        Should return list of activities
        '''

    @abstractmethod
    def find_by_name(self, connection, name : str) -> Union[Activity, bool]:
        '''
        Should return activity with given name 
        or False if no such activity found
        '''

    @abstractmethod
    def insert(self, connection, activities : List[Activity]):
        '''
        Should insert given list of activities
        '''

    @abstractmethod
    def update(self, connection, activities : List[Activity]) -> None:
        '''
        Should update given list of activities
        '''

    @abstractmethod
    def delete(self, connection, activities : List[Activity]) -> None:
        '''
        Should delete given list of activities 
        '''