@echo off
cls
del /q /f out
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo +                                                              +
echo +        todos os arquivos da pasta /out foram deletados       +
echo +                                                              +
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
timeout /t 3 >nul
echo pasta out precisa existir para que o script funcione depois > out/out.txt