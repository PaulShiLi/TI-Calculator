import json
import os

realPath = os.getcwd()
path = "/stat/resources"

with open(f"{realPath}{path}/lists.json", "r") as f:
	lists = json.load(f)
listkeys = [key for key in lists.keys()]

def NumLimit(Num, characterLimit: int):
	Num = str(Num)
	if len(Num) > characterLimit:
		Num = f"{Num[0:characterLimit-3]}..."
	return Num

def terminalList():
	maxview = 7
	listCount = "0-2"
	totalList = 7
	characterCount = 10
	while True:
		L1Key = listkeys[int(listCount.split("-")[0])]
		L2Key = listkeys[int(listCount.split("-")[0]) + 1]
		L3Key = listkeys[int(listCount.split("-")[-1])]
		L1 = lists[L1Key]
		L2 = lists[L2Key]
		L3 = lists[L3Key]
		heading = f"{L1Key}{(characterCount - len(L1Key))*' '}|{L2Key}{(characterCount - len(L1Key))*' '}|{L3Key}{(characterCount - len(L1Key))*' '}"
		splitter = f"{characterCount*'-'}|{characterCount*'-'}|{characterCount*'-'}"
		finalSplitter = f"{characterCount*3*'_'}{2*'_'}"
		
terminalList()