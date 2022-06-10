import json,requests as req,os

def show():
	user = input("Input Chanel username : ")
	url  ="https://tufaah.osc-fr1.scalingo.io/telegram-msgs/?user={}&onlyRemoved=1".format(user)
	res  = req.get(url)
	json = res.json()
	data = json["messages"]

	for i in data:
		dele = i["deleted"]
		mese = i["msg"]
		post = i["posted"]

		print("=="*16)
		print("\n [!] time posted :",post,"\n","[!] time delete :",dele,"\n","[-] messages :\n",mese,"\n\n")
		print("=="*16)

os.system('clear')
show()

