negative=0
positive=0
i=int(input("enter any number: "))
while i!=0:
    if i>0:
        positive=positive+1
    elif i<0:
        negative=negative+1 
    i=int(input("enter any number: "))
if i==0:
     print("დადებითი" ,positive , "უარყოფით" , negative)
   

