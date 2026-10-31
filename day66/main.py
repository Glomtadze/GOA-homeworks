# 1 -https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    result=""
    for i in str(num):
        result=result+str(int(i)**2)
    return int(result)
# 2 - https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    new_l=[]
    for i in range(len(l)):
        if type(l[i])!=str:
            new_l.append(l[i])
    return new_l

# 3 - https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
def get_middle(s):
    if len(s)%2==0:
        return s[(len(s)//2)-1:(len(s)//2)+1]
    else:
        return s[len(s)//2]

# 4 - https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string):
    string=string.lower()
    return len(string)==len(set(string))

# 5 - https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
def xo(s):
    s=s.lower()
    return s.count('x')==s.count('o')
