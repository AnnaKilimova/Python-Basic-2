a = [1, 2, 3, 4, 5, 6]
# a = [1, 2, 3]
# a = [1, 2, 3, 4, 5]
# a = []

d = []

if len(a) % 2 != 0:
    border = int((len(a) - 1) / 2 + 1)
else:
    border = int(len(a) / 2)

b = a[:border:]
c = a[border::]
d.append(b)
d.append(c)
print(d)