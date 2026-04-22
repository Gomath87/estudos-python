# -*- coding: utf-8 -*-

def linha():
    print("-"*39)
def traco():
    print(f"{'|':<37} {'|'}")
def um():
    print(f"|{'x = 35':<37}|")
def dois():
    print(f"|{'x = 35':^37}|")
def tres():
    print(f"|{'x = 35':>37}|")

#programa principal

linha()
um()
traco()
dois()
traco()
tres()
linha()