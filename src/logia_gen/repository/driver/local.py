from logia_gen.repository.driver.abstract import StorageDriverAbstract


class FileSystemDriver(StorageDriverAbstract):
    def __init__(self) -> None:
        super().__init__()

    def save_file(self, file_path: str, file_name: str) -> None:
        pass

    def save_folder(self, folder_path: str, folder_name: str) -> None:
        pass