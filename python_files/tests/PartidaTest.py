# tests Partidas: solo manejar punteros
from Partida import Partida
from Tablero import Tablero

test = {}
test[3] = Tablero('bc', [])
test[2] = Tablero('ba', [])
test[1] = Tablero('ab', [])
test[0] = Tablero('aa', [test[1], test[2]])
Test = Partida(test[0])
# print(test[0])

# checkear inicializador

assert Test.tablero_actual().llave == 'aa'
assert Test.turno_actual() == 0
assert len(Test.tablero_actual().jugadas_posibles_viables) == 2
assert Test.tablero_actual() == test[0]
# print(Test.tablero_actual())

# checkear agregar turno

Test.agregar_jugada(test[2])
assert Test.tablero_actual().llave == 'ba'
assert Test.turno_actual() == 1
assert len(Test.tablero_actual().jugadas_posibles_viables) == 0
assert Test.tablero_en_turno(0).llave == 'aa'
assert len(Test.tablero_en_turno(0).jugadas_posibles_viables) == 2

assert Test.tablero_en_turno(0) == test[0]
assert Test.tablero_en_turno(0).tableros_siguientes[1] == test[2]
assert Test.tablero_en_turno(0).tableros_siguientes[1] == Test.tablero_actual()
# print(Test.tablero_en_turno(0))

Test.tablero_actual().agregar_jugadas([test[3]])
Test.agregar_jugada(test[3])

# estos tres deben ser el mismo objeto
# print(test[3])
# print(Test.tablero_actual())
# print(Test.tablero_en_turno(1).jugadas_posibles[0])
# print(Test.tablero_en_turno(0).jugadas_posibles[1].jugadas_posibles[0])

assert Test.tablero_actual() == test[3]
assert Test.tablero_en_turno(1).tableros_siguientes[0] == test[3]
assert Test.tablero_en_turno(0).tableros_siguientes[1].tableros_siguientes[0] == test[3]

# checkear editar valores

assert Test.tablero_actual().valor == 0
assert Test.tablero_en_turno(1).valor == 0
assert Test.tablero_en_turno(0).valor == 0
# assert Test.tablero_actual().valor == 0.5
# assert Test.tablero_en_turno(1).valor == 0.5
# assert Test.tablero_en_turno(0).valor == 0.5

assert len(Test.tablero_actual().jugadas_posibles_viables) == 0
assert len(Test.tablero_en_turno(1).jugadas_posibles_viables) == 0
assert len(Test.tablero_en_turno(0).jugadas_posibles_viables) == 2

Test.actualizar_hacia_atras_turno(2)

assert len(Test.tablero_actual().jugadas_posibles_viables) == 0
assert len(Test.tablero_en_turno(1).jugadas_posibles_viables) == 1
assert len(Test.tablero_en_turno(0).jugadas_posibles_viables) == 2

Test.cambiar_valor_turno(1, 1)
assert Test.tablero_actual().valor == 0
assert Test.tablero_en_turno(1).valor == 1, Test.tablero_en_turno(1).valor
assert Test.tablero_en_turno(0).valor == -1
# Test.cambiar_valor_turno(1,1.0)
# assert Test.tablero_actual().valor == 0.5
# assert Test.tablero_en_turno(1).valor == 1.0, Test.tablero_en_turno(1).valor
# assert Test.tablero_en_turno(0).valor == 0.0

assert len(Test.tablero_actual().jugadas_posibles_viables) == 0
assert len(Test.tablero_en_turno(1).jugadas_posibles_viables) == 1
assert len(Test.tablero_en_turno(0).jugadas_posibles_viables) == 1

Test.cambiar_valor_turno(2, 1)
assert Test.tablero_actual().valor == 1
assert Test.tablero_en_turno(1).valor == -1
assert Test.tablero_en_turno(0).valor == 0, Test.tablero_en_turno(0).valor
# Test.cambiar_valor_turno(2,1)
# assert Test.tablero_actual().valor == 1.0
# assert Test.tablero_en_turno(1).valor == 0.0
# assert Test.tablero_en_turno(0).valor == 0.5, Test.tablero_en_turno(0).valor

assert len(Test.tablero_actual().jugadas_posibles_viables) == 0
assert len(Test.tablero_en_turno(1).jugadas_posibles_viables) == 1
assert len(Test.tablero_en_turno(0).jugadas_posibles_viables) == 1

test[1].cambiar_valor(-1)
test[0].actualizar_tableros_viables(True)
assert Test.tablero_actual().valor == 1
assert Test.tablero_en_turno(1).valor == -1
assert Test.tablero_en_turno(0).valor == 1, Test.tablero_en_turno(0).valor
# test[1].cambiar_valor(0)
# test[0].actualizar_tableros_viables(True)
# assert Test.tablero_actual().valor == 1
# assert Test.tablero_en_turno(1).valor == 0
# assert Test.tablero_en_turno(0).valor == 1, Test.tablero_en_turno(0).valor

assert len(Test.tablero_actual().jugadas_posibles_viables) == 0
assert len(Test.tablero_en_turno(1).jugadas_posibles_viables) == 1
assert len(Test.tablero_en_turno(0).jugadas_posibles_viables) == 2

# retroceder en el tiempo

assert Test.tablero_actual().llave == 'bc'
assert Test.turno_actual() == 2
assert Test.tablero_actual() == test[3]

Test.retroceder_antes_del_turno(2)

assert Test.tablero_actual().llave == 'ba'
assert Test.turno_actual() == 1
assert Test.tablero_actual() == test[2]

del Test
del test
