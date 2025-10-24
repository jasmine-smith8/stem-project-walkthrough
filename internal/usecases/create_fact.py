from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository

class CreateFactUseCase:
    def __init__(self, repository: FactRepository):
        self.repository = repository

    def create_fact(self, fact_text: str, category: str) -> Fact:
        return self.repository.create_fact(fact_text, category)
