# extrait de Algebraic graph Algorithm / chapter 5.2

import multiprocessing as mp
from multiprocessing import Pool
import numpy as np
import time

def sq(x):
    return x*x


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,3],[1,2,3],[1,2,3]])

def worker(me,C,l):
    l.acquire()
    Y = np.dot(A[me,:],B)
    print("me and my product",me, Y)
    C.append(Y)
    l.release()
    return Y

if __name__ == "__main__":
    
    print("cpu count ",mp.cpu_count())
    
    listNum=[i+1 for i in range(20000000)]
    
    start_time = time.time()
    p = Pool(20)
    result_list2= p.map(sq, listNum)
    # print(result_list2)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Temps d'exécution de la boucle multi-thread : {execution_time} secondes")    
    
    start_time2 = time.time()
    result_list2 = list(map(sq, listNum))
    # print(result_list2)
    end_time2 = time.time()
    execution_time2 = end_time2 - start_time2
    print(f"Temps d'exécution de la boucle single-thread : {execution_time2} secondes")    

# p = Pool(5)
# Temps d'exécution de la boucle multi-thread : 3.8191049098968506 secondes
# Temps d'exécution de la boucle single-thread : 2.0734567642211914 secondes
# p = Pool(20)
# Temps d'exécution de la boucle multi-thread : 3.7017087936401367 secondes
# Temps d'exécution de la boucle single-thread : 1.7882564067840576 secondes

    mgr = mp.Manager()
    C = mgr.list()
    lock = mp.Lock()
    procs = []
    for i in range(3):
        p = mp.Process(target=worker,args=(i,C,lock))
        procs.append(p)
        p.start()
    for proc in procs:
        proc.join()
        print(np.array(C))
