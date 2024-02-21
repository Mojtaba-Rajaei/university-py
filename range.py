rangeList = list(range(10,20))
print(rangeList)

for index in rangeList:
    sumIt = sum(range(index))
    print([i for i in range(index)],end=":")
    print(sumIt)


