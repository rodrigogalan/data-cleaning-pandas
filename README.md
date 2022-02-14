# Data-cleaning-pandas
<dl>
  <center>
  <img src="https://c.tenor.com/q4xhISzHE6MAAAAC/buscando-a-nemo.gif" alt="Gif">   
</center>
</dl>

En este proyecto se ha importado un data set de [Kaggle](https://www.kaggle.com/teajay/global-shark-attacks) sobre muertes de tiburón. Las hipótesis son:
1. El surf el deporte más peligroso en relacion a los accidentes por tiburón 
2. El número de muertes por tiburón en función del número de casos ha disminuido en los últimos años.

***
## Método
1. Descarga e importación del .csv como pandas data frame.
2. Exploración de los datos y limpieza rápida eliminando aquellas filas y columnas sin información.
3. Limpieza detallada de las columnas útiles empleando el archivo auxiliar de funciones y exportación de los datos, en este paso se ha usado un csv auxiliar [paises.csv](https://gist.github.com/brenes/1095110/4422fd7ba3a388f31a9a017757e21e5df23c5916).
4. Visualización de los datos para la obtención de conclusiones.

## Documentos
### Jupyter notebooks
* [1.clean.ipynb](https://github.com/rodrigogalan/data-cleaning-pandas/blob/main/code/1.clean.ipynb): importación de datos y limpieza
* [2.analysis.ipynb](https://github.com/rodrigogalan/data-cleaning-pandas/blob/main/code/2.analysis.ipynb): visulización de datos
### Data
* [data/shark_attacks.csv](https://github.com/rodrigogalan/data-cleaning-pandas/blob/main/data/shark_attacks.csv): datos limpios
* [data/paises.csv](https://github.com/rodrigogalan/data-cleaning-pandas/blob/main/data/paises.csv): nombres de paises
### Functions
* [src/cleaning_functions.py](https://github.com/rodrigogalan/data-cleaning-pandas/blob/main/src/cleaning_functions.py): funciones auxiliares de limpieza

## Librerias
* [re](https://docs.python.org/3/library/re.html) 
* [numpy](https://numpy.org/doc/1.22/)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/) 
* [sys](https://docs.python.org/3/library/sys.html)
* [plotly.express](https://plotly.com/python-api-reference/)

