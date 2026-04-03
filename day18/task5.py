i=int(input("enter any number: "))
while i!=0:
    if i%2==0 and i%3==0:
        print("good")
    elif i%2==0 and i%3!=0:
        print("two")
    elif i%3==0 and i%2!=0:
        print("three")
    else:
        print("none")
    i=int(input("enter anu number: "))