# 1) https://www.codewars.com/kata/57f8ff867a28db569e000c4a

# 2) https://www.codewars.com/kata/52b757663a95b11b3d00062d
def to_weird_case(string):
    res=[]
    index=0
    for i in string:
        if i==' ':
            res.append(' ')
            index=0
        else:
            if index%2==0:
                res.append(i.upper())
            else:
                res.append(i.lower())
            index=index + 1
    return ''.join(res)

# 3) https://www.codewars.com/kata/54e6533c92449cc251001667
def unique_in_order(sequence):
    res=[]
    for i in sequence:
        if len(res)==0 or i!=res[-1]:
            res.append(i)
    return res

# 4) https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n):
    count=0
    while n>=10:
        product=1
        for i in str(n):
            product=product*int(i)
        n=product
        count=count+1
    return count

# 5) https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    n=len(names)
    if n==0:
        return "no one likes this"
    elif n==1:
        return names[0]+" likes this"
    elif n==2:
        return names[0]+" and "+names[1]+" like this"
    elif n==3:
        return names[0]+", "+names[1]+" and "+names[2]+" like this"
    else:
        other=n-2
        return names[0]+","+names[1]+"and "+str(other)+"others like this"
# 6) https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
        
# 7) https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
def duplicate_count(text):
    text=text.lower()
    count=[]
    duplicates=0
    for i in text:
        if text.count(i)>1 and i not in count:
            count.append(i)
            duplicates=duplicates+1
    return duplicates