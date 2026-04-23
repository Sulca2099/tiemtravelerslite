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
		actions+=f"\t\t<button class=\"{["claimitem","goroom","executeact"][int(input("claim item=0\rgoto room=1\rdo something=2\r"))]}\"onclick=\"{funct}\">{textofbutton}</button><!--this is a button that preforms the function of {textofbutton} it calls the function {funct}-->\r"
template=f"<!DOCTYPE html>\r<html lang=\"en\"><!--the head for the html file set to english-->\r\t<head><!--defines the head of the html file-->\r\t\t<title>{titletext}</title><!--set the title-->\r\t\t<link rel=\"icon\" type=\"image/x-icon\" href=\"assets/favicon.ico\"><!--set the favicon-->\r\t\t<link rel=\"stylesheet\" href=\"assets/main.css\"><!--set the css file destinaton-->\r\t\t<script src=\"assets/main.js\"></script><!--import the javascript-->\r\t</head>\r\t<body><!--define the body of the Website-->\r\t\t<p>\r\t\t\t{description}\r\t\t</p> \r{actions}\r\t</body>\r</html>"
fileofyou=open(input("filename: "),"w")
with fileofyou as files:
	files.write(template)
fileofyou.close()
