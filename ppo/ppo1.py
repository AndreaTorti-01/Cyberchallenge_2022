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

    # 1, 2, 3
    x = re.search("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,16}$", nuova) 
    if x == None:
        return 0

    return 1

N = int(fin.readline().strip())
for _ in range(N):
    nuova, vecchia = fin.readline().strip().split(" ")
    print(controlla(nuova, vecchia), file=fout)