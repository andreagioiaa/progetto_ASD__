import seaborn as sb
import matplotlib.pyplot as plt
import misurazioni

def creaGrafico( df ):
    """
    Crea uno scatter plot comparativo con n in ascissa e t(n) in ordinata
    
    Args:
        df (pandas.DataFrame): DataFrame generato da creaDataFrame()
    """
    fig = plt.figure(figsize=(12, 7))
    
    # Prepara i dati in formato long
    df_long = df.melt(id_vars=['Dimensione'], 
                      value_vars=['QuickSort', 'CountingSort', 'QuickSort3Way'],
                      var_name='Algoritmo',
                      value_name='t(n)')
    
    # Palette di colori personalizzata
    palette = {'QuickSort': '#1f77b4', 
               'CountingSort': '#ff7f0e', 
               'QuickSort3Way': '#2ca02c'}

    # Scatter plot con Seaborn
    sb.scatterplot(data=df_long,
                   x='Dimensione',
                   y='t(n)',
                   hue='Algoritmo',
                   style='Algoritmo',
                   palette='dark',
                   s=80,
                   alpha=0.9)

    # Aggiungi rette di regressione per ogni algoritmo
    for algoritmo in df_long['Algoritmo'].unique():
        sb.regplot(data=df_long[df_long['Algoritmo'] == algoritmo],
                   x='Dimensione',
                   y='t(n)',
                   scatter=False,  # Non sovrascrivere gli scatter esistenti
                   color=palette[algoritmo],
                   #line_kws={'linestyle': '--', 'alpha': 0.5, 'label': f'Trend {algoritmo}'},
                   )  # Disabilita intervalli di confidenza
    
    # Formattazione matematica degli assi
    plt.xlabel('n', fontsize=13, labelpad=10)
    plt.ylabel('t(n)', fontsize=13, labelpad=10)
    
    # Titolo e griglia
    plt.title('Complessità temporale degli algoritmi', pad=20, fontsize=15)
    plt.grid(True, linestyle=':', alpha=0.7)
    
    # Legenda posizionata in alto a sinistra
    plt.legend(title='Algoritmi', 
               loc='upper left',
               framealpha=1)
    
    # Formattazione assi per evitare notazione scientifica
    plt.ticklabel_format(style='plain', axis='both')
    
    # Mostra il grafico
    plt.tight_layout()
    plt.show()
    fig.savefig("Grafico.png")
    return 0

# utility ==> DataFrame contenente i dati globali delle misurazioni
if( misurazioni.esiste_resoconto() ):
    df = misurazioni.leggiDF_CSV()
else:
    # creo il DataFrame
    df = misurazioni.creaDataFrame()
    # creo il file CSV contenente le misurazioni effettuate
    misurazioni.creaFileCSV_misurazioni( df )

# creo il grafico
creaGrafico( df )