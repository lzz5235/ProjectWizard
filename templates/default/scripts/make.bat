call clean.bat
cd scripts
call VS02008-vsvars32.bat
cd ..
"%QTDIR%\bin\qmake" -o MakeFile {{ config.project_name }}.pro
nmake debug
nmake release
