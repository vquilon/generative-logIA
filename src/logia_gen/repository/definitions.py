from enum import Enum

class StorageType(Enum):
    FILE_SYSTEM = "local"
    GOOGLE_DRIVE = "gdrive"
    KAGGLE_DATASET = "kaggle_dataset"

class RepoType(Enum):
    STORAGE = "storage"

