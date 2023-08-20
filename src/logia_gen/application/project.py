import os
from logia_gen.application.definitions import PlatformExecutor

from logia_gen.repository.definitions import StorageType


class LogiaGenProject:
    config_folder = "config"
    tokens_folder = "tokens"

    def __init__(self,
        project_name: str = "logia_generative",
        work_dir: str = None,
        config_folder: str = None, tokens_folder: str = None,
        platform_executor: PlatformExecutor = PlatformExecutor.LOCAL,
        storage_input_type: StorageType = StorageType.FILE_SYSTEM,
        storage_output_type: StorageType = StorageType.FILE_SYSTEM
    ):
        self.work_dir = work_dir or self.get_working_directory()

        self.config_folder = config_folder or self.config_folder
        self.tokens_folder = tokens_folder or self.tokens_folder

        self.platform_executor = platform_executor

        self.storage_input_type = storage_input_type
        self.storage_output_type = storage_output_type

    def get_working_directory(self) -> str:
        return os.getcwd()

    def get_absolute_path(self, relative_path: str) -> str:
        return os.path.join(self.work_dir, relative_path)
    
    def get_config_path(self, relative_path: str) -> str:
        return self.get_absolute_path(relative_path)