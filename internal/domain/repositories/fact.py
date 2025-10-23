from internal.domain.entities.fact import Fact

class FactRepository:
    def get_fact(self) -> Fact:
        pass
    
    def create_fact(self, fact_text: str, category: str) -> Fact:
        pass
