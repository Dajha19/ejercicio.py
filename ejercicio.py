import pandas as pd

estudiantes_df = pd.DataFrame({
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [15, 14, 16, 15],
    'Nota': [8.5, 9.0, 7.5, 8.0]
})

df = pd.DataFrame(estudiantes_df)


print(df.head())

# Mostrar su primera fila del data base
primera_fila = df.iloc[0]
print(primera_fila)

# Añade una nueva columna
import pandas as pd

estudiantes_df = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [15, 14, 16, 15],
    
    'Nota': [8.5, 9.0, 7.5, 8.0], 
    'Ciudad' :[ 'Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(estudiantes_df)


print(df.head())
