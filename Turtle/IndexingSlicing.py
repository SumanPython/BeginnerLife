digits = [0, 11, 21, 31, 41, 5, 6, 7, 8, 9]
print(digits[::-1])
print(digits[1: 6: 1])
print(digits[6: 1: -1])
print(digits[9: 4: -1])
print(digits[:])
print(digits[0:3])
st = "suman"
print(st[0:4])
print(digits[0: -1])
print(digits[0: -7])
print(digits[0: ])
print(digits[::-3])
print(digits[::4])
print(digits[::-2])
print(digits[5:0:-2])
for i in range(1, len(digits)-2):
    print(digits[-1: -len(digits): -1])
for i in range(len(digits)):
    print(digits[i: i+3])
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
window_size = 5
for i in range(0, len(digits) -4):
    print(digits[i:i + window_size])







