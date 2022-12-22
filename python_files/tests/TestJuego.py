from python_files.Estimador import Estimador
from python_files.Juego import Juego

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

U_test.tablero('22 ').cambiar_valor(1)
U_test.tablero('2 2').cambiar_valor(1)
U_test.tablero(' 22').cambiar_valor(1)
U_test.tablero('112').cambiar_valor(1)
U_test.tablero('121').cambiar_valor(1)
U_test.tablero('211').cambiar_valor(1)

U_test.actualizar_tableros_viables('222', True)
U_test.actualizar_tableros_viables('221', True)
U_test.actualizar_tableros_viables('212', True)
U_test.actualizar_tableros_viables('122', True)
U_test.actualizar_tableros_viables('211', True)
U_test.actualizar_tableros_viables('121', True)
U_test.actualizar_tableros_viables('112', True)
U_test.actualizar_tableros_viables('22 ', True)
U_test.actualizar_tableros_viables('21 ', True)
U_test.actualizar_tableros_viables('2 2', True)
U_test.actualizar_tableros_viables('2 1', True)
U_test.actualizar_tableros_viables('12 ', True)
U_test.actualizar_tableros_viables('11 ', True)
U_test.actualizar_tableros_viables('1 2', True)
U_test.actualizar_tableros_viables('1 1', True)
U_test.actualizar_tableros_viables(' 22', True)
U_test.actualizar_tableros_viables(' 21', True)
U_test.actualizar_tableros_viables(' 12', True)
U_test.actualizar_tableros_viables(' 11', True)
U_test.actualizar_tableros_viables('2  ', True)
U_test.actualizar_tableros_viables('1  ', True)
U_test.actualizar_tableros_viables(' 2 ', True)
U_test.actualizar_tableros_viables(' 1 ', True)
U_test.actualizar_tableros_viables('  2', True)
U_test.actualizar_tableros_viables('  1', True)
U_test.actualizar_tableros_viables('   ', True)

conocimiento_test = {}

for llave in U_test.tableros:
  conocimiento_test[llave] = U_test.valor(llave)


def regla_test(llave):
  jugadas_posibles = []
  for indice in range(len(llave)):
    if llave[indice] == ' ':
      jugadas_posibles.append(llave[:indice] + '1' + llave[indice + 1:])
      jugadas_posibles.append(llave[:indice] + '2' + llave[indice + 1:])
  return jugadas_posibles


assert regla_test('   ') == ['1  ', '2  ', ' 1 ', ' 2 ', '  1', '  2']


def con_vic_test(llave):
  valor = 0
  for casilla in llave:
    if casilla != ' ':
      valor += int(casilla)
  return valor == 4


assert not con_vic_test('   ')
assert con_vic_test(' 13')

juego_test = Juego(3, 1, '   ')
juego_test.cambiar_reglasJ1(regla_test)
juego_test.cambiar_reglasJ2(regla_test)
juego_test.cambiar_victoriaJ1(con_vic_test)
juego_test.cambiar_victoriaJ2(con_vic_test)
juego_test.agregar_conocimiento(conocimiento_test)
