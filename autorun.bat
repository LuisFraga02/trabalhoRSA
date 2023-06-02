@echo off
cls
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo +                                                              +
echo +              exemplo de funcionamento do RSA                 +
echo +                                                              +
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo.
timeout /t 3 >nul
echo criando chaves...
python 1_criar_chaves.py
rem n precisa de timeout pq o python ja demora um pouco pra criar as chaves
echo.
echo gerando assinaturas...
python 4_gerar_assinatura.py
timeout /t 3 >nul
echo.
echo mensagem para ser encriptada esta em in/mensagem.txt...
python 2_encriptar_mensagem.py
timeout /t 3 >nul
echo.
echo decriptando mensagem...
python 3_decriptar_mensagem.py
timeout /t 3 >nul
echo.
echo mensagem decriptada esta em out/mensagem_decriptada.txt