def binarySearch(myList, item):
    low = 0
    high = len(myList) - 1 
    while low <= high:
        mid = (low + high)
        guess = myList[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
 
myList = [1, 3, 5, 7, 9]
print(binarySearch(myList, 5))
print(binarySearch(myList, -3))  