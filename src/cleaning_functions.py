import re
import numpy as np
import pandas as pd
import random


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


def limpieza_year(x):
    if type(x) == float and x > 500:
        return int(x)
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
        return random.randint(12, 19)
    elif "morning" in x:
        return random.randint(7, 12)
    elif "a.m" in x or "am" in x:
        return random.randint(0,12)
    elif "p.m" in x or "pm" in x:
        return random.randint(13,23)
    elif "midnight" in x:
        return random.choice([23,0,1])
    elif "night" in x or "dusk" in x:
        return random.choice([18,19,20,21,22,23,0,1,2,3,4,5,6])
    elif "lunchtime" in x or "midday" in x or "noon" in x:
        return random.randint(11,14)
    elif "evening" in x:
        return random.randint(19, 23)
    elif "sunset" in x:
        return random.randint(16, 20)
    elif len(re.findall(pattern_time,x)) != 0:
        time = int(re.findall(pattern_time,x)[0])
        if time < 24:
            return time
        else:
            return np.nan
    else:
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


def limpieza_meses(x):
    meses = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    x = str(x)
    for i in range(12):
        if meses[i] in x.lower():
            return i+1
    else:
        return np.nan


pattern_dias1 = "\d{1,2}-"
pattern_dias2 =  "\.\d{2}\."
def limpieza_dias(x):
    x = str(x)
    if len(re.findall(pattern_dias1,x)) != 0:
        day = int(re.findall(pattern_dias1,x)[0][:-1])
        if day < 32:
            return day
        else:
            return np.nan
    elif len(re.findall(pattern_dias2,x)) != 0:
        day = int(re.findall(pattern_dias2,x)[0][1:3])
        if day<32 and day>0:
            return day
        else:
            return np.nan
    else:
        return np.nan


def limpieza_species(x):
    x = str(x).lower()
    if "whitetip" in x or "whtietip" in x:
        return "whitetip reef shark"
    elif "white" in x:
        return "white shark"
    elif "bull" in x or "sandtiger" in x:
        return "bull shark"
    elif "tiger" in x:
        return "tiger shark"
    elif "lemon" in x:
        return "lemon shark"
    elif "nurse" in x:
        return "nurse shark"
    elif "caribbean" in x:
        return "caribbean reef shark"
    elif "blacktip" in x or "blacktail" in x:
        return "blacktip reef shark"
    elif "grey" in x or "gray" in x:
        return "grey reef shark"
    elif "wobbegong" in x:
        return "wobbegong shark"
    elif "blue" in x:
        return "blue shark"
    elif "nan" == x:
        return np.nan
    elif "unconfirmed" in x or "confirmed" in x or "questionable" in x or "no " in x or "not " in x:
        return np.nan
    elif "cookiecutter" in x:
        return "cookiecutter shark"
    elif "spinner" in x:
        return "spinner shark"
    elif "porbeagle" in x:
        return "porbeagle shark"
    elif "galapagos" in x:
        return "galapagos shark"
    elif "hammerhead" in x:
        return "hammerhead shark"
    elif "mako" in x:
        return "mako shark"
    elif "raggedtooth" in x:
        return "raggedtooth shark"
    elif "goblin" in x:
        return "goblin shark"
    elif "sandbar" in x:
        return "sandbar shark"
    elif "whaler" in x:
        return "bronze whaler shark"
    elif "dogfish" in x:
        return "dogfish shark"
    elif "angel" in x:
        return "angel shark"
    elif "silky" in x:
        return "silky shark"
    elif "zambesi" in x:
        return "zambesi shark"
    elif "salmon" in x:
        return "salmon shark"
    elif "sevengill " in x:
        return "sevengill  shark"
    else:
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


path = "/mnt/d/rodrigo/escritorio/Ironhack/Data-analytics/proyectos/data-cleaning-pandas/data/paises.csv"
paises = pd.read_csv(path,encoding='utf-8')
list_paises=paises[" name"].tolist()
list_paises=list(map(quitar_acentos,list_paises))
def limpieza_country(x):
    if x!=x:
        return np.nan
    x = str(x).lower().title().strip()
    if x!=x:
        return np.nan
    if "Usa" == x:
        x = "United States of America"
    if x == "England":
        x = "United Kingdom"
    if x == "Columbia":
        x = "Colombia"
    if x == "Scotland":
        x = "United Kingdom"
    if x == "Okinawa":
        x = "Japan"
    if x not in list_paises:
        return np.nan
    else:
        return x


def limpieza_activity(x):
    if x != x:
        return np.nan
    x = str(x).lower().strip()
    if "swimming" in x:
        return "swimming"
    elif "fishing" in x:
        return "fishing"
    elif "diving" in x or "snorkel" in x:
        return "diving"
    elif "surf" in x or "body boarding" in x or "body-boarding" in x or "boogie boarding" in x or "paddleskiing" in x:
        return "surf"
    elif "bathing" in x or "floating" in x or "splashing" in x or "jumped into the water" in x or "playing" in x:
        return "bathing"
    elif "wading" in x or "walking" in x or "treading water" in x:
        return "wading"
    elif "standing" in x:
        return "standing"
    elif "kayaking" in x or "ship" in x or "sail" in x or "boat" in x or "canoeing" in x or "board" in x or "rowing" in x or "fell into the water" in x:
        return "boating"
    elif "sea disaster" in x:
        return "sea disaster"
    else:
        return np.nan