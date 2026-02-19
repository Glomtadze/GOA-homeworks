#მონაცემთა ტიპები არის იმისთვის საჭირო რომ ვიცოდეთ ცვლადში რა სახის ინფორმაცია ინახება.მაგალითად მასში თუ არის მთელი რიცხვები შენახული ანუ მასში ინახება ინტეჯერი თუ ინახება ათწილადები ანუ ინახება ფლოათი და თუ ინახება " " მოქცეული რაიმე სიტყვა ან რიცხვი ანუ ამ ცვლადში ინახება სტრინგი

#input-ის მაგალითად რეალური ცხოვრებიდან შეიძლება მოვიყვანოთ კლავიატურა,მაუსი და სკანერი
#output-ის მაგალითად შეგვიძლია მოვიყვანოთ ეკრანი,ყურსასმენები და სპიკერები

#task1
string_word="Giorgi"
integer_number=15
float_number=1.5

print(type(string_word))
print(type(integer_number))
print(type(float_number))

#task2
distance=float(input("enter the distance in kilometers= "))
print(distance*1000)

#task3
number1=int(input("enter any number= "))
number2=int(input("enter any second number you want= "))

print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1/number2)
print(number1//number2)
print(number1%number2)
print(number1**number2)

#task4(BMI)

weight=float(input("enter your weight in kg= "))
height=float(input("enter your height in meters= "))

BMI=(weight/(height**2))
print(BMI)


