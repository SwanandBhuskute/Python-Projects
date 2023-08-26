import pyttsx3

if __name__ == "__main__":
    print("Welcome to Text-to-Speech by Swanand!")
    eng = pyttsx3.init()

    while True:
        text = input("Enter what you want to say: ")

        if text.lower() == "q":
            eng.say("goodbye")
            eng.runAndWait()
            break
        eng.say(text)
        eng.runAndWait()
