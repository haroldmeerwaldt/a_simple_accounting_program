@echo off
SETLOCAL ENABLEEXTENSIONS
SET me=%~n0
SET parent=%~dp0

set filename=%~n1

echo %me%: Converting %filename%.ui to %filename%.py


..\..\env\Scripts\python -m PyQt5.uic.pyuic -x %filename%.ui -o %filename%.py

echo %me%: Copying to ..\..\modules\GUI_layouts
copy %filename%.py ..\..\modules\GUI_layouts\%filename%.py

pause