from abc import ABC, abstractmethod

class ChatDatabase(ABC):

    @abstractmethod
    def add_interaction(self):
        pass

    @abstractmethod
    def delete_interaction(self, id:int):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def get_interaction(self, id:int):
        pass

    @abstractmethod
    def get_all(self):
        pass