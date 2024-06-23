a = input()
b = []
for i in a:
    b.append(i)
if b[::1] == b[::-1]:
    print("YES")
else:
    print("NO")
