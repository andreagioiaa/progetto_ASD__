#funzioni da richiamare in ciascun algoritmo per generare gli array e calcolare il tempo
import random
import time

# valore minimo ( MIN_N ) e valore massimo ( MAX_N ) numero valori all'interno di un array
MIN_N = 100
MAX_N = 100000  #100 k

# valore minimo ( MIN_M ) e valore massimo ( MAX_M ) numero di un elemento di un array 
MIN_M = 1
MAX_M = 1000000 #milione

def generaNumero( minimo, massimo ):
    return random.randint(minimo, massimo)

def creaVettore( n ):   #  100 ≤ n ≤ 100000
    vettore = [0] * n
    for j in range(n):
        vettore[j] = generaNumero(MIN_M, MAX_M)
    return vettore

def getTime():
    return time.perf_counter()