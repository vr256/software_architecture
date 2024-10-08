from abc import ABCMeta, abstractmethod
from typing import List
from ...entities import TimeTracking

class ITimeTracking_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection) -> List[TimeTracking]:
        '''
        Should return list of users,
        activities and time spent on them
        '''

    @abstractmethod
    def find_by_user_id(self, connection, user_id : int) -> List[TimeTracking]:
        '''
        Should return list of activities 
        and time spent on them by given user
        '''

    @abstractmethod
    def find_by_activity_id(self, connection, activity_id : int) -> List[TimeTracking]:
        '''
        Should return list of users and 
        time spent by them on given activity
        '''

    @abstractmethod
    def find_by_action_id(self, connection, action_id : int) -> List[TimeTracking]:
        '''
        Should return list of users and 
        activities with given action
        '''

    @abstractmethod
    def insert(self, connection, time_trackings : List[TimeTracking]):
        '''
        Should insert given list of users,
        activities and time spent on them
        '''

    @abstractmethod
    def update(self, connection, time_trackings : List[TimeTracking]):
        '''
        Should update given list of users,
        activities and time spent on them
        '''

    @abstractmethod
    def delete(self, connection, time_trackings : List[TimeTracking]):
        '''
        Should delete given list of users,
        activities and time spent on them
        '''