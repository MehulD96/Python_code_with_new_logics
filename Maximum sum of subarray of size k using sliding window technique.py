#slicing window
#Maximum sum of subarray of size k
arr = [1,32,8,4,86,8,7,41]
window = int(input("enter the window size of the subarray:"))
start_size,end_size = 0,0
sum = 0
final_list = []
count = -1
for i,j in enumerate(arr):
    if i-start_size-1 == window-1:
        end_size = i
        count +=1
    sum = sum + arr[i]

    if end_size-start_size-1 >= window-1:
        start_size = count+1
        if i == len(arr):
            break
        else:
            sum = sum-arr[count]
            final_list.append(sum)

print("the original list",arr)
print("the sum from the sliding window:",final_list)
print("maximum sum:",max(final_list))

