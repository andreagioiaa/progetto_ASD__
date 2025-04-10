#importazione  moduli ( per ora senza simulativo )
import clock_and_generator
import QuickSort
import CountingSort
import QuickSort3Way
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # type: ignore

# valore minimo ( MIN_N ) e valore massimo ( MAX_N ) numero valori all'interno di un array
MIN_N = 100
MAX_N = 100000  #100 k

# valore minimo ( MIN_M ) e valore massimo ( MAX_M ) numero di un elemento di un array 
MIN_M = 10
MAX_M = 1000000 #milione

# numero di misurazioni per ogni algoritmo di ordinamento
N_MIS = 30

# misurazioni algoritmo: QuickSort ==> return: array di tuple con valori di n e t(n)
def misurazioni_QuickSort():
    print("Creo misurazioni QuickSort...\n")
    dati_misurazioni = []
    for i in range( N_MIS ):
        array = clock_and_generator.creaVettore( clock_and_generator.generaNumero(MIN_N, MAX_N) )
        start = clock_and_generator.getTime()
        QuickSort.QuickSort( array, 0, (len(array)-1) )
        end = clock_and_generator.getTime()
        dati_misurazioni.append((len(array), "{:.8f}".format(end - start)))
        # clock_and_generator.creaFileCSV(dati_misurazioni, "QuickSort--da--misurazioni")
    return dati_misurazioni

# misurazioni algoritmo: CountingSort ==> return: array di tuple con valori di n e t(n)
def misurazioni_CountingSort():
    print("Creo misurazioni CountingSort...\n")
    dati_misurazioni = []
    for i in range( N_MIS ):
        array = clock_and_generator.creaVettore( clock_and_generator.generaNumero(MIN_N, MAX_N) )
        start = clock_and_generator.getTime()
        CountingSort.countingSort(array)
        end = clock_and_generator.getTime()
        dati_misurazioni.append((len(array), "{:.8f}".format(end - start)))
    return dati_misurazioni

# misurazioni algoritmo: QuickSort3Way ==> return: array di tuple con valori di n e t(n)
def misurazioni_QuickSort3Way():
    print("Creo misurazioni QuickSort3Way...\n")
    dati_misurazioni = []
    for i in range( N_MIS ):
        array = clock_and_generator.creaVettore( clock_and_generator.generaNumero(MIN_N, MAX_N) )
        start = clock_and_generator.getTime()
        QuickSort3Way.QuickSort3Way(array, 0, len(array)-1)
        end = clock_and_generator.getTime()
        dati_misurazioni.append((len(array), "{:.8f}".format(end - start)))
    return dati_misurazioni

def creaDataFrame():
    """
    Crea un DataFrame pandas contenente i tempi di esecuzione per QuickSort, CountingSort e QuickSort3Way
    
    Args:
        n_range (int): Numero di misurazioni da effettuare per ciascun algoritmo
        
    Returns:
        pandas.DataFrame: DataFrame con colonne ['Dimensione', 'QuickSort', 'CountingSort', 'QuickSort3Way']
    """
    # Esegui le misurazioni per ciascun algoritmo
    mis_quick = misurazioni_QuickSort()
    mis_counting = misurazioni_CountingSort()
    mis_quick3way = misurazioni_QuickSort3Way()
    
    # Crea dizionari temporanei per facilitare la creazione del DataFrame
    data = {}
    
    # Aggiungi i dati al dizionario
    for dim, time in mis_quick:
        if dim not in data:
            data[dim] = {}
        data[dim]['QuickSort'] = float(time)
    
    for dim, time in mis_counting:
        if dim not in data:
            data[dim] = {}
        data[dim]['CountingSort'] = float(time)
    
    for dim, time in mis_quick3way:
        if dim not in data:
            data[dim] = {}
        data[dim]['QuickSort3Way'] = float(time)
    
    # Converti il dizionario in una lista di tuple per la creazione del DataFrame
    rows = []
    for dim in sorted(data.keys()):
        row = {
            'Dimensione': dim,
            'QuickSort': data[dim].get('QuickSort', None),
            'CountingSort': data[dim].get('CountingSort', None),
            'QuickSort3Way': data[dim].get('QuickSort3Way', None)
        }
        rows.append(row)
    
    # Crea il DataFrame
    df = pd.DataFrame(rows)
    
    # Riordina le colonne
    df = df[['Dimensione', 'QuickSort', 'CountingSort', 'QuickSort3Way']]
    
    return df
# GRAFICI VARI
# n ascissa
# t ( n ) ==> ordinata

def creaFileCSV_misurazioni():
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
        writer.writerows(misurazioni_QuickSort( ))

        writer.writerow("\n\n\n")

        # CountingSort
        writer.writerow(["CountingSort"])
        writer.writerow(field)
        writer.writerows(misurazioni_CountingSort(  ))

        writer.writerow("\n\n\n")

        # QuickSort3Way
        writer.writerow(["QuickSort3Way"])
        writer.writerow(field)
        writer.writerows(misurazioni_QuickSort3Way(  ))

    
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

creaFileCSV_misurazioni()
# py misurazioni.py