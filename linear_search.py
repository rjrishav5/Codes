def linear_search(arr,target):
    for i in range(0,len(arr)):
        if arr[i] ==target:
            return i
    return None

def verify(index):
    if index is not None:
        print("The position of index is :" ,index)   
    else:
        print("Target Not Found") 

arr=[1,2,3,4,5,6,7,8,9,10]
a =linear_search(arr,12)
verify(a)
a =linear_search(arr,8)
verify(a)