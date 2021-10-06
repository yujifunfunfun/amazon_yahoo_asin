


s = str(4530107941518)[3:12]
a = 10
c = 0

for i in range(0, len(s)):
    c += int(s[i]) *(a-i)

d = c % 11
d = 11 - d 
if d == 10:
    d = "X"

print(str(s) + str(d))