import pandas as pd

def dataframe_a_checkpoint(dataframe):
  checkpoint = {}
  for llave in dataframe:
    print(llave)
    if pd.isna(dataframe[llave][1]):
      jugadas_aux = ''
    else:
      jugadas_aux = str(dataframe[llave][1])
    checkpoint[llave] = [float(dataframe[llave][0]),jugadas_aux]
  return checkpoint

def checkpoint_a_dataframe(checkpoint):
  dataframe = pd.DataFrame(checkpoint)
  return dataframe

def guardar_checkpoint(checkpoint,nombre_checkpoint='checkpoint.csv'):
  df = checkpoint_a_dataframe(checkpoint)
  df.to_csv(nombre_checkpoint)

def cargar_checkpoint(nombre_csv='checkpoint.csv'):
  df = pd.read_csv(nombre_csv)
  return dataframe_a_checkpoint(df)
