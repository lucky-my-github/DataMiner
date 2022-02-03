import os  # help us to manage all the  operations
import json

def _get_absolute_path(relative_path):
    #find the pass with the directory name
    script_path = os.path.dirname(__file__)  #absolute path to the script
    abs_path = os.path.join(script_path, relative_path)

    return abs_path

class Settings:
    #the goal is to keep track different configurations
    _all_configs = None   #this is the class variable instead of the instance varable
    _file = "./config.json"
    def __init__(self):
        self.config = Settings._all_configs

        self.load()

    #load the instance
    def load(self):
        # load the file only once
        if Settings._all_configs is not None:
            return
        #open the file
        with open(self._file) as config_file:
            self.config = json.loads(config_file.read())
            Settings._all_configs = self.config

    def get_repository_file_path(self):
        return _get_absolute_path(self.config["repository_file"])

    def get_output_foder_path(self):
        return _get_absolute_path(self.config["output_folder"])

