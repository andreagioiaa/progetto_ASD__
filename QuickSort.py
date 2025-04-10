def QuickSort( A, p, q ):
    if( p < q ):
        r = Partition( A, p, q)
        QuickSort( A, p, r-1 )
        QuickSort( A, r+1, q )
    return A

def Partition(A, p, q):
    x = A[q]
    i = p - 1
    for j in range(p, q):
        if A[j] <= x:  # (corretto A[j], non A[q])
            i += 1
            Scambia(A, i, j)
    Scambia(A, i + 1, q)  # posiziona il pivot al centro
    return i + 1

def Scambia(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def test_QuickSort( A_length, n_volte ):
    inizio = 0
    fine = A_length-1
    for j in range( n_volte ):
        vettore = creaVettore( A_length )
        msg = "ESEMPIO " + str(j+1) + "\n"
        msg += "VETTORE DI PARTENZA\n" + str(vettore) 
        msg += "\nVETTORE ORDINATO\n" + str(QuickSort( vettore, inizio, fine ))
        #print( msg )
    return 0

#test_QuickSort( 10, 10)