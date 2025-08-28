from internal.domain.entities.fact import Fact
from internal.domain.repositories.fact import FactRepository

class RandomFactService:
    def __init__(self, repository: FactRepository):
        self.repository = repository

    def generate(self) -> Fact:
        return self.repository.get_random_fact()
