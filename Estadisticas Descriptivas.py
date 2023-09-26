import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import numpy as np


ruta=""
nombre = input("Nombre de quien corre: ")
if nombre.lower() == "carlos":
    ruta = "D:/datos usuario/Documents/Universidad de los Andes/2023-20/Analitica/Proyecto/data.xlsx"
elif nombre.lower() == "sebas":
    ruta= ""
else:
    ruta=""

data = pd.read_excel(ruta)
print("Primeras filas del DataFrame: \n", data.head())
print("Información de DataFrame: \n", data.info())
print("Estadisticas Descriptivas del DataFrame: \n", data.describe())
print("Número de valores faltantes por columna: \n", data.isnull().sum())

#Histograma Admission grade
plt.hist(data['Admission grade'], bins=10)
plt.title('Distribución de las notas de admision')
plt.xlabel('Admission grade')
plt.ylabel('Frecuencia')
media = np.mean(data['Admission grade'])
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()

#Histograma Age at enrollment
plt.hist(data['Age at enrollment'], bins=10)
plt.title('Distribución de la edad en la inscripción')
plt.xlabel('Age at enrollment')
plt.ylabel('Frecuencia')
media = np.mean(data['Age at enrollment'])
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()

#Histograma Curricular units 1st sem (enrolled)
plt.hist(data['Curricular units 1st sem (enrolled)'], bins=10)
plt.title('Distribución del número de créditos inscritos en el primer semestre')
plt.xlabel('Curricular units 1st sem (enrolled)')
plt.ylabel('Frecuencia')
media = np.mean(data['Curricular units 1st sem (enrolled)'])
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()

#Histograma Curricular units 2nd sem (enrolled)
plt.hist(data['Curricular units 2nd sem (enrolled)'], bins=10)
plt.title('Distribución del número de créditos inscritos en el segundo semestre')
plt.xlabel('Curricular units 2nd sem (enrolled)')
plt.ylabel('Frecuencia')
media = np.mean(data['Curricular units 2nd sem (enrolled)'])
plt.axvline(media, color='red', linestyle='dashed', linewidth=1)
plt.legend(['Media'], loc='upper right')
plt.show()


# Diagramas de caja para nota de admision, edad en inscripción y numero de creditos en los primeros dos semestres
nota = data['Admission grade'].tolist()
edad = data['Age at enrollment'].tolist()
semestre1 = data['Curricular units 1st sem (enrolled)'].tolist()
semestre2 = data['Curricular units 2nd sem (enrolled)'].tolist()
diagrama = [nota, edad, semestre1, semestre2]

plt.boxplot(diagrama)

plt.title('Diagrama de Caja')
plt.xlabel('Variables')
plt.ylabel('Valores')

nombres_variables = ['Nota', 'Edad', 'Créditos 1er sem','Créditos 2do sem']
plt.xticks([1, 2, 3,4], nombres_variables)
plt.show()


#Grafico de dispersion nota dada la edad
plt.scatter(data['Age at enrollment'], data['Admission grade'])
plt.xlabel('Edad')
plt.ylabel('Nota')
plt.title('Gráfico de dispersión de la nota dada la edad')
plt.show()

#Grafico de dispersion créditos 1er sem dada la edad
plt.scatter(data['Curricular units 1st sem (enrolled)'], data['Age at enrollment'])
plt.xlabel('Créditos 1er sem')
plt.ylabel('Edad')
plt.title('Gráfico de dispersión de la nota dada la edad')
plt.show()

#Grafico de dispersion créditos 2do sem dada la edad
plt.scatter(data['Curricular units 2nd sem (enrolled)'], data['Age at enrollment'])
plt.xlabel('Créditos 2do sem')
plt.ylabel('Edad')
plt.title('Gráfico de dispersión de la nota dada la edad')
plt.show()