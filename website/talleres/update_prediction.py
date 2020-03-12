# Script que calcula de nuevo el modelo de prediccion segun los datos en la base de datos de DJANGO
import pandas as pd
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'talleres.settings'
django.setup()

from taller_1.models import RatingTemporal

import numpy as np
import pandas as pd
import time
from surprise import Reader
from surprise import Dataset
from surprise.model_selection import train_test_split
from surprise import KNNBasic
from surprise import accuracy
import pickle
import warnings
import gzip
warnings.filterwarnings("ignore")



user_id = []
artname = []
rating_lineal = []
for rat in RatingTemporal.objects.all():

	user_id.append(rat.user_id_pos)
	artname.append(rat.artist_id_pos)
	rating_lineal.append(rat.rating_lineal)


tail = pd.DataFrame({'user_id':user_id, 'artname':artname, 'rating_lineal':rating_lineal})
head = pd.read_pickle('taller_1/otros/ratings.pkl')



final = pd.concat((tail,head), ignore_index = True)
final.drop_duplicates(subset = ['user_id','artname'], keep = 'last', inplace = True)

print('Loaded Ratings')
print('Initial Ratings: {}'.format(head.shape[0]) )
print('Total Ratings: {}'.format(final.shape[0]) )
print('New Ratings: {}'.format(final.shape[0] - head.shape[0]) )
print()

if final.shape[0] - head.shape[0] == 0:
	print('No new Ratings. Skipping')

else:
	reader = Reader( rating_scale = ( 1, 5 ) )

	dataset_ratings = Dataset.load_from_df( final[ [ 'user_id', 'artname', 'rating_lineal']], reader )
	trainset = dataset_ratings.build_full_trainset()

	# Configuración de parametros
	sim_options = {'name': 'cosine','user_based': True , 'min_support': 0.00001}
	model = KNNBasic(k=34, min_k=2, sim_options=sim_options)

	#Se le pasa la matriz de utilidad al algoritmo, es decir, el conjunto de entrenamiento
	model.fit(trainset=trainset)

	print('Model computed')

	f = gzip.open('taller_1/otros/3.Model_User_User.pklz','wb')
	pickle.dump(model,f)
	f.close()

	print('Model Saved')

	final.to_pickle('taller_1/otros/ratings.pkl', protocol = 4)
	print('Ratings Saved')


# Deletes the temporal ratings
RatingTemporal.objects.all().delete()

print('Temporal Ratings Removed')
