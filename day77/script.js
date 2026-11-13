const body=document.body
body.style.display="flex"
body.style.flexDirection="column"
body.style.alignItems="center"
const Logo=document.createElement("div")
Logo.style.marginBottom="50px"
const imLogo=document.createElement("img")
imLogo.src = "logo.svg"
imLogo.style.width = "119px"
Logo.appendChild(imLogo)
body.appendChild(Logo)
const Container=document.createElement("div")
Container.style.display="flex"
Container.style.alignItems="center"
Container.style.justifyContent="space-between"
const imLeft=document.createElement("img")
imLeft.src = "image-hero-right.png"
const center=document.createElement("div")
center.style.textAlign="center"
center.style.margin = "0 20px"
const par1=document.createElement("h1")
par1.innerText="Group Chat for Everyone"
par1.style.width="445px"
par1.style.fontSize="48px"
par1.style.fontWeight="900"
par1.style.color="rgb(40, 40, 61)"
par1.style.marginBottom = "24px"
const par2=document.createElement("p");
par2.innerText = "Meet makes it easy to connect with others face-to-face virtually and collaborate across any device."
par2.style.width="520px"
par2.style.fontSize = "16px"
par2.style.fontWeight = "500"
par2.style.color = "rgb(135, 135, 157)"
par2.style.marginBottom = "32px"
const btnContainer=document.createElement("div")
btnContainer.style.display="flex"
btnContainer.style.gap="16px"
btnContainer.style.justifyContent="center"
const btnDownload=document.createElement("button")
btnDownload.innerHTML="Download v1.3"
btnDownload.style.backgroundColor="rgb(77, 150, 169)"
btnDownload.style.color = "white"
btnDownload.style.border = "none"
btnDownload.style.padding="15px 30px"
btnDownload.style.borderRadius="30px"
btnDownload.style.fontWeight="bold"
const btnWht = document.createElement("button")
btnWht.innerText = "What is it?"
btnWht.style.backgroundColor = "rgb(133, 95, 177)"
btnWht.style.color="white"
btnWht.style.border="none"
btnWht.style.padding="15px 30px"
btnWht.style.borderRadius="30px"
btnWht.style.fontWeight="bold"
btnContainer.appendChild(btnDownload)
btnContainer.appendChild(btnWht)
center.appendChild(par1)
center.appendChild(par2)
center.appendChild(btnContainer)
const imRight=document.createElement("img")
imRight.src="image-men-in-meeting.jpg"
Container.appendChild(imLeft)
Container.appendChild(center)
Container.appendChild(imRight)
body.appendChild(Container)
const photos=document.createElement("div")
photos.style.display="flex"
photos.style.gap="30px"
photos.style.justifyContent="center"
photos.style.marginBottom="80px"
const img1=document.createElement("img")
img1.src="image-women-videochatting.jpg"
img1.style.width="255px"
img1.style.height="242px"
img1.style.borderRadius="8px"
const img2=document.createElement("img")
img2.src="image-hero-left.png"
img2.style.width="255px"
img2.style.height="242px"
img2.style.borderRadius="8px"
const img3=document.createElement("img")
img3.src="image-man-texting.jpg"
img3.style.width="255px"
img3.style.height="242px"
img3.style.borderRadius="8px"
const img4=document.createElement("img")
img4.src="image-man-texting.jpg"
img4.style.width="255px"
img4.style.height="242px"
img4.style.borderRadius="8px"
photos.appendChild(img1)
photos.appendChild(img2)
photos.appendChild(img3)
photos.appendChild(img4)
body.appendChild(photos)
const infoBox=document.createElement("div")
infoBox.style.display="flex"
infoBox.style.flexDirection="column"
infoBox.style.alignItems="center"
infoBox.style.textAlign="center"
infoBox.style.marginBottom="72px"
const title=document.createElement("p")
title.innerText="BUILT FOR MODERN USE"
title.style.fontSize="16px"
title.style.fontWeight="900"
title.style.color="rgb(77, 150, 169)"
title.style.marginBottom="16px"
const maintitle=document.createElement("h2")
maintitle.innerText="Smarter meetings, all in one place"
maintitle.style.width="445px"
maintitle.style.fontSize="40px"
maintitle.style.fontWeight="900"
maintitle.style.color="rgb(40, 40, 61)"
maintitle.style.marginBottom="32px"
const infotext=document.createElement("p")
infotext.innerText="Send messages, share files, show your screen, and record your meetings — all in one workspace. Control who can join with invite-only team access, data encryption, and data export."
infotext.style.width="540px"
infotext.style.fontSize="18px"
infotext.style.fontWeight="500"
infotext.style.color="rgb(135, 135, 157)"
infoBox.appendChild(title)
infoBox.appendChild(maintitle)
infoBox.appendChild(infotext)
body.appendChild(infoBox)
const footer=document.createElement("div")
footer.style.width="100%"
footer.style.height="308px"
footer.style.backgroundColor="rgb(77, 150, 169)"
footer.style.display="flex"
footer.style.alignItems="center"
footer.style.justifyContent="center"
const footerContainer=document.createElement("div")
footerContainer.style.width="1110px"
footerContainer.style.display="flex"
footerContainer.style.alignItems="center"
footerContainer.style.justifyContent="space-between"
const footerTitle=document.createElement("h2")
footerTitle.innerText="Experience more together"
footerTitle.style.width="350px"
footerTitle.style.fontSize="40px"
footerTitle.style.fontWeight="900"
footerTitle.style.color="white"
const footerText=document.createElement("p")
footerText.innerText="Stay connected with reliable HD meetings and unlimited one-on-one and group video sessions."
footerText.style.width="350px"
footerText.style.fontSize="18px"
footerText.style.fontWeight="500"
footerText.style.color="white"
const footerBtn=document.createElement("button")
footerBtn.innerHTML="Download v1.3"
footerBtn.style.backgroundColor="rgb(133, 95, 177)"
footerBtn.style.color="white"
footerBtn.style.border="none"
footerBtn.style.padding="15px 30px"
footerBtn.style.borderRadius="30px"
footerBtn.style.fontWeight="bold"
footerContainer.appendChild(footerTitle)
footerContainer.appendChild(footerText)
footerContainer.appendChild(footerBtn)
footer.appendChild(footerContainer)
body.appendChild(footer)