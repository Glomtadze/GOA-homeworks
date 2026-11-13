// 1)დაწერეთ ფუქნცია, სახელად sayHello, რომელიც დაპრინტავს - "Hello, World".
function sayHello(){
    console.log("Hello, World")
}
sayHello()
// 2)დაწერეთ ფუნქცია, სახელად greet, რომელიც პარამეტრა მიიღებს სახელს და დაპრინტავს - "გამარჯობა, [სახელი]"
function greet(name){
    console.log("გამარჯობა" , name)
}
greet("gio")
// 3)დაწერეთ ფუნქცია, სახელად sum, რომელიც არგუმენტებად მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს. შედეგი გამოიტანეთ ტერმინალში.
function sum(a,b){
    return a+b
}
sum(5, 10)
// 4)დაწერეთ ფუნქცია, სახელად calculateArea, რომელიც არგუმენტად მიიღებს ოთხკუთხედის სიგრესა და სიგანეს და დააბრუნებს მის ფართობს. შედეგი გამოიტანეთ ტერმინალში.
function calculateArea(length,width){
    return length*width
}
calculateArea(20 , 30)
// 5)დაწერეთ ფუნქცია, რომელიც მიიღებს ორ არგუმენტს და დააბრუნებს მათ შორის უდიდესს.
function getMax(a,b){
    if (a>b){
        return a
    }
    else{
        return b
    }
}
getMax(5 , 7)

// 6)დაწერეთ ფუქნცია, რომელიც პარამეტრად მიიღებს იმ რაოდენობას, რამდენჯერად უნდა გამოკონსოლდეს "Hello, World".

// 7)დაწერეთ ფუქნცია, სახელად celsiusToFahrenheit, რომელიც პარამეტრად მიიღებს ცელსიუსს და გადაიყვანს ფარენჰეიტში.
// ფორმულა - (Celsius * 9/5) + 32
function celsiusToFahrenheit(cel){
    return (cel*9/5)+32
}
celsiusToFahrenheit(20)
