#richiamo gli algoritmi e prendo i tempi
import clock_and_generator as cg
import QuickSort as qs
import CountingSort as cs

N = cg.generaNumero (cg.MIN_N, cg.MAX_N)
arr = cg.creaVettore (N)


start = cg.getTime()
qs.test_QuickSort(1000,1000)
end = cg.getTime()


print("tempo impiegato QuickSort: {:.5f}".format(end-start))


