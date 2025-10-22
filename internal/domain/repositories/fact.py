from internal.domain.entities.fact import Fact

class FactRepository:
    def get_random_fact(self) -> Fact:
        raise NotImplementedError
    
    def add_fact(self, fact_text: str) -> Fact:
        raise NotImplementedError
    
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