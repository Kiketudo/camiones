[Setup]
AppName=MiAplicacionFlask
AppVersion=1.0
DefaultDirName={pf}\MiAplicacionFlask
OutputDir=.
OutputBaseFilename=MiAplicacionFlask_Installer
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=yes

[Files]
; Incluir todos los archivos necesarios para la aplicación
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "start_app.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "install_env.bat"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MiAplicacionFlask"; Filename: "{app}\start_app.bat"

[Run]
; Ejecutar el script que crea el entorno virtual e instala las dependencias
Filename: "{app}\install_env.bat"; Description: "Instalando entorno virtual y dependencias"; Flags: runhidden waituntilterminated
Filename: "{app}\start_app.bat"; Description: "Ejecutar MiAplicacionFlask"; Flags: nowait postinstall skipifsilent
