# General modules
from flask import Flask
import os


# Custom modules
from config_reader import server_settings

from .handlers import home_blueprint
from .handlers import root_blueprint


# Main server class
class Server:
    def __init__(self, port, host) -> None:
        self.host = host
        self.port = port



    # Some Initializations
    def serverInitialise(self) -> None:
        """This function initialises a static server class. It does not require any arguments."""
        self.app = Flask(__name__)

    
    def foldersInitialise(self) -> None:
        template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "global"))
        static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "global", "assets"))

        self.app.template_folder = template_folder
        self.app.static_folder = static_folder

    
    def handlerInitialise(self) -> None:
        self.app.register_blueprint(home_blueprint)
        self.app.register_blueprint(root_blueprint)


    # Run Function
    def run(self) -> None:
        self.app.run(
            host=self.host,
            port=self.port
        )


# Server variable initializate
server = Server(
    host = server_settings.host.get_secret_value(),
    port = server_settings.port.get_secret_value()
)