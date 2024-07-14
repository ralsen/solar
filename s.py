import math
import matplotlib.pyplot as plt
import numpy as np

def berechne_katheten(winkel_grad, hypotenuse):
    # Umwandeln des Winkels von Grad in Bogenmaß
    winkel_rad = math.radians(winkel_grad)
    
    # Berechnen der Kathete (gegenüberliegende Seite)
    kathete = math.sin(winkel_rad) * hypotenuse
    
    # Berechnen der Ankathete (benachbarte Seite)
    ankathete = math.cos(winkel_rad) * hypotenuse
    
    return kathete, ankathete

def zeichne_dreieck(kathete, ankathete, hypotenuse):
    # Koordinaten der Dreieckspunkte
    A = (0, 0)
    B = (ankathete, 0)
    C = (0, kathete)
    
    # Plotten des Dreiecks
    plt.figure()
    plt.plot([A[0], B[0]], [A[1], B[1]], 'k-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'k-')
    plt.plot([C[0], A[0]], [C[1], A[1]], 'k-')
    
    # Beschriften der Punkte
    plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
    plt.text(B[0], B[1], 'B', fontsize=12, ha='left')
    plt.text(C[0], C[1], 'C', fontsize=12, ha='left')
    
    # Beschriften der Seiten
    plt.text(A[0] + ankathete/2, A[1] - 0.5, f'Ankathete: {ankathete:.2f}', fontsize=10, ha='center')
    plt.text(C[0] - 0.5, C[1]/2, f'Kathete: {kathete:.2f}', fontsize=10, va='center')
    plt.text(ankathete/2, kathete/2, f'Hypotenuse: {hypotenuse:.2f}', fontsize=10, va='center')
    
    # Achsen und Titel
    plt.xlim(-1, ankathete + 1)
    plt.ylim(-1, kathete + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('X-Achse')
    plt.ylabel('Y-Achse')
    plt.title('Rechtwinkliges Dreieck')
    
    # Achsen-Ticks in kleineren Schritten festlegen
    ax = plt.gca()
    ax.xaxis.set_major_locator(plt.MultipleLocator(10))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(10))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    
    # Gitterlinien für kleinere und größere Schritte anzeigen
    ax.grid(which='both')
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    ax.grid(which='major', linestyle='-', linewidth='1.0', color='black')
    
    # Anzeigen des Plots
    plt.show()

# Beispielhafte Eingaben
winkel_grad = 40
hypotenuse = 110

kathete, ankathete = berechne_katheten(winkel_grad, hypotenuse)
print(f"Kathete (gegenüberliegende Seite): {kathete}")
print(f"Ankathete (benachbarte Seite): {ankathete}")

zeichne_dreieck(kathete, ankathete, hypotenuse)

