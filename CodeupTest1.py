#21
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
#22
s = input()
print(s[0:2], s[2:4], s[4:])
#23
s = input().split(":")
print(s[1])
#24
w1, w2 = input().split()
s = w1 + w2
print(s)
#25
a, b = input().split()
c = int(a) + int(b)
print(c)
#26
a = input()
b = input()
b = float(b)
a = float(a)
c = b + a
print(c)
#31
c = int(input())
print(chr(c))
#32
n = int(input())
print(-n)
#33
c = input()
n = ord(c)+1
print(chr(n))
#34
a, b = input().split()
c = int(a) - int(b)
print(c)
#35
a, b = input().split()
m = float(a) * float(b)
print(m)
#36
w, n = input().split()
print(w*int(n))
#37
n = input()
s = input()
print(int(n)*s)
#38
a,b = input().split()
c = int(a) ** int(b)
print(c)