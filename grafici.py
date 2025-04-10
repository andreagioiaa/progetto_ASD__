import seaborn as sb
import matplotlib.pyplot as plt
import misurazioni

def creaGrafico(df):
    """
    Crea uno scatter plot comparativo con n in ascissa e t(n) in ordinata
    
    Args:
        df (pandas.DataFrame): DataFrame generato da creaDataFrame()
    """
    plt.figure(figsize=(12, 7))
    
    # Prepara i dati in formato long
    df_long = df.melt(id_vars=['Dimensione'], 
                      value_vars=['QuickSort', 'CountingSort', 'QuickSort3Way'],
                      var_name='Algoritmo',
                      value_name='t(n)')
    
    # Scatter plot con Seaborn
    sb.scatterplot(data=df_long,
                   x='Dimensione',
                   y='t(n)',
                   hue='Algoritmo',
                   style='Algoritmo',
                   palette='dark',
                   s=80,
                   alpha=0.9)
    
    # Formattazione matematica degli assi
    plt.xlabel('n (dimensione input)', fontsize=13, labelpad=10)
    plt.ylabel('t(n) (tempo esecuzione)', fontsize=13, labelpad=10)
    
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
    return 0

# Genera il grafico
creaGrafico( misurazioni.creaDataFrame(  ) )