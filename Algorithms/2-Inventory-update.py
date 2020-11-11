def updateInventory(arr1, arr2):
    n=0
    j=0
    for i in arr1:
        for m in range(0,len(arr2)-1):
            if(arr1[j][1] == arr2[n][1]):
                arr1[j][0] = arr1[j][0] +arr2[n][0]
                arr2.pop(n)
            n=n+1
        n=0
        j=j+1
    for l in range(0,len(arr2)-1):
        arr1.append(arr2[l])
    
    arr3=sorted(arr1, key=lambda arr1: arr1[1])
    print(arr3)
    return arr1
#  Example inventory lists
curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]


updateInventory(curInv, newInv)
