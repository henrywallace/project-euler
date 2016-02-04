"""The problem can be trivially solved with Python."""

for n in range(20):
	print(sum(int(x) for x in str(2**n)))



"""
2		2		1		0
4		4		1		0
8		8		1		0
16		7		2		0
32		5		3		0
64		1		4		9
128		2		4		9
256		4		4		9
512		8		4		0
1024	7		5		0
2048	5		6		9
4096	1		7		18
8192	2		7		18
"""