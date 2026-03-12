#sequencing-არის თანმიმდევრობით შესრულება ხოლო selection-არის კოდის შესრულება რაღაც პირობით
#პითონში არის ინდენტაცია საჭირო და მას ვიყენებთ მაგალითად if else ფუნქციის დაწერის დროს 

#task1
math=float(input("enter your math score : "))
english=float(input("enter your english score : "))
physics=float(input("enter your physics score : "))
if math>=90 and english>=90 and physics>=90:
    print("შენ შესანიშნავი მოსწავლე ხარ")
    print("ყველა საგანში მაღალი შედეგი გაქვს")
elif math>=70 and english>=70 and physics>=70:
    print("კარგი შედეგებია")
    print("სასწავლო წელი წარმატებულია")
elif math<50 or english<50 or physics<50:
    print("ერთ-ერთ საგანში დაბალი ქულა გაქვს")
    print("მეტი სწავლა დაგჭირდება")
else:
    print("შედეგები საშუალოა")
    print("შეგიძლია უკეთესიც")

#task2

age=float(input("enter your age : "))
license=input("do you have license?(yes or no) : ")
drunk=input("are you drunk?(yes or no) : ")

if age>=18 and license=="yes" and drunk=="no":
    print("შეგიძლია მანქანის მართვა")
    print("უსაფრთხო მგზავრობას გისურვებთ")
elif age>=18 and license=="no" and drunk=="no":
    print("ასაკი საკმარისია")
    print("მაგრამ მართვის მოწმობა არ გაქვს")
elif drunk=="yes" or age<18 or license=="no":
    print("მანქანის მართვა აკრძალულია")
    print("ეს შეიძლება საშიში იყოს")
else:
    print("მონაცემები ვერ გადამოწმდა")
    print("სცადე თავიდან")

#task3

price=float(input("enter price of the item : "))
quantity=float(input("enter quantity of the item : "))
member=input("are you member or not (type yes or no) : ")

if price>=100 and quantity>=3 and member=="yes":
    print("დიდი ფასდაკლება მიიღე")
    print("მადლობა ერთგული მომხმარებლობისთვის")
elif price>=100 and quantity>=3 and member=="no":
    print("ფასდაკლება მიიღო")
    print("წევრობის შემთხვევაში უფრო მეტს მიიღებ")
elif price<50 or quantity==1 or member=="no":
    print("ფასდაკლება არ გეკუთვნის")
    print("მეტი პროდუქტი შეიძინე")
else:
    print("მცირე ფასდაკლება მიიღე")
    print("გმადლობთ შენაძენისთვის")

#task4 

weight=float(input("enter your weight kg(kilograms): "))
height=float(input("enter your height in m(meters): "))
age=float(input("enter your age: "))
BMI=weight/(height*height)
if BMI<18.5 and age>=18:
    print("შენი BMI დაბალია")
    print("შესაძლოა წონის მომატება დაგჭირდეს")
elif BMI>=18.5 and BMI<=24.9 and age>=18:
    print("შენი BMI ნორმალურია")
    print("ჯანმრთელ ფორმაში ხარ")
elif BMI>=25 and BMI<30 or age<18:
    print("BMI საშუალოზე მაღალია")
    print("ჯანსაღი კვება მნიშვნელოვანია")
elif BMI>=30:
    print("BMI მაღალია")
    print("სასურველია ექიმთან კონსულტაცია")
else:
    print("მონაცემები ვერ დამუშავდა")
    print("სცადე თავიდან")