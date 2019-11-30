import speech_recognition as sr
r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)

print("Audio type: ")
print(type(audio))

result = r.recognize_google(audio)
#result = r.recognize_bing(audio)

print (result)
