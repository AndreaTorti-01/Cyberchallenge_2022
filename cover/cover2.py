import tkinter
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

fin = open(askopenfilename(initialdir = "D:\_Download"), 'r')
fout = open("output.txt", 'w')

MAX = 10000
def conta(K, ranges):

    num = [0] * (MAX+1)
    numofKnums = 0

    for i in range(MAX+1):
        for rangeX in ranges:
            if i>=rangeX[0] and i<=rangeX[1]:
                num[i] += 1
    
    for n in num:
        if n == K:
            numofKnums += 1

    return numofKnums


N, K = map(int, fin.readline().strip().split(" "))
ranges = []

for _ in range(N):
    start, end = map(int, fin.readline().strip().split(" "))
    ranges.append([start, end])

print(conta(K, ranges), file=fout)
