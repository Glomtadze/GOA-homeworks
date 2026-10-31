# 1) შექმენით ფუნქცია print_students, რომელიც მიიღებს მოსწავლეების dictionary-ს. dictionary-ში key იყოს მოსწავლის სახელი, ხოლო value — მისი ქულა. ციკლის გამოყენებით დაბეჭდეთ ყველა მოსწავლის სახელი და ქულა. თუ ქულა 50-ზე მეტია, დაბეჭდეთ "Passed", წინააღმდეგ შემთხვევაში — "Failed". გამოიყენეთ items() მეთოდი.
def print_students(dictionary):
    for name, score in dictionary.items():
        print(name, score)
        if score > 50:
            print("Passed")
        else:
            print("Failed")

# 2) შექმენით ფუნქცია count_passed_students, რომელიც მიიღებს მოსწავლეების dictionary-ს, სადაც key არის მოსწავლის სახელი, ხოლო value — მისი ქულა. ციკლისა და if-ის გამოყენებით დათვალეთ რამდენმა მოსწავლემ მიიღო 50 ან მეტი ქულა. გამოიყენეთ items() მეთოდი.
def count_passed_students(dictionary):
    count = 0
    for name, score in dictionary.items():
        if score >= 50:
            count = count + 1
    return count

# 3) შექმენით ფუნქცია find_expensive_products, რომელიც მიიღებს პროდუქტების dictionary-ს, სადაც key არის პროდუქტის სახელი, ხოლო value — ფასი. ციკლის გამოყენებით დაბეჭდეთ მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია. გამოიყენეთ items() მეთოდი.
def find_expensive_products(products):
    for name, value in products.items():
        if value > 100:
            print(name, value)

# 4) შექმენით ფუნქცია change_low_prices, რომელიც მიიღებს პროდუქტების dictionary-ს. ციკლის გამოყენებით შეამოწმეთ ყველა პროდუქტის ფასი. თუ ფასი 20-ზე ნაკლებია, შეცვალეთ იგი 20-ით. გამოიყენეთ items() მეთოდი.
def change_low_prices(products):
    for name, value in products.items():
        if value < 20:
            products[name] = 20
    return products

# 5) შექმენით ფუნქცია check_student_data, რომელიც მიიღებს მოსწავლის dictionary-ს და ციკლის გამოყენებით შეამოწმებს მის key-ებს. თუ dictionary-ში არის "name", "age" და "grade" key-ები, დაბეჭდეთ "Complete", წინააღმდეგ შემთხვევაში — "Incomplete". გამოიყენეთ keys() მეთოდი.
def check_student_data(student):
    required_keys = ["name", "age", "grade"]
    student_keys = student.keys()
    for i in required_keys:
        if i not in student_keys:
            return "Incomplete"

    return "Complete"

# 6) შექმენით ფუნქცია count_adults, რომელიც მიიღებს ადამიანების dictionary-ს, სადაც key არის სახელი, ხოლო value — ასაკი. ციკლის გამოყენებით დათვალეთ რამდენი ადამიანია 18 წლის ან უფროსი. გამოიყენეთ values() მეთოდი.
def count_adults(humans):
    count = 0
    for i in humans.values():
        if i >= 18:
            count = count + 1
    return count

# 7) შექმენით ფუნქცია find_student, რომელიც მიიღებს მოსწავლეების dictionary-ს და მოსწავლის სახელს. ციკლის გამოყენებით მოძებნეთ ეს სახელი. თუ არსებობს, დაბეჭდეთ მისი ქულა, ხოლო თუ არ არსებობს - "Student not found". გამოიყენეთ keys() მეთოდი.
def find_student(students, name):
    for i in students.keys():
        if i == name:
            return students[i]

    return "Student not found"

# 8) შექმენით ფუნქცია remove_failed_students, რომელიც მიიღებს მოსწავლეების dictionary-ს, სადაც key არის სახელი, ხოლო value - ქულა. ციკლის გამოყენებით იპოვეთ ყველა მოსწავლე, რომლის ქულაც 40-ზე ნაკლებია და წაშალეთ ისინი dictionary-დან.
def remove_faiked_students(students):
    for name in list(students.keys()):
        if students[name] < 40:
            del students[name]
    return students