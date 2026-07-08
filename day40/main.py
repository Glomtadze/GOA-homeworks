# 1--Sum of positive--https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count = count + arr[i]
    return count
print(positive_sum([-1 , 1 , 2 , 3]))

# 2--String repeat--https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
def repeat_str(repeat, string): return repeat * string
print(repeat_str(5 , "h"))

# 3--Remove First and Last Character--https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
def remove_char(s):
    new_str=""
    if len(s)<2:
        return new_str
    else:
        return s[1 : -1]
print(remove_char("hello"))

# 4--Square(n) Sum--https://www.codewars.com/kata/515e271a311df0350d00000f
def square_sum(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**2
    return sum(numbers)
print(square_sum([1 , 2 , 2]))

# 5--Find the smallest integer in the array--https://www.codewars.com/kata/55a2d7ebe362935a210000b2
def find_smallest_int(arr): return min(arr)
print(find_smallest_int([1 , 2 , 3 , 4 , 0]))

# 6--Grasshopper - Summation--https://www.codewars.com/kata/55d24f55d7dd296eb9000030
def summation(num):
    count=0
    for i in range(0,num+1):
        count=count+i
    return count
print(summation(3))

# 7--Counting sheep...--https://www.codewars.com/kata/54edbc7200b811e956000556
def count_sheeps(sheep): return sheep.count(True)
print(count_sheeps([True , False , True , True]))

# 8--Remove String Spaces--https://www.codewars.com/kata/57eae20f5500ad98e50002c5
def no_space(x): return x.replace(" " , "")
print(no_space("  h e llo"))

# 9--Keep Hydrated!--https://www.codewars.com/kata/582cb0224e56e068d800003c
def litres(time): return int(0.5*time)
print(litres(5))

# 10--Century From Year--https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
def century(year): return (year+99)//100
print(century(2742))