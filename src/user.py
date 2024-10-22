class User:
    def __init__(self, name: str):
        self.name = name
        self.emotional_states = []

    def add_emotional_state(self, emotional_state):
        self.emotional_states.append(emotional_state)