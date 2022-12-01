import tkinter
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

fin = open(askopenfilename(initialdir = "D:\_Download"), 'r')
fout = open("output.txt", 'w')

def swap(N, V):
    for i in range(N):
        if V[i] != i:
            wrong = i
            break
    err_size = abs(V.index(wrong) - wrong)
    return err_size

N = int(fin.readline().strip())
V = list(map(int, fin.readline().strip().split(" ")))
print(swap(N, V), file=fout)
