# 1) ახსენით რა არის dictionary-ში key, value და item. მოიყვანეთ თითოეულის მაგალითი.
# key-არის გასაღები  value-არის მნიშვნელობა ხოლო item-არის key_ს და value_ს ერთობლიობა

# 2) შექმენით ფუნქცია student_info, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს მასში არსებული ელემენტების რაოდენობას.
def student_info(info):
    return len(info)

print(student_info({"name": "gio", "age": 16}))

# 3) შექმენით ფუნქცია get_student_name, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს "name" key-ის შესაბამის value-ს.
def get_student_name(info):
    return info["name"]

print(get_student_name({"name": "gio", "age": 16}))

# 4) შექმენით ფუნქცია get_student_age, რომელიც მიიღებს მოსწავლის dictionary-ს და დააბრუნებს "age" key-ის შესაბამის value-ს.
def get_student_age(info):
    return info["age"]

print(get_student_age({"name": "gio", "age": 16}))

# 5) შექმენით ფუნქცია count_products, რომელიც მიიღებს პროდუქტების dictionary-ს და დააბრუნებს მასში არსებული პროდუქტების რაოდენობას.
def count_products(products):
    return len(products)

# 6) შექმენით ფუნქცია get_price, რომელიც მიიღებს პროდუქტების dictionary-ს და პროდუქტის სახელს და დააბრუნებს შესაბამის ფასს.
def get_price(products, name):
    return products[name]

# 7) შექმენით ფუნქცია create_student, რომელსაც ექნება name, lastname, age, weight, height, grades, passed_test პარამეტრები. თქვენმა ფუნქციამ უნდა შექმნას dict შესაბამისი key-value ებით.
def create_student(name, lastname, age, weight, height, grades, passed_test):
    return {
        "name": name,
        "lastname": lastname,
        "age": age,
        "weight": weight,
        "height": height,
        "grades": grades,
        "passed_test": passed_test,
    }

# 8) შექმენით ფუნქცია print_student, რომელიც მიიღებს მოსწავლის dictionary-ს, რომელსაც ექნება name, lastname, age, weight, height, grades, passed_test გასაღებები.
#   - თქვენმა ფუნქციამ უნდა დაპრინტოს მოსწავლის შესახებ ინფორმაცია შემდეგი ფორმატით:


# -- Student Info --
# Name: Zaza
# Lastname: Dumbadze
# Age: 16
# Weight: 78.5
# Height: 1.78
# Grades: 9, 10, 8, 10, 9, 10, 10
# Passed_test: True
# --- -- -- -- -- ---
def print_student(info):
    print("-- Student Info --")
    print("Name: " + str(info["name"]))
    print("Lastname: " + str(info["lastname"]))
    print("Age: " + str(info["age"]))
    print("Weight: " + str(info["weight"]))
    print("Height: " + str(info["height"]))
    print("Grades: " + str(info["grades"]))
    print("Passed_test: " + str(info["passed_test"]))
    print("--- -- -- -- -- ---")

print_student({
        "name": "Zaza",
        "lastname": "Dumbadze",
        "age": 16,
        "weight": 78.5,
        "height": 1.78,
        "grades": [9, 10, 8, 10, 9, 10, 10],
        "passed_test": True,
    })