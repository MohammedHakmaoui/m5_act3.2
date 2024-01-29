from Treballador import Treballador

import unittest

class TreballadorTest(unittest.TestCase):
#Aquest test prova si el programa detecta que volem assignar un nom
#incorrecte i llença l'excepció que toca
#Noteu que per als objectes individuals de la classe Treballador i
#Exception podem triar els noms que ens done la gana,
#no cal fer-los coincidir amb els de les classes"""
    def test_nom_treballador_incorrecte(self):
        treballador_meu = Treballador()
        #Codi per a provocar excepcions
        excepcio_meva = self.assertRaises(Exception, lambda:
        treballador_meu.set_nom(""))
        self.assertEqual("El nom ha de tenir 3 o més caracters",
        excepcio_meva.message)
    #L'assercio mira si el text de l'excepció avisa del problema de nom curt
    def test_nom_treballador_correcte(self):
    #Assignem un nom, com el mètode setNom pot produir excepcions ha d'anar en un
    #bloc try catch
    #A diferencia del cas anterior, aquí no estem provocant l'excepció a propòsit,
    #sino que és el tractament
    #habitual de les excepcions, ja ho veureu en M3"""
        nom_test = ""
        treballador = Treballador()
    #Si es produeix una excepcio, el bloc catch la captura i mostra per pantalla,
    #així el programa no peta
        try:
            treballador.set_nom(nom_test)
        except Exception as e:
            print(e.message)
    # L'assercio comprova que el nom és correcte i en cas contrari mostraria el
    #missatge d'error
        self.assertEqual(nom_test, treballador.get_nom(), "Els noms han de coincidir!!!")
    def test_nomina(self):
        nomina = 2300
        treballador = Treballador()
    #Assignem una nomina, com aquest mètode no provoca excepcions no necessitem el
    #bloc try-catch
        treballador.set_nomina(nomina)
        self.assertEqual(nomina, treballador.get_nomina(), "Els dos valors de la nomina han de coincidir!!!")
    #L'asserció comprova que la nomina és correcta i en cas contrari
    #mostra missatge d'error
    def test_hores_extres(self):
        hores_extres = 10
        treballador = Treballador()
        # Assignem hores extres, com aquest mètode no provoca excepcions no necessitem el bloc try-catch
        treballador.set_hores_extres(hores_extres)
        self.assertEqual(hores_extres, treballador.get_hores_extres(), "Els dos valors d'hores extres han de coincidir!!!")
        # L'asserció comprova que les hores extres són correctes i en cas contrari
        # mostra missatge d'error
        
        '''
    def test_tipus_treballador_incorrecte(self):
        treballador = Treballador()
# intentem assignar un treballador incorrecte
        with self.assertRaises(Exception) as context:
            treballador.set_tipus_treballador("INVALID")
            #verificació
        self.assertEqual("Tipus de treballador no vàlid", str(context.exception)) '''

    def test_tipus_treballador_incorrecte(self):
        treballador = Treballador()
    # intentem assignar un treballador incorrecte
        with self.assertRaises(Exception) as context:
            treballador.set_tipus_treballador("INVALID")
            #verificació
        self.assertEqual("Tipus de treballador no vàlid", str(context.exception))

    def test_tipus_treballador_correcte(self):
        tipus_treballador_correcte = Treballador.DIRECTOR
        treballador = Treballador()

        # Utilitzem el mètode set_tipus_treballador
        try:
            treballador.set_tipus_treballador(tipus_treballador_correcte)
        except Exception as e:
            print(e.message)
        # L'asserció comprova que el tipus de treballador és correcte i en cas contrari mostra el missatge d'error
        self.assertEqual(tipus_treballador_correcte, treballador.get_tipus_treballador(), "Els tipus de treballador han de coincidir!!!")

if __name__ == '__main__':
    unittest.main()