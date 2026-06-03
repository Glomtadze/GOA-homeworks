# 1) რა არის ფუნქცია? ახსენით საკუთარი სიტყვებით.
# ფუნქცია არის ისეთი დამხმარე რომელსაც ჩვენ კოდით ერთხელ დავწერთ სახელს დავარქმევთ და როცა მოგვინდება გამოვიყენებთ

# 2) რატომ არის ფუნქციები საჭირო პროგრამირებაში? - ჩამოწერეთ მინიმუმ 3 მიზეზი
# ფუნქია იმიტომ არის საჭირო რომ კოდი შევამოკლოთ უფრო ადვილი დასაწერი გავხადოთ და მკითხველისთვის უფრო ადვილი იყოს გასაგებად

# 3) რა არის პარამეტრი (Parameter)?
# პარამეტრი არის ცვლადი რომელსაც ფუნქციის შექმნის დროს ვწერთ

# 4) რა არის არგუმენტი (Argument)?
# არგუმენტი არის მნიშვნელობა რომელსაც ფუნქციას ვანიჭებთ

# 5) რა განსხვავებაა პარამეტრსა და არგუმენტს შორის?
# პარამეტრი არის ცვლადი რომელსაც ფუნქციის დაწერის შემდეგ მივანიჭებთ მნიშვნელობას და არგუმენტი არის მნიშვნელობა რომელსაც ფუნქციის შექმნის დროს ვანიჭებთ

# 6) შექმენით ფუნქცია repeat_word(word, count).
# - ფუნქციამ count-ჯერ უნდა დაბეჭდოს `word`
# - გამოიყენეთ for ციკლი

def repeat_word(word , count):
    for i in range(count):
        print(word)
repeat_word("hello" , 5)

# 7) შექმენით ფუნქცია print_numbers(start, end).
# - ფუნქციამ უნდა დაბეჭდოს ყველა რიცხვი start-დან end-მდე
def print_numbers(start , end):
    i=0
    while i!=end:
        print(start+i)
        i=i+1
print_numbers(1 , 10)

# 8) შექმენით ფუნქცია count_even(numbers).
# - პარამეტრად მიიღოს სია
# - დაითვალოს რამდენი ლუწი რიცხვია სიაში
# - გამოიტანოს შედეგი
def count_even(numbers):
    count=0
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            count=count+1
    print(count)
numbers=[1 , 2 , 3 , 4 , 5 , 6]
count_even(numbers)

# 9) შექმენით ფუნქცია count_vowels(text).
# - პარამეტრად მიიღოს სტრინგი
# - დაითვალოს რამდენი ხმოვანია ტექსტში
# - გამოიტანოს შედეგი
def count_vowels(text):
    count=0
    for i in range(len(text)):
        if text[i]=="a" or "A" or "E" or "e" or "i" or "I" or "o" or "O" or "u" or "U":
            count=count+1
    print(count)
text="ae"
count_vowels(text)

# 10) შექმენით ფუნქცია longest_word(words).
# - პარამეტრად მიიღოს სიტყვების სია
# - გამოიტანოს ყველაზე გრძელი სიტყვა
def longest_word(words):
    longest=words[0]
    for i in range(len(words)):
        if len(longest)<len(words[i]):
            longest=words[i]
    print(longest)
words=["aa" , "bbb" , "c"]
longest_word(words)

# 11) შექმენით ფუნქცია filter_long_words(words, n).
# - პარამეტრად მიიღოს წინადადება
# - გამოიტანოს მხოლოდ ის სიტყვები, რომელთა სიგრძე n-ზე მეტია
def filter_long_words(word, n):
    for i in range(len(word)):
        if len(word[i])>n:
            print(word[i])

word="hello worlddd"
word=word.split()
filter_long_words(word, 6)

# 12) მომხმარებელს შემოატანინეთ რამდენიმე სახელი ერთი სტრინგის სახით (მაგ: "nika luka ana gio").
# - split მეთოდით გადააქციეთ სიად
# - შექმენით ფუნქცია name_lengths(names)
# - ფუნქციამ თითოეული სახელის გვერდით უნდა დაბეჭდოს მისი სიგრძე

names="gio nika luka"
names=names.split()
def name_lengths(names):
    for i in range(len(names)):
        print(names[i] , len(names[i]))
name_lengths(names)

# 13) შექმენით ფუნქცია find_max(numbers).
# - პარამეტრად მიიღოს რიცხვების სია
# - ციკლის გამოყენებით იპოვოს ყველაზე დიდი რიცხვი
def find_max(numbers):
    max=numbers[0]
    for i in range(len(numbers)):
        if max<numbers[i]:
            max=numbers[i]
    print(max)
numbers=[1 , 2 , 3 , 4 , 5]
find_max(numbers)

# 14) შექმენით ფუნქცია find_min(numbers).
# - პარამეტრად მიიღოს რიცხვების სია
# - ციკლის გამოყენებით იპოვოს ყველაზე პატარა რიცხვი
def find_min(numbers):
    min=numbers[0]
    for i in range(len(numbers)):
        if min>numbers[i]:
            min=numbers[i]
    print(min)
numbers=[1 , 2 , 3 , 4 , 5 , 0]
find_min(numbers)

# 15) შექმენით ფუნქცია remove_duplicates(numbers).
# - პარამეტრად მიიღოს სია
# - შექმნას ახალი სია დუბლიკატების გარეშე
# - გამოიტანოს შედეგი
numbers=[1 , 1 , 2 , 2 , 3 , 3 , 4 , 4 , 5 , 5]
numbers.sort()
new=[]
def remove_duplicates(numbers):
    for i in range(len(numbers)):
        if numbers[i]!=numbers[i-1]:
            new.append(numbers[i])
    print(new)
remove_duplicates(numbers)

# 16) მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13").
# - split() მეთოდით დაყავით ელემენტებად
# - გადააქციეთ integer-ებად
# - შექმენით ფუნქცია `analyze_numbers(numbers)`
# - ფუნქციამ უნდა:
#   - გამოიტანოს ჯამი
#   - გამოიტანოს საშუალო არითმეტიკული
#   - გამოიტანოს ყველაზე დიდი რიცხვი
#   - გამოიტანოს ყველაზე პატარა რიცხვი
#   - დაითვალოს ლუწი რიცხვების რაოდენობა
numbers="10 25 7 90 13"
numbers=numbers.split()
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
def analyze_numbers(numbers):
    count=0
    for i in range(len(numbers)):
        count=count+numbers[i]

    min=numbers[0]
    for i in range(len(numbers)):
        if min>numbers[i]:
            min=numbers[i]

    max=numbers[0]
    for i in range(len(numbers)):
        if max<numbers[i]:
            max=numbers[i]
    even=0
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            even=even+1
    half=count/len(numbers)
    print(count , half , min , max , even)
analyze_numbers(numbers)