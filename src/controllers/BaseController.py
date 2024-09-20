from helpers.config import get_settings, Settings
import os
import random
import string

class BaseController:
    
    def __init__(self):

        self.app_settings = get_settings()
        #os.path.dirname(__file__ ) return direct of current file(base_controller) ,full line will return path of controller
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
        
    def generate_random_string(self, length: int=12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
