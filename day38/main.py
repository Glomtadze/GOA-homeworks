# 1) აღსენით დღეს ნასწავლი 3 ფუნქცია: `min()`, `max()`, `sum()`
# min()-პოულობს მინიმალურ მნიშვნელობას
# max()-პოულობს მაქსიმალურ მნიშნელობას
# sum()-ითვლის ჯამს

# 2) მოიფიქრეთ თუ როგორ გამოიყენებთ მათ პრაქტიკაში
# თუ პირობა გვთხოვს მინიმალური მნიშვნელობის ან მაქსიმალურის პოვნას ლისტში ან გვთხოვს ლისტში მოცემული რიცხვების ჯამის პოვნას

# 3) შექმენით ფუნქცია `max_difference(numbers)`, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს სხვაობას ყველაზე დიდ და ყველაზე პატარა ელემენტს შორის.
# მაგალითი:
# [8, 3, 15, 6] -> 12
# გამოიყენეთ `max()` და `min()` ფუნქციები.
def max_difference(numbers):
    max_numbers=max(numbers)
    min_numbers=min(numbers)
    return max_numbers-min_numbers
numbers=[1 , 2 , 3 , 4 , 5 , 6]
print(max_difference(numbers))

# 4) შექმენით ფუნქცია `unique_characters(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს სიას იმ სიმბოლოებისგან, რომლებიც ტექსტში მხოლოდ ერთხელ გვხვდება.
# მაგალითი:
# "banana" -> ["b", "n"]
def unique_characters(text):
    new_list=[]
    for i in range(len(text)):
        if text[i] not in new_list:
            new_list.append(text[i])
    return new_list
text="aabbccdd"
print(unique_characters(text))

# 5) შექმენით ფუნქცია `highest_char(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს იმ სიმბოლოს, რომელსაც ყველაზე დიდი char code აქვს.
# მაგალითი:
# "Az9" → "z"
# გამოიყენეთ `max()` ფუნქცია.
def highest_char(text):
    return max(text)
text="Az9"
print(highest_char(text))

# 6) შექმენით ფუნქცია `numbers_summary(numbers)`, რომელიც მიიღებს რიცხვების სიას და **დააბრუნებს** შემდეგი ფორმატის ტექსტს:
# მაგალითი:
# [5, 10, 15]
# შედეგი:
# "რაოდენობა: 3 | ჯამი: 30 | მინიმალური: 5 | მაქსიმალური: 15"
def numbers_summary(numbers):
    count=len(numbers)
    sum_numbers=sum(numbers)
    min_numbers=min(numbers)
    max_numbers=max(numbers)
    return ["რაოდენობა" , count , "ჯამი", sum_numbers , "მინიმალური" , min_numbers , "მაქსიმალური" , max_numbers]
numbers=[1 , 2 , 3 , 4 , 5 , 6]
print(numbers_summary(numbers))

# 7) მოიძიეთ ინფორმაცია `ord()` ფუნქციაზე და შექმენით ფუნქცია `char_code_sum(text)`, რომელიც მიიღებს სტრინგს და დააბრუნებს მის ყველა სიმბოლოს char code-ების ჯამს.
# მაგალითი:
# "ABC" -> 198
def char_code_sum(text):
    count=0
    for i in range(len(text)):
        count=count+ord(text[i])
    return count
text="ABC"
print(char_code_sum(text))
