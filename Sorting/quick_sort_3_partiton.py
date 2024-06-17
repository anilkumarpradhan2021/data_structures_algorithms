""""
https://www.simplilearn.com/tutorials/data-structure-tutorial/quick-sort-algorithm#:~:text=Space%20Complexity,stack%20in%20the%20worst%20case.

"""

def quick_sort(arr):
	if len(arr) <=1 :
		return arr	
	# Left partition with elements < Pivot
	pivot = arr[len(arr)//2]
	left = [x for x in arr if x < pivot]
	# medium partition with elements < Pivot
	medium = [x for x in arr if x == pivot]
	# right partition with elements > Pivot
	right = [x for x in arr if x > pivot]
	return quick_sort(left) + medium + quick_sort(right)


if __name__ == "__main__":
	arr = [12, 23, 1, 24, 111, 34, 1, 12, 2 ]
	print(arr)
	a = quick_sort(arr)
	print(a)