import speech_recognition as sr

rec = sr.Recognizer()


with sr.AudioFile('audio.wav') as arquivo:
    audio = rec.record(arquivo)

    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)