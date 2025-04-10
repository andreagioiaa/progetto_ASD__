#importazione  moduli ( per ora senza simulativo )
import clock_and_generator
import QuickSort
import CountingSort
import QuickSort3Way
import csv
import matplotlib.pyplot as plt
import numpy as np

# valore minimo ( MIN_N ) e valore massimo ( MAX_N ) numero valori all'interno di un array
MIN_N = 100
MAX_N = 100000  #100 k

# valore minimo ( MIN_M ) e valore massimo ( MAX_M ) numero di un elemento di un array 
MIN_M = 10
MAX_M = 1000000 #milione

# commentato ==> si può togliere?
'''
N = clock_and_generator.generaNumero (clock_and_generator.MIN_N, clock_and_generator.MAX_N) 
arr = clock_and_generator.creaVettore (N)


start = clock_and_generator.getTime()
QuickSort.test_QuickSort(1000,1000)
end = clock_and_generator.getTime()


print("Tempo impiegato QuickSort: {:.5f}".format(end-start))


start = clock_and_generator.getTime()
QuickSort3Way.QuickSort3Way(arr, 0, len(arr)-1)
end = clock_and_generator.getTime()

print("Tempo QuickSort3Way: {:.5f}".format(end-start))


start = clock_and_generator.getTime()
CountingSort.countingSort(arr)
end = clock_and_generator.getTime()

print("Tempo CountingSort: {:.5f}".format(end-start))
'''

# misurazioni algoritmo: QuickSort
def misurazioni_QuickSort( n_range ):
    print("Creo misurazioni QuickSort...\n")
    dati_misurazioni = []
    for i in range( n_range ):
        array = clock_and_generator.creaVettore( clock_and_generator.generaNumero(MIN_N, MAX_N) )
        start = clock_and_generator.getTime()
        QuickSort.QuickSort( array, 0, (len(array)-1) )
        end = clock_and_generator.getTime()
        dati_misurazioni.append((len(array), "{:.8f}".format(end - start)))
        # clock_and_generator.creaFileCSV(dati_misurazioni, "QuickSort--da--misurazioni")
    return dati_misurazioni

# misurazioni algoritmo: CountingSort
def misurazioni_CountingSort( n_range ):
    print("Creo misurazioni CountingSort...\n")
    dati_misurazioni = []
    for i in range( n_range ):
        array = clock_and_generator.creaVettore( clock_and_generator.generaNumero(MIN_N, MAX_N) )
        start = clock_and_generator.getTime()
        CountingSort.countingSort(array)
        end = clock_and_generator.getTime()
        dati_misurazioni.append((len(array), "{:.8f}".format(end - start)))
    return dati_misurazioni

# misurazioni algoritmo: QuickSort3Way
def misurazioni_QuickSort3Way( n_range ):
    print("Creo misurazioni QuickSort3Way...\n")
    dati_misurazioni = []
    for i in range( n_range ):
        array = clock_and_generator.creaVettore( clock_and_generator.generaNumero(MIN_N, MAX_N) )
        start = clock_and_generator.getTime()
        QuickSort3Way.QuickSort3Way(array, 0, len(array)-1)
        end = clock_and_generator.getTime()
        dati_misurazioni.append((len(array), "{:.8f}".format(end - start)))
    return dati_misurazioni


# GRAFICI VARI
# n ascissa
# t ( n ) ==> ordinata

def creaFileCSV_misurazioni( n_range = 10 ):
    """
    Genera un file CSV con le misurazioni fornite.
    
    Args:
        misurazioni (list): Lista di tuple contenenti i valori ( n, t(n) )
        nome_algoritmo_test: Nome dell'algoritmo di scrittura dati
    """

    # Intestazioni del file CSV
    filename = "Resoconto.csv"
    field = ["n", "t(n)"]

    # Scrivo sul file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        
        # QuickSort
        writer.writerow(["QuickSort"])
        writer.writerow(field)
        writer.writerows(misurazioni_QuickSort( n_range))

        writer.writerow("\n\n\n")

        # CountingSort
        writer.writerow(["CountingSort"])
        writer.writerow(field)
        writer.writerows(misurazioni_CountingSort( n_range ))

        writer.writerow("\n\n\n")

        # QuickSort3Way
        writer.writerow(["QuickSort3Way"])
        writer.writerow(field)
        writer.writerows(misurazioni_QuickSort3Way( n_range ))

    
    print(f"File '{filename}' generato con successo nella cartella corrente.")
    apri_resoconto()
    return 0

def apri_resoconto(filename="Resoconto.csv"):
    """
    Apre e legge un file CSV, stampandone il contenuto.
    
    Args:
        filename (str): Nome del file CSV da aprire (default: "Resoconto.csv")
    
    Returns:
        list: Contenuto del file come lista di righe (opzionale)
    """
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')  # Assumendo separatore ;
            contenuto = list(reader)  # Converti in lista
            
            # Stampa il contenuto con formattazione
            print(f"Contenuto di '{filename}':")
            for riga in contenuto:
                print(" | ".join(riga))
            
            return contenuto  # Opzionale: restituisce i dati
    
    except FileNotFoundError:
        print(f"Errore: il file '{filename}' non esiste.")
        return None
    except Exception as e:
        print(f"Errore durante la lettura: {str(e)}")
        return None

creaFileCSV_misurazioni( 50 )
# py misurazioni.py