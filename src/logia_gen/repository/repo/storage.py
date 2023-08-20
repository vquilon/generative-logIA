import logging
import os
from logia_gen.application.project import LogiaGenProject

from logia_gen.repository.definitions import RepoType, StorageType
from logia_gen.repository.driver.local import (
    FileSystemDriver, GoogleDriveDriver, KaggleDatasetDriver)
from logia_gen.repository.repo.abstract import RepositoryAbstract
from logia_gen.repository.settings import RepoSettings

logger = logging.getLogger(__name__)


class StorageSettings(RepoSettings):
    def __init__(self, logia_gen_project: LogiaGenProject):
        super().__init__(logia_gen_project, RepoType.STORAGE)

    def load_settings(self):
        super().load_settings()
        self.storage_type = self._settings["storage_type"]
        self.storage_settings = self._settings["storage_settings"]


class StorageRepo(RepositoryAbstract):
    def __init__(self, logia_gen_project: LogiaGenProject, storage_type: StorageType):
        self.storage_type = storage_type
        if storage_type == StorageType.FILE_SYSTEM:
            driver = FileSystemDriver()
        elif storage_type == StorageType.GOOGLE_DRIVE:
            driver = GoogleDriveDriver()
        elif storage_type == StorageType.KAGGLE_DATASET:
            driver = KaggleDatasetDriver()
        else:
            raise ValueError(f"Storage type '{storage_type}' is not supported.")

        self._storage_settings = StorageSettings(logia_gen_project)

        super().__init__(driver)

    def save_file(self, file_path: str, file_name: str = None) -> None:
        logger.debug(f"Saving file '{file_path}'")
        self.driver.save_file(file_path, file_name=file_name)

    def save_folder(self, folder_path: str, folder_name: str = None) -> None:
        logger.debug(f"Saving folder '{folder_path}'")
        self.driver.save_folder(folder_path, folder_name=folder_name)

    def save(self, path: str, name: str) -> None:
        if os.path.isfile(path):
            self.save_file(path, name)
        elif os.path.isdir(path):
            self.save_folder(path, name)
        else:
            raise ValueError(f"Path '{path}' is not a file or a folder.")
