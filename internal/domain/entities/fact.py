class Fact:
    def __init__(self, id: int, fact: str):
        self.id = id
        self.fact = fact

    def __repr__(self):
        return f"<Fact id={self.id} fact='{self.fact}'>"
