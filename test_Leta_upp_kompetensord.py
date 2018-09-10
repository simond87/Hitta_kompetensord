import Leta_upp_kompetensord as luk
import unittest


class Testa_inlaest_data(unittest.TestCase):

    def testa_typer(self):
        """
        Kollar att det blir rätt felsvar något inte är av den datatyp som funktionerna förväntar sig.
        I kommentarerna till respektive assertRaises-anrop står vilken parameter som är fel.
        """

        bra_lista = ["Sverige", "Norge", "Finland"]
        sifferlista = [0, 1, 2]
        booleanlista = [True, False, False]
        tupel = ("Sverige", "Norge", "Finland")
        straeng = "aaaaabbbbbccccc"

        self.assertRaises(TypeError, luk.leta_upp, bra_lista, 10)
        """en int istället för en sträng"""

        self.assertRaises(TypeError, luk.leta_upp, sifferlista, straeng)
        """en lista med intar ist för med strängar"""

        self.assertRaises(TypeError, luk.leta_upp, booleanlista, straeng)
        """en lista med booleaner ist för med strängar """

        self.assertRaises(TypeError, luk.leta_upp, tupel, straeng)
        """en tupel med strängar istället för en lista"""

