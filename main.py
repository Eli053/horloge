
import time
import time

import threading

class Horloge:
    def __init__(self):
        self.heure = 0
        self.minute = 0
        self.seconde = 0
        self.pause = False
        self.thread = threading.Thread(target=self.incrementer_temps)

    def incrementer_temps(self):
        while True:
            if not self.pause:
                self.seconde += 1
                if self.seconde == 60:
                    self.seconde = 0
                    self.minute += 1
                if self.minute == 60:
                    self.minute = 0
                    self.heure += 1
                if self.heure == 24:
                    self.heure = 0
            time.sleep(1)

    def demarrer(self):
        self.pause = False
        if not self.thread.is_alive():
            self.thread.start()

    def mettre_en_pause(self):
        self.pause = True

# Test de la classe Horloge
horloge = Horloge()
horloge.demarrer()
time.sleep(5)  # Attendre 5 secondes
horloge.mettre_en_pause()
print(horloge.heure, horloge.minute, horloge.seconde)  # Affiche 0 0 5

class Horloge:
    def __init__(self):
        self.heure_actuelle = (0, 0, 0)
        self.alarme = None

    def afficher_heure(self, heure):
        self.heure_actuelle = heure

    def regler_alarme(self, heure):
        self.alarme = heure

    def demarrer(self):
        while True:
            print(f"{self.heure_actuelle[0]:02}:{self.heure_actuelle[1]:02}:{self.heure_actuelle[2]:02}")
            if self.heure_actuelle == self.alarme:
                print("L'alarme sonne !")
            time.sleep(1)
            self.heure_actuelle = (self.heure_actuelle[0], self.heure_actuelle[1], (self.heure_actuelle[2] + 1) % 60)
            if self.heure_actuelle[2] == 0:
                self.heure_actuelle = (self.heure_actuelle[0], (self.heure_actuelle[1] + 1) % 60, self.heure_actuelle[2])
            if self.heure_actuelle[1] == 0 and self.heure_actuelle[2] == 0:
                self.heure_actuelle = ((self.heure_actuelle[0] + 1) % 24, self.heure_actuelle[1], self.heure_actuelle[2])
