# 1) ახსენით რა განსხვავებაა union, intersection, difference და symmetric_difference მეთოდებს შორის.
# union-გვიბრუნებს ორი სეტის გაერთიანებას
# intersection-გვიბრუნებს ორი სეტის თანაკვეთას
# difference-გვიბრუნებს მხოლოდ იმ ელემენტებს რომელიც მხოლოდ პირველ სეტშია
# symmetric_difference-გვიბრუნებს ყველა დანარჩენ ელემენტს რომელიც საერთო არ აქვთ ამ სეტებს

# 2) შექმენით ფუნქცია merge_students, რომელიც მიიღებს მოსწავლეების სახელების ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს ორივე ჯგუფის ყველა მოსწავლეს.
def merge_students(set_1 , set_2):
    return set_1.union(set_2)
print(merge_students({"nika " , "luka "} , {"gio" , "aleqsi"}))

# 3) შექმენით ფუნქცია common_courses, რომელიც მიიღებს ორი მოსწავლის კურსების set-ებს და დააბრუნებს მხოლოდ იმ კურსებს, რომლებსაც ორივე მოსწავლე სწავლობს.
def common_courses(course_1 , course_2):
    return course_1.intersection(course_2)
print(common_courses({"math" , "english"} , {"math"}))

# 4) შექმენით ფუნქცია only_first, რომელიც მიიღებს ორ set-ს და დააბრუნებს იმ ელემენტებს, რომლებიც მხოლოდ პირველ set-შია.
def only_first(set_1 , set_2):
    return set_1.difference(set_2)
print(only_first({1 , 2 , 3 , 4 , 5} , { 1 , 2  , 4  , 6}))

# 5) შექმენით ფუნქცია different_hobbies, რომელიც მიიღებს ორი ადამიანის ჰობების set-ებს და დააბრუნებს იმ ჰობებს, რომლებიც მხოლოდ ერთ-ერთ ადამიანს აქვს.
def different_hobbies(set_1 , set_2):
    return set_1.symmetric_difference(set_2)
print(different_hobbies({1 , 2 , 3 , 4 , 5} , { 1 , 2  , 4  , 6}))

# 6) შექმენით ფუნქცია all_colors, რომელიც მიიღებს თბილი და ცივი ფერების ორ set-ს და დააბრუნებს ყველა უნიკალურ ფერს.
def all_colors(color_1 , color_2):
    return color_1.union(color_2)

# 7) შექმენით ფუნქცია shared_friends, რომელიც მიიღებს ორი მომხმარებლის მეგობრების set-ებს და დააბრუნებს მათ საერთო მეგობრებს.
def shared_friends(friends_1 , friends_2):
    return friends_1.intersection(friends_2)

# 8) შექმენით ფუნქცია absent_students, რომელიც მიიღებს ყველა მოსწავლისა და გაკვეთილზე მყოფი მოსწავლეების set-ებს და დააბრუნებს გაცდენილი მოსწავლეების set-ს.
def absent_students(all_students , present):
    return all_students.difference(present)

# 9) შექმენით ფუნქცია unique_products, რომელიც მიიღებს ორი მაღაზიის პროდუქტების set-ებს და დააბრუნებს იმ პროდუქტებს, რომლებიც მხოლოდ ერთ-ერთ მაღაზიაში იყიდება.
def unique_products(products_1 , products_2):
    return products_1.symmetric_difference(products_2)

# 10) შექმენით ფუნქცია combine_three_sets, რომელიც მიიღებს სამ set-ს და დააბრუნებს მათში არსებულ ყველა უნიკალურ ელემენტს.
def combine_three_sets(set_1 , set_2 , set_3):
    return set_1.union(set_2 , set_3)

# 11) შექმენით ფუნქცია common_in_three, რომელიც მიიღებს სამ set-ს და დააბრუნებს მხოლოდ იმ ელემენტებს, რომლებიც სამივე set-ში გვხვდება.
def common_in_three(set_1 , set_2 , set_3):
    return set_1.intersection(set_3 , set_2)

# 12) შექმენით ფუნქცია first_only_words, რომელიც მიიღებს ორ ტექსტს, თითოეულს გადააქცევს სიტყვების set-ად და დააბრუნებს იმ სიტყვებს, რომლებიც მხოლოდ პირველ ტექსტში გვხვდება.
def first_only_words(text_1 , text_2):
    words_1 = set(text_1.split())
    words_2 = set(text_2.split())
    return words_1.difference(words_2)

# 13) შექმენით ფუნქცია different_letters, რომელიც მიიღებს ორ ტექსტს და დააბრუნებს იმ უნიკალურ სიმბოლოებს, 
# რომლებიც მხოლოდ ერთ-ერთ ტექსტში გვხვდება
def different_letters(text_1 , text_2):
    letters_1 = set(text_1)
    letters_2 = set(text_2)
    return letters_1.symmetric_difference(letters_2)

# 14) შექმენით ფუნქცია has_common_element, რომელიც მიიღებს ორ set-ს და დააბრუნებს True-ს, თუ მათ ერთი საერთო ელემენტი მაინც აქვთ, წინააღმდეგ შემთხვევაში კი False-ს.
def has_common_element(set_1 , set_2):
    common_elements = set_1.intersection(set_2)
    return len(common_elements)>0

# 15) შექმენით ფუნქცია are_disjoint, რომელიც მიიღებს ორ set-ს და დააბრუნებს True-ს, თუ მათ არცერთი საერთო ელემენტი არ აქვთ, წინააღმდეგ შემთხვევაში კი False-ს.
def are_disjoint(set_1 , set_2):
    common_element=set_1.intersection(set_2)
    return len(common_element)==0

# 16) შექმენით ფუნქცია exclusive_count, რომელიც მიიღებს ორ set-ს და დააბრუნებს იმ ელემენტების რაოდენობას, რომლებიც მხოლოდ ერთ-ერთ set-ში გვხვდება.
def exclusive_count(set_1 , set_2):
    return len(set_1.symmetric_difference(set_2))

# 17) შექმენით ფუნქცია missing_permissions, რომელიც მიიღებს საჭირო უფლებებისა და მომხმარებლის უფლებების set-ებს და დააბრუნებს იმ უფლებებს, რომლებიც მომხმარებელს აკლია.
def missing_permissions(permissions , user_permissions):
    return permissions.difference(user_permissions)

# 18) შექმენით ფუნქცია common_numbers, რომელიც მიიღებს ორ set-ს და დააბრუნებს ახალ set-ს, რომელიც შეიცავს ორივე set-ში არსებულ რიცხვებს.
#     - არ გამოიყენოთ სეტის მეთოდები!!! no intersection.
#     - გამოიყენეთ ციკლი და პირობა.
def common_numbers(set_1 , set_2):
    new_set=set()
    for i in set_1:
        if i in set_2:
            new_set.add(i)
    return new_set

# 19) შექმენით ფუნქცია analyze_sets, რომელიც მიიღებს ორ set-ს და დააბრუნებს tuple-ს ოთხი შედეგით:
#     - ყველა უნიკალური ელემენტი.
#     - საერთო ელემენტები.
#     - მხოლოდ პირველ set-ში არსებული ელემენტები.
#     - მხოლოდ ერთ-ერთ set-ში არსებული ელემენტები.
def analyze_sets(set_1 , set_2):
    all_elements=set_1.union(set_2)
    common=set_1.intersection(set_2)
    only_first=set_1.difference(set_2)
    symmetric_difference=set_1.symmetric_difference(set_2)
    return (all_elements, common, only_first, symmetric_difference)
