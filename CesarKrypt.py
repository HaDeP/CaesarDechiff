import os
import random

encodings = ['utf32', 'utf8', 'ascii', 'latin1', 'latin2', 'latin3', 'windows-1250', 'windows-1252']
program_action = ''

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Funktion zum einlesen/ zur Eingabe des Textes
# Abhängig davon, ob der Text ent- oder verschlüsselt werden soll, bestehen verschiedene Auswahlmöglichkeiten
# Desweiteren wird die Sprach-Codierung des Textes berücksichtigt
def text_eingeben():
    global program_action
    input_correct = False
    valid_filename = False

    # (Verschlüsselten) Text einlesen
    while not input_correct:
        refChar = input("How do you want to enter the text (Default = deposited standard text)\n\n"
                        "I.    1 = from file\n"
                        "II.   2 = manuelle Eingabe\n\n"
                        "Your choice: ")
        # print("\n**********************************************************************************************\n")
        if refChar == '1':  # Eingabe via Datei
            while not valid_filename:
                clear()
                input('Please copy the file containing the text to the program directory')
                filename = input("Insert filename ('' = Default): ")
                print('\n')
                if filename == '':
                    filename = 'kryptoText.txt'
                if not os.path.isfile(filename):
                    input("A file with the name {} does not exist in the program directory!\n".format(filename))
                else:
                    valid_filename = True

            clear()
            for e in encodings:
                try:
                    inputFile = open(filename, "r", encoding=e)
                    inputFile.readlines()
                    inputFile.seek(0)
                    print('Trying to open file {} with encoding: {}'.format(filename, encodings[0]))
                except FileNotFoundError:
                    print("A file with the name {} does not exist in the program directory!\n".format(filename))
                    input("Continuing using default file.")
                    filename = '1kryptoText.txt'
                except UnicodeDecodeError:
                    if not FileNotFoundError:
                        print('Got unicode error with %s , trying different encoding' % e)
                else:
                    clear()
                    input('Opening the file with encoding:  %s \n' % e)
                    text = inputFile.read()
                    inputFile.close()
                    clear()
                    return text

            input("There was an error the programmer didn't think about.\n"
                  "Aborting program!")
            break
        elif refChar == '2':  # Eingabe manuell
            clear()
            manText = input("Please enter the text:\n\n")
            clear()
            return manText
        elif refChar == '':  # Default Text
            clear()
            if program_action == "decrypt":
                returnText = "Y|rz-v}z-q|y|-v-nzr9-p|{rr-nqv}pv{t-ryv9-rq-qvnz-{|{z-rvz|q" \
                             "-rz}|-v{vq{--yno|r-r-q|y|r-znt{n-nyv~nz-rn9-rq-qvnz-|y}n;"
            else:
                returnText = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor " \
                             "invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua."
            return returnText
        else:
            clear()
            input("Your input is invalid!\nPlease try again.\n\n")
            clear()

# Funktion zur Verschlüsselung eines im Caesar-Verfahren verschlüsseltem Text (übergabe als Parameter)
# Jedes Zeichen wird in den korrespondierenden Zahlencode transferiert, der Schlüssel als Zufallszahl generiert,
# zu dem vorher erstellten Zeichencode addiert und anschliessend wieder in das der neuen Zahl entsprechende Zeichen
# umgewandelt. Der verschlüsselte Text wird als Rückgabewert der Funktion übergeben und in einer Datei gespeichert
def enCrypt(clearText):
    charList = []
    shift = random.randint(1, 20)
    for item in clearText:
        charList.append(chr(ord(item)+shift))
    cryptoText = ''.join(charList)
    filename = 'krypt.txt'
    outputFile = open(filename, "w", encoding="utf8")
    outputFile.write(cryptoText)
    outputFile.close()
    return cryptoText


# Funktion zur Entschlüsselung eines im Caesar-Verfahren verschlüsseltem Text (übergabe als Parameter)
# Jedes Zeichen wird in den korrespondierenden Zahlencode transferiert, der Schlüssel
# von dieser Zahl subtrahiert und anschliessend wieder in das der neuen Zahl entsprechende Zeichen umgewandelt
# Der entschlüsselte Text wird als Rückgabewert der Funktion übergeben
def deCrypt(cryptoText):
    input_correct = False
    charList = []
    decryptText = ''

    # Text aufbereiten
    try:
        for item in cryptoText:
            countChar = cryptoText.count(item)
            charList.append([countChar, item])
    except TypeError:
        input()

    # Referenzzeichen festlegen & Verschiebung (Verschlüsselungsschlüssel) ermitteln
    while not input_correct:
        input_correct = True
        refChar = input("Which character should be used as reference? (Default = ' ')\n\n"
                        "I.     1 = ' '\n"
                        "II.    2 = 'e'\n"
                        "III.   3 = 'i'\n"
                        "IV.    4 = 'n'\n\n"
                        "Your choice: ")
        clear()
        if refChar == '1':
            shift = ord(max(charList)[1]) - ord(' ')
        elif refChar == '2':
            shift = ord(max(charList)[1]) - ord('e')
        elif refChar == '3':
            shift = ord(max(charList)[1]) - ord('i')
        elif refChar == '4':
            shift = ord(max(charList)[1]) - ord('n')
        elif refChar == '':
            shift = ord(max(charList)[1]) - ord(' ')
        else:
            clear()
            input("Your input is invalid!\nPlease try again.\n\n")
            clear()
            input_correct = False

    # Entschlüsselen des Textes
    try:
        for item in cryptoText:
            decChar = ord(item) - shift
            decryptText += chr(decChar)
            # print(chr(decChar), end='')
    except ValueError:
        decryptText += item

    return decryptText

# "Hauptprogramm" als Konsolenprogramm in einer Schleife
def main():
    global program_action
    program_end = False

    while not program_end:
        clear()
        choice = input("Do you want to en- or decrypt a text?\n\n"
                       "1 = encrypt\n"
                       "2 = decrypt\n"
                       "0 = exit program\n\n"
                       "Your choice: ")
        if choice == "1":
            clear()
            program_action = "encrypt"
            enCrypt(text_eingeben())
        elif choice == "2":
            clear()
            program_action = "decrypt"
            print(deCrypt(text_eingeben()))
            input()
        elif choice == "0":
            break
# Start des Programms
main()