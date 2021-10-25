a = [64, 25, 12, 22, 11]

for i in range(len(a)):

    min_index = i
    for j in range(i+1, len(a)):
        if a[min_index] > a[j]:
            min_index = j
    
    a[min_index], a[i] = a[i], a[min_index]

print("Sorted Array:", end=' ')
for i in range(len(a)):
    print(a[i],end=' ')