import os
import tempfile
import time
import uuid
import speech_recognition as sr
from pydub import AudioSegment
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from random import random

valAleatorio = random() + 0.1
print(valAleatorio)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--incognito")
options.add_argument('user-agent: Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/37.0.2049.0 Safari/537.36')


driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=20)

driver.get('https://www63.bb.com.br/portalbb/djo/id/comprovante/consultaDepositoJudicial,802,4647,4650,0,1,1.bbx')

time.sleep(1)
recaptcha = driver.find_element('xpath', "/html/body/div[1]/div/div/div/div/form/div[3]/div/div/div/div/iframe").click()

iframeRecaptcha = driver.find_element('xpath', "//iframe[starts-with(@name, 'c-') and starts-with(@src, 'https://www.google.com/recaptcha')]")

driver.switch_to.frame(iframeRecaptcha)
time.sleep(5 * valAleatorio)

btnAudio = driver.find_element('xpath', '//*[@id="recaptcha-audio-button"]').click()

time.sleep(6 * valAleatorio)
downloadAudio = driver.find_element('class name', 'rc-audiochallenge-tdownload-link').get_attribute('href')
print(downloadAudio)

# tmp_dir = tempfile.gettempdir()

id_ = uuid.uuid4().hex

mp3_file, wav_file = os.path.join('./mp3', f'{id_}_tmp.mp3'), os.path.join('./wav', f'{id_}_tmp.wav')

tmp_files = {mp3_file, wav_file}
print(mp3_file, wav_file)

with open(mp3_file, 'wb') as f:
    audio_download = requests.get(url=downloadAudio, allow_redirects=True)

    f.write(audio_download.content)

    f.close()

AudioSegment.from_mp3(mp3_file).export(wav_file, format='wav')
time.sleep(8 * valAleatorio)
r = sr.Recognizer()

with sr.AudioFile(wav_file) as source:
    audio = r.record(source)

try:
    texto = r.recognize_google(audio, language="en-US")
    print(texto)
except sr.UnknownValueError:
    print("Não foi possível reconhecer o áudio")
except sr.RequestError as e:
    print("Erro na solicitação ao serviço de reconhecimento de fala: {0}".format(e))


audioResposta = driver.find_element('id', 'audio-response').send_keys(texto)

driver.find_element('id', 'recaptcha-verify-button').click()

time.sleep(10 * valAleatorio)

driver.quit()




