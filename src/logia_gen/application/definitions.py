from enum import Enum


class PlatformExecutor(Enum):
    LOCAL = "local"
    COLAB = "colab"
    KAGGLE = "kaggle"


class ConfigFiles(Enum):
    REPOSITORY = "repository.cfg"