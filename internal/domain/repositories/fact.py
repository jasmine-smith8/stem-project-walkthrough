from internal.domain.entities.fact import Fact

class FactRepository:
    def get_random_fact(self) -> Fact:
        raise NotImplementedError
