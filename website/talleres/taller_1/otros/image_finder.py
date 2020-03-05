#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import pickle
import requests
import random
import pandas as pd
import sys

# Script the python para extraer URL de imagenes (con Google, obvio)

location = os.path.realpath(__file__)[0:-3]

images_location = 'taller_1/static/taller_1/img/'

link_header = 'taller_1/img/'

generic_image = 'taller_1/img/generic_artist.png'
  
def get_image(artist_name):

    #loads link data base
    db = load_obj()
    #print(str(db), file=sys.stderr)
    if artist_name in db:
        return(db[artist_name])

    # Default
    db[artist_name] = generic_image


    query = artist_name.replace(' ','+')
    
    url = 'https://www.google.com/search?q=' + query + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        if link != None and 'http' in link:
            # Saves link
            

            # Creates random name
            file_name = str(random.randint(10000,99999)) + '-' + str(random.randint(10000,99999)) + '-' + str(random.randint(10000,99999))
            file_location = images_location + file_name
            final_link = link_header + file_name
            resp = save_image(file_location, link)

            if resp:
                db[artist_name] = final_link
            else:
                db[artist_name] = generic_image

            save_db(db)

            break

    
    return(db[artist_name])

     

    
  
#print(get_image('underworld'))

def save_image(name, link):

    with open(name, 'wb') as handle:
            response = requests.get(link, stream=True)

            if not response.ok:
                return(False)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

    return(True)


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