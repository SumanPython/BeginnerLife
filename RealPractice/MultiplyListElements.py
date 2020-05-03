class MultiplyListElements:
    l = [1, 2, 3]
    nl = []
    def __init__(self, n):
        self.n = n
    def multipliedlist(self):
        nl = [nl * self.n for nl in self.l]
        print(nl)
m = MultiplyListElements(4)
m.multipliedlist()