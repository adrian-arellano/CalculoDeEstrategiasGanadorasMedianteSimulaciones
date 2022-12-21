def MonteCarlo(u, distribucion):
  acumulado_aux = 0

  # invariante de entrada al loop: u no ha caido en ningun indice previo
  for indice in range(len(distribucion)):
    acumulado_aux += distribucion[indice]
    if acumulado_aux >= u:  # checkear si esta es la que salio sorteada
      return indice

  # boton de panico (?)
  return -1