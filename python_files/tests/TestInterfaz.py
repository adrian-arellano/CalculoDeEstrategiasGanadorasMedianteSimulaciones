from matplotlib import pyplot as plt

from python_files.Estimador import Estimador
from python_files.Interfaz import graficar_red, graficar_tablero
from python_files.Partida import Partida

test_3tab = {'   ': [0, '1  &2  & 1 & 2 &  1&  2'],
             '1  ': [0, '12 &11 &1 1&1 2'],
             '2  ': [0, '22 &21 &2 1&2 2'],
             ' 1 ': [0, '11 &21 & 11& 12'],
             ' 2 ': [0, '12 &22 & 21& 22'],
             '  1': [0, '1 1&2 1& 11& 21'],
             '  2': [0, '1 2&2 2& 12& 22'],
             '11 ': [0, '111&112'],
             '12 ': [0, '121&121'],
             '21 ': [0, '211&212'],
             ' 11': [0, '111&211'],
             ' 12': [0, '112&212'],
             ' 21': [0, '121&221'],
             '2 1': [0, '211&221'],
             '1 2': [0, '112&122'],
             '1 1': [0, '111&121']}

U_test = Estimador(test_3tab, separador='&')
Partida_test = Partida(U_test.tablero('   '))
Partida_test.agregar_jugada(U_test.tablero('1  '))
Partida_test.agregar_jugada(U_test.tablero('1 2'))
Partida_test.agregar_jugada(U_test.tablero('112'))

U_test.tablero('112').cambiar_valor(1)
U_test.tablero('   ').visitado = True
U_test.tablero('1  ').visitado = True
U_test.tablero('1 2').visitado = True
U_test.tablero('112').visitado = True

fig1 = plt.figure(figsize=(5, 9))
graficar_red(3, U_test, partida=Partida_test)
plt.show()

U_test.tablero('22 ').cambiar_valor(1)
U_test.tablero('2 2').cambiar_valor(1)
U_test.tablero(' 22').cambiar_valor(1)
U_test.tablero('112').cambiar_valor(1)
U_test.tablero('121').cambiar_valor(1)
U_test.tablero('211').cambiar_valor(1)

for llave in U_test.tableros:
  U_test.tablero(llave).visitado = True

fig2 = plt.figure(figsize=(5, 9))
graficar_red(3, U_test)
plt.show()

del U_test
del test_3tab

test_llave = 'abcdefghijklmnopqrstuvwxy'

graficar_tablero(5, 5, test_llave, scale=2, font=1.5)

# test_fig.show() #no funciona, table plotea automaticamente

del test_llave
# del test_fig
