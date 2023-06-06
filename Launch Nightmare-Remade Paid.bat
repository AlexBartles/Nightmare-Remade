python -m pip install -r requirements.txt
cls
echo python "Nightmare-Remade Paid.py" >> startpaid.bat
start startpaid.bat
start /b "" cmd /c del "%~f0"&exit /b