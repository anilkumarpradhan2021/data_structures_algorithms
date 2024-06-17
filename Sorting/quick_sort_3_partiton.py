""""
Variation	    Time Complexity	    Space Complexity
Best Case	    O(n log n)	        O(log n)
Average Case	O(n log n)	        O(log n)
Worst Case	    O(n^2)	            O(n)

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
