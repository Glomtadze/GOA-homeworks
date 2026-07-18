# 1) ახსენით რა არის set და რა არის მისი მთავარი განსხვავება list-ისა და tuple-ისგან.
# set არის უნიკალური ელემენტების დაულაგებელი სია რომელიც არის mutable

# 2) მოიფიქრეთ, რომელ რეალურ სიტუაციებში გამოიყენებდით set-ს, სადაც მნიშვნელობების გამეორება დაუშვებელია.
# მაგალითად აპლიკაციის პაროლისთვის თუ მოვთხოვთ მომხმარებელს ისეთ პაროლოს რომელშიც არცერთი მნიშვნელობა არ მეორდება

# 3) შექმენით ფუნქცია add_fruit(fruits, fruit), რომელიც მიიღებს set-ს და ერთ ხილს, შემდეგ კი დაამატებს მას add() მეთოდის გამოყენებით და დააბრუნებს განახლებულ set-ს.
def add_fruit(fruits,fruit):
    fruits.add(fruit)
    return fruits
print(add_fruit({"apple" , "mango"} , "kiwi"))

# 4) შექმენით ფუნქცია merge_sets(first, second), რომელიც მიიღებს ორ set-ს, გააერთიანებს მათ update() მეთოდის გამოყენებით და დააბრუნებს შედეგს.
def merge_sets(first,second):
    first.update(second)
    return first
print(merge_sets({1 , 2 , 3} , {4 , 5 , 6}))

# 5) შექმენით ფუნქცია remove_color(colors, color), რომელიც მიიღებს set-ს და ფერს, შემდეგ კი წაშლის მას remove() მეთოდის გამოყენებით.
def remove_color(colors , color):
    colors.remove(color)
    return colors
print(remove_color({"blue" , "red" , "green"} , "green"))

# 6) შექმენით ფუნქცია safe_remove(numbers, value), რომელიც მიიღებს set-ს და რიცხვს, შემდეგ კი წაშლის მას ისე, რომ შეცდომა არ წარმოიშვას, თუ ელემენტი არ არსებობს.
def safe_remove(numbers , value):
    numbers.discard(value)
    return numbers
print(safe_remove({1 , 2 , 3 , 4 ,5}  , 6))

# 7) შექმენით ფუნქცია remove_random(items), რომელიც მიიღებს set-ს, წაშლის ერთ შემთხვევით ელემენტს pop() მეთოდის გამოყენებით და დააბრუნებს წაშლილ ელემენტს.
def remove_random(items):
    return items.pop()
print(remove_random({1 , 2 , 3 , 4}))

# 8) შექმენით ფუნქცია clear_set(items), რომელიც მიიღებს set-ს, გაასუფთავებს მას clear() მეთოდის გამოყენებით და დააბრუნებს ცარიელ set-ს.
def clear_set(items):
    items.clear()
    return items
print(clear_set({1, 2 ,3 , 4}))

# 9) შექმენით ფუნქცია copy_set(items), რომელიც მიიღებს set-ს, შექმნის მის ასლს copy() მეთოდის გამოყენებით და დააბრუნებს ახალ set-ს.
def copy_set(items):
    return items.copy()
print(copy_set({1 , 2 , 3 , 4}))

# 10) შექმენით ფუნქცია unique_letters(text), რომელიც მიიღებს ტექსტს და დააბრუნებს set-ს, რომელიც შეიცავს მხოლოდ უნიკალურ სიმბოლოებს.
def unique_letters(text):
    text_set=set()
    for i in range(len(text)):
        if text[i] not in text_set:
            text_set.add(text[i])
    return text_set
print(unique_letters("Hello"))

# 11) შექმენით ფუნქცია common_elements(first, second), რომელიც მიიღებს ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს მხოლოდ ორივე set-ში არსებულ ელემენტებს
#   - არ გამოიყენოთ სეტის მეთოდები!!!(no intersection).
def common_elements(first , second):
    new_set=set()
    for i in first:
        if i in second:
            new_set.add(i)
    return new_set
print(common_elements({1 , 2 , 3 , 4 , 5} , {1 , 5}))

# 12) შექმენით ფუნქცია all_unique(numbers), რომელიც მიიღებს list-ს და დააბრუნებს True-ს, თუ ყველა ელემენტი განსხვავებულია, წინააღმდეგ შემთხვევაში კი False.
#   - გამოიყენეთ set.
def all_unique(numbers):
    if len(numbers)==len(set(numbers)):
        return True
    else:
        return False
print(all_unique([1 , 2 , 3 , 4 , 5 , 5]))

# 13) შექმენით ფუნქცია unique_digits(number), რომელიც მიიღებს მთელ რიცხვს და დააბრუნებს set-ს, რომელიც შეიცავს ამ რიცხვის ყველა უნიკალურ ციფრს.
def unique_digits(number):
    new_set=set()
    number=str(number)
    for i in range(len(number)):
        if number[i] not in new_set:
            new_set.add(number[i])
    return new_set
print(unique_digits(1122334455))