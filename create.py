import os
titletext=input("title: ")
description=input("description: ")
a=""
actions=""
while a!="exit":
	a=input("where to go? ")
	if a!= "exit":
		funct=input("button function: ")
		textofbutton=input("button text: ")
		actions+=f"<button onclick=\"{funct}\">{textofbutton}</button><!--this is a button that preforms the function of {textofbutton} it calls the function {funct}-->\r"
template=f"<DOCTYPE HTML>\r<html>\r<head><title>{titletext}</title><!--set the title-->\r<link rel=\"icon\" type=\"image/x-icon\" href=\"/assents/favicon.ico\"><!--set the favicon-->\r<link rel=\"stylesheet\" href=\"/assets/main.css\"><!--set the css file destinaton--><script type=\"module\" src=\"/assets/main.js\"><!--import the javascript-->\r</head>\r<body><p>{description} \r{actions}\r</body>\r</html>"
fileofyou=open(input("filename: "),"w")
with fileofyou as files:
	files.write(template)
fileofyou.close()