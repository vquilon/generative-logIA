from abc import ABC, abstractmethod
from logia_gen.repository.driver.abstract import DriverAbstract

class RepositoryAbstract(ABC):
    def __init__(self, driver: DriverAbstract) -> None:
        self.driver = driver