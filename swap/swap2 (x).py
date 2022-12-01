import tkinter
from tkinter.filedialog import askopenfilename

swaXXX = 0

root = tkinter.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

fin = open(askopenfilename(initialdir = "D:\_Download"), 'r')
fout = open("output.txt", 'w')

def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if   arr[j] <= x:
  
            # increment index of smaller element
            i = i+1
            swaXXX += 1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr,l,h):

    swapX = 0
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return swapX

def swap(N, V):
    for i in range(N):
        if V[i] > V[i+1]:
            break
    if max(V[i-1:i+2]) == V[i]: # elemento piccolo in avanti
        wrong = V[i+1]
        wrong_i = i+1
        V_rev = V[::-1]

        occ = 0
        for i in range(N):
            if V_rev[i] == wrong:
                occ += 1
            if occ == 2:
                break

        last_place_i_similar = N-i

        
        return quickSortIterative(V, last_place_i_similar, wrong_i)

    else: # elemento grosso indietro
        wrong = V[i]
        wrong_i = i

    return 0


N = int(fin.readline().strip())
V = list(map(int, fin.readline().strip().split(" ")))
print(swap(N, V), file=fout)
