from abc import ABC, abstractmethod

class DriverAbstract(ABC):
    ...


class StorageDriverAbstract(DriverAbstract):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def save_file(self, file_path: str, file_name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def save_folder(self, folder_path: str, folder_name: str) -> None:
        raise NotImplementedError
