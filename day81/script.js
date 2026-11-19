//1
const par1 = document.getElementById("par1")
const btn1 = document.getElementById("btn1")
btn1.addEventListener("click", () => {
    par1.innerHTML = "Hello, JavaScript!"
})

//2
const par2 = document.getElementById("par2")
const btn2 = document.getElementById("btn2")
btn2.addEventListener("click", () => {
    par2.style.display = "none"
})

//3
const par3 = document.getElementById("par3")
const btn3 = document.getElementById("btn3")
let non = false
btn3.addEventListener("click", () => {
    if (non == false) {
        par3.style.display = "none"
        non = true
    }
    else {
        par3.style.display = "block"
        non = false
    }
})

//4
const div1 = document.getElementById(".div1")
const btn4 = document.getElementById(".btn4")
let blue = false
btn4.addEventListener("click", () => {
    if (blue == false) {
        div1.style.backgroundColor = "blue"
        blue = true
    }
    else {
        div1.style.backgroundColor = "yellow"
        blue = false
    }
})

//5
const btn5 = document.getElementById("btn5")
const par4 = document.getElementById("par4")
let count = 0

btn5.addEventListener("click", () => {
    count = count + 1
    par4.innerHTML = count
})

//6
const h1 = document.getElementById("h1")
const par5 = document.getElementById("par5")
const btn6 = document.getElementById("btn6")
const box = document.getElementById("box")
let black = false
btn6.addEventListener("click", () => {
    if (black == false) {
        box.style.backgroundColor = "black"
        h1.style.color = "white"
        par5.style.color = "white"
        black = true
    }
    else {
        box.style.backgroundColor = ""
        h1.style.color = ""
        par5.style.color = ""
        black = false
    }
})

//7
const img1 = document.getElementById("img1")
const btn7 = document.getElementById("btn7")
btn7.addEventListener("click", () => {
    img1.src = "https://images.unsplash.com/photo-1628948266286-bc981b29c672?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"
})

//8
const par6 = document.getElementById("par6")
const btn8 = document.getElementById("btn8")
const btn9 = document.getElementById("btn9")
const btn10 = document.getElementById("btn10")
let count2 = 0
btn8.addEventListener("click", () => {
    count2 = count2 + 1
    par6.innerHTML = count2
})
btn9.addEventListener("click", () => {
    count2 = count2 - 1
    par6.innerHTML = count2
})
btn10.addEventListener("click", () => {
    count2 = 0
    par6.textContent = count2
})

//9
const par7 = document.getElementById("par7")
const btn11 = document.getElementById("btn11")
const btn12 = document.getElementById("btn12")
let font = 16
btn11.addEventListener("click",()=>{
    font=font+2
    par7.style.fontSize=`$(font)px`
})
btn12.addEventListener("click",()=>{
    font=font-2
    par7.style.fontSize=`$(font)px`
})

//10
const btn13 = document.getElementById("btn13")
const par8 = document.getElementById("par8")
let ans1 = false
btn13.addEventListener("click", () => {
    if (ans1 == false) {
        par8.style.display = "block"
        ans1 = true
    }
    else {
        par8.style.display = "none"
        ans1 = false
    }
})

const btn14 = document.getElementById("btn14")
const par9 = document.getElementById("par9")
let ans2 = false
btn14.addEventListener("click", () => {
    if (ans2 == false) {
        par9.style.display = "block"
        ans2 = true
    }
    else {
        par9.style.display = "none"
        ans2 = false
    }
})

const btn15 = document.getElementById("btn15")
const par10 = document.getElementById("par10")
let ans3 = false
btn15.addEventListener("click", () => {
    if (ans3 == false) {
        par10.style.display = "block"
        ans3 = true
    }
    else {
        par10.style.display = "none"
        ans3 = false
    }
})

