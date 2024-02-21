
mapList = {"ali":"active","reza":"no-active","ahmad":"active","mohammad":"no-active"}
activeList = {}

for user,state in mapList.copy().items():
    if(state == "active"):
        activeList[user] = state
    

for i in range(len(activeList)):
    print(i,":",(list(activeList.keys()))[i])

print("active user: ",activeList)