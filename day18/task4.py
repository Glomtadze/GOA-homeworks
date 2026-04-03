negative=0
positive=0
number=int(input("enter any number: "))
for i in range(9):

    if number>0:
        positive=positive+1
    else:
        negative=negative+1
    number=int(input("enter any number: "))

print("დადებითია ",positive )
print("უარყოფითია ",negative)