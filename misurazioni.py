#richiamo gli algoritmi e prendo i tempi
import clock_and_generator as cg
import QuickSort as qs
import CountingSort as cs
import QuickSort3Way as cs3

N = cg.generaNumero (cg.MIN_N, cg.MAX_N) 
arr = cg.creaVettore (N)


start = cg.getTime()
qs.test_QuickSort(1000,1000)
end = cg.getTime()


print("Tempo impiegato QuickSort: {:.5f}".format(end-start))


start = cg.getTime()
cs3.QuickSort3Way(arr, 0, len(arr)-1)
end = cg.getTime()

print("Tempo QuickSort3Way: {:.5f}".format(end-start))


start = cg.getTime()
cs.countingSort(arr)
end = cg.getTime()

print("Tempo CountingSort: {:.5f}".format(end-start))


