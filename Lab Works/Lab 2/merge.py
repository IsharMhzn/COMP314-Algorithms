def merge_sort(values, p, r):
	if p < r:
		q = (p+r)//2
		merge_sort(values, p , q)
		merge_sort(values, q+1, r)
		merge(values, p, q, r)

def merge(values, p, q, r):
	L = values[p:q+1]
	R = values[q+1:r+1]
	i, j, n1, n2 = 0, 0, q-p+1, r-q
	for k in range(p, r):
		if L[i] <= R[j]:
			values[k] = L[i]
			i += 1
			if i == n1:
				while j < n2:
					values[k+1] = R[j]
					j += 1
					k += 1
				break
		else:
			values[k] = R[j]
			j += 1
			if j == n2:
				while i < n1:
					values[k+1] = L[i]
					k += 1
					i += 1
				break