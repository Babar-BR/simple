import pyttsx3

engine = pyttsx3.init()
print("this is modified file")
text = input("Enter text: ")
print(text)          # shows output
engine.say(text)     # speaks output
engine.runAndWait()