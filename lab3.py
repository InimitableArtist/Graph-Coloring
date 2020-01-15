# -*- coding: utf-8 -*-

from math import sqrt

def procitajFile(fileName):
    with open(fileName, "r") as f:
        next(f)
        matrica = f.read().splitlines()
    f.close()
    matricaSusjedstva = []
    m = [i.replace(" ", "") for i in matrica if i != ""]
    for i in m:
        
        for j in i:
            
            matricaSusjedstva.append(int(j))
    return matricaSusjedstva



def provjeri(graf, vrh, boje, c, n):
   
    for i in range(n):
        if graf[vrh*n + i] == 1 and boje[i] == c:
            return False
    return True



def oboji(brojBoja, graf, boje, vrh, n):
    
    if vrh == n:
        return True
    
    
    for c in range(1, brojBoja + 1):
        if provjeri(graf, vrh, boje, c, n):
            boje[vrh] = c
            
            if(oboji(brojBoja, graf, boje, vrh + 1, n)):
                return True
            
            boje[vrh] = 0
            
    return False
            
def bojanjeGrafa(graf, brojBoja, n):
    
    
    boje = [0 for i in range(n)]
    
    if not (oboji(brojBoja, graf, boje, 0, n)):
        return False
    return True
            


def main():
    matricaSusjedstva = procitajFile("graf.txt")
    
    
    brojVrhova = int(sqrt(len(matricaSusjedstva)))
    
    for i in range(1, len(matricaSusjedstva)):
        if (bojanjeGrafa(matricaSusjedstva, i, brojVrhova)):
            print("Kromatski broj grafa je: ", i)
            break
    
    
    
if __name__ == "__main__":
    main()    