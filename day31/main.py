# 1) შექმენით სტრინგი ზედმეტი სფეისებით დასაწყისში და ბოლოში. strip მეთოდის გამოყენებით მოაშორეთ ზედმეტი სფეისები
string="     hello     "
print(string.strip())

# 2) მომხმარებელს შემოატანინეთ სახელი ზედმეტი სფეისებით. მოაშორეთ ზედმეტი სფეისები და დაპრინტეთ შედეგი
name="   gio lomtadze  "
print(name.strip())

# 3) მომხმარებელს შემოატანინეთ სიტყვა. შეამოწმეთ იწყება თუ არა "A" ასოთი startswith მეთოდის გამოყენებით
word=input("enter any word: ")
print(word.startswith("A"))

# 4) მომხმარებელს შემოატანინეთ ვებსაიტის მისამართი. შეამოწმეთ იწყება თუ არა "https"-ით
adress=input("enter website adress: ")
print(adress.startswith("https"))

# 5) მომხმარებელს შემოატანინეთ ფაილის სახელი. შეამოწმეთ მთავრდება თუ არა .py-ზე endswith მეთოდის გამოყენებით
file_name=input("enter file name: ")
print(file_name.endswith("py"))

# 6) მომხმარებელს შემოატანინეთ ელფოსტა. შეამოწმეთ მთავრდება თუ არა "@gmail.com"-ზე
email=input("enter your email: ")
print(email.endswith("@gmail.com"))

# 7) შექმენით ტექსტი. `replace()` მეთოდის გამოყენებით შეცვალეთ სიტყვა "dog" სიტყვით "cat"
sentence="i like my dog"
print(sentence.replace("dog" , "cat"))

# 8) მომხმარებელს შემოატანინეთ წინადადება. ყველა სფეისი შეცვალეთ "-" სიმბოლოთი
number=input("enter any sentence: ")
print(number.replace(" ", "-"))

# 9) მომხმარებელს შემოატანინეთ ტელეფონის ნომერი ფორმატით "599-12-34-56". replace მეთოდის გამოყენებით წაშალეთ ყველა "-" სიმბოლო
number=input("enter phone number(like this 599-12-34-56): ")
print(number.replace("-",""))

# 10) მომხმარებელს შემოატანინეთ ტექსტი ზედმეტი სფეისებით. ჯერ strip მეთოდით მოაშორეთ ზედმეტი სფეისები, შემდეგ შეამოწმეთ იწყება თუ არა ტექსტი "Hello" სიტყვით
sentence=input("enter sentence with extra spaces: ")
sentence=sentence.strip()
print(sentence.startswith("hello"))

# 11) მომხმარებელს შემოატანინეთ პაროლი. შეამოწმეთ:
# - იწყება თუ არა დიდი ასოთი
# - მთავრდება თუ არა ციფრით "1"
password=input("enter password: ")
if password[0]==password[0].upper():
    print(True)
else:
    print(False)
print(password.endswith("1"))

# 12) მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - მოაშოროს ზედმეტი სფეისები
# - ყველა სფეისი შეცვალოს "_" სიმბოლოთი
# - შეამოწმოს მთავრდება თუ არა "." სიმბოლოზე
# - თუ არ მთავრდება, ბოლოში დაამატოს "."
sentence=input("enter any sentence: ")
sentence=sentence.strip()
sentence=sentence.replace(" " , "-")
if sentence.endswith("."):
    print(True , sentence)
else:
    sentence=sentence+"."
    print(sentence)

# 13) მომხმარებელს შემოატანინეთ სრული სახელი (სახელი, გვარი, მამის სახელი). `split()` მეთოდის გამოყენებით:
# - ცალ-ცალკე გამოიტანეთ თითოეული ნაწილი
# - დაითვალეთ რამდენი სიტყვაა შეყვანილ ტექსტში
names=input("enter your name and surename and your dads name: ")
names=names.split()
print(names , len(names))

# 14) მომხმარებელს შემოატანინეთ წინადადება. პროგრამამ უნდა:
# - დაყოს ტექსტი სიტყვებად
# - გამოიტანოს ყველაზე გრძელი სიტყვა
# - გამოიტანოს ყველაზე მოკლე სიტყვა
sentence=input("enter sentence: ")
sentence=sentence.split()
max=sentence[0]
for i in range(len(sentence)):
    if len(sentence[i])>len(max):
        max=sentence[i]
min=sentence[0]
for i in range(len(sentence)):
    if len(sentence[i])<len(min):
        min=sentence[i]
print(sentence, "min " ,min , "max" , max)

# 15) მომხმარებელს შემოატანინეთ რამდენიმე რიცხვი ერთი სტრინგის სახით (მაგ: "10 25 7 90 13"). split მეთოდის გამოყენებით:
# - გადააქციეთ ისინი integer-ებად
# - იპოვეთ ჯამი
# - იპოვეთ ყველაზე დიდი და ყველაზე პატარა რიცხვი
numbers=input("enter any numbers: ")
numbers=numbers.split()
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
print(numbers)
count=0
for i in range(len(numbers)):
    count=count+numbers[i]
max=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
min=numbers[0]
for i in range(len(numbers)):
    if numbers[i]<min:
        min=numbers[i]

print(numbers, "min " , min , "max" , max , "count" , count)