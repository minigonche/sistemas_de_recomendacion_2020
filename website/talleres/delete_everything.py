# Script que elimina todas los elementos de las tablas
import pandas as pd
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'talleres.settings'
django.setup()

from taller_1.models import RatingTemporal, User, User_info, Reproduction, Ratings, Artist, Homologacion_user, Homologacion_artist

RatingTemporal.objects.all().delete()
User.objects.all().delete()
User_info.objects.all().delete()
Reproduction.objects.all().delete()
Ratings.objects.all().delete()
Artist.objects.all().delete()
Homologacion_user.objects.all().delete()
Homologacion_artist.objects.all().delete()

# Resetea la matriz de ratings
df = pd.read_pickle('taller_1/otros/ratings.pkl')
df.loc[df.user_id <= 991].to_pickle('taller_1/otros/ratings.pkl', protocol = 4)
print('Deleted Everything')