# 1) ახსენით რა არის `tuple` და რით განსხვავდება ის `list`-ისგან.
# tuple ისევე როგორც ლისტი გამოიყენება მონაცემების შესანახად მაგრამ განსხვავება არის ის რომ tuple არის immutable list არის mutable

# 2) მოიფიქრეთ, რომელ რეალურ სიტუაციებში გამოიყენებდით `tuple`-ს `list`-ის ნაცვლად.
# გამოიყენება მაშინ როცა შენახული მონაცემები აღარ უნდა შეიცვალოს

# 3) შექმენით ფუნქცია first_and_last(items), რომელიც მიიღებს `tuple`-ს და დააბრუნებს ახალ `tuple`-ს, რომელიც შეიცავს მხოლოდ პირველ და ბოლო ელემენტს.
def first_and_last(items): return (items[0] , items[-1])
print(first_and_last((1 , 2 , 3 , 4)))

# 4) შექმენით ფუნქცია middle_element(items), რომელიც მიიღებს კენტსიგრძიან tuple-ს და დააბრუნებს მის შუა ელემენტს.
def middle_element(items): return items[len(items)//2]
print(middle_element((1 , 2 , 3 , 4 , 5 , 6 , 7)))

# 5) შექმენით ფუნქცია count_occurrences(items, value), რომელიც მიიღებს tuple-ს და ნებისმიერ მნიშვნელობას, შემდეგ კი დააბრუნებს რამდენჯერ გვხვდება ეს მნიშვნელობა tuple-ში. არ გამოიყენოთ count() მეთოდი.
def count_occurrences(items , value):
    count=0
    for i in range(len(items)):
        if value==items[i]:
            count=count+1
    return count
print(count_occurrences((1 , 2 , 3 , 1 , 1 , 3 , 1) , 1))

# 6) შექმენით ფუნქცია contains_duplicates(items), რომელიც მიიღებს tuple-ს და დააბრუნებს True, თუ მასში რომელიმე ელემენტი მეორდება, წინააღმდეგ შემთხვევაში კი False.
def contains_duplicates(items):
    for i in range(len(items)):
        count=items.count(items[i])
        if count>1:
            return True
print(contains_duplicates((1 , 2 , 1 , 3)))

# 7) შექმენით ფუნქცია swap_edges(items), რომელიც მიიღებს მინიმუმ ორი ელემენტისგან შემდგარ tuple-ს და დააბრუნებს ახალ tuple-ს, სადაც პირველი და ბოლო ელემენტები ადგილებს გაცვლიან.
def swap_edges(items): return(( items[-1], ) + (items[1:-1]) + ( items[0],) )
print(swap_edges((1 , 2 , 3 , 4 , 5 , 6 , 7)))

# 8) მოიძიეთ ინფორმაცია index() მეთოდზე და შექმენით ფუნქცია first_position(items, value), რომელიც დააბრუნებს გადაცემული მნიშვნელობის პირველ ინდექსს.
def first_position(items , value):
    index=items.index(value)
    word=items[index]
    return word[0]
print(first_position(("hello" , "world") , "world"))

# 9) შექმენით ფუნქცია tuple_summary(numbers), რომელიც მიიღებს რიცხვების tuple-ს და დააბრუნებს შემდეგი ფორმატის ტექსტს:
# "რაოდენობა: X | ჯამი: Y | პირველი: A | ბოლო: B"
def tupple_summary(numbers):
    x=len(numbers)
    y=sum(numbers)
    A=numbers[0]
    B=numbers[-1]
    return "რაოდენობა" , x , "ჯამი" , y , "პირველი" , A , "ბოლო" , B 
print(tupple_summary((1 , 2 , 3 , 4 , 5 , 6)))

# 10) შექმენით ფუნქცია reverse_tuple(items), რომელიც მიიღებს tuple-ს და დააბრუნებს მის შებრუნებულ ვერსიას. გამოიყენეთ slicing
def reverse_tuple(items): return items[::-1]
print(reverse_tuple((1 , 2 , 3 , 4 , 5 , 6)))