import tkinter
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

fin = open(askopenfilename(initialdir = "D:\_Download"), 'r')
fout = open("output.txt", 'w')

N, K = map(int, fin.readline().strip().split(" "))
ranges = []

for _ in range(N):
    start, end = map(int, fin.readline().strip().split(" "))
    ranges.append([start, end])

ranges.sort()

open_ranges = []
out = 0
prev = 0

for start, end in ranges:
    open_ranges.sort()

    if len(open_ranges) == K:
        out += start - prev
    elif len(open_ranges) > K and open_ranges[-K] < start:
        out += open_ranges[-K] - open_ranges[-K-1]

    c = 0
    for r in open_ranges:
        if r >= start:
            break
        c += 1
    open_ranges = open_ranges[c:]

    open_ranges.append(end)
    prev = start

open_ranges.sort()
if len(open_ranges) == K:
    out += open_ranges[0] - start
elif len(open_ranges) > K:
    out += open_ranges[-K] - open_ranges[-K-1]

print(out, file=fout)