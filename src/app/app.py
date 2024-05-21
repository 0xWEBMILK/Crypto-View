# General modules
from flask import Flask
import logging
import os


# Custom modules
from config_reader import server_settings

from .handlers import home_blueprint
from .handlers import root_blueprint


logging.basicConfig(level=logging.INFO)

# Main server class
class Server:
    def __init__(self, port: str, host: str) -> None:
        """
        Initialize the Server object with port and host information.
        
        Args:
            port (int): Port number to run the server.
            host (str): Host address to run the server.
        """
        
        self.logger = logging.getLogger('ServerLogger')
        self.host = host
        self.port = port


    def server_initialise(self) -> None:
        """
        Initialize the Flask application within the server object. 
        
        This method initializes the Flask application object within the server instance. 
        The Flask application is used to handle HTTP requests and responses.
        """

        self.app = Flask(__name__)
        self.logger.info('Flask application initialized')

    
    def folders_initialise(self) -> None:
        """
        Initialize template and static folders for the Flask application.
        """

        template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "global"))
        static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "global", "assets"))

        self.app.template_folder = template_folder
        self.app.static_folder = static_folder
        self.logger.info('Template and static folders initialized')

    
    def handler_initialise(self) -> None:
        """
        Register blueprint routes with the Flask application.
        """
        self.app.register_blueprint(home_blueprint)
        self.app.register_blueprint(root_blueprint)
        self.logger.info('Blueprints registered')


    def run(self) -> None:
        """
        Run the Flask application with specified host and port.
        """

        try:
            self.logger.info(f'Starting server at {self.host}:{self.port}')
            self.app.run(
                host=self.host,
                port=self.port
            )
        except Exception as e:
            self.logger.error(f'Error running the server: {e}')


# Server variable initializate
server = Server(
    host = server_settings.host.get_secret_value(),
    port = server_settings.port.get_secret_value()
)