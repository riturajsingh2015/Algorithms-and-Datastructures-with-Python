# bSearch in Reverse Sorted Array
def bSearch(arr,key):
    try:
        mid=len(arr)//2
        if key==arr[mid]:
            return (True)
        elif key > arr[mid]:
            return bSearch(arr[:mid],key)
        elif key < arr[mid]:
            return bSearch(arr[mid+1:],key)
    except IndexError:
        return False


arr=[10,9,8,7,6,3,2,1]
print(arr)
key=int(input('Enter the Element you want to Search :'))
print(bSearch(arr,key))
