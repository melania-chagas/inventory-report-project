from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, path_file):
        raise NotImplementedError
