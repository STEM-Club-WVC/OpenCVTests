import speech_recognition as sr
names = sr.Microphone.list_microphone_names()
print("mic names: ")
print(names)
