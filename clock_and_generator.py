#funzioni da richiamare in ciascun algoritmo per generare gli array e calcolare il tempo
import random
import time


MIN_N = 100
MAX_N = 100000  #100 k

MIN_M = 10
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