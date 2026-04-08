N=int(input("enter any number: "))
i=1
count=0
while i<N:
    if i%3==0:
        count=count+1
    i=i+1
print(count)