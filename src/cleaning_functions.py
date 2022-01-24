import re
import numpy as np
import pandas as pd

pattern_age = "\d{1,}"
def limpieza_age(i):
    if type(i) == str:
        if "month" in i:
            return int(np.mean(list(map(lambda x : int(int(x)//12), re.findall(pattern_age,i)))))

        elif "month" not in i:
            if len(list(map(lambda x: int(x),re.findall(pattern_age,i))))!= 0:
                return int(np.mean(list(map(lambda x: int(x),re.findall(pattern_age,i)))))
            else:
                return "unknown"
    else:
        return "unknown"

def limpieza_sex(x):
    if x == "M " or x == "M":
        return "M"
    elif x == "F":
        return "F"
    else:
        return None

def limpieza_year(x):
    if type(x) == float and x > 500:
        return int(x)
    else:
        return "unknown"

def limpieza_fatal(x):
    if x in ['N', 'M',' N', 'N ']:
        return "NO"
    elif x in ['Y','y']:
        return "YES"
    else:
        return "unknown"

pattern_time = "\d{1,}"

        
