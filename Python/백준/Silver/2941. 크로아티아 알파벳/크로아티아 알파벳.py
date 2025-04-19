w = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia:
    w = w.replace(i, "0")
print(len(str(w)))