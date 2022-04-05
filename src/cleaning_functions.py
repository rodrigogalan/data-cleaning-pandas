import re
import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta


def todatetime(x):
    if x != x:
        return np.nan
    try: return datetime.strptime(x,"%d-%b-%Y")
    except: return np.nan


def limpieza_year(x):
    if type(x) == float and x > 1700:
        x=int(x)
        return str(x)
    else:
        return np.nan


def limpieza_date1(x):
    if x != x:
        return np.nan
    x=str(x).replace(".", "-").replace(",","-")
    if x.split("-")[0].isdigit() and int(x.split("-")[0]) < 1700:
        return np.nan
    y=""
    for e in x:
        if e.isdigit() or e=="-":
            y+=e
    return y.strip("-")


def todatetime1(x):
    if x != x:
        return np.nan
    try: return datetime.strptime(x,"%Y-%m-%d")
    except: return np.nan


pattern_age = "\d{1,}"
def limpieza_age(i):
    if type(i) == str:
        if "month" in i:
            return int(np.mean(list(map(lambda x : int(int(x)//12), re.findall(pattern_age,i)))))

        elif "month" not in i:
            if len(list(map(lambda x: int(x),re.findall(pattern_age,i))))!= 0:
                return int(np.mean(list(map(lambda x: int(x),re.findall(pattern_age,i)))))
            else:
                return np.nan
    else:
        return  np.nan


def limpieza_sex(x):
    if x == "M " or x == "M":
        return "M"
    elif x == "F":
        return "F"
    else:
        return np.nan


def limpieza_fatal(x):
    if x in ['N', 'M',' N', 'N ']:
        return "NO"
    elif x in ['Y','y']:
        return "YES"
    else:
        return np.nan


pattern_time = "\d{1,2}"
def limpieza_time(x):
    x = str(x).lower()
    if "afternoon" in x or "afternon" in x:
        return str(random.randint(12, 19))
    elif "morning" in x:
        return str(random.randint(7, 12))
    elif "a.m" in x or "am" in x:
        return str(random.randint(0,12))
    elif "p.m" in x or "pm" in x:
        return str(random.randint(13,23))
    elif "midnight" in x:
        return str(random.choice([23,0,1]))
    elif "night" in x or "dusk" in x:
        return str(random.choice([18,19,20,21,22,23,0,1,2,3,4,5,6]))
    elif "lunchtime" in x or "midday" in x or "noon" in x:
        return str(random.randint(11,14))
    elif "evening" in x:
        return str(random.randint(19, 23))
    elif "sunset" in x:
        return str(random.randint(16, 20))
    elif len(re.findall(pattern_time,x)) != 0:
        time = int(re.findall(pattern_time,x)[0])
        if time < 24:
            return str(time)
    return np.nan


def limpieza_type(x):
    x = str(x).lower()
    if "boat" in x:
        return "Boating"
    elif "unprovoked" in x:
        return "Provoked"   
    elif "provoked" in x:
        return "Provoked"
    elif "sea" in x:
        return "Sea disaster"
    else:
        return np.nan


species_dict={
    "whitetip" : "whitetip reef shark",
    "whtietip" : "whitetip reef shark",
    "white" : "white shark",
    "bull" : "bull shark",
    "sandtiger" : "bull shark",
    "tiger" : "tiger shark",
    "lemon" : "lemon shark",
    "nurse" : "nurse shark",
    "caribbean" : "caribbean reef shark",
    "blacktip" : "blacktip reef shark",
    "blacktail" : "blacktip reef shark",
    "grey" : "grey reef shark",
    "gray" : "grey reef shark",
    "wobbegong" : "wobbegong shark",
    "blue" : "blue shark",
    "cookiecutter" : "cookiecutter shark",
    "spinner":"spinner shark",
    "sner" : "sner shark",
    "porbeagle" : "porbeagle shark",
    "galapagos" : "galapagos shark",
    "hammerhead" : "hammerhead shark",
    "mako" : "mako shark",
    "raggedtooth" : "raggedtooth shark",
    "gob" : "gob shark",
    "sandbar" : "sandbar shark",
    "whaler" : "bronze whaler shark",
    "dogfish" : "dogfish shark",
    "angel" : "angel shark",
    "silky" : "silky shark",
    "zambesi" : "zambesi shark",
    "salmon" : "salmon shark",
    "sevengill " : "sevengill  shark"
}


def limpieza_species(x):
    if x != x:
        return np.nan
    x = str(x).lower()
    for e in species_dict.keys():
        if e in x:
            return species_dict[e]    
    return np.nan


def limpieza_injury(x):
    if x != x:
        return np.nan
    x = str(x).lower()
    if "fatal" in x and "non" not in x:
        return "fatal"
    elif "no injury" in x or "not injured" in x:
        return "no injury"
    else:
        return "injury"


def quitar_acentos(palabra):
    cambios = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in cambios:
        palabra = palabra.replace(a, b).replace(a.upper(), b.upper())
    return palabra
    

path = "./data/paises.csv"
paises = pd.read_csv(path,encoding='utf-8')
list_paises=paises[" name"].tolist()
list_paises=list(map(quitar_acentos,list_paises))

country_dict={
    "Usa":"United States of America",
    "England":"United Kingdom",
    "Columbia":"Colombia",
    "Scotland":"United Kingdom",
    "Okinawa":"Japan"
}

def limpieza_country(x):
    if x!=x:
        return np.nan
    x = str(x).lower().title().strip()
    for e in country_dict.keys():
        if e == x:
            x = country_dict[e]
    if x not in list_paises:
        return np.nan
    else:
        return x

activity_dict = {
    "swimming":"swimming",
    "fishing":"fishing",
    "diving":"diving",
    "snorkel":"diving",
    "surf":"surf",
    "body boarding":"surf",
    "body-boarding":"surf",
    "boogie boarding":"surf",
    "paddleskiing":"surf",
    "bathing":"bathing",
    "floating":"bathing",
    "splashing":"bathing",
    "jumped into the water":"bathing",
    "playing":"bathing",
    "wading":"wading",
    "walking":"wading",
    "treading water":"wading",
    "standing":"standing",
    "kayaking":"boating",
    "ship":"boating",
    "sail":"boating",
    "boat":"boating",
    "canoeing":"boating",
    "board":"boating",
    "rowing":"boating",
    "fell into the water":"boating",
    "sea disaster":"sea disaster"
    }
    
def limpieza_activity(x):
    if x != x:
        return np.nan
    x = str(x).lower().strip()
    for e in activity_dict.keys():
        if e in x:
            return activity_dict[e]
    return np.nan


