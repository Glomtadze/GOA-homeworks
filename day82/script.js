const box2=document.getElementById("box2")
const par1=document.getElementById("par1")
const par2=document.getElementById("par2")
const img1=document.getElementById("img1")
let non=false
box2.addEventListener("click" , ()=>{
    if(non==false){
        par1.style.fontWeight="400"
        img1.style.transform="none"
        par2.style.display="none"
        non=true
    }
    else{
        par1.style.fontWeight="700"
        par2.style.display="block"
        par2.style.opacity="50%"
        img1.style.transform="Rotate(180deg)"
        non=false
    }
})

const box3=document.getElementById("box3")
const par3=document.getElementById("par3")
const par4=document.getElementById("par4")
const img2=document.getElementById("img2")
let no=false
box3.addEventListener("click" , ()=>{
    if(no==false){
        par3.style.fontWeight="400"
        img2.style.transform="none"
        par4.style.display="none"
        no=true
    }
    else{
        par3.style.fontWeight="700"
        par4.style.display="block"
        par4.style.opacity="50%"
        par4.style.fontSize="12px"
        img2.style.transform="Rotate(180deg)"
        no=false
    }
})

const box4=document.getElementById("box4")
const par5=document.getElementById("par5")
const par6=document.getElementById("par6")
const img3=document.getElementById("img3")
let none=false
box4.addEventListener("click" , ()=>{
    if(none==false){
        par5.style.fontWeight="400"
        img3.style.transform="none"
        par6.style.display="none"
        none=true
    }
    else{
        par5.style.fontWeight="700"
        par6.style.display="block"
        par6.style.opacity="50%"
        par6.style.fontSize="12px"
        img3.style.transform="Rotate(180deg)"
        none=false
    }
})

const box5=document.getElementById("box5")
const par7=document.getElementById("par7")
const par8=document.getElementById("par8")
const img4=document.getElementById("img4")
let n=false
box5.addEventListener("click" , ()=>{
    if(n==false){
        par7.style.fontWeight="400"
        img4.style.transform="none"
        par8.style.display="none"
        n=true
    }
    else{
        par7.style.fontWeight="700"
        par8.style.display="block"
        par8.style.opacity="50%"
        par8.style.fontSize="12px"
        img4.style.transform="Rotate(180deg)"
        n=false
    }
})

const box6=document.getElementById("box6")
const par9=document.getElementById("par9")
const par10=document.getElementById("par10")
const img5=document.getElementById("img5")
let nonee=false
box6.addEventListener("click" , ()=>{
    if(nonee==false){
        par9.style.fontWeight="400"
        img5.style.transform="none"
        par10.style.display="none"
        nonee=true
    }
    else{
        par9.style.fontWeight="700"
        par10.style.display="block"
        par10.style.opacity="50%"
        par10.style.fontSize="12px"
        img5.style.transform="Rotate(180deg)"
        nonee=false
    }
})
