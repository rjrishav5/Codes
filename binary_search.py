def binary_search(arr,target):
    first =0
    last = len(arr)-1
    while(first <= last):
        midpoint =(first +last)//2
        if arr[midpoint]==target:
            return midpoint
        elif arr[midpoint]<target:
            first =midpoint +1
        else:
            last=midpoint-1
def verify(index):
    if index is not None:
        print("The position of index is :" ,index)   
    else:
        print("Target Not Found") 


arr=[1,2,3,4,5,6,7,8,9,10]
a =binary_search(arr,12)
verify(a)
a =binary_search(arr,8)
verify(a)    