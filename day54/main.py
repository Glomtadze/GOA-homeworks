# 1) https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    total = 0
    for stop in bus_stops:
        total=total+stop[0]-stop[1]
    return total

# 2) https://www.codewars.com/kata/52fba66badcd10859f00097e
def disemvowel(string_):
    for i in string_:
        if i in "aeiouAEIOU":
            string_ = string_.replace(i,'')
    return string_

# 3) https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string):
    string=string.lower()
    return len(string)==len(set(string))

# 4) https://www.codewars.com/kata/56747fd5cb988479af000028
def get_middle(s):
    if len(s)%2==0:
        return s[(len(s)//2)-1:(len(s)//2)+1]
    else:
        return s[len(s)//2]
    
# 5) https://www.codewars.com/kata/55908aad6620c066bc00002a
def xo(s):
    s=s.lower()
    return s.count('x')==s.count('o')

# 6) https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
def accum(s):
    result=[]
    for i in range(len(s)):
        a=s[i]
        b=a.upper()+(a.lower()*i)
        result.append(b)
    return "-".join(result)

# 7) https://www.codewars.com/kata/55b42574ff091733d900002f
def friend(x):
    friends=[]
    for i in x:
        if len(i)==4:
            friends.append(i)
    return friends

# 8) https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
def reverse_words(text): return " ".join(word[::-1] for word in text.split(" "))

# 9) https://www.codewars.com/kata/539ee3b6757843632d00026b
def capitals(word):
    result=[]
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result

# 10) https://www.codewars.com/kata/580a4734d6df748060000045
def is_sorted_and_how(arr):
    if arr==sorted(arr):
        return "yes, ascending"
    elif arr==sorted(arr,reverse=True):
        return "yes, descending"
    else:
        return "no"