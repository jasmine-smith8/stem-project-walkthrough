from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository

class VoteFactUseCase:
    def __init__(self, repository: FactRepository):
        self.repository = repository

    def vote_fact(self, fact_id: int, vote_type: str) -> Fact:
        if vote_type not in ['like', 'dislike']:
            raise ValueError("Invalid vote type")
        
        updated_fact = self.repository.vote_fact(fact_id, vote_type)
        return updated_fact