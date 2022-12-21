from Tablero import *

# tests tablero

test2 = Tablero('baa', [])
test3 = Tablero('aba', [])
test4 = Tablero('aab', [])
test1 = Tablero('aaa', [test2, test3])

# checkear inicializador
assert test1.llave == 'aaa'
assert test1.tableros_siguientes[0].llave == 'baa'
assert test1.tableros_siguientes[1].llave == 'aba'

assert test1.valor == 0
assert test1.tableros_siguientes[0].valor == 0
assert test1.tableros_siguientes[1].valor == 0
# assert test1.valor == 0.5
# assert test1.jugadas_posibles[0].valor == 0.5
# assert test1.jugadas_posibles[1].valor == 0.5

assert test1.llaves_jugadas_posibles() == ['baa', 'aba']
assert test1.llaves_jugadas_posibles_viables() == ['baa', 'aba']
assert len(test1.tableros_siguientes) == 2
assert len(test1.jugadas_posibles_viables) == 2

# checkear agregar jugadas
test1.agregar_jugadas([test4])

assert test1.llave == 'aaa'
assert test1.tableros_siguientes[0].llave == 'baa'
assert test1.tableros_siguientes[1].llave == 'aba'
assert test1.tableros_siguientes[2].llave == 'aab'

assert test1.valor == 0
assert test1.tableros_siguientes[0].valor == 0
assert test1.tableros_siguientes[1].valor == 0
assert test1.tableros_siguientes[2].valor == 0
# assert test1.valor == 0.5
# assert test1.jugadas_posibles[0].valor == 0.5
# assert test1.jugadas_posibles[1].valor == 0.5
# assert test1.jugadas_posibles[2].valor == 0.5

assert len(test1.tableros_siguientes) == 3
assert len(test1.jugadas_posibles_viables) == 2  # no actualizado
assert test1.llaves_jugadas_posibles() == ['baa', 'aba', 'aab']
assert test1.llaves_jugadas_posibles_viables() == ['baa', 'aba']  # no actualizado

test1.actualizar_tableros_viables()
assert len(test1.jugadas_posibles_viables) == 3
assert test1.llaves_jugadas_posibles_viables() == ['baa', 'aba', 'aab']

# checkear editar valores

test4.cambiar_valor(-1)
assert test1.valor == 0
assert test1.tableros_siguientes[0].valor == 0
assert test1.tableros_siguientes[1].valor == 0
assert test1.tableros_siguientes[2].valor == -1
# test4.cambiar_valor(0.0)
# assert test1.valor == 0.5
# assert test1.jugadas_posibles[0].valor == 0.5
# assert test1.jugadas_posibles[1].valor == 0.5
# assert test1.jugadas_posibles[2].valor == 0.0
assert len(test1.jugadas_posibles_viables) == 3  # no actualizado

test1.actualizar_tableros_viables()
assert test1.valor == 0
assert test1.tableros_siguientes[0].valor == 0
assert test1.tableros_siguientes[1].valor == 0
assert test1.tableros_siguientes[2].valor == -1
# assert test1.valor == 0.5
# assert test1.jugadas_posibles[0].valor == 0.5
# assert test1.jugadas_posibles[1].valor == 0.5
# assert test1.jugadas_posibles[2].valor == 0.0
assert len(test1.jugadas_posibles_viables) == 2

test2.cambiar_valor(1)
test1.actualizar_tableros_viables()
assert test1.valor == 0  # no actualizado
assert test1.tableros_siguientes[0].valor == 1
assert test1.tableros_siguientes[1].valor == 0
assert test1.tableros_siguientes[2].valor == -1
# test2.cambiar_valor(1.0)
# test1.actualizar_tableros_viables()
# assert test1.valor == 0.5 # no actualizado
# assert test1.jugadas_posibles[0].valor == 1.0
# assert test1.jugadas_posibles[1].valor == 0.5
# assert test1.jugadas_posibles[2].valor == 0.0
assert len(test1.jugadas_posibles_viables) == 1

test1.actualizar_valor()

assert test1.valor == -1
assert test1.tableros_siguientes[0].valor == 1
assert test1.tableros_siguientes[1].valor == 0
assert test1.tableros_siguientes[2].valor == -1
# assert test1.valor == 0.0
# assert test1.jugadas_posibles[0].valor == 1.0
# assert test1.jugadas_posibles[1].valor == 0.5
# assert test1.jugadas_posibles[2].valor == 0.0
assert len(test1.jugadas_posibles_viables) == 1

test2.cambiar_valor(-1)
test3.cambiar_valor(-1)
# test2.cambiar_valor(0.0)
# test3.cambiar_valor(0.0)
test1.actualizar_tableros_viables(True)

assert test1.valor == 1
assert test1.tableros_siguientes[0].valor == -1
assert test1.tableros_siguientes[1].valor == -1
assert test1.tableros_siguientes[2].valor == -1
# assert test1.valor == 1.0
# assert test1.jugadas_posibles[0].valor == 0.0
# assert test1.jugadas_posibles[1].valor == 0.0
# assert test1.jugadas_posibles[2].valor == 0.0
assert len(test1.jugadas_posibles_viables) == 3

del test4
del test3
del test2
del test1

# test manual

test = {}
test['aaa'] = Tablero('aaa', [])
test['aab'] = Tablero('aab', [])
test['aba'] = Tablero('aba', [])
test['baa'] = Tablero('baa', [])
test['bba'] = Tablero('bba', [])
test['bab'] = Tablero('bab', [])
test['abb'] = Tablero('abb', [])
test['bbb'] = Tablero('bbb', [])

test['aaa'].agregar_jugadas([test['aba'], test['baa'], test['aab']])
test['aab'].agregar_jugadas([test['bab'], test['abb']])
test['aba'].agregar_jugadas([test['bba'], test['abb']])
test['baa'].agregar_jugadas([test['bba'], test['bab']])
test['bba'].agregar_jugadas([test['bbb']])
test['bab'].agregar_jugadas([test['bbb']])
test['abb'].agregar_jugadas([test['bbb']])

test['bbb'].cambiar_valor(0.0)

test['bbb'].actualizar_tableros_viables(True)
test['abb'].actualizar_tableros_viables(True)
test['bba'].actualizar_tableros_viables(True)
test['bab'].actualizar_tableros_viables(True)
test['aab'].actualizar_tableros_viables(True)
test['aba'].actualizar_tableros_viables(True)
test['baa'].actualizar_tableros_viables(True)
test['aaa'].actualizar_tableros_viables(True)

for llave in test: print(llave, ':', test[llave].valor, '-', test[llave].llaves_jugadas_posibles_viables())

del test
