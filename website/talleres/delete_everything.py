# Script que elimina todas los elementos de las tablas
import pandas as pd
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'talleres.settings'
django.setup()

from surprise import Reader
from surprise import Dataset
from surprise.model_selection import train_test_split
from surprise import KNNBasic
from surprise import accuracy
import pickle
import warnings
import gzip
warnings.filterwarnings("ignore")


from taller_1.models import RatingTemporal, User, User_info, Reproduction, Ratings, Artist, Homologacion_user, Homologacion_artist

# Resetea la matriz de ratings
print('Resetea los ratings')
df = pd.read_pickle('taller_1/otros/ratings.pkl')
df.loc[df.user_id <= 991].to_pickle('taller_1/otros/ratings.pkl', protocol = 4)
df.drop_duplicates(subset = ['user_id','artname'], keep = 'last', inplace = True)


reader = Reader( rating_scale = ( 1, 5 ) )

dataset_ratings = Dataset.load_from_df( df[ [ 'user_id', 'artname', 'rating_lineal']], reader )
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

df.to_pickle('taller_1/otros/ratings.pkl', protocol = 4)




RatingTemporal.objects.all().delete()
User.objects.all().delete()
User_info.objects.all().delete()
#Reproduction.objects.all().delete()
Ratings.objects.all().delete()
#Artist.objects.all().delete()
Homologacion_user.objects.all().delete()
#Homologacion_artist.objects.all().delete()


print('Deleted Everything')