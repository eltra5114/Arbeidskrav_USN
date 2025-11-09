#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PY1010_Arbeidskrav 2

@author: Elena Tranvåg (eltra5114@usn.no)

Sist oppdatert 2025 - 11 - 8

"""

# Oppgave 1

alder = int(input("Hvilket år er du født? "))
print("I 2024 vil du være", 2024-alder)


# Oppgave 2

antall_elever = int(input("Skriv inn antall elever:" ))
print("Ved", antall_elever, " elever, vil man trenge man", int(antall_elever * 1/4), "pizzaer")


# Oppgave 3

import numpy as np
v_grad = float(input("Skriv inn gradtallet: "))
v_rad = v_grad * np.pi/180

print(f"Vinkelen {int (v_grad)} grader tilsvarer {v_rad:.2f}")


# Oppgave 4

Land = {
        "Norge":["Oslo", 0.634],
        "England": ["London",8.982],
        "Frankriket": ["Paris", 2.161],
        "Italia": ["Roma", 2.873], 
        "Spania": ["Madrid",3.416]
        }



Land_input = input("Skriv et navn på et land: " )

Hovedstad = Land [Land_input][0]
Befolkning = Land [Land_input] [1]

print(f"Hovedstad i {Land_input} er {Hovedstad}, og der bor {Befolkning: .2f} millioner folk.")

nytt_Land = input("Skriv navn på det landet du ønsker å legge til :")
Hovedstad = input(f"Hva er hovedstaden i {nytt_Land}? ")
Befolkning = float(input(f"Hva er befolningen i {nytt_Land} (i millioner)?"))

Land[nytt_Land] = [Hovedstad, Befolkning]

print(f" {Land} Dette er den nye dicitonary")

# Oppgave 5

import math
def fin_areal(a, b):
    radius = a / 2
    
    areal_halvsirkel = 0.5 * math.pi * radius**2
    
    areal_trekant = 0.5 * a * b
    
    total_areal = areal_halvsirkel + areal_trekant
    
    hypotenus = math.sqrt(a**2 + b**2)
    
    ytre_omkrets = b + hypotenus + (0.5 * math.pi * a)
    
    return total_areal, ytre_omkrets



#Oppgave 6 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return -x**2 - 5

x = np.linspace(-10, 10, 200)
y = f(x)

plt.title("Plotting av funksjon fra oppgave 6")
plt.plot(x,y, label = "f(x) = -x**2 - 5" )


    

    
    


