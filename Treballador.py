class Treballador:
    """La classe treballador es una classe per crear traballador amb parametres predefinits"""

    def __init__(self, nom="", tipus="BASE", nomina=0.0, hores=0): 
        # Constructor de la classe, s'executa quan es crea un nou treballador.
        # Els paràmetres tenen valors per defecte per ser opcionals.
        self.nomTreballador = nom                           
        self.tipusTreballador = tipus                       
        self.nominaTreballador = nomina
        self.horesExtresTreballador = hores

        # Inicialitzem els atributs del treballador amb els valors proporcionats o els valors per defecte.

    def set_nom(self, nom):  

        # Mètode per establir el nom del treballador.
                                               
        if len(nom) < 3:                                            
            raise Exception("El nom ha de tenir 3 o més caracters") 
        # Llença una excepció si el nom té menys de 3 caràcters.
        self.nomTreballador = nom                                 

        # Establim el nom del treballador si el nombre de caràcters és vàlid.  

    def get_nom(self):                     
        return self.nomTreballador                  # Mètode per obtenir el nom del treballador.

    def set_nomina(self, euros):           
        self.nominaTreballador = euros     # Mètode per establir la nòmina del treballador.
        # Establim la nòmina del treballador amb el valor proporcionat.

    def get_nomina(self):                  
    # Mètode per obtenir la nòmina del treballador.
        return self.nominaTreballador      

    def set_hores_extres(self, hores):     
        self.horesExtresTreballador = hores

    def get_hores_extres(self):             
        return self.horesExtresTreballador 

    def set_tipus_treballador(self, tipus):                          
        if tipus in [self.DIRECTOR, self.SUBDIRECTOR, self.BASE]:   
            self.tipusTreballador = tipus                           
        else:
            raise Exception("Tipus de treballador no vàlid")

    def get_tipus_treballador(self):       
        return self.tipusTreballador       