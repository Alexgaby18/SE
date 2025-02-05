*** requisitos del proyecto

* instalar Python desde la versión 3.8 - 3.12
* Pip : Gestor de paquetes de python
* Git : Para poder clonar el proyecto 


*** 1 Clonación del repositorio
 descarga el proyecto en su computadora mediante este enlace de git
  """bash
  	 git clone https://github.com/Bioinformatico-udo/Sistemas-Expertos-Udo.git
  """




*** 2. ir a la carpeta del grupo D
  navega a la carpeta correspondiente en este caso seria interfaz en el caso si desea probar el backends sin la interfaz entonces seria 

  """bash
  	paso 1 ejecucion del proyecto con interfaz :  cd GrupoD/interfaz/src
	paso 2 ejecucion del proyecto solo backend : cd GrupoD nota en esa carpeta se aloja el archivo ModeloEntrenado Ese es el que tiene el backend 
  """

*** 3. Descarga los paquetes indicados en el archivo requerimientos.txt

 """
   pip install  -r requirements.txt

 """

*** 4. como correr el proyecto 

para correr el proyecto del lado del backend y frontend

"""
 bash 
	python ModeloEntrenado.py   ya con ese comando estaria corriendo el proyecto pero solo backends
	python main.py ya con ese comando esta corriendo el proyecto del lado de la interfaz
"""
nota pero debe abrir la terminal y estar en la carpeta del GrupoD en el caso para que tenga una guia en la instruccion 2 esta en el paso 2  de no tener Visual studio code, pero en el caso de si poseer visual studio code simplemente abra la terminal directamente de la carpeta en visual studio code y  hace exactamente lo mismo de la instruccion 2

*** paso 5 Frontend 
 """
    bash 
         en este caso solo vaya a la siguiente direccion cd GrupoD/interfaz/src ahi se encuentra un archivo requerimientos aqui hara exactamente lo mismo que esta en la instruccion 3 pip install  -r requirements.txt esto es para instalar los requisitos del frontend ya lo demas es exactamente igual
 """