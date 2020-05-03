import pyttsx3

friend = pyttsx3.init()
userInput = input('Write Something:- ')
friend.say(userInput)
friend.runAndWait()