import os
import json

RealPath = os.getcwd()

class IntegrityCheck:
	def __init__(self):
		self.checkResources()
	def checkResources(self):
		files = ["settings.json", "lists.json", "RAM.json"]
		path = "/stat/resources"
		resourceFiles = os.listdir(RealPath + path)
		for file in files:
			if str(file) not in resourceFiles:
				with open(f"{RealPath}{path}/{file}", "w") as f:
					if ".json" in file:
						json.dump({}, f)
					f.close()
				if "lists.json" in file:
					self.createList()
				if "RAM.json" in file:
					self.createRAM()
	def createList(self, limit:int=6):
		path = "/stat/resources"
		with open(f"{RealPath}{path}/lists.json", "r") as f:
			lists = json.load(f)
		#Create Lists just in case Lists have no variable
		[lists.update({f"L{n}":[]}) for n in range(limit)]
		with open(f"{RealPath}{path}/lists.json", "w") as g:
			json.dump(lists, g)
			g.close()
	def createRAM(self):
		path = "/stat/resources"
		with open(f"{RealPath}{path}/RAM.json", "r") as f:
			values = json.load(f)
		alphabets = "ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
		[values.update({alphabet: 0.0}) for alphabet in alphabets]
		values.update({"ans": 0.0})
		with open(f"{RealPath}{path}/RAM.json", "w") as f:
			values = json.dump(values, f)

IntegrityCheck()