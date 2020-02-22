#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import pickle

# Script the python para extraer URL de imagenes (con Google, obvio)

location = os.path.realpath(__file__)[0:-3]
  
def get_image(artist_name):

    #loads link data base
    db = load_obj()

    if artist_name in db:
        return(db[artist_name])

    artist_name = artist_name.replace(' ','+')
    query = artist_name
    
    url = 'https://www.google.com/search?q=' + query + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        if link != None and 'http' in link:
            # Saves link
            db[artist_name] = link
            save_db(db)
            return(link)

    return('link geenrico')
  
#print(get_image('underworld'))


def save_db(db):
    with open(location + '_links_db.pkl', 'wb') as f:
        pickle.dump(db, f, pickle.HIGHEST_PROTOCOL)

def load_obj():
    try:
        with open(location + '_links_db.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        with open(location + '_links_db.pkl', 'wb') as f:
            pickle.dump({}, f, pickle.HIGHEST_PROTOCOL)
            return({})