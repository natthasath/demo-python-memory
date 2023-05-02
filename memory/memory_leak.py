import random

class MemoryLeak:
    def __init__(self):
        self.data = []

    def generate_data(self):
        for i in range(100000):
            self.data.append(random.randint(1, 100))

    def clear_memory(self):
        self.data = []