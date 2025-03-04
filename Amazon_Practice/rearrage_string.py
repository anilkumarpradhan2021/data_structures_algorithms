from collections import Counter
s = "aab"
import heapq


def rearrange_string(s):
	count_letter = Counter(s)
	
	# create a min heap
	# create a array which contain tuples , element like this (ch,number_ch)
	heap_array = []
	for key,value in count_letter.items():
		heapq.heappush(heap_array,(key,-value))
		print(key,value)
	
	
	print(heap_array)
	
	result = ""
	last_ch = ""
	while len(heap_array) > 0:
		ch,ch_frequency = heapq.heappop(heap_array)
		result = result + ch
		last_ch = ch
		if last_ch == ch:
			result = ""
			break

		ch_frequency = ch_frequency + 1
		if ch_frequency !=0:
			heapq.heappush(heap_array,(ch,ch_frequency))
	print("result", result)
	print(heap_array)

if __name__ == "__main__":
	print("Hi")
	rearrange_string(s)