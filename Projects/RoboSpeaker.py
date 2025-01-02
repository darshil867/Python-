import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker Created by Darshil Jayani")

    while True:
        x = input("Enter what you want to speak: ")

        if x.lower() == "q":
            os.system('PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'See you soon\')"')
            break

        command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)
