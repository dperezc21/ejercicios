arr = [3,1,5,5,8,1]

arr = list(reversed(sorted(arr)))
for i in range(len(arr)):
  if arr[i] > arr[i+1]:
    print(arr[i+1])
    break
