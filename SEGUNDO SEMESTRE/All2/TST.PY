# Contenido para el archivo CSV (alternativo)
csv_content = """Tipo,Pregunta,Opciones,Respuesta
Verdadero/Falso,La aplicación más conocida de la psicología es su vertiente clínica, que tiene como meta ayudar a resolver problemas mentales y conductuales.,"Verdadero,Falso",Verdadero
Verdadero/Falso,La investigación psicológica se engloba en “el estudio del comportamiento y de los procesos mentales humanos.,"Verdadero,Falso",Verdadero
Verdadero/Falso,La carta se caracteriza porque su mensaje sea breve y preciso.,"Verdadero,Falso",Verdadero
Verdadero/Falso,El objetivo prioritario de una carta es enviar un comunicado.,"Verdadero,Falso",Verdadero
Selección Múltiple,Elementos que conforman la estructura de la carta.,"El encabezado,La fecha,El saludo,Conclusión,Desarrollo","El encabezado,La fecha,El saludo,Desarrollo"
Selección Múltiple,Primer paso para la elaboración de una guía práctica.,"Tema de guía,Metodología,Recursos Resultados",Tema de guía
Selección Múltiple,Estilos de puntuaciones.,"Estilo bloque extremo,Puntuación mixta o estándar,Estilo sencillo,Puntuación normal",Puntuación mixta o estándar
Completación,La comunicación escrita logra diferenciarse de la comunicación oral gracias a que no está sujeta al _______________ ni al _______________, esto quiere decir que esta comunicación que se establece entre un _______________ y un _______________.,,,tiempo;espacio;emisor;receptor
Completación,La persona que redacta un _______________ debe hacer uso _______________ del lenguaje mediante su _______________.,,,texto;adecuado;claridad
Completación,Cuando se prepara una carta, un _______________ adecuado que nos ayuda en gran parte en la elaboración de una no importando cuando sea _______________ o _______________.,,,lenguaje;formal;informal
"""

# Guardar el archivo CSV
csv_file_path = "/mnt/data/ExamView_Questions_Alt.csv"
with open(csv_file_path, "w") as csv_file:
    csv_file.write(csv_content)

# Contenido para el archivo de importación en texto plano
txt_import_content = """
Type: TF
Question: La aplicación más conocida de la psicología es su vertiente clínica, que tiene como meta ayudar a resolver problemas mentales y conductuales.
Answer: True

Type: TF
Question: La investigación psicológica se engloba en “el estudio del comportamiento y de los procesos mentales humanos.
Answer: True

Type: TF
Question: La carta se caracteriza porque su mensaje sea breve y preciso.
Answer: True

Type: TF
Question: El objetivo prioritario de una carta es enviar un comunicado.
Answer: True

Type: MC
Question: Elementos que conforman la estructura de la carta.
A) El encabezado
B) La fecha
C) El saludo
D) Conclusión
E) Desarrollo
Answer: ABCE

Type: MC
Question: Primer paso para la elaboración de una guía práctica.
A) Tema de guía
B) Metodología
C) Recursos Resultados
Answer: A

Type: MC
Question: Estilos de puntuaciones.
A) Estilo bloque extremo
B) Puntuación mixta o estándar
C) Estilo sencillo
D) Puntuación normal
Answer: B

Type: Completion
Question: La comunicación escrita logra diferenciarse de la comunicación oral gracias a que no está sujeta al _______________ ni al _______________, esto quiere decir que esta comunicación que se establece entre un _______________ y un _______________.
Answer: tiempo; espacio; emisor; receptor

Type: Completion
Question: La persona que redacta un _______________ debe hacer uso _______________ del lenguaje mediante su _______________.
Answer: texto; adecuado; claridad

Type: Completion
Question: Cuando se prepara una carta, un _______________ adecuado que nos ayuda en gran parte en la elaboración de una no importando cuando sea _______________ o _______________.
Answer: lenguaje; formal; informal
"""

# Guardar el archivo de importación
txt_file_path = "/mnt/data/ExamView_Questions_Import.txt"
with open(txt_file_path, "w") as txt_file:
    txt_file.write(txt_import_content)

csv_file_path, txt_file_path
