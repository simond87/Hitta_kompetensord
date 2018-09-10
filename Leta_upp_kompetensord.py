import re

def leta_upp(kompetenser, soektext):
    """

    :param kompetenser: en med lista strängar som ska motsvara termerna att söka på i texten
    :param soektext: strängen vi ska söka i mha reguljära uttryck och match-objekt.
    :return: inget returneras, resultaten skrivs ut

    Letar upp kompetensorden i söktexten med reguljära uttryck mha finditer och match-objekt
    och skriver ut de hittade kompetensorden till konsolen med start- och slutposition
    """
    if type(soektext) != str:
        raise TypeError("fel, söktexten är inte en sträng")
    elif type(kompetenser) != list:
        raise TypeError("fel, kompetensorden är inte en lista, det är en " + str(type(kompetenser)))

    for kompetens in kompetenser:
        if type(kompetens) != str:
            raise TypeError("fel, följande kompetensord är inte en sträng: " + str(kompetens))

        regexanpassat_soekord = re.compile('\\b' + re.escape(kompetens.rstrip()) + '\\b', re.IGNORECASE)
        """ Sökuttryck behöver kompileras för att kunna använda finditer"""

        upptaeckter = regexanpassat_soekord.finditer(soektext)
        """upptaeckter är en lista match-objekt som motsvarar alla träffar
        som programmet får i texten på kompetensordet"""

        for upptaeckt in upptaeckter:
            print("Startposition " + str(upptaeckt.start()) + " och slutposition " + str(upptaeckt.end()) + '\t\t' + kompetens.rstrip())
