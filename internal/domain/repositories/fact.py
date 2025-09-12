from internal.domain.entities.fact import Fact

class FactRepository:
    def get_random_fact(self) -> Fact:
        raise NotImplementedError
    
    def add_fact(self, fact_text: str) -> Fact:
        raise NotImplementedError
