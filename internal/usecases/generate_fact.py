from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository

class RandomFactService:
    def __init__(self, repository: FactRepository):
        self.repository = repository

    def generate(self) -> Fact:
        return self.repository.get_random_fact()
    
    def create(self, fact_text: str) -> Fact:
        return self.repository.add_fact(fact_text)
    
    def like_fact(self, fact_id: int) -> None:
        self.repository.increment_likes(fact_id)

    def dislike_fact(self, fact_id: int) -> None:
        self.repository.increment_dislikes(fact_id)
