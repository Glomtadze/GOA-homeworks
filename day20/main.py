#task1
my_favourite_colours = ["black", "white", "red"]
#task2
weekdays = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]
#task3
numbers = [1, 2, 3, 4, 5]
print(numbers[3])
#task4
cities = ["kutaisi", "tbilisi", "gori", "batumi", "qobuleti"]
cities[2] = "rustavi"
#task5
names = ["gio", "temo", "kaxa", "bela"]
print(names[0], names[3])
#task6
numbers = [12, 23, 24, 25, 9, 7]
numbers[4] = 100
#task7
dog_names = ["Max" , "Luna" , "Rocky" ,"Charlie" , "Daisy" , "Milo" , "Coco" , "Zeus" , "Ruby" , "Buddy"]
dog_names[5]="Shadow"
#task8
types=["hello " , "world" , "hello" , 1 , 2 , 3 , True , False , True]
print(types[5])
#task9
artists=["drake" , "BIG" , "NAS" , "2Pac" , "kendrcik"]
if artists[0]=="drake":
    artists[0]="50Cent"
print(artists)
#task10
numbers=[1 ,2 ,3 ,4 ,5 ,5.5 , 6.5  , 9.9]
numbers[0]=numbers[0]+1000
numbers[7]=numbers[7]+1000

#task11
numbers=[11, 29 , 5.5]

if numbers[0]>10:
    numbers[2]=numbers[2]+numbers[1]*numbers[0]
else:
    numbers[0]=numbers[0]+numbers[1]*numbers[2]

print(numbers)
    