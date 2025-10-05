from abc import ABC, abstractmethod
from agent_api.schemas.interaction_schema import Interaction
from agent_api.schemas.chat_session_schema import ChatSession

class ChatDatabase(ABC):

    @abstractmethod
    def add_interaction(self, intercation:Interaction):
        pass

    @abstractmethod
    def add_session(self, chat_session:ChatSession):
        pass

    @abstractmethod
    def update_session(self, chat_session:ChatSession):
        pass

    @abstractmethod
    def delete_interaction_by_id(self, id:int):
        pass

    @abstractmethod
    def delete_all_by_session_id(self, session_id:int):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def get_interaction_by_id(self, id:int):
        pass

    @abstractmethod
    def get_all_by_session_id(self, session_id:int):
        pass

    @abstractmethod
    def get_all(self):
        pass