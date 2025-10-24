from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository

class GetFactUseCase:
    def __init__(self, repository: FactRepository):
        self.repository = repository

    def get_fact(self) -> Fact:
        return self.repository.get_fact()