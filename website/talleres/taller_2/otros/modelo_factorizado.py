# Script Modelo Por Contexto
# Scripts para el modelo por contenido


import json
import os
import pandas as pd
import numpy as np
import pickle


import gzip
import surprise

todos_lugares = set(['OTHER', 'NC', 'AZ', 'QC', 'NV', 'IL', 'ON', 'AB', 'PA', 'WI', 'SC', 'OH'])


                
ubicacion = 'taller_2/otros/data/SVD/'




def dar_calificacion(id_usuarios, id_businesses):
    
    id_usuario = id_usuarios[0]
    id_business = id_businesses[0]
    
    # Lee las bd
    tabla_u = pd.read_pickle(ubicacion + 'usuarios_id.pkl')
    tabla_b = pd.read_pickle(ubicacion + 'negocios_id.pkl')
    
    # Lee la matriz de calificaciones
    f = gzip.open(ubicacion +'0.Model_SVM.pklz','rb')
    Model_SVM = pickle.load(f)
    
    pred = []
    for i in range(len(id_usuarios)):
        usuario = tabla_u.loc[id_usuarios[i]].new_id
        neg = tabla_b.loc[id_businesses[i]].new_id
        
        p = Model_SVM.predict(usuario, neg).est
        pred.append(p)
    
    return(pred)