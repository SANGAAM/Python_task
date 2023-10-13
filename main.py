import helper

arr = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    arr.append(num)

sorted_nums = helper.sort_array(arr)

print("Sorted numbers:", sorted_nums)
