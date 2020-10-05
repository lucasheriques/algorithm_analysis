# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''


def elevador_lotado(num_andares, cap, pessoas, para_visitar):
    para_visitar.sort(reverse=True)
    menor_tempo = 0

    for i in range(0, pessoas, cap):
        menor_tempo += (2 * para_visitar[i])

    return menor_tempo


n_inputs = int(input())

for i in range(n_inputs):
    parametros = [int(x) for x in input().split()]
    andares = [int(x) for x in input().split()]
    elevador_lotado(parametros[0], parametros[1], parametros[2], andares)
