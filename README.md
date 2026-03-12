[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tKFkieDb)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23040446)
﻿# DAFE1000-oblig-template


Name: Celine Tuong Khanh Tang
Oslomet email address: cetan2605@oslomet.no


# Oppgave - innlevering nr.2

Vi ser på funksjonen:  f(x) = e^{-x/4} arctan(x)
Funksjonen har et maksimalpunlt. 
Vi skal viser at toppunktet er bestemt av likningen: arctan(x) - 4/(x^2 + 1) = 0 

__

## Analytisk løsning

Funksjonen er et produkt av 2 funksjoner:
u(x) = e^{-x/4}
v(x) = arctan(x)

Ved produktregelen:
f'(x) = u'(x)v(x) + u(x)v'(x)

Vi får: 
u'(x) = -1/4 e^{-x/4}
v'(x) = 1/(1 + x^2)

Dermed: 
f'(x) = e^{-x/4} (-1/4 arctan(x) + 1/(1 + x^2))

For toppunkt må f'(x)=0.

Siden e^{-x/4} aldri er 0 må parentesen være 0: 
-1/4 arctan(x) + 1/(1 + x^2) = 0

Multiplikasjon med 4 gir:
arctan(x) - 4/(x^2 + 1) = 0

Dermed er toppunktet bestemt av denne likningen. 

__

## Numerisk løsning

Likningen ble løst numerisk i Python.

Resultatet ble x ≈ 0.6786

Toppunktet er derfor (1.7744 , 0.6786)

__

## Plot av funksjonen 

Plottet under viser funksjonen og toppunktet. 
![Plot](plots/plot.png)


