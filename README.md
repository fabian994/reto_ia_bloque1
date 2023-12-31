# reto_ia_bloque1
 
Libreta de Kaggle utilizada: https://www.kaggle.com/code/carolinaarratia/sales-reto

La evidencia relacionada a los **Datos** - sobre el manejo de datos que incluye limpieza y transformación de datos utilizando ETL - se encuentra en la carpeta "Documentos", en el documento LimpiezadelConjuntodeDatos.pdf -> https://github.com/fabian994/reto_ia_bloque1/blob/main/Documentos/LimpiezadelConjuntodeDatos.pdf

La evidencia relacionada al **Modelo Evaluación y refinamiento** se puede encontrar en la libreta de Kaggle o en el archivo sales-reto.ipynb, ambos contienen la misma información.

La evidencia de **Solución** - interfaz web - también se encuentra en este repositorio.

La evidencia de la competencia **SEG0403 Compromiso ético y ciudadano** se lee en la carpeta de "Documentos" en el archivo EvidenciaSEG0403.pdf -> [https://github.com/fabian994/reto_ia_bloque1/tree/main/Documentos](https://github.com/fabian994/reto_ia_bloque1/blob/main/Documentos/EvidenciaSEG0403.pdf)

Por último, la presentación usada se encuentra dentro de la carpeta de Docuementos con el título PresentacionRetoSales.pdf -> https://github.com/fabian994/reto_ia_bloque1/blob/main/Documentos/PresentacionRetoSales.pdf

**Integrantes:**

Carolina Arratia Camacho
a01367552

Frida Lizett Zavala Pérez
a01275226

Fabián González Vera
a01367585

Jazzareth Bernal Martínez
a01367882

Requisitos
-----
La interfaz requiere de los siguientes requisitos:
Python 3.11.4
Librerias:
- Django==4.2.5
- django-bootstrap-v5==1.0.11
- django-bootstrap-icons==0.8.3
- django-crispy-forms==2.0
- django-jquery==3.1.0
- crispy-bootstrap5==0.7
- scikit-learn==1.2.2
- scipy==1.11.1
- joblib==1.3.2
- patool==1.12
- pyunpack==0.3
- gdown==4.7.1

Para poder usar la interfaz de Django se requieren las siguientes acciones:
1. Mover el cursor de terminal a la carpeta *interfaz\IAB1_reto_int*.
2. Correr el comando `pip install -r r.txt`.

Correr el programa
---
Para correr el programa se deben de realizar las siguientes acciones:
1. Asegurarse que se tiene instaladas las versiones especificadas de la librerias requeridas.
2. Mover el cursor de la terminal a la carpeta donde se encuentra el archivo *downloadModel.py*.
3. Usar el comando `py downloadModel.py`
4. Mover el cursor de la terminal a la carpeta *interfaz\IAB1_reto_int*.
5. Usar el comando `py manage.py runserver`
