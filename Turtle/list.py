l = ["suman"]
l.append("PalisettY")
print(l)
l.insert(0, "hammer")
print(l)
l.remove("suman")
print(l)
print("sorting")
l.sort(reverse=True)
print(l)

newlist = [1, 2, 3, 4]
to_be_added = [5, 6, 7, 8]
for i in to_be_added:
    newlist.append(i)
print(newlist)