
import pandas as pd

def predecir_probabilidad_desercion(Debtor, Gender, Scholarship, approved1 , grade1, approved2, grade2):
    
    ruta = "D:/datos usuario/Documents/Universidad de los Andes/2023-20/Analitica/Proyecto/data_mod_copia2.xlsx"

    datos = pd.read_excel(ruta)

    from pgmpy.models import BayesianNetwork
    modelo = BayesianNetwork ([("Gender", "Scholarship holder"), ("Scholarship holder", "Debtor"), ("Scholarship holder", "Target"), ("Debtor","Target"), 
                            ("Curricular units 1st sem (grade)","Target"), ("Curricular units 1st sem (grade)", "Curricular units 1st sem (approved)"), ("Curricular units 1st sem (approved)","Target"), 
                            ("Curricular units 2nd sem (grade)","Target"), ("Curricular units 2nd sem (grade)", "Curricular units 2nd sem (approved)"), ("Curricular units 2nd sem (approved)","Target")])

    from sklearn.model_selection import train_test_split
    # Dividir los datos
    # X crea un dataframe que contiene todas la columnas menos 'target'. Es decir, las caracteristicas que utilizara para hacer predicciones
    X = datos.drop(columns=['Target'])
    # Y crea una serie que contiene solo la columna "Target". 
    y = datos['Target']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

    from pgmpy.estimators import MaximumLikelihoodEstimator
    emv = MaximumLikelihoodEstimator(modelo , data = datos)

    modelo.fit(data=datos , estimator = MaximumLikelihoodEstimator )

    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

    y_pred = modelo.predict(X_test)

    from pgmpy.inference import VariableElimination 
    infer = VariableElimination(modelo)

    # Utilizar el modelo Bayesian Network para predecir la probabilidad de deserción
    probabilidad_desercion = infer.query(["Target"], evidence={"Debtor": Debtor , "Gender": Gender, "Scholarship holder": Scholarship, "Curricular units 1st sem (approved)": approved1, "Curricular units 1st sem (grade)": grade1, "Curricular units 2nd sem (approved)": grade2, "Curricular units 2nd sem (grade)": approved2})

    return probabilidad_desercion

predecir_probabilidad_desercion(0, 1, 1, 1, 1, 2, 2)