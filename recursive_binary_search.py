def recursive_binary_search(arr,target):
    if len(arr)==0:
        return False
    else:
        mid =(len(arr))//2
        if arr[mid] ==target:
            return True
        else:
            if arr[mid] < target:
                return recursive_binary_search(arr[mid +1:],target)
            else:
                return recursive_binary_search(arr[:mid],target)
def verify(result):
    print("Target Found:",result)

arr=[1,2,3,4,5,6,7,8,9,10]
result =recursive_binary_search(arr,12)
verify(result)
result =recursive_binary_search(arr,8)
verify(result)