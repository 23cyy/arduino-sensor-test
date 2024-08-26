import serial
import time

# Créez une instance de liaison série
ser = serial.Serial('COM5', 9600)  # Remplacez 'COMx' par le port série approprié

# Attendez quelques secondes pour que la liaison série soit prête
time.sleep(2)

# Fonction pour lire la température
def read_temperature():
    ser.write(b'T')  # Envoyer le caractère 'T' pour demander la température
    temperature = ser.readline().decode().strip()  # Lire la réponse et la décoder
    return temperature

# Fonction principale
if __name__ == "__main__":
    try:
        while True:
            temperature = read_temperature()
            print("Temperature =", temperature)
            time.sleep(1)  # Attendre 1 seconde
    except KeyboardInterrupt:
        print("Arrêt du programme.")
    finally:
        ser.close()  # Fermer la liaison série en cas d'arrêt du programme
