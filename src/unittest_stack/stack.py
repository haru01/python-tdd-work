class Stack(object):
    def __init__(self, capacity=10):
        self.nodes = []

        self.capacity = capacity

    def size(self):
        return len(self.nodes)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

    def push(self, node):
        if self.is_full():
            raise FullStackError("スタックが満杯のためpushできません")
        self.nodes.append(node)

    def pop(self):
        if self.is_empty():
            raise EmptyError("スタックが空のためpopできません")
        return self.nodes.pop()

    def __str__(self):
        return "<Stack:" + str(self.nodes) + ">"


class EmptyError(Exception):
    pass


class FullStackError(Exception):
    pass
