#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

# Script the python para extraer URL de imagenes (con Google, obvio)

  
def get_image(artist_name): 

    artist_name = artist_name.replace(' ','+')
    query = artist_name
    
    url = 'https://www.google.com/search?q=' + query + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    for raw_img in soup.find_all('img'):
        link = raw_img.get('src')
        if link != None and 'http' in link:
        	return(link)

    return('link geenrico')
  
#print(get_image('underworld'))