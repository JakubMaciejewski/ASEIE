import numpy as np
import random
import sys
from time import clock

sys.setrecursionlimit(5000)
dlugosc =  3000

lista =  np.zeros(dlugosc)

for i in range(len(lista)):

	lista[i] = random.uniform(1, 10)

lista_bombel= lista 

#print(lista)

start = clock()

for i in range(len(lista) - 1, 0, -1):
	for j in range(i):
		if lista_bombel[j] > lista_bombel[j + 1]:
			buff = lista_bombel[j]
			lista_bombel[j] = lista_bombel[j + 1]
			lista_bombel[j + 1] = buff
end = clock() - start
#print(lista_bombel)
print("czas bomblekowy: " )
print(end)


select_sort = lista


start = clock()
for i in range(len(lista) - 1, 0, -1):
	maxindeks = 0
	for j in range(1,i+1):
		if select_sort[j]>select_sort[maxindeks]:
			maxindeks = j 
			
	buff = select_sort[i]
	select_sort[i] = select_sort[j]
	select_sort[j] = select_sort[i]
end = clock() - start

#print(select_sort)
print("czas select: " )
print(end)

quick_lista = lista


def quicksort(quick_lista):
	mniejsze_rowne = []
	wieksze = []
	if len(quick_lista) > 1:
		poczatek = quick_lista[0]
		for x in quick_lista:
			if x <= poczatek:
				mniejsze_rowne.append(x)
			if x > poczatek:
				wieksze.append(x)
		return quicksort(mniejsze_rowne)+quicksort(wieksze)
	else:
		return quick_lista

start = clock()
quicksort(quick_lista)
end = clock() - start
print("czas quick: " )
#print(quick_lista)
print(end)



