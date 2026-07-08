# N1-Powers of 2-https://www.codewars.com/kata/57a083a57cb1f31db7000028
def powers_of_two(n):
    count=[]
    for i in range(n+1):
        count.append(2**i)
    return count

# N2-Reversed Wordshttps://www.codewars.com/kata/51c8991dee245d7ddf00000e
def reverse_words(s):
    words=s.split()
    words.reverse()
    return " ".join(words)

# N3-L1: Set Alarm-https://www.codewars.com/kata/568dcc3c7f12767a62000038
def set_alarm(employed, vacation): return employed and not vacation

# N4-https://www.codewars.com/kata/577bd026df78c19bca0002c0-Correct the mistakes of the character recognition software
def correct(s):
    s=s.replace("5" , "S")
    s=s.replace("0" , "O")
    s=s.replace("1" , "I")
    return s
    
# N5-https://www.codewars.com/kata/5ad0d8356165e63c140014d4-Student's Final Grade
def final_grade(exam, projects):
    if exam>90 or projects>10:
        return 100
    elif exam>75 and projects>=5:
        return 90
    elif exam>50 and projects>=2:
        return 75
    else:
        return 0
    
# N6-https://www.codewars.com/kata/59342039eb450e39970000a6-Count Odd Numbers below n
def odd_count(n):return n//2

# N7-https://www.codewars.com/kata/58ca658cc0d6401f2700045f-Find Multiples of a Number
def find_multiples(integer, limit):
    res=[]
    num=integer
    while num<=limit:
        res.append(num)
        num=num+integer
    return res

# N8-https://www.codewars.com/kata/50654ddff44f800200000007-Short Long Short
def solution(a, b):
    if len(a)<len(b):
        return a+b+a
    else:
        return b+a+b
    
# N9-https://www.codewars.com/kata/57a1fd2ce298a731b20006a4-Is it a palindrome?
def is_palindrome(s):
    s=s.lower()
    if s==s[::-1]:
        return True
    else:
        return False

# N10-https://www.codewars.com/kata/57f6ad55cca6e045d2000627-To square(root) or not to square(root)
def square_or_square_root(arr):
    new_arr=[]
    for i in range(len(arr)):
        root=arr[i]**0.5
        if root==int(root):
            new_arr.append(root)
        else:
            new_arr.append(arr[i]**2)
    return new_arr