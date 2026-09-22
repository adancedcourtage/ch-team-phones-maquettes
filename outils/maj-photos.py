#!/usr/bin/env python3
"""Met a jour la liste des photos du site.

Utilisation :
    1. deposer les photos dans le dossier  img/
       nom du fichier = identifiant du produit  (ex : iphone-17-pro.jpg)
    2. lancer :  python3 outils/maj-photos.py

Formats acceptes : .jpg .jpeg .png .webp
Ideal : fond blanc ou transparent, produit detoure, 1200 px de haut minimum.
"""
import os, re, json, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(RACINE, 'img')
HTML = os.path.join(RACINE, 'index.html')
EXT = ('.jpg', '.jpeg', '.png', '.webp')

s = open(HTML, encoding='utf-8').read()
a = s.index('  var CATALOGUE = ') + len('  var CATALOGUE = ')
b = s.index(';\n  var LIB=')
catalogue = json.loads(s[a:b])
ids = {p['id'] for p in catalogue}

photos, inconnus = {}, []
for f in sorted(os.listdir(IMG)) if os.path.isdir(IMG) else []:
    base, ext = os.path.splitext(f)
    if ext.lower() not in EXT:
        continue
    if base in ids:
        photos[base] = f
    else:
        inconnus.append(f)

nouveau = '  var PHOTOS = ' + json.dumps(photos, ensure_ascii=False, sort_keys=True) + ';'
s = re.sub(r'  var PHOTOS = \{.*?\};', nouveau, s, count=1, flags=re.S)
open(HTML, 'w', encoding='utf-8').write(s)

print('%d photos reconnues sur %d produits' % (len(photos), len(catalogue)))
manquants = sorted(ids - set(photos))
if inconnus:
    print('\nFichiers ignores (nom inconnu au catalogue) :')
    for f in inconnus:
        print('   ', f)
if manquants:
    print('\n%d produits encore sans photo :' % len(manquants))
    for i in manquants:
        print('   ', i)
