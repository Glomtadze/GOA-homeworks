// 1)დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება თავის ასაკს და დაადგენს არის თუ არა 18 წლის ან უფრო მეტის. თუ არის, გამოპრინტეთ "Adult", თუარადა - "Minor". გამოიყენე ternary operator
let age = prompt("enter your age: ")
let res = (age >= 18) ? "adult" : "minor"

// 2) დაწერეთ ფუნქცია სახელად countBs, რომელიც იღებს სტრიქონს თავის ერთადერთ არგუმენტად და აბრუნებს სტრიქონში დიდი "B" სიმბოლოების რაოდენობას. გამოიყენე function expression
const countBs = function (text) {
    let count = 0
    for (let i = 0; i <= text.length - 1; i++) {
        if (text[i] == "B") {
            count = count + 1
        }
    }
    return count
}

// 3) შექმენი ცვლადი number. თუ რიცხვი 10-დან 100-ის ჩათვლით არის, გამოიტანე "In Range", სხვა შემთხვევაში "Out of Range". გამოიყენე ternary
let number=35
let res2=(number>=10 && number<=100) ? "in range" : "out of range"

// 4)შექმენით Arrow Function, რომელსაც გადაეცემა ადამიანის ასაკი.
// თუ ასაკი 18 ან მეტია, დააბრუნოს "You can get a driving license", სხვა შემთხვევაში "You are too young".
const func=(age)=>{
    if(age>=18){
        return "you can get a driving license"
    }
    else{
        return "you are too young"
    }
}