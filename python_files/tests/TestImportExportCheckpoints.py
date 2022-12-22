# Test estimador
from python_files.ImportExportCheckpoints import guardar_checkpoint, cargar_checkpoint

test1 = {}
test1['aa'] = [0.0, 'ab ba']
test1['ab'] = [0.5, '']
test1['ba'] = [0.5, '']

guardar_checkpoint(test1, 'test.csv')

test2 = cargar_checkpoint('test.csv')

for llaves in ['aa', 'ab', 'ba']:
  assert test1[llaves] == test2[llaves]

del test1
del test2
