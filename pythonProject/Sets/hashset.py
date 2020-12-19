
class MyHashSet:
    def __init__(self):
        self.l = []

def add(self, key: int) -> None:
    if key not in self.l:
        self.l.append(key)

def remove(self, key: int) -> None:
    if key in self.l:
        self.l.remove(key)

def contains(self, key: int) -> bool:
    return key in self.l

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(3)
obj.add(2)
obj.add(1)
obj.remove(2)
param_3 = obj.contains(3)