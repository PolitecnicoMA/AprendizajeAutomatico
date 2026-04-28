## Origen de los datos Encuesta Nacional de Factores de Riesgo.
El set de datos es tomado de la base de datos del indec en el área de salud https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos-2. El dataset que se toma en cuenta es el del año 2018, la población encuestada y evaluada es mayor de 18 años de toda la región Argentina. 

##### Diccionario de datos
| Base usuario ENFR-2018	
    
Especificaciones	FORMATO Y CODIFICACIÓN: .txt UTF-8
    DELIMITADOR DE CAMPOS: | (pipe)
    DELIMITADOR DE TEXTO: " (comilla doble)
    DELIMITADOR DE DECIMALES: . (punto)
    
Diccionario de registros	
    
Variable	Codificación
Dominios de estimación geográfica e información muestral	
id	Identificacion única del caso
cod_provincia	Jurisdicción del país
    2 Ciudad de Buenos Aires
    6  Buenos Aires
    10 Catamarca
    14 Córdoba
    18 Corrientes
    22 Chaco
    26 Chubut
    30 Entre Ríos
    34 Formosa
    38 Jujuy
    42 La Pampa
    46 La Rioja
    50 Mendoza
    54 Misiones
    58 Neuquén
    62 Río Negro
    66 Salta
    70 San Juan
    74 San Luis
    78 Santa Cruz
    82 Santa Fe
    86 Santiago del Estero
    90 Tucumán
    94 Tierra del Fuego
region	Código de región INDEC
    1. Metropolitana
    2. Pampeana
    3. Noroeste
    4. Noreste
    5. Cuyo
    6. Patagónica
tamanio_aglomerado	Tamaño del aglomerado
    1. Más de 1.500.000 habitantes
    2. 500.001 a 1.500.000 habitantes
    3. 150.001 a 500.000 habitantes
    4. Menos de 150.000 habitantes
aglomerado	Aglomerado urbano de 500.000 y más habitantes
    1. Gran Buenos Aires
    2. Gran Córdoba
    3. Gran Rosario
    4. Gran Mendoza
    5. Tucumán - Tafí Viejo
    6. Gran La Plata
    7. Mar del Plata - Batán
    8. Gran Salta
    9. Resto de los aglomerados
localidades_150	Tamaño de localidad - 150.000 habitantes o más
    1. Localidad de 150.000 o más habitantes
    0. Localidad de menos de 150.000 habitantes
submuestra	Identificación de la submuestra de los pasos 2 y 3
    1. Submuestra
    0. Sin submuestra
BLOQUE HOGAR (BH)	
    
Características de la vivienda (CV)	
bhcv01	Tipo de vivienda
    1. Casa 
    2. Casilla
    3. Depertamento 
    4. Pieza de inquilinato 
    5. Pieza en hotel o pensión
    6. Local no construido para habitación+B33
    7. Otros
bhcv02	¿Cuántos ambientes/habitaciones tiene la vivienda en total? (Excluyendo baño, cocina, pasillos, lavadero, garage)
     (Cantidad en cifras) 
bhcv03	¿Cuál es el material predominante de los pisos?
    1. Cerámica, baldosa, mosaico, mármol, madera o alfombra
    2. Cemento o ladrillo fijo
    3. Tierra o ladrillo suelto
    4. Otros
bhcv04	"¿Cuál es el material predominante de la cubierta 
exterior del techo?"
    1. Cubierta asfáltica o membrana
    2. Baldosa o losa (sin cubierta)
    3. Pizarra o teja
    4. Chapa de metal (sin cubierta)
    5. Chapa de fibrocemento o plástico
    6. Chapa o cartón
    7. Caña, tabla o paja con barro, paja sola
    8. N/S Depto. en propiedad horizontal
    9. Otros
bhcv05	"En el techo, ¿tiene cielorraso/revestimiento 
interior?"
    1. Sí
    2. No
    9. Ns/Nc
bhcv06	¿Para cocinar, utiliza principalmente…
    1. ...gas de red?
    2. ...gas de tubo/garrafa?
    3. ...kerosene/leña/carbón?
    4. ...otro? 
bhcv07	¿Tiene agua…
    1. ...por cañería dentro de la vivienda?
    2. ...fuera de la vivienda pero dentro del terreno?
    3. ...fuera del terreno?
bhcv08	¿Obtiene el agua a través de…
    1 ...red pública (agua corriente)?
    2 ...perforación con bomba a motor?
    3 ...perforación con bomba manual?
    4 ...aljibe o pozo?
    5 Otras fuentes
bhcv09	¿Tiene baño/letrina?
    1. Sí
    2. No 
bhcv10	¿El baño tiene…
    1 ...inodoro con botón/mochila/cadena y arrastre de agua?
    2 ...inodoro sin botón/cadena y con arrastre de agua? (a balde)
    3 ...letrina? (sin arrastre de agua)
bhcv11	¿El desagüe del inodoro va...
    1 ...a red pública? (cloaca)
    2 ...a cámara séptica y pozo ciego?
    3 ...sólo a pozo ciego?
    4 ...a hoyo, excavación en tierra?
Características del hogar (HO)	
bhho01	El baño, ¿es de uso exclusivo de este hogar?
    1. Sí
    2. No 
bhho02	¿Cuántos ambientes/habitaciones tiene este hogar para su uso exclusivo? (Excluyendo baño, cocina, pasillos, lavadero, garage)
    (Cantidad en cifras)
bhho03	"De esos ¿cuántos usan habitualmente para 
dormir? "
    (Cantidad en cifras) 
cant_componentes	Cantidad de miembros del hogar
    (Cantidad en cifras)
miembros_18	"Cantidad de miembros del hogar de 18 años y
más"
    (Cantidad en cifras)
tipo_hogar	Tipo de hogar
    1 Hogar unipersonal
    2 Hogar multipersonal conyugal completo sin hijos ni otros miembros
    3 Hogar multipersonal conyugal completo sin hijos y con otros miembros
    4 Hogar multipersonal conyugal completo con hijos sin otros miembros
    5 Hogar multipersonal conyugal completo con hijos y con otros miembros
    6 Hogar multipersonal conyugal incompleto sin otros miembros
    7 Hogar multipersonal conyugal incompleto con otros miembros
    8 Hogar multipersonal no conyugal
Ingresos del hogar (IH)	
bhih01	Monto del ingreso total mensual del hogar en pesos
    Min 1
    Max 300000
bhih01_02	Sin ingresos / Ns/Nc 
    2. Sin ingresos
    99. Ns/Nc
rango_ingreso	Rango del ingreso total mensual del hogar en pesos
    0 Sin ingresos
    1 1 a 3.000
    2 3.001 a 5000 
    3 5.001 a 8.000
    4 8.001 a 12.000
    5 12.001 a 15.000
    6 15.001 a 18.000
    7 18.001 a 23.000
    8 23.001 a 27.000
    9 27.001 a 31.000
    10 31.001 a 35.00
    11 35.001 a 38.000
    12 38.001 a 41.000
    13 41.001 a 45.000
    14 45.001 a 49.000
    15 49.001 a 53.000
    16 53.001 a 60.000
    17 60.001 y más
     99 Ns/Nc
quintil_uc	Quintil de hogares según ingreso por unidad consumidora
    1. Quintil 1
    2. Quintil 2
    3. Quintil 3
    4. Quintil 4
    5. Quintil 5
imputado	Marca de imputación de la variable ingreso
    1. Imputado
    [Vacío] No imputado
bhih03	¿Percibió algún ingreso en dinero o en especie en los últimos 6 meses por Asignación Universal por Hijo, planes sociales u otras transferencias estatales?
    1. Sí
    2. No
    99. Ns/Nc
Características de la jefatura del hogar	
bhch03_j	Sexo del jefe/a de hogar
    1 Varón
    2 Mujer
bhch04_j	Edad del jefe/a de hogar en años cumplidos
    (Edad en años)
rango_edad_j	Rango de edad del jefe/a de hogar
    0. 0 a 17 años
    1 .18 a 24 años 
    2. 25 a 34 años
    3. 35 a 49 años
    4. 50 a 64 años
    5. 65 años y más
bhch05_j	Situación conyugal del jefe/a de hogar
    1 Unido/a
    2 Casado/a
    3 Separado/a
    4 Divorciado/a
    5 Viudo/a
    6 Soltero/a 
nivel_instruccion_j	Nivel de instrucción del jefe/a de hogar
    1 Sin instrucción
    2 Primario incompleto
    3 Primario completo
    4 Secundario incompleto
    5 Secundario completo
    6 Terciario o universitario incompleto
    7 Terciario o universitario completo y más
    8 Educación especial 
nivel_instruccion_agrupado_j	Nivel de instrucción agrupado del jefe/a de hogar
    1 Hasta primario incompleto
    2 Primario completo y secundario incompleto
    3 Secundario completo y más
    4 Educación especial
bhch10_01_j	¿Está asociado a…? Obra social (incluye PAMI)
     1 Sí
     2 No 
bhch10_02_j	¿Está asociado a…? Una prepaga a través de obra social
    1. Sí
    2. No
bhch10_03_j	¿Está asociado a…? Una prepaga por contratación voluntaria
    1. Sí
    2. No
bhch10_04_j	"¿Está asociado a…? Un servicio de emergencia
 médica"
    1 Sí
    2 No
bhch10_05_j	¿Está asociado a…? Un programa o plan estatal de salud
    1. Sí
    2. No
bhch10_06_j	¿Está asociado a…? No está asociado a nada
    1. Sí
    2. No
bhch10_99_j	¿Está asociado a…? Ns/Nc
     99 Ns/Nc
cobertura_salud_j	Cobertura de salud del jefe/a de hogar
    1 Con obra social o prepaga
    2 Sólo cobertura pública
Situación laboral del jefe/a de hogar (SL)	
bhsl01	La semana pasada, ¿trabajó por lo menos una hora, hizo alguna changa, fabricó algo para vender, ayudó a un familiar/amigo en su negocio?
    1. Sí
    2. No
bhsl02	¿La semana pasada…
    1 ...no deseaba/no quería/no podía trabajar?
    2 ...no tenía/no conseguía trabajo?
    3 ...no tuvo pedidos/clientes?
    4 ...tenía un trabajo/negocio al que no concurrió?
bhsl03	¿No concurrió por…
    1 ...vacaciones, licencia? (enfermedad, matrimonio, embarazo, etc.)
    2 ...huelga/conflicto laboral?
    3 ...suspensión con pago?
    4 ...suspensión sin pago?
    5 ...otras causas laborales y volverá a lo sumo en un mes?
    6 ...otras causas laborales y volverá en más de un mes?
bhsl04	En los últimos 30 días, ¿estuvo buscando trabajo de alguna manera, consultó amigos/parientes, puso carteles, hizo algo para ponerse por su cuenta?
    1. Sí
    2. No
bhsl05	Durante esos 30 días, ¿no buscó trabajo porque…
    1 ...está suspendido?
    2 ...ya tiene trabajo asegurado?
    3 ...se cansó de buscar trabajo?
    4 ...hay poco trabajo en esta época del año?
    5 ...por otras razones?
bhsl06	¿Cuántas horas semanales trabaja habitualmente en todos sus empleos/ocupaciones?
    1 Menos de 35 horas semanales
    2 Entre 35 y 45 horas semanales
    3 Más de 45 horas semanales
    99 Ns/Nc
condicion_actividad_j	Condición de actividad
    1. Ocupado
    2. Desocupado
    3. Inactivo 
Características del respondente del Bloque Individual	
bhch02	Relación de parentesco con el jefe/a de hogar
    1 Jefe de hogar
    2 Cónyuge/pareja
    3 Hijo/a hijastro/a
    4 Padre/madre
    5 Hermano/a
    6 Suegro/a
    7 Yerno
    8 Nieto
    9 Otro familiar
    10 Otro no familiar
bhch03	Sexo
    1. Varón
    2. Mujer
bhch04	Edad en años cumplidos
    Min 0
    Max 104
rango_edad	Rango de edad del seleccionado
    1. 18 a 24 años
    2. 25 a 34 años
    3. 35 a 49 años
    4. 50 a 64 años
    5. 65 años y más
bhch05	Situación conyugal
    1 Unido/a
    2 Casado/a
    3 Separado/a
    4 Divorciado/a
    5 Viudo/a
    6 Soltero/a
nivel_instruccion	Nivel de instrucción
    1. Sin instrucción
    2. Primario incompleto
    3. Primario completo
    4. Secundario incompleto
    5. Secundario completo
    6. Terciario/universitario incompleto
    7. Terciario/universitario completo
    8. Educación especial.
nivel_instruccion_agrupado	Nivel de instrucción agrupado
    1. Hasta primario incompleto (incluye educación especial)
    2. Hasta secundario incompleto
    3. Secundario completo y más
bhch10_01	¿Está asociado a... una obra social (incluye PAMI)?
    1. Sí
    2. No
bhch10_02	¿Está asociado a…? Una prepaga a través de obra social
    1.Sí
    2. No
bhch10_03	¿Está asociado a…? Una prepaga por contratación voluntaria?
    1. Sí
    2. No
bhch10_04	¿Está asociado a…? Un servicio de emergencia médica?
    1. Sí
    2. No
bhch10_05	¿Está asociado a…? Un programa o plan estatal de salud?
    1. Sí
    2. No
bhch10_06	No está asociado a nada
    1. Sí
    2. No
bhch10_99	Ns/Nc
    99. Ns/Nc
cobertura_salud	Cobertura de salud
    1 Con obra social, prepaga o servicio de emergencia médica
    2 Sólo cobertura pública
BLOQUE INDIVIDUAL (BI)	
    
Situación laboral (SL)	
bisl01	La semana pasada, ¿trabajó por lo menos una hora, hizo alguna changa, fabricó algo para vender, ayudó a un familiar/amigo en su negocio?
    1. Sí
    2. No
bisl02	¿La semana pasada…
    1 ...no deseaba/no quería/no podía trabajar?
    2 ...no tenía/no conseguía trabajo?
    3 ...no tuvo pedidos/clientes?
    4 ...tenía un trabajo/negocio al que no concurrió?
bisl03	¿No concurrió por…
    1 ...vacaciones, licencia? (enfermedad, matrimonio, embarazo, etc.)
    2 ...huelga/conflicto laboral?
    3 ...suspensión con pago?
    4 ...suspensión sin pago?
    5 ...otras causas laborales y volverá a lo sumo en un mes?
    6 ...otras causas laborales y volverá en más de un mes?
bisl04	En los últimos 30 días, ¿estuvo buscando trabajo de alguna manera, consultó amigos/parientes, puso carteles, hizo algo para ponerse por su cuenta?
    1. Sí
    2. No
bisl05	Durante esos 30 días, ¿no buscó trabajo porque…
    1 ...está suspendido?
    2 ...ya tiene trabajo asegurado?
    3 ...se cansó de buscar trabajo?
    4 ...hay poco trabajo en esta época del año?
    5 ...por otras razones?
bisl06	¿Cuántas horas semanales trabaja habitualmente en todos sus empleos/ocupaciones?
    1 Menos de 35 horas semanales
    2 Entre 35 y 45 horas semanales
    3 Más de 45 horas semanales
    99 Ns/Nc
condicion_actividad	Condición de actividad 
    1 Ocupado 
    2 Desocupado 
    3 Inactivo 
 Salud general (SG)	
bisg01	En general, ¿usted diría que su salud es…
    1 ...excelente?
    2 ...muy buena?
    3 ...buena?
    4 …regular?
    5 …mala?
bisg02	En relación a su movilidad, ¿en el día de hoy…
    1 …no tiene problemas para caminar?
    2 …tiene algunos problemas para caminar?
    3 …no puede caminar?
bisg03	En relación al cuidado personal, ¿en el día de hoy…
    1 …no tiene problemas para lavarse o vestirse solo?
    2 …tiene algunos problemas para lavarse o vestirse solo?
    3 …es incapaz de lavarse o vestirse solo?
bisg04	En relación a las actividades cotidianas, ¿en el día de hoy...
    1…no tiene problemas para realizar sus actividades cotidianas?
    2…tiene algunos problemas para realizar sus actividades cotidianas?
    3…es incapaz de realizar sus actividades cotidianas?
bisg05	En relación al dolor/malestar, ¿en el día de hoy…
    1 ...no tiene dolor ni malestar?
    2 …tiene un dolor o malestar moderado?
    3 …tiene mucho dolor o malestar?
bisg06	En relación a la ansiedad/depresión, ¿en el día de hoy…
    1 …no está ansioso ni deprimido?
    2 …está moderadamente ansioso o deprimido?
    3 ...está muy ansioso o deprimido?
Actividad física (AF)	
biaf01	Las actividades físicas intensas son aquellas que lo hacen respirar mucho más rápido y le exigen un mayor esfuerzo físico y aceleran el ritmo cardiaco. En la última semana, ¿cuántos días realizó actividades físicas intensas, durante al menos 10 minutos? (excluyendo caminata) [Días por semana]
    Min 0
    Max 7
biaf02_m	En los días de la semana en que usted realiza este tipo de actividades, ¿cuánto tiempo en total emplea en realizarlas?  [En minutos semanales]
    Min 0
    Max 4200
biaf02_99	Ns/Nc 
    99. Ns/Nc
biaf03	Las actividades físicas moderadas son aquellas que le implican una ligera aceleración del ritmo cardiaco y la respiración. En la última semana, cuántos días realizó actividades físicas moderadas, durante al menos 10 minutos? (puede incluir caminata rapida) [Días por semana]
    Min 0 
    Max 7
biaf04_m	En los días de la semana en que usted realiza este tipo de actividades, ¿cuánto tiempo en total emplea en realizarlas?  [En minutos semanales]
    Min 0
    Max 4260
biaf04_99	Ns/Nc 
    99. Ns/Nc
biaf05	En la última semana, ¿cuántos días caminó, durante al menos 10 minutos? [Días por semana]
    Min 0
    Max 7
biaf06_m	En los días de la semana en que usted realiza este tipo de actividad, ¿cuánto tiempo en total emplea en realizarla? [En minutos semanales]
    Min 0
    Max 5040
biaf06_99	Ns/Nc
    99. Ns/Nc
biaf07_m	Habitualmente, ¿cuánto tiempo por día pasa sentado, por ejemplo en su casa, en el trabajo, o en clase?  [En minutos diarios
    Min 0
    Max 1439
biaf07_99	Ns/Nc
    99. Ns/Nc
biaf08	¿Cuál es la razón principal por la que, en la última semana,  no practicó actividad física?
    1. Por falta de tiempo
    2. Por falta de dinero
    3. Por falta de instalaciones
    4. Por la distancia
    5. Por razones de salud
    6. Por falta de información
    7. Por falta de seguridad
    8. Porque no le interesa/no le gusta
    9. Por falta de voluntad
biaf09	¿Cuál es la razón principal por la que, en la última semana,  no realizó más actividad física?
    1. Hago la cantidad de actividad física que necesito/indicada
    2. Por falta de voluntad
    3. Por falta de dinero
    4. Por falta de instalaciones
    5. Por la distancia
    6. Por razones de salud
    7. Por falta de información
    8. Por falta de seguridad
    9. Porque no le interesa/no le gusta
biaf10_01	Las actividades físicas que realizó en la última semana, ¿fueron parte de su actividad doméstica?
    1. Sí
    2. No
biaf10_02	 ...parte de su actividad laboral?
    1. Sí
    2. No
biaf10_03	 ...para desplazarse/trasladarse?
    1. Sí
    2. No
biaf10_04	...para mejorar su condición física/hacer deporte?
    1. Sí
    2. No
nivel_actividad_fisica	Nivel de actividad física
    1. Alto
    2. Medio 
    3. Bajo
    99. Ns/Nc
barreras_actividad_fisica	Barreras a la realización de actividad física
    1. Falta de tiempo
    2. Falta de dinero
    3. Falta de instalaciones 
    4. Por la distancia
    5. Razones de salud
    6. Falta de información
    7. Falta de seguridad
    8. No le interesa/no le gusta
    9. Falta de voluntad
    10. Otro
    11. Hace la cantidad de actividad física que necesita/indicada
    12. Razones climáticas
    13. Por cuidado de personas
Tabaco (TA)	
bita01	¿Alguna vez fumó cigarrillos?
    1. Sí
    2. No
bita02	¿Qué edad tenía cuando fumó por primera vez? 
    Min 5
    Max 82
bita02_99	Ns/Nc
    99. Ns/Nc
bita03	En toda su vida ¿ha fumado por lo menos 100 cigarrillos?
    1. Sí
    2. No
    99. Ns/Nc
bita04	Actualmente ¿fuma usted cigarrillos…
    1 ...todos los días?
    2 ...algunos días?
    3 ...no fuma?
bita04_01	Actualmente, ¿fuma cigarrillo armado?
    1. Sí
    2. No
bita04_02	Actualmente, ¿fuma cigarrillo de paquete?
    1. Sí
    2. No
bita05	¿Qué marca de cigarrillos fuma habitualmente?
    1. Lucky Strike 
    2. Camel 
    3. Pall Mall 
    4. Marlboro 
    5. Philip Morris
    6. 43/70
    7. Baltimore
    8. Bashia
    9. Benson & Hedges 100s 
    10. Chesterfield 
    11. CJ 
    12. Dunhill fine cut master 
    13. Freeport box 
    14. Gavilán
    15. Gitanes blondes 
    16. Gudang Gararm
    17. Imparciales 100s
    18. Inter gold
    19. Jockey club
    20. John Player gold leaf 
    21. L&M 
    22. Melbourne
    23. Milenio
    24. Paladium
    25. Parisiennes 
    26. Parliament
    27. Particulares 
    28. Red Point 
    29. Rodeo
    30. Rothmans 
    31. V8
    32. Viceroy
    33. Virginia super Slims 100s box
    34. Winston
    35. Otro
bita06_a	¿Qué tipo de paquete compra  habitualmente?
    1. Box
    2. Común(blando)
    98. Fuma cigarrillos sueltos
    99. Ns/Nc
bita06_b	¿De qué cantidad? 
    Min 10
    Max 20
bita06_b_99	¿De qué cantidad? Ns/Nc
    99. Ns/Nc
bita06_c	¿De qué sabor? 
    1. Común (sin saborizar) 
    2. Mentolados
    3. Otro sabor
bita06_d	¿Con qué tipo de  cápsula?
    1. Cápsula simple
    2. Cápsula doble 
    99.Ns/Nc 
bita07	Pensando en la última vez que compró cigarrillos de esta marca y variedad para su propio consumo, ¿cuánto dinero pagó por esa compra?
    Min 20
    Max 100
bita07_99	 Ns/Nc 
    99. Ns/Nc
bita08	¿Intentó dejar de fumar en el último año?
    1. Sí
    2. No
    99. Ns/Nc
bita09_01	Actualmente, de los siguientes productos de tabaco que no son cigarrillos de paquete ni armados a mano, ¿usted consume… cigarros o habanos?
    1.Sí
    2. No
bita09_02	Actualmente, de los siguientes productos de tabaco que no son cigarrillos de paquete ni armados a mano, ¿usted consume… cigarritos?
    1. Sí
    2. No
bita09_03	Actualmente, de los siguientes productos de tabaco que no son cigarrillos de paquete ni armados a mano, ¿usted consume… pipa común?
    1. Sí
    2. No
bita09_04	Actualmente, de los siguientes productos de tabaco que no son cigarrillos de paquete ni armados a mano, ¿usted consume… pipa de agua?
    1. Sí
    2.No
bita09_05	Actualmente, de los siguientes productos de tabaco que no son cigarrillos de paquete ni armados a mano, ¿usted consume… tabaco para masticar?
    1.Sí
    2.No
bita09_06	Actualmente, de los siguientes productos de tabaco que no son cigarrillos de paquete ni armados a mano, ¿usted consume… cigarrillo electrónico?
    1.Sí
    2. No
bita10_01	Durante los últimos 30 días, ¿notó que alguien fumó en alguno de los  siguientes lugares cerrados… dentro de su casa?
    1.Sí
    2. No
    98. No estuvo
bita10_02	Durante los últimos 30 días, ¿notó que alguien fumó en alguno de los  siguientes lugares cerrados… dentro de su trabajo?
    1. Sí
    2. No
    98. No estuvo
bita10_03	Durante los últimos 30 días, ¿notó que alguien fumó en alguno de los  siguientes lugares cerrados… dentro de instituciones educativas?
    1. Sí
    2. No
    98. No estuvo
bita10_04	Durante los últimos 30 días, ¿notó que alguien fumó en alguno de los  siguientes lugares cerrados… dentro de bares/restaurantes?
    1.Sí
    2. No
    98. No estuvo
bita10_05	Durante los últimos 30 días, ¿notó que alguien fumó en alguno de los  siguientes lugares cerrados… dentro de hospitales/centros de salud?
    1. Sí
    2. No
    98. No estuvo
bita10_06	Durante los últimos 30 días, ¿notó que alguien fumó en alguno de los  siguientes lugares cerrados… dentro de otros lugares?
    1. Sí
    2. No
    98. No estuvo
bita11	En los últimos 30 días, ¿Vio alguna publicidad de cigarrillos en comercios donde se venden cigarrillos?
    1. Sí
    2. No
    98. No fue a comercios donde se venden cigarrillos
bita12	En los últimos 30 días ¿recibio por correo electrónico publicidad de cigarrillos o material de promoción de cigarrillos? 
    1. Sí
    2. No
bita13	En los últimos 30 días ¿se suscribio en alguna página web de una empresa que produce cigarrillos, una página web de una marca de cigarrillos o una página web que tuviera los logos de marcas de cigarrillos? 
    1. Sí
    2. No
bita14	En los últimos 30 días, ¿vio alguna frase o imagen sobre el riesgo de fumar impresa en paquetes de cigarrillos?
    1. Sí
    2. No
    98. No vio paquetes de cigarrillos
bita15	¿Las frases o imágenes que vienen en los paquetes de cigarrillos lo hicieron pensar en dejar de fumar?
    1. Sí
    2. No
    99. Ns/Nc
bita16	¿Está de acuerdo con el aumento del impuesto al tabaco?
    1. Sí
    2. No
    99. Ns/Nc
consumo_tabaco_100	Condición de fumador
    1. Fumador actual
    2. Ex fumador
    3. No fumador 
ta_paquete_y_armado	Prevalencia de consumo combinado de cigarrillos de paquete y armados
     1. Sí
     2. No
ta_dejar_fumar	Intentó dejar de fumar en el último año
     1. Sí
     2. No
    99. Ns/Nc
ta_otros_productos	Consumo de al menos un producto de tabaco que no sean cigarrilllos
     1. Sí
     2. No
hta_nofumadores	Exposición de no fumadores al humo de tabaco ajeno en lugares cerrados
    1. Sí
    2. No
ta_perc_publicidad	Vio alguna publicidad de cigarrillos en comercios donde venden cigarrillos
     1. Sí
     2. No
ta_percepcion_riesgo	Vio alguna frase o imagen sobre el riesgo de fumar impresa en paquetes de cigarrillos
     1. Sí
     2. No
imagenes_tabaco	Pensó en dejar de fumar por las frases o imágenes de los paquetes de cigarrillos en los últimos 30 días
    1. Sí
    2. No
Hipertensión (HA)	
biha01	¿Alguna vez le han tomado la presión arterial?
    1 Sí
    2 No
    99 Ns/Nc 
biha02	¿Cuándo fue la última vez que le tomaron la presión arterial?
    1 Menos de 1 año
    2 De 1 a 2 años
    3 Más de 2 años
    99 Ns/Nc
biha03	¿Cuántas veces un médico, un enfermero u otro profesional de la salud le dijo que tenía presión alta?
    1 Sólo 1 vez
    2 Más de 1 vez
    3 Ninguna
    99 Ns/Nc
biha04	¿En las últimas dos semanas, estuvo haciendo algún tratamiento (medicamentos, dieta, ejercicio) indicado por un profesional de la salud para controlar su presión arterial?
    1. Sí
    2. No
biha05_01	¿El tratamiento es... con dieta, ejercicios, reducción de peso?
    1. Sí
    2. No 
biha05_02	¿El tratamiento es... con medicamentos?
    1. Sí
    2. No
biha06	¿Y cuántas pastillas debe tomar por día para el control de su presión arterial? [Cantidad por día]
    Min 1
    Max 13
biha06_99	¿Y cuántas pastillas debe tomar por día para el control de su presión arterial? Ns/Nc 
    99. Ns/Nc
biha07	Muchas personas tiene dificultades para tomar diariamente su medicación. ¿Alguna vez se olvida de tomar la medicación para controlar su presión arterial?
    1. Sí
    2. No 
biha08	Por lo general, cuando usted se siente bien ¿deja de tomar la medicación para controlar su presión arterial?
    1. Sí
    2. No  
    99. Ns/Nc
biha09	Por lo general, cuando usted se siente mal ¿deja de tomar la medicación para controlar su presión arterial?
    1. Sí
    2. No
    99. Ns/Nc
biha10	Durante la última semana, ¿usted …
    1. ..tomó todas las pastillas indicadas para controlar su presión arterial?
    2. …no tomó algunas de las pastillas indicadas para controlar su presión arterial?
    3. …no tomó ninguna pastilla indicada para controlar su presión arterial?
biha11	¿Y cuántas pastillas para controlar su presión arterial no tomó? [Cantidad en la última semana]
    Min 1
    Min 24
biha11_99	¿Y cuántas pastillas para controlar su presión arterial no tomó? Ns/Nc 
    99. Ns/Nc
biha12	 Excluyendo tomarse la presión arterial ¿hay algún lugar al que usted vaya habitualmente para hacerse un control relacionado con la presión alta ?
    1. Sí
    2. No 
biha13	 Excluyendo tomarse la presión arterial ¿a qué lugar va habitualmente a hacerse un control relacionado con la presión alta que no sea sólo tomarse la presión? 
    1. Un consultorio individual
    2. Un consultorio médico dentro de una clínica o sanatorio privado
    3. Un consultorio en un hospital
    4. Un consultorio en un centro de salud comunitario, de barrio o centro vecinal
    5. Un servicio de guardia de un hospital o clinica
    6. Otro lugar 
biha14	Cuando usted va a ese lugar, ¿siempre lo atiende el mismo profesional de la salud?
    1. Sí
    2. No 
    99. Ns/Nc
biha15	¿El médico o profesional que lo atiende en ese lugar conoce su historia clínica?
    1. Sí
    2. No
    99. Ns/Nc
control_hipertension	Medición de la presión arterial por un profesional de la salud en los últimos 2 años por autorreporte
    1. Sí
    2. No
    99. Ns/Nc
prevalencia_hipertension	Prevalencia de presión arterial elevada por autorreporte 
    1. Sí
    2. No
    99. Ns/Nc
Peso corporal (PC)	
bipc01	En el último año ¿un médico, un enfermero u otro profesional de la salud le ha dicho que tiene que bajar de peso?
    1 Sí
    2 No
    99 Ns/Nc
bipc02	¿Está usted en estos momentos haciendo algo para bajar de peso? (dieta, ejercicios)
    1 Sí
    2 No
bipc03	¿En estos momentos está haciendo algo para mantener controlado su peso?
    1 Sí
    2 No
bipc04	¿Cuánto cree usted que está pesando? [Peso en kg. por autorreporte]
    Min 30
    Max 200
bipc04_99	¿Cuánto cree usted que está pesando? Ns/Nc
    99 Ns/Nc
bipc05	¿Cuánto mide? [Altura en cm. por autorreporte]
    Min 110
    Max 203
bipc05_99	¿Cuánto mide? Ns/Nc 
    99 Ns/Nc
imc	Indice de masa corporal por autorreporte
    Min 10.38
    Max 66.67
imc_categorias	Indice de masa corporal agrupado por autorreporte
    1. Bajo (<25)
    2. Medio (>=25 y <30)
    3. Alto (>=30)
    99. Ns/Nc
Alimentacion (AL)	
bial01	Habitualmente, ¿le agrega sal a las comidas durante la cocción?
    1. Sí
    2. No
    99. Ns/Nc
bial02	Habitualmente, ¿le agrega sal a los alimentos una vez que está cocidos o al sentarse a la mesa…
    1. ...siempre o casi siempre?
    2. ...raras veces?
    3…nunca?
bial03	En una semana típica, ¿cuántos días come usted frutas frescas, cocidas, en jugos o licuados naturales?
    Min 1
    Max 7
bial03_99	Ns/Nc 
    99. Ns/Nc
bial04	En una semana típica, ¿cuántas porciones de frutas come en uno de esos días? [Porciones por día]
    Min 0.5
    Max 17
bial04_99	Ns/Nc 
    99. Ns/Nc
bial05	En una semana típica, ¿cuántos días come usted verduras?
    Min 1
    Max 7 
bial05_99	Ns/Nc 
    99. Ns/Nc
bial06	¿Cuántas porciones de fruta come en uno de esos días? [Porciones por día]
    Min 
    Max 
bial06_99	Ns/Nc 
    99. Ns/Nc
bial07	¿Cuál es la razón principal por la que no consume más porciones de frutas y/o verduras? 
    1. Come la cantidad que considera adecuada
    2. Su compra y preparación requiere mucho tiempo
    3. Pocas opciones de/en lugares de compra (supermercado, verdulería, almacén, etc.)
    4. Pocas opciones de/en lugares para comer (restaurantes, bares, etc.)
    5. Son caras
    6. Falta de apoyo del entorno
    7. No le gustan
    8. Prefiere otro tipo de comidas
    9. Dificultad por los hábitos y exigencias de la vida cotidiana
    10. Falta de voluntad
    11. Otros (especificar)
bial08	Pensando en su alimentación o dieta habitual o de todos los días, ¿considera que es…
    1…muy saludable?
    2…bastante saludable?
    3…poco saludable?
    4…nada saludable?
    99. Ns/Nc 
bial09	¿Cuál es la razón principal por la que considera que su alimentación o dieta habitual es poco/nada saludable?
    1. Falta de tiempo para comprar y/o cocinar
    2. En su casa o trabajo no se come comida saludable
    3. Come muchos alimentos altos en azúcares, grasas, sal (por ejemplo comidas rápidas o alimentos procesados)
    4. Dificultad para conseguir alimentos saludables cerca de los lugares que frecuenta (hogar, trabajo, facultad, etc. )
    5. Pocas opciones de comida saludable en lugares donde come habitualmente (restaurantes, bares, etc. )
    6. Los precios de los alimentos saludables son muy altos
    7. Las comidas saludables no lo llenan o sacan el hambre
    8. No le gustan las comidas saludables
    9. No le interesa tener una alimentación saludable
    10. Otros
bial10	¿Está de acuerdo o no con el aumento del impuesto a las bebidas azucaradas?
    1. Sí
    2. No
    99. Ns/Nc
promedio_fv_diario	Promedio de consumo diario de frutas o verduras [Cantidad en porciones]
    Min 0.2
    Max 12
consumo_fv	Consumo de al menos cinco porciones diarias de frutas o verduras
    1. Sí
    2. No
    99. Ns/Nc
barreras_fyv	Barreras para el consumo de frutas y verduras
    1. Factores condicionantes individuales 
    2. Factores condicionantes del entorno 
    3. Factores económicos 
    4. Come la cantidad que considera adecuada
    5. Otros
tipo_dieta_razones	Razones por las que considera que su dieta no es saludable
    1. Hábitos alimentarios 
    2. Entorno 
    3. Precio y accesibilidad 
    4. Otros
Colesterol (CO)	
bico01	¿Alguna vez le han medido el colesterol?
    1. Sí
    2. No
    99. Ns/Nc
bico02	¿Cuándo fue la última vez que le midieron el colesterol?
    1 Menos de 1 año
    2 De 1 a 2 años
    3 Más de 2 años
    99 Ns/Nc
bico03	¿Alguna vez un médico, un enfermero u otro profesional de la salud le dijo que tenía el colesterol alto?
    1. Sí
    2. No
    99. Ns/Nc
bico04	¿En las últimas dos semanas estuvo haciendo algún tratamiento (medicamentos, dieta, ejercicio) indicado por un profesional de la salud para mantener controlado su colesterol?
    1 Sí
    2 No
bico05_01	¿Está haciendo algún tratamiento con dieta, ejercicios, reducción de peso?
    1 Sí
    2 No
bico05_02	¿Está haciendo algún tratamiento con medicamentos?  
    1 Sí
    2 No
control_colesterol	Medición de colesterol alguna vez por autorreporte en varones de 35 años y más y mujeres de 45 años y más 
    1. Sí
    2. No
    99. Ns/Nc
prevalencia_colesterol	Prevalencia de colesterol elevado por autorreporte
    1. Sí
    2. No
    99. Ns/Nc
Consumo de alcohol (CA)	
bica01	¿Ha consumido alguna bebida alcohólica, como por ejemplo vino, cerveza, whisky o parecidos (vodka, ron) alguna vez en la vida?
    1. Sí
    2. No
    99. Ns/Nc
bica02	¿Cuándo fue la última vez que tomó alguna de estas bebidas alcohólicas?
    1. Durante los últimos 30 días
    2. Hace más de un mes, hasta un año
    3. Hace más de un año
    99. Ns/Nc
bica03_01	¿Con qué frecuencia tomó alguna bebida alcohólica en los últimos 30 días? [Días por semana]
    Min 1
    Max 7
bica03_02	¿Con qué frecuencia tomó alguna bebida alcohólica en los últimos 30 días? [Días por mes]
    Min 0
    Max 30
bica03_99	 Ns/Nc 
    99. Ns/Nc
bica04_01_b	[Cantidad de tragos]
bica04_01_c	No toma
    98. No toma
bica04_02_b	[Cantidad de tragos]
bica04_02_c	No toma
    98.No toma
bica04_03_b	[Cantidad de tragos]
bica04_03_c	No toma
    98.No toma
bica04_04	Y ese mismo día, ¿toma otras bebidas alcohólicas?
    1. Sí
    2. No
bica05_01_b	[Cantidad de tragos]
bica05_01_c	No toma
    98. No toma
bica05_02_b	[Cantidad de tragos]
bica05_02_c	 No toma 
    98. No toma
bica05_03_b	[Cantidad de tragos]
bica05_03_c	No toma
    98. No toma
bica05_04	Y ese mismo día, ¿tomó otras bebidas alcohólicas?
    1. Sí
    2. No
bica06	En los últimos 30 días, ¿al menos una vez manejó un auto, moto o bicicleta luego de haber tomado alguna bebida con alcohol?
    1. Sí
    2. No
    98. No manejó en los últimos 30 días
bica07	¿Está de acuerdo con el aumento del impuesto a las bebidas con alcohol?
    1. Sí
    2. No
    99. Ns/Nc
consumo_regular_riesgo	Consumo regular de riesgo de alcohol
    1. Sí
    2. No
consumo_episodico_excesivo	Consumo episódico excesivo de alcohol
    1. Sí
    2. No
Diabetes (DI)	
bidi01	¿Alguna vez un médico, un enfermero u otro profesional de la salud le dijo que tenía diabetes o azúcar alta en la sangre?
    1. Sí
    2. No
    99. Ns/Nc
bidi02	¿Eso ocurrió cuando estaba embarazada?
    1. Sí
    2. No
    99. Ns/Nc
bidi03	¿En las últimas dos semanas, estuvo haciendo algún tratamiento (medicamentos, dieta, ejercicio) indicado por un profesional de la salud para mantener controlada su diabetes/azúcar en sangre?
    1. Sí
    2. No
bidi04_01	¿Usted está haciendo algún tratamiento… con insulina?
    1. Sí
    2. No
bidi04_02	¿Usted está haciendo algún tratamiento… con dieta,ejercicios, reducción de peso?
    1. Sí
    2. No
bidi04_03	¿Usted está haciendo algún tratamiento… con medicamentos?
    1. Sí
    2. No
bidi05	¿Es insulinodependiente?
    1. Sí
    2. No
bidi06_01	¿Ha habido al menos un diagnóstico de diabetes entre sus familiares cosanguíneos directos (padres, hijos, hermanos)?
    1. Sí
    2. No
    99. Ns/Nc
bidi06_02	¿Ha habido al menos un diagnostico de diabetes entre otros familiares cosanguíneos (abuelos, tíos, primos)?
    1. Sí
    2. No
    99. Ns/Nc
bidi07	¿Cuando fue la última vez que le midieron glucemia/azúcar en sangre?
    1. Menos de 1 año
    2. De 1 a 2 años
    3. Más de 2 años
    4. Nunca se la midió
    9. Ns/nc
bidi08	¿Excluyendo la medición de glucemia o azúcar en sangre, hay algún lugar al que usted vaya habitualmente para hacerse un control relacionado con la diabetes?
    1. Sí
    2. No
bidi09	Excluyendo la medición glucemia  y azúcar en sangre, ¿a qué lugar va habitualmente a hacerse esos controles?
    1. Un consultorio individual
    2. Un consultorio médico dentro de una clínica o sanatorio privado
    3. Un consultorio en un hospital
    4. Un consultorio en un centro de salud comunitario, de barrio o centro vecina
    5. Un servicio de guardia de un hospital o clinica
    6. Otro lugar 
bidi10	Cuando usted va a ese lugar, ¿siempre lo atiende el mismo profesional de la salud?
    1. Sí
    2. No
    99. Ns/Nc
bidi11	¿El médico o profesional que lo atiende en ese lugar conoce su historia clínica?
    1. Sí
    2. No
    99. Ns/Nc
bidi12	En los últimos 12 meses, ¿un profesional de la salud le examinó los pies para detectarle heridas o irritaciones?
    1. Sí
    2. No
    99. Ns/Nc
bidi13	En los últimos 12 meses, ¿le hicieron un examen de a vista en el que le dilataron las pupilas? (Este examen le habría ocasionado una sensibilidad temporal de luz brillante)
    1. Sí
    2. No
    99. Ns/Nc
bidi14	¿Ha tomado alguna vez un curso o una clase sobre cómo controlar usted mismo su diabetes?
    1. Sí
    2. No
    99. Ns/Nc
control_diabetes	Medición de la glucemia/azúcar en sangre alguna vez por autorreporte
    1. Sí
    2. No
    99. Ns/Nc
prevalencia_diabetes	Prevalencia de glucemia elevada/diabetes por autorreporte
    1. Sí
    2. No
    99. Ns/Nc
Lesiones (LE)	
bile01	Si maneja o viaja en bicicleta, ¿con qué frecuencia usa casco?
    1. Siempre
    2. A veces
    3. Nunca
    98. No viaja en bicicleta
bile02	Si maneja o viaja en moto, ¿con qué frecuencia usa casco?
    1. Siempre
    2. A veces
    3. Nunca
    98. No viaja en moto
bile03	Si maneja o viaja en auto, ¿con qué frecuencia usa cinturón de seguridad?
    1. Siempre
    2. A veces
    3. Nunca
    98. No viaja en auto
Prácticas preventivas (PP)	
bipp01	¿Alguna vez se hizo una mamografía? (Una mamografía es una radiografía de cada mama)
    1. Sí
    2. No
    99. Ns/Nc
bipp02	¿Cuándo fue la última vez que se hizo una mamografía?
    1 Menos de 1 año
    2 De 1 a 2 años
    3 Más de 2 a 3 años
    4 Más de 3 años
    99 Ns/Nc
bipp03	¿Alguna vez se hizo un Papanicolaou? (Un Papanicolaou es un examen para detectar problemas en el cuello del útero)
    1. Sí
    2. No
    99. Ns/Nc
bipp04	¿Cuándo fue la última vez que se hizo un Papanicolaou?
    1 Menos de 1 año
    2 De 1 a 2 años
    3 Más de 2 a 3 años
    4 Más de 3 años
    99 Ns/Nc
control_mamografia	Realización de mamografía en los últimos 2 años
    1. Sí
    2. No
control_pap	Realización de Papanicolaou en los últimos 2 años
    1. Sí
    2. No
Prevención de cáncer colorrectal (CC)   	
bicc01_01	¿Alguna vez te ha hecho algún estudio para detectar pólipos o cáncer de colon, tal como prueba de sangre oculta en materia fecal?
    1   Sí
    2   No
    99  Ns/Nc
bicc01_02	¿Alguna vez se ha hecho algún estudio para detectar pólipos o cáncer de colon, tal como colonoscopía?
    1   Sí
    2   No
    99  Ns/Nc
bicc01_03	¿Alguna vez e ha hecho algún estudio para detectar pólipos o cáncer de colon, tal como radiografía de colon por enema? 
    1. Sí
    2. No
    99. Ns/Nc
bicc02	¿Cuál fue el último estudio que se realizó?
    1 Prueba de sangre oculta en materia fecal
    2 Colonoscopía
    3 Radiografía de colon por enema
bicc03	¿Hace cuánto se lo realizó?
    1 En el último año
    2 Más de 1 año hasta 2 años
    3 Más de 2 años  hasta 4 años
    4 Más de 4 años hasta 5 años 
    5 Más de  5 años hasta 10 años
    6 Más de 10 años
    99 Ns/Nc
control_colon	Realización de algún estudio de rastreo de cáncer de colon alguna vez (población de 50 años y más)
    1. Sí
    2. No
    99. Ns/Nc
Mediciones antropométricas (MA)	
bima01	Respuesta válida al Paso 2
    1. Sí
    2. No
bima02	Esta mañana, ¿ha tomado café, café con leche, té, mate u otras bebidas que puedan contener cafeína?
    1. Sí
    2. No
bima03	¿El encuestado consintió medirse la presión?
    1. Sí
    2. No
bima04_01_a	Primera medición/sistólica
    [Medición en mm/Hg]
bima04_01_b	Primera medición/diastólica
    [Medición en mm/Hg]
bima04_02_a	Segunda medición/sistólica
    [Medición en mm/Hg]
bima04_02_b	Segunda medición/ diastólica
    [Medición en mm/Hg]
bima04_03_a	Tercera medición/sistólica
    [Medición en mm/Hg]
bima04_03_b	Tercera medición/diastólica
    [Medición en mm/Hg]
promedio_sistolica	Promedio de las dos últimas mediciones de tensión sistólica
    [Promedio de la medición en mm/Hg]
promedio_diastolica	Promedio de las dos últimas mediciones de tensión diastólica
    [Promedio de la medición en mm/Hg]
ta_elevada	Presión arterial elevada según mediciones físicas
    1. Elevada (promedio_sistólica>=140 y promedio_diastólica>=90)
    2. No elevada (promedio_sistolica < 140 y promedio_diastolica < 90)
prevalencia_hipertension_combinada	Prevalencia de presión arterial elevada por autorreporte y/o medición física
    1. Elevado 
    2. No elevado 
bima06	¿El encuestado consintió medirse la altura?
    1. Sí
    2. No
bima07	Medición de la altura en centímetros
    [Altura en cm. según mediciones antropométricas]
bima09	¿El encuestado consintió pesarse?
    1. Sí
    2. No
bima10	Medición del peso en kilogramos
    [Peso en kg. por mediciones antropométricas]
imc_bima	Índice de masa corporal según mediciones antropométricas
    Min 14.15
    Max 86.57
imc_categorias_bima	IMC agrupado según mediciones antropométricas
    1. Bajo (<25)
    2. Medio( >=25 y <30)
    3. Alto ( >=30)
    99. Ns/Nc
bima12	¿El encuestado consintió medirse el perímetro de la cintura?
    1. Sí
    2. No
bima13	Perímetro de cintura en centímetros
    [Perímetro de cintura en cm. según mediciones antropométricas]
bima14	Medición realizada
    1 Directamente sobre la piel
    2 Con ropa fina
Mediciones bioquímicas (MQ)	
bimq01	Respuesta válida al Paso 3
    1. Sí
    2. No
bimq05	Registre los valores de glucosa que le informe el personal de Salud [Medición en mg/dl]
    Min 20
    Max 382
bimq05_01	Valor no registrado por el dispositivo
    98. Valor no registrado por el dispositivo
glucemia_elevada	Glucemia elevada en mediciones bioquímicas
    1. Elevada (>=110)
    2. No elevada(<110)
prevalencia_glucemia_elevada_combinada	Prevalencia de glucemia por autorreporte o medición bioquímica
    1. Elevada 
    2. No elevada 
findrisc	Riesgo de desarrollar diabetes mellitus en los próximos 10 años según puntaje FINDRISC
    1. Muy bajo riesgo
    2. Bajo riesgo
    3. Riesgo moderado
    4. Alto riesgo 
    5. Muy alto riesgo
bimq06	Registre los valores de colesterol que le informe el personal de Salud [Medición en mg/dl]
    Min 150
    Max 300
bimq06_01	Valor no registrado por el dispositivo
    98. Valor no registrado por el dispositivo
colesterol_elevado	Colesterol elevado en mediciones bioquímicas
    1. Elevado (>= 200)
    2. No elevado (< 200)
prevalencia_colesterol_combinada	Prevalencia de colesterol por autorreporte o medición bioquímica
    1. Elevada 
    2. No elevada 
Factores de expansión	
wf1p	Factor de expansión Paso 1
wf2p	Factor de expansión Paso 2
wf3p	Factor de expansión Paso 3


