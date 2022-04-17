from flask_restx import Api

from .sessionService import api as session_management
from .accountService import api as account_management

api = Api(
    title='ECRA Endpoints',
    version='1.0',
    description='To test the configuration settings',
)

api.add_namespace(session_management)
api.add_namespace(account_management)
