def insertion_sort(values):
	for j in range(1, len(values)):
		key = values[j]
		i = j - 1
		while i >= 0 and values[i] > key:
			values[i+1] = values[i]
			i = i - 1
		values[i+1] = key

if __name__ == "__main__":
	a = [8 ,5 ,1, 6, 2]
	insertion_sort(a)
	print(a)
