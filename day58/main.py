# 1) https://www.codewars.com/kata/5a03b3f6a1c9040084001765
def angle(n): return (n-2)*180

# 2) https://www.codewars.com/kata/55d1d6d5955ec6365400006d
def round_to_next5(n):
    while n%5!=0:
        n=n+1
    return n

# 3) https://www.codewars.com/kata/57a049e253ba33ac5e000212
def factorial(n):
    i=1
    res=1
    while i<=n:
        res=res*i
        i=i+1
    return res

# 4) https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
def row_weights(array):
    first=[]
    second=[]
    for i in range(len(array)):
        if i%2==0:
            first.append(array[i])
        else:
            second.append(array[i])
    return (sum(first) , sum(second))

# 5) https://www.codewars.com/kata/59a96d71dbe3b06c0200009c
def generate_shape(n): return "\n".join(["+"*n]*n)

# 6) https://www.codewars.com/kata/556196a6091a7e7f58000018
def largest_pair_sum(numbers): 
    largest1=max(numbers)
    numbers.remove(largest1)
    largest2=max(numbers)
    return largest1+largest2 

# 7) https://www.codewars.com/kata/59377c53e66267c8f6000027
def alphabet_war(fight):
    left_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left_score = 0
    right_score = 0
    for i in fight:
        if i in left_side:
            left_score=left_score+left_side[i]
        elif i in right_side:
            right_score=right_score+right_side[i]
    if left_score>right_score:
        return "Left side wins!"
    elif right_score>left_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"
    
# 8) https://www.codewars.com/kata/57f759bb664021a30300007d
def switcheroo(s):
    ret=""
    for i in s:
        if i=="a":
            ret=ret+"b"
        elif i=="b":
            ret=ret+"a"
        else:
            ret=ret+i
    return ret

# 9) https://www.codewars.com/kata/544a54fd18b8e06d240005c0
def find_smallest(numbers, to_return):
    min_index=numbers.index(min(numbers))
    if to_return=="value":
        return min(numbers)
    else:
        return min_index