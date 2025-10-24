from internal.domain.entities.fact import Fact

class FactRepository:
    def get_fact(self) -> Fact:
        pass
    
    def create_fact(self, fact_text: str, category: str) -> Fact:
        pass
    
    def increment_likes(self, fact_id: int) -> None:
        raise NotImplementedError
    
    def increment_dislikes(self, fact_id: int) -> None:
        raise NotImplementedError
    
    def get_likes_count(self, fact_id: int) -> int:
        raise NotImplementedError

    def get_dislikes_count(self, fact_id: int) -> int:
        raise NotImplementedError

    def get_fact_by_id(self, fact_id: int) -> Fact:
        raise NotImplementedError

