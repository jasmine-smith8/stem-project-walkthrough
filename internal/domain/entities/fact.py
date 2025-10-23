class Fact:
    def __init__(self, id: int, fact: str, category: str ):
        self.id = id
        self.fact = fact
        self.category = category

    def __repr__(self):
        return f"<Fact id={self.id} fact='{self.fact}' category='{self.category}'>"
