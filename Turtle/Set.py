se = set()
print(se)
s1 = {"a", 3, "b", True}
print(s1)
s1.add("c")
print(s1)
s1.add("as")
s1.add(3)
s1.add(2)
print(s1)
li = list(s1)
print(li)
s1 = {"a", "b", "c", "d", "e", "f", "g"}
s2 = {"b", "c", "j"}
print(s1.union(s2))
print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1.difference(s2))
print(s2.difference(s1))