i=1
while i<100:
    if i%2==0 and i%5==0:
        print(i , "evenfive")
    elif i%2==0 and i%5!=0:
        print(i , "even")
    elif i%5==0 and i%2!=0:
        print(i , "five")
    else:
        print(i)
    i=i+1