# 1) ახსენით რას აკეთებს lower მეთოდი და მოიყვანეთ მაგალითი
# ეს მეთოდი გამოიყენება იმისთვის რომ სტრინგში ყველა ასო პატარა შრიპტით დაიწეროს

# 2) შექმენით სტრინგი დიდი ასოებით. lower მეთოდის გამოყენებით გადააკეთეთ ყველა ასო პატარად და დაპრინტეთ შედეგი
string="HELLO"
string_two=string.lower()
print(string_two)

# 3) ახსენით რას აკეთებს upper მეთოდი და მოიყვანეთ მაგალითი
# upper მეთოდი სტრინგში ყველა ასოს დიდი შრიტით წერს
string="hello"
string_two=string.upper()
print(string_two)

# 4) მომხმარებელს შემოატანინეთ სიტყვა. upper მეთოდის გამოყენებით გადააკეთეთ ეს სიტყვა დიდ ასოებად
word=input("enter any word: ")
word_two=word.upper()
print(word_two)

# 5) ახსენით რას აკეთებს title მეთოდი და მოიყვანეთ მაგალითი
# ამ მეთოდით სტრინგის პირველი ასო დიდია დანარჩენი პატარა
word="hello"
word_two=word.title()
print(word_two)

# 6) შექმენით სტრინგების სია. გამოიყენეთ title მეთოდი თითოეულ სტრინგზე
listi=["hello" , "world" , "welcome"]
for i in range(len(listi)):
    listi[i]=listi[i].title()
print(listi)

# 7) შექმენით სტრინგი, სადაც შერეული იქნება დიდი და პატარა ასოები. swapcase მეთოდის გამოყენებით შეცვალეთ ასოების ზომები და დაპრინტეთ შედეგი
word="aBioLiQRt"
print(word.swapcase())

# 8) შექმენით სტრინგი. count მეთოდის გამოყენებით დაითვალეთ რამდენჯერ გვხვდება კონკრეტული ასო
word="aabbaqerga"
print(word.count("a"))

# 9) მომხმარებელს შემოატანინეთ წინადადება და ერთი სიმბოლო. count მეთოდის გამოყენებით გაიგეთ რამდენჯერ გვხვდება ეს სიმბოლო წინადადებაში
sentence=input("enter any sentence: ")
print(sentence.count(input("enter symbol to count: ")))

# 10) მომხმარებელს შემოატანინეთ სახელი და გვარი. title მეთოდის გამოყენებით სწორ ფორმატში დაპრინტეთ ორივე.
name=input("enter your name: ")
surename=input("enter your surename: ")
print(name.title() , surename.title())

# 11) მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც). დათვალეთ ხმოვნების რაოდენობა.
sentence=input("enter sentence use both uppercase and lowercase letters: ")
count=0
for i in range(len(sentence)):
    if sentence[i]=="a" or sentence[i]=="A" or sentence[i]=="e" or sentence[i]=="E" or sentence[i]=="i" or sentence[i]=="I" or sentence[i]=="o" or sentence[i]=="O" or sentence[i]=="u" or sentence[i]=="U":
        count=count+1
print(count)

# 12) მომხმარებელს შემოატანინეთ წინადადება(დიდი ასოებითაც და პატარებითაც).
#   - გაიგეთ დიდი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ პატარა ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ ხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ თანხმოვანი ასოების პროცენტული რაოდენობა სტრინგში
#   - გაიგეთ სფეისების პროცენტული რაოდენობა სტრინგში
sentence=input("enter sentence use both uppercase and lowercase letters: ")
lowr=0
upper=0
xmovani=0
tanxmovani=0
space=0
for i in range(len(sentence)):
    if  sentence[i]!=" " and sentence[i]==sentence[i].lower():
        lowr=lowr+1
    elif sentence[i]!=" " and sentence[i]==sentence[i].upper():
        upper=upper+1
for i in range(len(sentence)):
    if sentence[i]=="a" or sentence[i]=="A" or sentence[i]=="e" or sentence[i]=="E" or sentence[i]=="i" or sentence[i]=="I" or sentence[i]=="o" or sentence[i]=="O" or sentence[i]=="u" or sentence[i]=="U":
        xmovani=xmovani+1
    elif sentence[i]==" ":
        space=space+1
    else:
        tanxmovani=tanxmovani+1
print(lowr, upper , xmovani , tanxmovani , space)

print("ხმოვნის" ,((xmovani/len(sentence))*100) ,"თანხმოვნის" , ((tanxmovani/len(sentence))*100) ,"uppercase" ,((upper/len(sentence))*100) , "lowercase" , ((lowr/len(sentence))*100), "space" ,((space/len(sentence))*100) )

    

