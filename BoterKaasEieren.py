import os 

class bord:
    def __init__(self): 
        self.__veld_status = {"1":"", "2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":""}
        self.teken()

    def herstel(self): 
        self.__init__()

    def teken(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
        print(" " + self.__veld_status["1"] + " | " + self.__veld_status["2"] + " | " + self.__veld_status["3"])
        print("--------")
        print(" " + self.__veld_status["4"] + " | " + self.__veld_status["5"] + " | " + self.__veld_status["6"])
        print("--------")
        print(" " + self.__veld_status["7"] + " | " + self.__veld_status["8"] + " | " + self.__veld_status["9"])

    def zet_veld(self, veld: int, speler_symbool: str):
        if (self.__veld_status[veld]== ""):
            self.__veld_status[veld] = speler_symbool
            self.teken()
            return True
        else: 
            return False
    
    def __is_er_een_winnaar(self): 
        # Controleer of er drie op een rij zitten in een regel
        if (self.__veld_status["1"] == self.__veld_status["2"] == self.__veld_status["3"] != ""):
            return True
        if (self.__veld_status["4"] == self.__veld_status["5"] == self.__veld_status["6"] != ""):
            return True
        elif (self.__veld_status["7"] == self.__veld_status["8"] == self.__veld_status["9"] != ""):
            return True
        # Controleer of er drie op een rij zitten in een kolom
        if (self.__veld_status["1"] == self.__veld_status["4"] == self.__veld_status["7"] != ""):
            return True
        if (self.__veld_status["2"] == self.__veld_status["5"] == self.__veld_status["8"] != ""):
            return True
        elif (self.__veld_status["3"] == self.__veld_status["6"] == self.__veld_status["9"] != ""):
            return True
        # Controleer of er drie op een rij zitten in een diagonaal
        elif (self.__veld_status["1"] == self.__veld_status["5"] == self.__veld_status["9"] != ""):
            return True
        elif (self.__veld_status["3"] == self.__veld_status["5"] == self.__veld_status["7"] != ""):
            return True   
        else: 
            return False    

    def __is_gelijkspel(self):
        if not("" in self.__veld_status):
            return True
        else: 
            return False

    def zet_mogelijk(self):
        if (self.__is_er_een_winnaar()):
            return False, "winnaar"
        elif (self.__is_gelijkspel()):
            return False, "gelijkspel"
        return True, ""


class speler: 
    def __init__(self, symbool): 
        self.__symbool = symbool

    def __valideer_input(self, veld):
        try: 
            veld = int(veld)
            if(veld >= 1) or (veld <=9): 
                return True
        except:
            return False 

    def geef_symbool(self):
        return self.__symbool

    def doe_zet(self, bord: bord): 
        valide_zet = False
        while not(valide_zet): 
            veld = input("Welk veld wil je spelen speler {} (1-9)? >> ".format(self.__symbool))
            if (self.__valideer_input(veld)): 
                if (bord.zet_veld(veld, self.__symbool)):
                    valide_zet = True
                else: #er is een veld gekozen die al gekozen is
                    print("Het gekozen veld -" + veld + "- is al bezet.") 
            else: #Er is geen getal ingevoerd
                print("Geen geldige waarden ingevuld: Je kunt kiezen uit een getal van 1 tot 9.")

class spel: 
    def __init__(self): 
        os.system('cls' if os.name == 'nt' else 'clear')
        self.__speler1 = speler(input("Met welk symbool speelt speler 1? >> "))
        self.__speler2 = speler(input("Met welk symbool speelt speler 2? >> "))
        self.__bord = bord()
    
    def start(self):
        doorspelen = True
        while doorspelen:
            zet_mogelijk = True
            while zet_mogelijk:
                self.__speler1.doe_zet(self.__bord)
                zet_mogelijk, status = self.__bord.zet_mogelijk()
                if zet_mogelijk: 
                    self.__speler2.doe_zet(self.__bord)
                    zet_mogelijk, status = self.__bord.zet_mogelijk()
            if (status == "winnaar"): 
                print("Speler {} is de winnaar!!".format(self.__speler1.geef_symbool()))
            elif (status == "gelijkspel"):
                print("Het is een gelijkspel!")
            antwoord = input("Nog een potje? (J/N) >> ")
            if (antwoord.upper() == "J"): 
                self.__bord.herstel()
            else:
                doorspelen = False

    def start2(self):
        #blijf het spel spelen tot dat gebruiker niet meer verder wil. 
        doorspelen = True 
        while doorspelen: 
            #maak een lijst waarin speler 1 en 2 10 keer voorkomen. (maximaal aantal)
            spelerslijst = [self.__speler1, self.__speler2] * 5 
            for speler in spelerslijst: 
                speler.doe_zet(self.__bord)
                zet_mogelijk, status = self.__bord.zet_mogelijk()
                if zet_mogelijk == False :
                    if (status == "winnaar"): 
                        print("Speler {} is de winnaar!!".format(speler.geef_symbool()))
                    elif (status == "gelijkspel"):
                        print("Het is een gelijkspel!")
                    antwoord = input("Nog een potje? (J/N) >> ")
                    if (antwoord.upper() == "J"): 
                        self.__bord.herstel()
                    else:
                        doorspelen = False              



s = spel()
s.start2()

