import os

DB_ENGINE = 'postgres'
DB_USER = os.environ['DB_USER']
DB_SECRET = os.environ['DB_SECRET']
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
ADMIN_RESOURCES_JWT_SECRET = os.environ['ADMIN_RESOURCES_JWT_SECRET']
API_VERSION = 'v1'
SERVICE_NAME = 'user_identity_service'
SERVICE_SECRET = os.environ['SERVICE_SECRET']
DB_CONN_STRING = f'{DB_ENGINE}://{DB_USER}:{DB_SECRET}@{DB_HOST}/{DB_NAME}'
SERVER_IDENTITY_SERVICE_HOST = os.environ['SERVER_IDENTITY_SERVICE_HOST']
SERVER_IDENTITY_SERVICE_PORT = os.environ['SERVER_IDENTITY_SERVICE_PORT']
SERVER_IDENTITY_SERVICE_PATH = os.environ['SERVER_IDENTITY_SERVICE_PATH']
SERVER_IDENTITY_URL = \
    f'{SERVER_IDENTITY_SERVICE_HOST}:{SERVER_IDENTITY_SERVICE_PORT}/' \
    f'{SERVER_IDENTITY_SERVICE_PATH}'
DISCOVERY_SERVICE_HOST = os.environ['DISCOVERY_SERVICE_HOST']
DISCOVERY_SERVICE_PORT = os.environ['DISCOVERY_SERVICE_PORT']
DISCOVERY_SERVICE_PATH = os.environ['DISCOVERY_SERVICE_PATH']
DISCOVERY_URL = \
    f'{DISCOVERY_SERVICE_HOST}:{DISCOVERY_SERVICE_PORT}/' \
    f'{DISCOVERY_SERVICE_PATH}'