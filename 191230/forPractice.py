limit = 1000
multipleOf = 23


for i in range(limit):
    if(i%multipleOf==0):
        print(i)

multipleOf = 2
for i in range(limit):
    if(i%multipleOf!=0):
        print(i)
