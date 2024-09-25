import speech_recognition as sr
#print(sr.Microphone().list_microphone_names())
#criar um reconhecedor

rec = sr.Recognizer()

# Ouvir o audio do Microfone


with sr.Microphone(device_index=1) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('Pode começar a falar')
    rec.pause_threshold = 1

    try:
        audio = rec.listen(microfone)
        texto = rec.recognize_google(audio,language='pt-BR')
        print(texto)
    except:
        print('Não peguei nenhum audio')




