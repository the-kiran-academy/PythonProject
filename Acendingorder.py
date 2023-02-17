arr=[22,55,10,2,8,15]
temp=0
#Displaying element of original array
print('Elements of original array: ')
for i in range(0,len(arr)):
    print(arr[i],end=' ')

# Sort the array in asending order
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print()
# Displaying elements of the array after sorting
print('Element of array sorted in ascending order: ')
for i in range(0,len(arr)):
    print(arr[i],end=' ')