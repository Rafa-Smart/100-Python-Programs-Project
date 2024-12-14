n = 5
for i in range(1,n+1,+1):
    print("*"*i)

print()
for i in range(n ,0,-1):
    print("*"*i)

print()

for i in range(n):
    for j in range(n -i -1):
        print(" ",end='')
    for k in range(2 * i + 1):
        print("*",end='')
    print()


print()
for i in range(n):
    for j in range(i):
        print(" ",end='')
    for k in range(2 * (n - i - 1) + 1):
        print("*",end='')
    print()
