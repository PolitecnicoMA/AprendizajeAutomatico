# Descripción de la base completa

**En este cuaderno se trabaja con la descripción de las variables que componen el dataframe**


```python
import numpy as np
import pandas as pd
```


```python
df = pd.read_csv(r'C:\Users\nadpe\Downloads\df_completo.csv')
```


```python
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>fecha</th>
      <th>prov_residencia_persona_en_situacion_violencia</th>
      <th>genero_persona_en_situacion_de_violencia</th>
      <th>edad_persona_en_situacion_de_violencia</th>
      <th>pais_nacimiento_persona_en_situacion_de_violencia</th>
      <th>tipo_de_violencia_fisica</th>
      <th>tipo_de_violencia_psicologica</th>
      <th>tipo_de_violencia_sexual</th>
      <th>tipo_de_violencia_economica_y_patrimonial</th>
      <th>tipo_de_violencia_simbolica</th>
      <th>tipo_de_violencia_domestica</th>
      <th>modalidad_de_violencia_institucional</th>
      <th>modalidad_de_violencia_laboral</th>
      <th>modalidad_violencia_contra_libertad_reproductiva</th>
      <th>modalidad_de_violencia_obstetrica</th>
      <th>modalidad_de_violencia_mediatica</th>
      <th>modalidad_de_violencia_otras</th>
      <th>vinculo_con_la_persona_agresora</th>
      <th>genero_de_la_persona_agresora</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2020-01-01</td>
      <td>Tucumán</td>
      <td>Mujer</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2020-01-01</td>
      <td>Buenos Aires</td>
      <td>Mujer</td>
      <td>39.0</td>
      <td>NaN</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ex pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2020-01-01</td>
      <td>Buenos Aires</td>
      <td>Mujer</td>
      <td>22.0</td>
      <td>Argentina</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ex pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2020-01-01</td>
      <td>Buenos Aires</td>
      <td>Mujer</td>
      <td>53.0</td>
      <td>NaN</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2020-01-01</td>
      <td>Buenos Aires</td>
      <td>Mujer</td>
      <td>38.0</td>
      <td>Argentina</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>2020-01-01</td>
      <td>Buenos Aires</td>
      <td>Mujer</td>
      <td>23.0</td>
      <td>Argentina</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ex pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>2020-01-01</td>
      <td>Santiago Del Estero</td>
      <td>Mujer</td>
      <td>25.0</td>
      <td>Paraguaya</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>2020-01-01</td>
      <td>Santa Fe</td>
      <td>Mujer</td>
      <td>24.0</td>
      <td>Argentina</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ex pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>2020-01-01</td>
      <td>Santa Fe</td>
      <td>Mujer</td>
      <td>NaN</td>
      <td>Argentina</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Pareja</td>
      <td>Varon</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>2020-01-01</td>
      <td>San Juan</td>
      <td>Mujer</td>
      <td>21.0</td>
      <td>Argentina</td>
      <td>Si</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Pareja</td>
      <td>Varon</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 89541 entries, 0 to 89540
    Data columns (total 20 columns):
     #   Column                                             Non-Null Count  Dtype  
    ---  ------                                             --------------  -----  
     0   Unnamed: 0                                         89541 non-null  int64  
     1   fecha                                              89541 non-null  object 
     2   prov_residencia_persona_en_situacion_violencia     88377 non-null  object 
     3   genero_persona_en_situacion_de_violencia           87637 non-null  object 
     4   edad_persona_en_situacion_de_violencia             72263 non-null  float64
     5   pais_nacimiento_persona_en_situacion_de_violencia  59260 non-null  object 
     6   tipo_de_violencia_fisica                           89541 non-null  object 
     7   tipo_de_violencia_psicologica                      89541 non-null  object 
     8   tipo_de_violencia_sexual                           89541 non-null  object 
     9   tipo_de_violencia_economica_y_patrimonial          89541 non-null  object 
     10  tipo_de_violencia_simbolica                        89541 non-null  object 
     11  tipo_de_violencia_domestica                        89541 non-null  object 
     12  modalidad_de_violencia_institucional               89541 non-null  object 
     13  modalidad_de_violencia_laboral                     89541 non-null  object 
     14  modalidad_violencia_contra_libertad_reproductiva   89541 non-null  object 
     15  modalidad_de_violencia_obstetrica                  89541 non-null  object 
     16  modalidad_de_violencia_mediatica                   89541 non-null  object 
     17  modalidad_de_violencia_otras                       89541 non-null  object 
     18  vinculo_con_la_persona_agresora                    86146 non-null  object 
     19  genero_de_la_persona_agresora                      80328 non-null  object 
    dtypes: float64(1), int64(1), object(18)
    memory usage: 13.7+ MB
    

Aquí se observa que la base cuenta con 89540 observaciones y 20 variables. Algunas de ellas poseen menos cantidad de datos no nulos. (género_persona_en_situacion_de_violencia, edad_persona_en_situacio_de_violencia, prov_residencia_persona_en_situacion_violencia pais_nacimiento_persona_en_situacion_de_violencia, vinculo_con_la_persona_agresora y genero_de_la_persona_agresora) 

## Se describen las variables

### Variable provincia de residencia


```python
#Se chequean la cantidad de ocurrencias de cada uno de los elementos de la variable prov_residencia_persona_en_situacion_violencia
provincias = df.groupby('prov_residencia_persona_en_situacion_violencia')['prov_residencia_persona_en_situacion_violencia'].nunique()
print(provincias)
```

    prov_residencia_persona_en_situacion_violencia
    Buenos Aires                                               1
    Catamarca                                                  1
    Chaco                                                      1
    Chubut                                                     1
    Ciudad Autónoma de Buenos Aires                            1
    Cordoba                                                    1
    Corrientes                                                 1
    Córdoba                                                    1
    Entre Ríos                                                 1
    Formosa                                                    1
    Jujuy                                                      1
    La Pampa                                                   1
    La Rioja                                                   1
    Mendoza                                                    1
    Misiones                                                   1
    Neuquén                                                    1
    Río Negro                                                  1
    Salta                                                      1
    San Juan                                                   1
    San Luis                                                   1
    Santa Cruz                                                 1
    Santa Fe                                                   1
    Santiago Del Estero                                        1
    Santiago del Estero                                        1
    Sin Datos                                                  1
    Sin datos                                                  1
    Tierra del Fuego  Antártida e Islas del Atlántico Sur""    1
    Tierra del Fuego, Antártida e Islas del Atlántico Sur      1
    Tucumán                                                    1
    Name: prov_residencia_persona_en_situacion_violencia, dtype: int64
    


```python
#Debieron modificarse unos valores que se duplicaban

df['prov_residencia_persona_en_situacion_violencia'] = df['prov_residencia_persona_en_situacion_violencia'].replace('Sin Datos','Sin datos')
```


```python
df['prov_residencia_persona_en_situacion_violencia'] = df['prov_residencia_persona_en_situacion_violencia'].replace('Santiago Del Estero','Santiago del Estero')
```


```python
df['prov_residencia_persona_en_situacion_violencia'] = df['prov_residencia_persona_en_situacion_violencia'].replace('Tierra del Fuego  Antártida e Islas del Atlántico Sur""','Tierra del Fuego, Antártida e Islas del Atlántico Sur')
```


```python
cantidad_por_provincia = df.groupby(['prov_residencia_persona_en_situacion_violencia']).size()
cantidad_por_provincia
```




    prov_residencia_persona_en_situacion_violencia
    Buenos Aires                                             48565
    Catamarca                                                  298
    Chaco                                                      801
    Chubut                                                     280
    Ciudad Autónoma de Buenos Aires                          17397
    Cordoba                                                    660
    Corrientes                                                 512
    Córdoba                                                   1950
    Entre Ríos                                                 631
    Formosa                                                    333
    Jujuy                                                     1252
    La Pampa                                                    92
    La Rioja                                                   291
    Mendoza                                                   3132
    Misiones                                                   545
    Neuquén                                                    613
    Río Negro                                                  454
    Salta                                                     1232
    San Juan                                                   654
    San Luis                                                   733
    Santa Cruz                                                 140
    Santa Fe                                                  3785
    Santiago del Estero                                        562
    Sin datos                                                  148
    Tierra del Fuego, Antártida e Islas del Atlántico Sur       93
    Tucumán                                                   3224
    dtype: int64



En esta variable se observa la distribución real de los casos por provincia, en futuros análisis se realizará el análisis proporcional de la distribución de frecuencias. La mayor cantidad de casos se encuentra en la provincia de Buenos Aires y la menor en Jujuy.

### Variable edades



```python
desc_edades = df['edad_persona_en_situacion_de_violencia'].describe()
desc_edades
#Se observan datos atípicos tanto en los valores máximos como en los mismos.
#Se decide la búsqueda y la eliminación de aquellas observación con valor de 127 por tratarse de un valor atípico que
#puede estar haciendo referencia a otro error.
```




    count    72263.000000
    mean        35.687945
    std         12.596980
    min          1.000000
    25%         27.000000
    50%         34.000000
    75%         42.000000
    max        127.000000
    Name: edad_persona_en_situacion_de_violencia, dtype: float64




```python
mayores = df[df['edad_persona_en_situacion_de_violencia'] >100]
mayores
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>fecha</th>
      <th>prov_residencia_persona_en_situacion_violencia</th>
      <th>genero_persona_en_situacion_de_violencia</th>
      <th>edad_persona_en_situacion_de_violencia</th>
      <th>pais_nacimiento_persona_en_situacion_de_violencia</th>
      <th>tipo_de_violencia_fisica</th>
      <th>tipo_de_violencia_psicologica</th>
      <th>tipo_de_violencia_sexual</th>
      <th>tipo_de_violencia_economica_y_patrimonial</th>
      <th>tipo_de_violencia_simbolica</th>
      <th>tipo_de_violencia_domestica</th>
      <th>modalidad_de_violencia_institucional</th>
      <th>modalidad_de_violencia_laboral</th>
      <th>modalidad_violencia_contra_libertad_reproductiva</th>
      <th>modalidad_de_violencia_obstetrica</th>
      <th>modalidad_de_violencia_mediatica</th>
      <th>modalidad_de_violencia_otras</th>
      <th>vinculo_con_la_persona_agresora</th>
      <th>genero_de_la_persona_agresora</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>47135</th>
      <td>17429</td>
      <td>2021-09-10</td>
      <td>Ciudad Autónoma de Buenos Aires</td>
      <td>NaN</td>
      <td>127.0</td>
      <td>Venezolana</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>Padre o tutor</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>58006</th>
      <td>2999</td>
      <td>2022-02-14</td>
      <td>Ciudad Autónoma de Buenos Aires</td>
      <td>Mujer</td>
      <td>103.0</td>
      <td>NaN</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Si</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Otro familiar</td>
      <td>Varon</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df[df['edad_persona_en_situacion_de_violencia'] != 127]
```


```python
df['edad_persona_en_situacion_de_violencia'].describe()
```




    count    72262.000000
    mean        35.686682
    std         12.592487
    min          1.000000
    25%         27.000000
    50%         34.000000
    75%         42.000000
    max        103.000000
    Name: edad_persona_en_situacion_de_violencia, dtype: float64



En esta descripción se observa que la totalidad de las filas del data frame que tienen datos son 72262, es decir que hay 17189 casos en los que no se registra la edad de las personas.
La media de la edad es de 35 años, con una desviación estandar de 12. La mediana es 34 años, con lo que puede pensarse que el conjunto de datos tiende a la simetría.
La edad mínima es de 1 año y la máxima de 103.


### Descripción del género de la persona en situación de violencia


```python
desc_gen1 = df.groupby(df['genero_persona_en_situacion_de_violencia']).size()
desc_gen1
```




    genero_persona_en_situacion_de_violencia
    Intersexual        4
    Mujer          86884
    Mujer Trans      141
    No Binarie         3
    Otro              67
    Queer              1
    Transgenero      128
    Transgénero       23
    Travesti          11
    Varon            349
    Varon Trans       12
    Varon trans        1
    Varón Trans       13
    dtype: int64




```python
#Debió homogeneizarse las categorías de la siguiente manera
df['genero_persona_en_situacion_de_violencia'] = df['genero_persona_en_situacion_de_violencia'].replace('Transgénero','Transgenero')
df['genero_persona_en_situacion_de_violencia'] = df['genero_persona_en_situacion_de_violencia'].replace('Varon trans','Varon Trans')
df['genero_persona_en_situacion_de_violencia'] = df['genero_persona_en_situacion_de_violencia'].replace('Varón Trans','Varon Trans')

```


```python
desc_gen1 = df.groupby(df['genero_persona_en_situacion_de_violencia']).size()
desc_gen1
```




    genero_persona_en_situacion_de_violencia
    Intersexual        4
    Mujer          86884
    Mujer Trans      141
    No Binarie         3
    Otro              67
    Queer              1
    Transgenero      151
    Travesti          11
    Varon            349
    Varon Trans       26
    dtype: int64



Como se vio anteriormente esta variable cuenta con 87637 observaciones. De ellas, la mayoría corresponden con el género "Mujer" que tiene la mayor cantidad de frecuencia, mientras que el género "Queer" es el que menor cantidad de frecuencias tiene (1).

### Descripción de país de nacimiento


```python
desc_nac = df.groupby(df['pais_nacimiento_persona_en_situacion_de_violencia']).size()
desc_nac
```




    pais_nacimiento_persona_en_situacion_de_violencia
    ARABE                 1
    ARMENIA               5
    Alemana               8
    Arabe                 2
    Argentina         52943
    Armenia              10
    Australiana           6
    Belga                 2
    Boliviana          1290
    Brasileña           146
    Canadiense            1
    Chilena             131
    Colombiana          237
    Costarricense         1
    Cubana                7
    Dominicana           23
    Ecuatoriana          12
    Española             13
    Estadounidense       13
    Francesa              1
    Griega                1
    Guatemalteca          2
    Israelí               1
    Italiana              5
    Japonesa              2
    Letona                1
    Libano                1
    Lituania              1
    Mexicana              8
    Nicaragüense          1
    Otra                111
    Otro                 44
    Palestina             1
    Panameña              1
    Paraguaya          2553
    Peruana             989
    Rusa                  2
    Salvadoreña           3
    Turca                 1
    Ucraniana             1
    Uruguaya            201
    Venezolana          475
    Vietnamita            1
    peruana               1
    dtype: int64




```python
#Debió homogeneizarse las categorías de la siguiente manera
df['pais_nacimiento_persona_en_situacion_de_violencia'] = df['pais_nacimiento_persona_en_situacion_de_violencia'].replace('peruana','Peruana')
df['pais_nacimiento_persona_en_situacion_de_violencia'] = df['pais_nacimiento_persona_en_situacion_de_violencia'].replace('Otro','Otra')
df['pais_nacimiento_persona_en_situacion_de_violencia'] = df['pais_nacimiento_persona_en_situacion_de_violencia'].replace('ARABE','Arabe')

```


```python
desc_nac1 = df.groupby(df['pais_nacimiento_persona_en_situacion_de_violencia']).size()
desc_nac1
```




    pais_nacimiento_persona_en_situacion_de_violencia
    ARMENIA               5
    Alemana               8
    Arabe                 3
    Argentina         52943
    Armenia              10
    Australiana           6
    Belga                 2
    Boliviana          1290
    Brasileña           146
    Canadiense            1
    Chilena             131
    Colombiana          237
    Costarricense         1
    Cubana                7
    Dominicana           23
    Ecuatoriana          12
    Española             13
    Estadounidense       13
    Francesa              1
    Griega                1
    Guatemalteca          2
    Israelí               1
    Italiana              5
    Japonesa              2
    Letona                1
    Libano                1
    Lituania              1
    Mexicana              8
    Nicaragüense          1
    Otra                155
    Palestina             1
    Panameña              1
    Paraguaya          2553
    Peruana             990
    Rusa                  2
    Salvadoreña           3
    Turca                 1
    Ucraniana             1
    Uruguaya            201
    Venezolana          475
    Vietnamita            1
    dtype: int64



Como se vio anteriormente esta variable cuenta con 59260  observaciones. De ellas, la mayoría corresponden con país de nacimiento "Argentina" que tiene la mayor cantidad de frecuencia (52943) y se observan diversos países con solo 1 observación.

## Descripción tipo de violencia


```python
desc_tv_fisica = df.groupby(df['tipo_de_violencia_fisica']).size()
desc_tv_fisica

```




    tipo_de_violencia_fisica
    No    30575
    Si    58965
    dtype: int64




```python
desc_tv_psicologica = df.groupby(df['tipo_de_violencia_psicologica']).size()
desc_tv_psicologica
```




    tipo_de_violencia_psicologica
    No     4547
    Si    84993
    dtype: int64




```python
desc_tv_sexual = df.groupby(df['tipo_de_violencia_sexual']).size()
desc_tv_sexual
```




    tipo_de_violencia_sexual
    No    77302
    SI        1
    Si    12237
    dtype: int64




```python
df['tipo_de_violencia_sexual'] = df['tipo_de_violencia_sexual'].replace('SI','Si')

```


```python
desc_tv_economica_y_patrimonial = df.groupby(df['tipo_de_violencia_economica_y_patrimonial']).size()
desc_tv_economica_y_patrimonial

```




    tipo_de_violencia_economica_y_patrimonial
    No    53609
    Si    35931
    dtype: int64




```python
desc_tv_simbolica = df.groupby(df['tipo_de_violencia_simbolica']).size()
desc_tv_simbolica
```




    tipo_de_violencia_simbolica
    No    58958
    SI      427
    Si    30155
    dtype: int64




```python
df['tipo_de_violencia_simbolica'] = df['tipo_de_violencia_simbolica'].replace('SI','Si')
```


```python
desc_tv_domestica = df.groupby(df['tipo_de_violencia_domestica']).size()
desc_tv_domestica
```




    tipo_de_violencia_domestica
    No     8205
    Si    81335
    dtype: int64




```python
tv_agrupada = [desc_tv_fisica, desc_tv_psicologica,desc_tv_sexual,desc_tv_economica_y_patrimonial,desc_tv_simbolica,desc_tv_domestica]
tv_agrupada
```




    [tipo_de_violencia_fisica
     No    30575
     Si    58965
     dtype: int64,
     tipo_de_violencia_psicologica
     No     4547
     Si    84993
     dtype: int64,
     tipo_de_violencia_sexual
     No    77302
     SI        1
     Si    12237
     dtype: int64,
     tipo_de_violencia_economica_y_patrimonial
     No    53609
     Si    35931
     dtype: int64,
     tipo_de_violencia_simbolica
     No    58958
     SI      427
     Si    30155
     dtype: int64,
     tipo_de_violencia_domestica
     No     8205
     Si    81335
     dtype: int64]



En el caso de la descripción de las variables que califican los tipos de violencia consultadas a la línea 144 podemos observar las siguientes conclusiones:
 - El tipo de violencia con mayor recurrencia fue la violencia psicológica (84993) 
 - El tipo de violenciacon menor recurrencia fue la violencia sexual (12238)
 

## Descripción modalidad de violencia


```python
desc_mv_institucional = df.groupby(df['modalidad_de_violencia_institucional']).size()
desc_mv_institucional
```




    modalidad_de_violencia_institucional
    No    88236
    SI       16
    Si     1288
    dtype: int64




```python
df['modalidad_de_violencia_institucional'] = df['modalidad_de_violencia_institucional'].replace('SI','Si')

```


```python
desc_mv_laboral = df.groupby(df['modalidad_de_violencia_laboral']).size()
desc_mv_laboral
```




    modalidad_de_violencia_laboral
    No    88289
    SI        1
    Si     1250
    dtype: int64




```python
df['modalidad_de_violencia_laboral'] = df['modalidad_de_violencia_laboral'].replace('SI','Si')
```


```python
desc_mv_contra_libertad_reproductiva  = df.groupby(df['modalidad_violencia_contra_libertad_reproductiva']).size()
desc_mv_contra_libertad_reproductiva 
```




    modalidad_violencia_contra_libertad_reproductiva
    No    89140
    SI        5
    Si      395
    dtype: int64




```python
df['modalidad_de_violencia_obstetrica'] = df['modalidad_de_violencia_obstetrica'].replace('SI','Si')
desc_mv_obstetrica = df.groupby(df['modalidad_de_violencia_obstetrica']).size()
desc_mv_obstetrica
```




    modalidad_de_violencia_obstetrica
    No    89455
    Si       85
    dtype: int64




```python
df['modalidad_de_violencia_mediatica'] = df['modalidad_de_violencia_mediatica'].replace('SI','Si')
desc_mv_mediatica = df.groupby(df['modalidad_de_violencia_mediatica']).size()
desc_mv_mediatica
```




    modalidad_de_violencia_mediatica
    No    89487
    Si       53
    dtype: int64




```python
df['modalidad_de_violencia_otras'] = df['modalidad_de_violencia_otras'].replace('SI','Si')
desc_mv_otras = df.groupby(df['modalidad_de_violencia_otras']).size()
desc_mv_otras
```




    modalidad_de_violencia_otras
    No    87434
    Si     2106
    dtype: int64




```python
mv_agrupada = [desc_mv_mediatica, desc_mv_obstetrica,desc_mv_contra_libertad_reproductiva,desc_mv_laboral,desc_mv_institucional,desc_mv_otras]
mv_agrupada
```




    [modalidad_de_violencia_mediatica
     No    89487
     Si       53
     dtype: int64,
     modalidad_de_violencia_obstetrica
     No    89455
     Si       85
     dtype: int64,
     modalidad_violencia_contra_libertad_reproductiva
     No    89140
     SI        5
     Si      395
     dtype: int64,
     modalidad_de_violencia_laboral
     No    88289
     SI        1
     Si     1250
     dtype: int64,
     modalidad_de_violencia_institucional
     No    88236
     SI       16
     Si     1288
     dtype: int64,
     modalidad_de_violencia_otras
     No    87434
     Si     2106
     dtype: int64]



En el caso de la descripción de las variables que califican las modalidades de violencia consultadas a la línea 144 podemos observar las siguientes conclusiones:
 - La modalidad con mayor recurrencia se encuentra en la categoria "otras" (2106) 
 - La modalidad con menor recurrencia se encuentra en la categoria "mediatica"  (53)

## Descripción vínculo con la persona agresora


```python
df['vinculo_con_la_persona_agresora'] = df['vinculo_con_la_persona_agresora'].replace('Superior jerárquico','Superior jerarquico')
desc_vinculo_con_la_persona_agresora  = df.groupby(df['vinculo_con_la_persona_agresora']).size()
desc_vinculo_con_la_persona_agresora 
```




    vinculo_con_la_persona_agresora
    Ex pareja              42247
    Madre o tutor            170
    Otro                    6804
    Otro familiar           3182
    Padre o tutor           1081
    Pareja                 32255
    Superior jerarquico      406
    dtype: int64



Según se observa, la categoría con mayor recurrencia es la que corresponde al vínculo "Ex Pareja", mientras que la categoría con menor recurrencia es la de "Madre o tutor"

## Descripción género de la persona agresora


```python
df['genero_de_la_persona_agresora'] = df['genero_de_la_persona_agresora'].replace('Varon Trans','Varon trans')
df['genero_de_la_persona_agresora'] = df['genero_de_la_persona_agresora'].replace('OTRO','Otro')
df['genero_de_la_persona_agresora'] = df['genero_de_la_persona_agresora'].replace('Transgénero','Transgenero')

desc_genero_de_la_persona_agresora  = df.groupby(df['genero_de_la_persona_agresora']).size()
desc_genero_de_la_persona_agresora
```




    genero_de_la_persona_agresora
    Mujer           1034
    Mujer Trans       10
    No Binarie         1
    Otro             223
    Queer              1
    Transgenero        9
    Travesti           2
    Varon          79026
    Varon trans       22
    dtype: int64



En relación a la variable género de la persona agresora se reconoce que la mayoría de los casos corresponden a las personas de género "Varón", mientras que los géneros menos frecuente son el "Queer" y "No binarie"


```python
df.to_csv('df_limpio.csv')
```
