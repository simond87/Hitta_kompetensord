
import Leta_upp_kompetensord as luk

def rensa_listdubletter(ordlista):
    """
    :param ordlista: en lista med strängar inlästa från textfilen med alla termer
    :return: samma ordlista men rensad på dubletter och med bara små bokstäver, för att effektivisera sökningen
    """

    if (type(ordlista)) != list:
        raise TypeError("något är fel, ordlistan blev inte en lista!")
        return None

    nedraeknare = len(ordlista)-1 # indexvariabel för att börja längst upp i listan och räkna ner

    while nedraeknare > 0:
        if type(ordlista[nedraeknare]) != str:
            raise TypeError("fel! termen är ingen sträng")
            return None
        ordlista[nedraeknare] = ordlista[nedraeknare].lower()

        if ordlista[nedraeknare] == ordlista[nedraeknare-1].lower():
            """ om nästa term i listan är likadan, tas denna bort, på så vis raderas dubletterna """
            del ordlista[nedraeknare]

        nedraeknare -= 1
    return ordlista

if __name__ == '__main__':

    annonsfil = open('job-posting.txt', 'r')
    kompetensordsfil = open('skills.txt', 'r')
    """ läser in textfilerna jobbannons och kompetenser """

    annonstext = annonsfil.read() # annonsen hamnar i en stor sträng
    annonsfil.close()

    kompetensorden = rensa_listdubletter(kompetensordsfil.readlines())
    """ Från filen inläses en lista där varje element är ett visst kompetensord i form av en sträng.
    Innan den sparas i listan kompetensorden rensas dubletterna bort och
    alla bokstäver konverteras alla element till gemener """
    kompetensordsfil.close()

    if type(kompetensorden) == list:
        luk.leta_upp(kompetensorden, annonstext) # letar upp och skriver ut de hittade kompetensorden
    else:
        raise ValueError("fel, det blev ingen lista av kompetensorden")