#task1

temperature=int(input("enter temperature: "))
if temperature>30:
    print("ძალიან ცხელია")
elif temperature>20:
    print("სასიამოვნო ამინდია")
elif temperature>10:
    print("ცოტა ცივა")
elif temperature>0:
    print("ცივა, ჩაიცვი თბილად")
else:
    print("გაიყინები, სახლში დარში")

#task2

score=int(input("enter score: "))
attendance=int(input("enter attendance : "))

if score>80 and attendance>90:
    print("შენ შესანიშნავად დაწერე გამოცდა")
elif score>50 and attendance>70:
    print("საშუალოდ დაწერე გამოცდა")
elif score>30 and attendance>50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")
else:
    print("ჩაიჭერი!")

#task3

temperature=int(input("enter temperature : "))
rain=input("yes or no : ")
if temperature>25 and rain=="no":
    print("შესანიშნავი ამინდია სასეირნოდ")
elif temperature>25 and rain=="yes":
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება")
elif temperature<10 or rain=="yes":
    print("სჯობს სახლში დარჩე")
else:
    print("სასიამოვნო ამინდია")

#task4

age=int(input("enter your age: "))
student=input("are you student?(if yes type yes if no type no): ")
if age<12 or age>65:
    print("ბილეთი უფასოა")
elif student=="yes" and age>12:
    print("ბილეთი ნახევარ ფასად")
else:
    print("სრული ფასი უნდა გადაიხადო")

#task5

username=input("enter your username: ")
password=input("enter your password: ")
if username=="admin" and password=="superSecretPassword":
    print("მოგესალმები, ადმინ")
elif username=="guest" and password=="1234":
    print("მოგესალმები, სტუმარო")
else:
    print("მომხმარებელი არ მოიძებნა")
#task1

temperature=int(input("enter temperature: "))
if temperature>30:
    print("ძალიან ცხელია")
elif temperature>20:
    print("სასიამოვნო ამინდია")
elif temperature>10:
    print("ცოტა ცივა")
elif temperature>0:
    print("ცივა, ჩაიცვი თბილად")
else:
    print("გაიყინები, სახლში დარში")

#task2

score=int(input("enter score: "))
attendance=int(input("enter attendance : "))

if score>80 and attendance>90:
    print("შენ შესანიშნავად დაწერე გამოცდა")
elif score>50 and attendance>70:
    print("საშუალოდ დაწერე გამოცდა")
elif score>30 and attendance>50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")
else:
    print("ჩაიჭერი!")

#task3

temperature=int(input("enter temperature : "))
rain=input("yes or no : ")
if temperature>25 and rain=="no":
    print("შესანიშნავი ამინდია სასეირნოდ")
elif temperature>25 and rain=="yes":
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება")
elif temperature<10 or rain=="yes":
    print("სჯობს სახლში დარჩე")
else:
    print("სასიამოვნო ამინდია")

#task4

age=int(input("enter your age: "))
student=input("are you student?(if yes type yes if no type no): ")
if age<12 or age>65:
    print("ბილეთი უფასოა")
elif student=="yes" and age>12:
    print("ბილეთი ნახევარ ფასად")
else:
    print("სრული ფასი უნდა გადაიხადო")

#task5

username=input("enter your username: ")
password=input("enter your password: ")
if username=="admin" and password=="superSecretPassword":
    print("მოგესალმები, ადმინ")
elif username=="guest" and password=="1234":
    print("მოგესალმები, სტუმარო")
else:
    print("მომხმარებელი არ მოიძებნა")
