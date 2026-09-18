# COMPOSITION
class Nucleus:
    def __init__(self):
        print("Nucleus created")
    def __del__(self):
        print("Nucleus is gone")

class Mitochondria:
    def __init__(self):
        print("Mitochondria created")
    def powerTheCell(self):
        print("Mitochondria is providing energy")
    def __del__(self):
        print("Mitochondria is gone")

class Cell:
    def __init__(self):
        print("Cell created")
        self.nucleus = Nucleus()
        self.mitochondria = Mitochondria()
    def exist(self):
        print("Cell is existing")
        self.mitochondria.powerTheCell()
    def __del__(self):
        del self.nucleus
        del self.mitochondria
        print("Cell is gone")

cellAtWork = Cell()
cellAtWork.exist()
del cellAtWork
