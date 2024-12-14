list = ["apple","mangga","jambu"]

i = 0
while i < len(list):
    print(list[i])
    i += 1

for no,n in enumerate(list):
    print(f"{no+1} = {n}")










list = ["apple","mangga","jambu"]

for no,i in enumerate(list):
    print(no+1,"=",i)


no = 1
while no < len(list):
    print(f"{no} = {list[no]}")
    no += 1