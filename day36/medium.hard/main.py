# 13) შექმენით ფუნქცია `remove_duplicates(numbers)`, რომელიც მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც დუბლიკატები აღარ იქნება.
# მაგალითი: 
# [1, 2, 2, 3, 1, 4] → [1, 2, 3, 4]
def remove_duplicates(numbers):
    new_list=[]
    for i in range(len(numbers)):
        if numbers[i] not in new_list:
            new_list.append(numbers[i])
    return new_list

# 14) შექმენით ფუნქცია `second_largest(numbers)`, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს მეორე ყველაზე დიდ რიცხვს.
# მაგალითი:
# [4, 7, 2, 9, 5] → 7
def second_largest(numbers):
    largest=numbers[0]
    for i in range(len(numbers)):
        if largest<numbers[i]:
            largest=numbers[i]
    index=numbers.index(largest)
    numbers.pop(index)
    sec_largest=numbers[0]
    for i in range(len(numbers)):
        if sec_largest<numbers[i]:
            sec_largest=numbers[i]
    return sec_largest
print(second_largest([4, 7, 2, 9, 5]))

# 18) შექმენით ფუნქცია `count_occurrences(numbers, target)`, რომელიც მიიღებს სიას და რიცხვს.
# ფუნქციამ უნდა დააბრუნოს რამდენჯერ გვხვდება ეს რიცხვი სიაში.
# `count()` მეთოდის გამოყენება აკრძალულია.
def count_occurrences(numbers , target):
    count=0
    for i in range(len(numbers)):
        if target==numbers[i]:
            count=count+1
    return count

# 19) შექმენით ფუნქცია `merge_lists(list1, list2)`, რომელიც მიიღებს ორ სიას და დააბრუნებს ახალ სიას, სადაც ჯერ იქნება პირველი სიის ელემენტები, შემდეგ კი მეორე სიის ელემენტები.
# ამისთვის არ გამოიყენოთ `+` ოპერატორი და არც `.extend()` მეთოდი.
def merge_lists(list1 , list2):
    new_list=[]
    for i in range(len(list1)):
        new_list.append(list1[i])
    for i in range(len(list2)):
        new_list.append(list2[i])
    return new_list
print(merge_lists([1 ,2 ,3 ,4 ,5] , ["hello" , 2 , True]))

# 20) შექმენით ფუნქცია `analyze_numbers(numbers)`, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სიას შემდეგი მონაცემებით:
# - ყველაზე დიდი რიცხვი
# - ყველაზე პატარა რიცხვი
# - ელემენტების ჯამი
# - ელემენტების რაოდენობა
# - საშუალო არითმეტიკული
# მაგალითი:
# [4, 8, 2, 6] # argument
# შედეგი:
# [8, 2, 20, 4, 5] # result

def analyze_numbers(numbers):
    count=0
    for i in range(len(numbers)):
        count=count+numbers[i]

    min=numbers[0]
    for i in range(len(numbers)):
        if min>numbers[i]:
            min=numbers[i]

    largest=numbers[0]
    for i in range(len(numbers)):
        if largest<numbers[i]:
            largest=numbers[i]
    number_count=len(numbers)
    half=count/number_count
    new_list=["count" , count , "min" , min , "largest" , largest , "number count" , number_count , "half" , half]
    return new_list
print(analyze_numbers([1 , 2 , 3 , 4 , 5 , 6]))

