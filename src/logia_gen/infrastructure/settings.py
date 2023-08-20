from configparser import ConfigParser
import os

from logia_gen.application.definitions import ConfigFiles



class Settings:
    def __init__(self, config_folder: str, config_file: ConfigFiles) -> None:
        self._config = ConfigParser()

        config_filepath = os.path.join(config_folder, config_file.value)
        self._config.read(config_filepath)

    def load_settings(self):
        raise NotImplementedError