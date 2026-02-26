import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('movies_initial.csv')

# Guardar como JSON con orient='records' (cada fila es un registro)
df.to_json('movie/management/commands/movies.json', orient='records')

print('Archivo movies.json generado correctamente.')
