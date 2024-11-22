@echo off
REM Activar entorno virtual
call venv\Scripts\activate

REM Ejecutar la aplicación Flask
python dist\app.exe

REM Desactivar entorno virtual
deactivate