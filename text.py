# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
# def binary_search(arr, x):
# 	low = 0
# 	high = len(arr) - 1
# 	mid = 0
#
# 	while low <= high:
# 		mid = (high + low) // 2
#
#
# 		if arr[mid] < x:
# 			low = mid + 1
#
# 		# If x is smaller, ignore right half
# 		elif arr[mid] > x:
# 			high = mid - 1
#
# 		# means x is present at mid
# 		else:print(high, low, mid); return mid
#
#
#
# 	# If we reach here, then the element was not present
# 	print(high, low, mid); return mid
#
#
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 51
#
# # Function call
# result = binary_search(arr, x)
#
# print(result)

digits = [4,3,2,1]
print(str(digits).join(","))