const body=document.body
const h1=document.createElement("h1")
h1.innerText = "1. Personal Bio Page"
body.appendChild(h1)
const par1= document.createElement("p")
par1.innerHTML="<b>Description:</b> Create a simple webpage introducing yourself. Add a heading with your name, a paragraph about you, line breaks, and a horizontal line."
body.appendChild(par1)
const par2= document.createElement("p")
par2.innerHTML="<b>Tags Covered:</b> &lt;h1&gt;, &lt;p&gt;, &lt;br&gt;, &lt;hr&gt;"
body.appendChild(par2)
const par3=document.createElement("p")
par3.innerHTML="<b>Result:</b>"
body.appendChild(par3)
const br2=document.createElement("br")
body.appendChild(br2)
const heading2=document.createElement("h2")
heading2.innerText="John Doe"
body.appendChild(heading2)
const par4=document.createElement("p")
par4.innerText="Hello! My name is John Doe."
body.appendChild(par4)
const par5=document.createElement("p")
par5.innerText="I am learning web development and this is my very first HTML page"
body.appendChild(par5)
const hr1=document.createElement("hr")
body.appendChild(hr1)
const par6=document.createElement("p");
par6.innerText="I love coding and exploring new technologies."
body.appendChild(par6)
const br=document.createElement("br")
body.appendChild(br)
const hr2=document.createElement("hr")
body.appendChild(hr2)
const h2=document.createElement("h1")
h2.innerText="2. Favorite Books/Movies List"
body.appendChild(h2)
const par7=document.createElement("p")
par7.innerHTML="<b>Description:</b> Make a page listing your favorite books (unordered list) and movies (ordered list)."
body.appendChild(par7)
const par8=document.createElement("p")
par8.innerHTML="<b>Tags Covered:</b> &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt;"
body.appendChild(par8)
const par9=document.createElement("p")
par9.innerHTML="<b>Result:</b>"
body.appendChild(par9)
const br3=document.createElement("br")
body.appendChild(br3)
const h3=document.createElement("h2")
h3.innerText="My Favorite Books"
body.appendChild(h3)
const ul=document.createElement("ul");
const li1=document.createElement("li")
const par10=document.createElement("p")
par10.innerText="Harry Potter"
li1.appendChild(par10)
ul.appendChild(li1)
const li2=document.createElement("li")
const par11=document.createElement("p")
par11.innerText="The Hobbit"
li2.appendChild(par11)
ul.appendChild(li2)
const li3=document.createElement("li")
const par12=document.createElement("p")
par12.innerText="Atomic Habbits"
li3.appendChild(par12)
ul.appendChild(li3)
body.appendChild(ul)
const h4=document.createElement("h2")
h4.innerText="My Favorite Movies"
body.appendChild(h4)
const ol=document.createElement("ol")
const li4=document.createElement("li")
const par14=document.createElement("p")
par14.innerText="Inception"
li4.appendChild(par14)
ol.appendChild(li4)
const li5=document.createElement("li")
const par15=document.createElement("p")
par15.innerText="Interstellar"
li5.appendChild(par15)
ol.appendChild(li5)
const li6=document.createElement("li")
const par16=document.createElement("p")
par16.innerText="Avengers: Endgame"
li6.appendChild(par16)
ol.appendChild(li6)
body.appendChild(ol)
const hr3=document.createElement("hr")
body.appendChild(hr3)