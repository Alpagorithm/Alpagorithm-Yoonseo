target = 6
nums = [1, 3, 5, 6]

low, high = 0, len(nums)-1

while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < nums[high]:
        low = mid + 1
    else:
        high = mid - 1
