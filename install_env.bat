@echo off
REM Definir la ruta del ejecutable de Python 32 bits
set PYTHON_PATH=C:/Users/Enrique.estebanez/AppData/Local/Programs/Python/Python313/python.exe

REM Crear entorno virtual con Python de 32 bits
"%PYTHON_PATH%" -m venv venv

REM Activar entorno virtual
call venv\Scripts\activate

REM Instalar dependencias desde el archivo requirements.txt
pip install -r requirements.txt

REM Desactivar entorno virtual
deactivate
