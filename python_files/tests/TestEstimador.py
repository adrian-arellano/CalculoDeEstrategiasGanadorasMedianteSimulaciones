# test Estimador
from Estimador import Estimador

# checkear traspaso de info


# checkear autocompletatacion

test1 = {}
test1['aaa'] = [-1, 'baa aba aab']
# test1['aaa'] = [0.0,'baa aba aab']
# test1['baa'] = [1,'']
# test1['aba'] = [0.5,'']
# test1['aab'] = [0,'']

U = Estimador()

U.agregar_tablero('aaa', test1['aaa'][1].split(' '))
U.tablero('aaa').cambiar_valor(test1['aaa'][0])

assert len(U.tableros) == 4

assert U.tableros['aaa'].tableros_siguientes[0] == U.tableros['baa']
assert U.tableros['aaa'].tableros_siguientes[1] == U.tableros['aba']
assert U.tableros['aaa'].tableros_siguientes[2] == U.tableros['aab']

assert U.tablero('aaa').tableros_siguientes[0] == U.tablero('baa')
assert U.tablero('aaa').tableros_siguientes[1] == U.tablero('aba')
assert U.tablero('aaa').tableros_siguientes[2] == U.tablero('aab')

assert U.conoce_a('aaa')
assert U.conoce_a('baa')
assert U.conoce_a('aba')
assert U.conoce_a('aab')
assert not U.conoce_a('bba')
assert not U.conoce_a('bab')
assert not U.conoce_a('abb')
assert not U.conoce_a('bbb')

assert U.valor('aaa') == -1
assert U.valor('baa') == 0
assert U.valor('aba') == 0
assert U.valor('aab') == 0
assert U.valor('abb') == 0  # crea tablero
assert U.valor('bab') == 0  # crea tablero
assert U.valor('bba') == 0  # crea tablero
assert U.valor('bbb') == 0  # crea tablero
# assert U.valor('aaa') == 0.0
# assert U.valor('baa') == 0.5
# assert U.valor('aba') == 0.5
# assert U.valor('aab') == 0.5
# assert U.valor('abb') == 0.5 #crea tablero
# assert U.valor('bab') == 0.5 #crea tablero
# assert U.valor('bba') == 0.5 #crea tablero
# assert U.valor('bbb') == 0.5 #crea tablero

assert U.conoce_a('aaa')
assert U.conoce_a('baa')
assert U.conoce_a('aba')
assert U.conoce_a('aab')
assert U.conoce_a('bba')
assert U.conoce_a('bab')
assert U.conoce_a('abb')
assert U.conoce_a('bbb')

assert len(U.tableros) == 8

assert len(U.jugadas_viables('aaa')) == 3  # actualizado
assert len(U.jugadas_viables('baa')) == 0
assert len(U.jugadas_viables('aba')) == 0
assert len(U.jugadas_viables('aab')) == 0
assert len(U.jugadas_viables('abb')) == 0
assert len(U.jugadas_viables('bab')) == 0
assert len(U.jugadas_viables('bba')) == 0
assert len(U.jugadas_viables('bbb')) == 0

assert len(U.tablero('aaa').tableros_siguientes) == 3
assert len(U.tablero('baa').tableros_siguientes) == 0
assert len(U.tablero('aba').tableros_siguientes) == 0
assert len(U.tablero('aab').tableros_siguientes) == 0
assert len(U.tablero('bba').tableros_siguientes) == 0
assert len(U.tablero('bab').tableros_siguientes) == 0
assert len(U.tablero('abb').tableros_siguientes) == 0
assert len(U.tablero('bbb').tableros_siguientes) == 0

# checkear actualizar

U.actualizar_tableros_viables('bbb', True)
U.actualizar_tableros_viables('abb', True)
U.actualizar_tableros_viables('bab', True)
U.actualizar_tableros_viables('bba', True)
U.actualizar_tableros_viables('aab', True)
U.actualizar_tableros_viables('aba', True)
U.actualizar_tableros_viables('baa', True)
U.actualizar_tableros_viables('aaa', True)

assert U.valor('aaa') == 0
assert U.valor('baa') == 0
assert U.valor('aba') == 0
assert U.valor('aab') == 0
assert U.valor('abb') == 0
assert U.valor('bab') == 0
assert U.valor('bba') == 0
assert U.valor('bbb') == 0
# assert U.valor('aaa') == 0.5
# assert U.valor('baa') == 0.5
# assert U.valor('aba') == 0.5
# assert U.valor('aab') == 0.5
# assert U.valor('abb') == 0.5
# assert U.valor('bab') == 0.5
# assert U.valor('bba') == 0.5
# assert U.valor('bbb') == 0.5

assert len(U.jugadas_viables('aaa')) == 3, U.jugadas_viables('aaa')
assert len(U.jugadas_viables('baa')) == 0
assert len(U.jugadas_viables('aba')) == 0
assert len(U.jugadas_viables('aab')) == 0
assert len(U.jugadas_viables('abb')) == 0
assert len(U.jugadas_viables('bab')) == 0
assert len(U.jugadas_viables('bba')) == 0
assert len(U.jugadas_viables('bbb')) == 0

# checkear sobreescritura

test2 = {}
test2['baa'] = [1, '']  # nuevo valor
test2['aba'] = [0, '']  # nuevo valor
test2['aab'] = [-1, '']  # nuevo valor
test2['abb'] = [0, 'bbb']
test2['bab'] = [-1, 'bbb']
test2['bba'] = [-1, 'bbb']
test2['bbb'] = [1, '']
# test2['baa'] = [1,''] # nuevo valor
# test2['aba'] = [0.5,''] # nuevo valor
# test2['aab'] = [0.0,''] # nuevo valor
# test2['abb'] = [0.5,'bbb']
# test2['bab'] = [0.0,'bbb']
# test2['bba'] = [0.0,'bbb']
# test2['bbb'] = [1,'']

U.leer_checkpoint(test2)

assert U.tableros['aaa'].tableros_siguientes[0] == U.tableros['baa']
assert U.tableros['aaa'].tableros_siguientes[1] == U.tableros['aba']
assert U.tableros['aaa'].tableros_siguientes[2] == U.tableros['aab']

assert U.tablero('aaa').tableros_siguientes[0] == U.tablero('baa')
assert U.tablero('aaa').tableros_siguientes[1] == U.tablero('aba')
assert U.tablero('aaa').tableros_siguientes[2] == U.tablero('aab')

assert U.valor('aaa') == 0
assert U.valor('baa') == 1
assert U.valor('aba') == 0
assert U.valor('aab') == -1
assert U.valor('abb') == 0
assert U.valor('bab') == -1
assert U.valor('bba') == -1
assert U.valor('bbb') == 1
# assert U.valor('aaa') == 0.5
# assert U.valor('baa') == 1
# assert U.valor('aba') == 0.5
# assert U.valor('aab') == 0.0
# assert U.valor('abb') == 0.5
# assert U.valor('bab') == 0.0
# assert U.valor('bba') == 0.0
# assert U.valor('bbb') == 1

assert U.tableros['abb'].tableros_siguientes[0] == U.tableros['bbb']
assert U.tableros['bab'].tableros_siguientes[0] == U.tableros['bbb']
assert U.tableros['bba'].tableros_siguientes[0] == U.tableros['bbb']

U.actualizar_tableros_viables('bbb')
U.actualizar_tableros_viables('abb')
U.actualizar_tableros_viables('bab')
U.actualizar_tableros_viables('bba')
U.actualizar_tableros_viables('aab')
U.actualizar_tableros_viables('aba')
U.actualizar_tableros_viables('baa')
U.actualizar_tableros_viables('aaa')

assert len(U.jugadas_viables('aaa')) == 1, [U.valor(llave) for llave in U.jugadas_posibles('aaa')]
assert len(U.jugadas_viables('baa')) == 0, U.jugadas_posibles('baa')
assert len(U.jugadas_viables('aba')) == 0
assert len(U.jugadas_viables('aab')) == 0
assert len(U.jugadas_viables('abb')) == 1
assert len(U.jugadas_viables('bab')) == 1
assert len(U.jugadas_viables('bba')) == 1
assert len(U.jugadas_viables('bbb')) == 0

U.actualizar_valor('bbb')
U.actualizar_valor('abb')
U.actualizar_valor('bab')
U.actualizar_valor('bba')
U.actualizar_valor('aab')
U.actualizar_valor('aba')
U.actualizar_valor('baa')
U.actualizar_valor('aaa')

assert U.valor('aaa') == -1, U.tablero('aaa').llaves_jugadas_posibles_viables()  # , U.valor('aaa')
assert U.valor('baa') == 1
assert U.valor('aba') == 0
assert U.valor('aab') == -1
assert U.valor('abb') == -1
assert U.valor('bab') == -1
assert U.valor('bba') == -1
assert U.valor('bbb') == 1
# assert U.valor('aaa') == 0.0, U.tablero('aaa').llaves_jugadas_posibles_viables()#, U.valor('aaa')
# assert U.valor('baa') == 1
# assert U.valor('aba') == 0.5
# assert U.valor('aab') == 0.0
# assert U.valor('abb') == 0.0
# assert U.valor('bab') == 0.0
# assert U.valor('bba') == 0.0
# assert U.valor('bbb') == 1


# checkear backpropagation

test3 = {}

test3['baa'] = [1, 'bba bab']
test3['aba'] = [0, 'bba abb']
test3['aab'] = [-1, 'bab abb']
# test3['baa'] = [1,'bba bab']
# test3['aba'] = [0.5,'bba abb']
# test3['aab'] = [0.0,'bab abb']

U.leer_checkpoint(test3)

assert U.tableros['baa'].tableros_siguientes[0] == U.tableros['bba']
assert U.tableros['baa'].tableros_siguientes[1] == U.tableros['bab']
assert U.tableros['aba'].tableros_siguientes[0] == U.tableros['bba']
assert U.tableros['aba'].tableros_siguientes[1] == U.tableros['abb']
assert U.tableros['aab'].tableros_siguientes[0] == U.tableros['bab']
assert U.tableros['aab'].tableros_siguientes[1] == U.tableros['abb']

assert U.valor('aaa') == -1
assert U.valor('baa') == 1
assert U.valor('aba') == 0
assert U.valor('aab') == -1
assert U.valor('abb') == -1
assert U.valor('bab') == -1
assert U.valor('bba') == -1
assert U.valor('bbb') == 1
# assert U.valor('aaa') == 0.0
# assert U.valor('baa') == 1
# assert U.valor('aba') == 0.5
# assert U.valor('aab') == 0.0
# assert U.valor('abb') == 0.0
# assert U.valor('bab') == 0.0
# assert U.valor('bba') == 0.0
# assert U.valor('bbb') == 1

U.actualizar_tableros_viables('bbb', True)
U.actualizar_tableros_viables('abb', True)
U.actualizar_tableros_viables('bab', True)
U.actualizar_tableros_viables('bba', True)
U.actualizar_tableros_viables('aab', True)
U.actualizar_tableros_viables('aba', True)
U.actualizar_tableros_viables('baa', True)
U.actualizar_tableros_viables('aaa', True)

assert U.valor('aaa') == -1
assert U.valor('baa') == 1
assert U.valor('aba') == 1
assert U.valor('aab') == 1
assert U.valor('abb') == -1
assert U.valor('bab') == -1
assert U.valor('bba') == -1
assert U.valor('bbb') == 1
# assert U.valor('aaa') == 0.0
# assert U.valor('baa') == 1
# assert U.valor('aba') == 1
# assert U.valor('aab') == 1
# assert U.valor('abb') == 0.0
# assert U.valor('bab') == 0.0
# assert U.valor('bba') == 0.0
# assert U.valor('bbb') == 1

assert len(U.jugadas_viables('aaa')) == 3, U.tableros['aaa'].llaves_jugadas_posibles()  # U.jugadas_posibles('aaa')
assert len(U.jugadas_viables('baa')) == 2
assert len(U.jugadas_viables('aba')) == 2
assert len(U.jugadas_viables('aab')) == 2
assert len(U.jugadas_viables('abb')) == 1
assert len(U.jugadas_viables('bab')) == 1
assert len(U.jugadas_viables('bba')) == 1
assert len(U.jugadas_viables('bbb')) == 0

del test1
del test2
del test3
del U
