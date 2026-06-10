# 1) ახსენით რას აკეთებს `return` ბრძანება ფუნქციაში და მოიყვანეთ მარტივი მაგალითი.
# return ბრძანება ფუნქციაში აბრუნებს შედეგს

# 2) შექმენით ფუნქცია `greet()`, რომელიც აბრუნებს (return) ტექსტს: `"Hello, World!"`. გამოიძახეთ ფუნქცია და დაპრინტეთ შედეგი.
def greet():
    return "hello, world!"
print(greet())

# 3) შექმენით ფუნქცია `square(number)`, რომელიც აბრუნებს რიცხვის კვადრატს. შეამოწმეთ რამდენიმე მნიშვნელობაზე.
def square(number):
    return number**2
print(square(2))

# 4) შექმენით ფუნქცია `add(a, b)`, რომელიც აბრუნებს ორი რიცხვის ჯამს. მომხმარებელს შემოატანინეთ ორი რიცხვი და გამოიყენეთ ფუნქცია
def add(a,b):
    return a+b
a=int(input("enter number: "))
b=int(input("enter number: "))
print(add(a,b))

# 5) შექმენით ფუნქცია `is_even(number)`, რომელიც აბრუნებს `True`-ს თუ რიცხვი ლუწია და `False`-ს თუ კენტია.
def is_even(number):
    if number%2==0:
        return "True"
    else:
        return "False"
print(is_even(5))

# 6) შექმენით ფუნქცია `count_vowels(text)`, რომელიც აბრუნებს სტრინგში ხმოვანი ასოების რაოდენობას.
def count_vowels(text):
    count=0
    for i in range(len(text)):
        if text[i] in "aAeEiIoOuU":
            count=count+1
    return count
print(count_vowels("aAbIi"))

# 7) შექმენით ფუნქცია `largest(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს ყველაზე დიდ ელემენტს.
def largest(numbers):
    largest=numbers[0]
    for i in range(len(numbers)):
        if largest<numbers[i]:
            largest=numbers[i]
    return largest

# 8) შექმენით ფუნქცია `sum_list(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს ყველა ელემენტის ჯამს.
def sum_list(numbers):
    count=0
    for i in range(len(numbers)):
        count=count+numbers[i]
    return count

# 9) შექმენით ფუნქცია `count_letter(text, letter)`, რომელიც აბრუნებს რამდენჯერ გვხვდება კონკრეტული ასო სტრინგში.
def count_letter(text , letter):
    count=0
    for i in range(len(text)):
        if letter==text[i]:
            count=count+1
    return count

# 10) შექმენით ფუნქცია `filter_even(numbers)`, რომელიც იღებს რიცხვების სიას და აბრუნებს მხოლოდ ლუწი რიცხვების სიას.
def filter_even(numbers):
    new_list=[]
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            new_list.append(numbers[i])
    return new_list

# 11) მომხმარებელს შემოატანინეთ სახელი. შექმენით ფუნქცია `format_name(name)`, რომელიც აბრუნებს სახელს title ფორმატში (პირველი ასო დიდი, დანარჩენი პატარა).
def format_name(name):
    return name.title()
name=input("enter name: ")
print(format_name(name))