class ArrayBinTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root == None:
            self.root = ArrayBinTree()
            self.size = 1
            return True

        if value < self.root:
            self.insert(value)
            return True

    def search(self, value):
        if self.root == None:
            return False
