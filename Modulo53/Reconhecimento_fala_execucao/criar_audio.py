import speech_recognition as sr

rec = sr.Recognizer()

#Gravar o audio
with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('Pode Começar a falar')
    audio = rec.listen(microfone)

#Salvar o audio
with open('audio.wav', 'wb') as arquivo:
    arquivo.write(audio.get_wav_data())