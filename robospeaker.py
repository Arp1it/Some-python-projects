from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

if __name__ == "__main__":
    while True:
        print("Welcome to RoboSpeaker 1.1. Created by HARRY")
        x = input("Enter what you want me to pronounce: ")

        if x == "exit":
            speak("bye bye friend.")
            break

        command = f"{x}" 
        speak(command)