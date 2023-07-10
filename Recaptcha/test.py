from pydub import AudioSegment

audio = 'C:\\Users\\andre\\Desktop\\Recaptcha\\mp3\\76cba05a7298478d98a7bc39e464ebea_tmp.mp3'

AudioSegment.from_mp3(audio).export('./wav/teste.wav', format='wav')