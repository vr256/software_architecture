# App
APP_VERSION = '1.1'
DBMS = 'MySQL'

# Logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
LOG_PATHES = {
    'time_tracking.services.admin_service' : 'time_tracking/logs/admin.txt',
    'time_tracking.services.auth_service' : 'time_tracking/logs/auth.txt',
    'time_tracking.tools.connector' : 'time_tracking/logs/general.txt',
    'time_tracking.models.DAO.MDAO.maction_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.DAO.MDAO.mactivity_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.DAO.MDAO.mcategory_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.DAO.MDAO.mrole_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.DAO.MDAO.mtime_tracking_dao' : 'time_tracking/logs/DB.txt',
    'time_tracking.models.DAO.MDAO.muser_dao' : 'time_tracking/logs/DB.txt',
}

# DB config
POOL_SIZE = 5
POOL_NAME = 'pool'
DB_CONFIG = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'time_tracking_db'
}

# Routing
ROUTES = {
    '': '',
}

ROLES = {
    'user': 1, 
    'admin': 2,
}


VALIDATORS = {
    'login': r'^[A-Za-z_]{1}\w{,15}$', 
    'password': r'^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[A-Z]).{8,16}$',
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
}