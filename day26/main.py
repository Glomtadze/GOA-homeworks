# 1) ახსენით რას აკეთებს append მეთოდი და მოიყვანეთ მაგალითი
#ამატებს სიის ბოლოში ერთ ელემენტს
list=[1 ,2 , 3]
list.append(4)
print(list)

# 2) შექმენით ცარიელი სია. append მეთოდის გამოყენებით დაამატეთ მასში 5 სხვადასხვა რიცხვი და დაპრინტეთ სია
list=[]
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
print(list)

#3) შექმენით სია სიტყვებით. remove მეთოდის გამოყენებით წაშალეთ ერთ-ერთი სიტყვა და დაპრინტეთ შედეგი
list=["hello" , "gio" , "nika"]
list.remove("nika")
print(list)

#4) ახსენით განსხვავება remove და pop მეთოდებს შორის
# remove სრულიად შლის ხოლო pop შლის და აბრუნებს

#5) შექმენით სია რიცხვებით. pop მეთოდის გამოყენებით ამოიღეთ ბოლო ელემენტი და დაპრინტეთ როგორც ამოღებული ელემენტი, ასევე განახლებული სია
list=[1 , 3 , 5 ,  4 , 7 , 2]
list2=list.pop(-1)
print(list2)
print(list)

#6) შექმენით სია. insert მეთოდის გამოყენებით ჩასვით ახალი ელემენტი სიის შუაში
list=[1 , 3 , 4 , 5]
list.insert(1 , 2)
print(list)

#7) შექმენით რიცხვების სია. sort მეთოდის გამოყენებით დაალაგეთ ეს სია და დაბეჭდეთ შედეგი
list=["b" , "c" , "a" , "e " ,"d"]
list.sort()
print(list)

#8) ახსენით როგორ მუშაობს reverse მეთოდი და მოიყვანეთ მაგალითი
#reverse ლისტის ელემენტებს ატრიალებს ანუ ბოლო ელემენტი პირველზე გადმოინაცვლებს
list=[1 , 2 , 3 , 4 ]
list.reverse()
print(list)

#9)შექმენით სია სიტყვებით. reverse მეთოდის გამოყენებით შეცვალეთ ელემენტების რიგი
list=["gio" , "nika" , "hello"]
list.reverse()
print(list)

#10) შექმენით სია და გამოიყენეთ clear მეთოდი. რა შედეგი მიიღეთ?
list=[1 ,2 , 3 ,4 , 5 ,6]
list.clear()
print(list)
#clear ლისტს ცარიელ სიად ხდის

#11) შექმენით სია რიცხვებით. გამოიყენეთ index მეთოდი, რომ იპოვოთ კონკრეტული რიცხვის ინდექსი
list=[1, 2 ,3 ,4 ,5 , 6 ,7]
print(list.index(3))

#12) შექმენით სია სიტყვებით. მომხმარებელს მოთხოვეთ რაიმე სიტყვა.
# - თუ ეს სიტყვა არის სიაში იპოვეთ რომელ ინდექსზე დგას ეს სიტყვა
# - სხვა შემთხვევაში დაპრინტეთ 'ვერ მოიძებნდა'
list=["gio" , "nika" , "hello"]
word=input("enter word: ")
for i in range(len(list)):
    if word==list[i]:
       print(list.index(word))
    else:
        print("ვერ მოიძებნა")

# 13) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 10 რიცხვი და დაამატეთ ისინი ამ სიაში.
list=[]
for i in range(10):
    list.append(int(input("enter any number: ")))
print(list)

# # 14) შექმენით ცარიელი სია. მომხმარებელს მოთხოვეთ 7 რიცხვი და დაამატეთ ისინი ამ სიაში. დაპრინტეთ ამ რიცხვებიდან უდიდესი და უმცირესი რიცხვები
# list=[]
for i in range(7):
    list.append(int(input("enter any number: ")))
max=list[0] 
min=list[0]
for i in range(len(list)):
    if max<list[i]:
        max=list[i]
if min>list[i]:
    min=list[i]
print("min" , min , "max" , max)

# 15) (|HARD|) შექმენით ცარიელი სია. მომხმარებელს სათითაოდ მოთხოვეთ 10 რიცხვი. სიაში დაამატეთ რიცხვი თუ: 
#   - დადებითია და არის ლუწი
#   - უარყოფითია და არის კენტი
# საბოლოოდ გაიგეთ ამ რიცხვების საშუალო
numbers=[]
for i in range(10):
    number=(int(input("enter any number: ")))
    if number>0 and number%2==0:
        numbers.append(number)
    elif number<0 and number%2!=0:
        numbers.append(number)
count1=0
for i in range(len(numbers)):
    count1=count1+numbers[i]
print(numbers)
print(count1)
count=count1/len(numbers)
print(count)