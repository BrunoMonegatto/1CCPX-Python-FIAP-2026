# Importa a biblioteca winsound
# Essa biblioteca já vem no Windows e serve para tocar sons
import winsound

# Toca o arquivo de áudio
# 'musica.wav' é o nome do arquivo que está na mesma pasta do código
# winsound.SND_FILENAME indica que estamos passando o nome de um arquivo
winsound.PlaySound('kaazoom-chrome-pulse-30-sec-edit-cinematic-hybrid-electronic-music-514117.wav', winsound.SND_FILENAME)