# N1-https://www.codewars.com/kata/59cfc000aeb2844d16000075
def capitalize(s):
    s1=s.upper()
    even=""
    odd=""
    for i in range(len(s)):
        if i%2==0:
            even=even+s1[i]
            odd=odd+s[i]
        else:
            even=even+s[i]
            odd=odd+s1[i]
    return[even , odd]

# N2-https://www.codewars.com/kata/5aff237c578a14752d0035ae
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages=[age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    total=0
    for i in ages:
        total=total+i*i
    root=total**0.5
    return int(root/2)

# N3-https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c
def even_numbers(arr,n):
    new_arr=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            new_arr.append(arr[i])
    return new_arr[-n:]

# N4-https://www.codewars.com/kata/59a96d71dbe3b06c0200009c
def generate_shape(n):return "\n".join(["+" * n] * n)

# N5-https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3
def sort_gift_code(code):return "".join(sorted(code))

# N6-https://www.codewars.com/kata/5b39e3772ae7545f650000fc
def remove_duplicate_words(s):
    new_s=[]
    words=s.split()
    for i in words:
        if i not in new_s:
            new_s.append(i)
    return " ".join(new_s)

# N7-https://www.codewars.com/kata/59706036f6e5d1e22d000016
def words_to_marks(s):
    total=0
    for i in s:
        value=ord(i)-96
        total=total+value
    return total

# N8-https://www.codewars.com/kata/5680781b6b7c2be860000036
def vowel_indices(word):
    new_list = []
    vowels = "aeiouy"
    for i in range(len(word)):
        if word[i].lower() in vowels:
            new_list.append(i + 1)
    return new_list

# N9-https://www.codewars.com/kata/556196a6091a7e7f58000018
def largest_pair_sum(numbers): 
    largest1=max(numbers)
    numbers.remove(largest1)
    largest2=max(numbers)
    return largest1+largest2 

# N10-https://www.codewars.com/kata/580755730b5a77650500010c
def sort_my_string(s):
    even=""
    odd=""
    for i in range(len(s)):
        if i % 2 == 0:
            even=even+s[i]
        else:
            odd=odd+s[i]
    return even+" "+odd