# 4 grafici per quicksort e quicksort3way

# codice dei due algoritmi:
import sys
sys.setrecursionlimit(10**6)  # Aumento limite ricorsione

def Scambia(A, i, j):
    """Scambia gli elementi in posizione i e j"""
    A[i], A[j] = A[j], A[i]

# QuickSort Classico (Lomuto Partition)
def Partition(A, p, q):
    """Partiziona l'array usando il pivot in posizione q"""
    x = A[q]  # Elemento pivot
    i = p - 1  # Indice del gruppo minore
    
    for j in range(p, q):
        if A[j] <= x:
            i += 1
            Scambia(A, i, j)
    
    Scambia(A, i + 1, q)  # Posiziona il pivot correttamente
    return i + 1  # Restituisce la posizione finale del pivot

def QuickSort(A, p, q):
    """Implementazione ricorsiva di QuickSort classico"""
    if p < q:
        r = Partition(A, p, q)  # Indice di partizionamento
        QuickSort(A, p, r - 1)   # Ordina la parte sinistra
        QuickSort(A, r + 1, q)   # Ordina la parte destra
    return A

# QuickSort 3-Way 
def QuickSort3Way(arr, l, r):
    """Partizionamento a 3 vie per gestire duplicati"""
    if l >= r:
        return l, r  # Caso base
    
    lt = l  # Fine della sezione < pivot
    i = l   # Puntatore corrente
    gt = r  # Inizio della sezione > pivot
    pivot = arr[l]  # Pivot iniziale

    while i <= gt:
        if arr[i] < pivot:
            Scambia(arr, i, lt)
            lt += 1
            i += 1
        elif arr[i] > pivot:
            Scambia(arr, i, gt)
            gt -= 1
        else:
            i += 1  # Elemento uguale al pivot
    
    QuickSort3Way(arr, l, lt - 1)  # Ordina elementi minori
    QuickSort3Way(arr, gt + 1, r)  # Ordina elementi maggiori
    return lt, gt  # Restituisce i confini delle partizioni

# codice grafici:

import time
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Misurazione risoluzione clock
def measure_clock_resolution():
    start = time.perf_counter()
    while time.perf_counter() == start:
        pass
    return time.perf_counter() - start

# 2. Sequenza geometrica per campionamento
def geometric_sequence(start, end, num=100):
    ratio = (end / start) ** (1/(num-1))
    return [int(start * ratio**i) for i in range(num)]

# 3. Misura tempo medio inizializzazione
def measure_init_time(n, m, T_min):
    count = 0
    start = time.perf_counter()
    while True:
        arr = [random.randint(1, m) for _ in range(n)]
        count += 1
        if time.perf_counter() - start >= T_min:
            break
    return (time.perf_counter() - start) / count

# 4. Misura tempo medio esecuzione algoritmo
def measure_sort_time(n, m, algo, T_min, init_time):
    count = 0
    start = time.perf_counter()
    
    while True:
        arr = [random.randint(1, m) for _ in range(n)]
        
        if algo == "QuickSort":
            QuickSort(arr.copy(), 0, len(arr)-1)
        else:
            QuickSort3Way(arr.copy(), 0, len(arr)-1)
        
        count += 1
        end_time = time.perf_counter()
        if end_time - start >= T_min:
            break
    
    total_avg = (end_time - start) / count
    return total_avg - init_time  # Sottrae tempo inizializzazione

# 5. Configurazione esperimenti
R = measure_clock_resolution()
T_min = 1.5 * R  # Formula progetto: R*(1/2 + 1)
print(f"Risoluzione clock: {R:.2e}s, T_min: {T_min:.2e}s")

n_values = geometric_sequence(100, 100000)
m_values = geometric_sequence(10, 1000000)
algorithms = ["QuickSort", "QuickSort3Way"]

# 6. Raccolta dati
results = []
for algo in algorithms:
    # Variazione n (m fisso a 100000)
    for n in n_values:
        init_time = measure_init_time(n, 100000, T_min)
        sort_time = measure_sort_time(n, 100000, algo, T_min, init_time)
        results.append({"n": n, "m": 100000, "algo": algo, "time": sort_time})
    
    # Variazione m (n fisso a 10000)
    for m in m_values:
        init_time = measure_init_time(10000, m, T_min)
        sort_time = measure_sort_time(10000, m, algo, T_min, init_time)
        results.append({"n": 10000, "m": m, "algo": algo, "time": sort_time})

df = pd.DataFrame(results)

# 7. Generazione grafici
def plot_comparison(df, x_var, hue, title):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=x_var, y="time", hue=hue, style=hue, markers=True)
    plt.title(title, fontsize=14)
    plt.xlabel(x_var, fontsize=12)
    plt.ylabel("Tempo medio (s)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_')}.png")
    plt.show()
    
    # Plot log-log
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x=x_var, y="time", hue=hue, style=hue, markers=True)
    plt.xscale("log")
    plt.yscale("log")
    plt.title(f"Log-Log: {title}", fontsize=14)
    plt.xlabel(x_var, fontsize=12)
    plt.ylabel("log(Tempo)", fontsize=12)
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"LogLog_{title.replace(' ', '_')}.png")
    plt.show()

# Grafici comparativi
df_n = df[df["m"] == 100000]
plot_comparison(df_n, "n", "algo", "Tempo di esecuzione vs n (m=100000)")

df_m = df[df["n"] == 10000]
plot_comparison(df_m, "m", "algo", "Tempo di esecuzione vs m (n=10000)")
