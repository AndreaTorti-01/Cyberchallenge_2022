import tkinter
from tkinter.filedialog import askopenfilename
import re 

root = tkinter.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)

fin = open(askopenfilename(initialdir = "D:\_Download"), 'r')
fout = open("output.txt", 'w')

def controlla(nuova, vecchia):
    # SCRIVI QUA IL TUO CODICE
    # RITORNA 0 SE LA NUOVA PASSWORD NON SEGUE LE SPECIFICHE
    # RITORNA 1 SE LA NUOVA PASSWORD SEGUE LE SPECIFICHE

    # 2
    if len(nuova) > 16:
        return 0

    # 1, 3, 4
    x = re.search("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_'()]).{8,}$", nuova) 
    if x == None:
        return 0

    # 5
    for i in range(len(nuova) - 1):
        if nuova[i] == nuova[i+1]:
            return 0

    return 1

N = int(fin.readline().strip())
for _ in range(N):
    nuova, vecchia = fin.readline().strip().split(" ")
    print(controlla(nuova, vecchia), file=fout)