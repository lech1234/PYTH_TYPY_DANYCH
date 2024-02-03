class Kontakt:
    """
    Klasa modelu reperezentująca kontakt.
    """

    def __init__(self, imie, nazwisko, telefony):
        """
        Metoda tworząca atrybuty instancyjne opisujące osobę.

        :param imie: imię osoby
        :param nazwisko: nazwisko osoby
        :param telefony: lista obiektów typu Telefon
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefony = telefony

    def __str__(self):
        """
        Metoda konwersji osoby na reprezentację tekstową.

        :return: reprezentacja tekstowa
        """
        return f'{self.imie} {self.nazwisko}, tel: {self.telefony}'

    def __repr__(self):
        return str(self)


class Telefon:
    """
    Klasa modelu reprezentująca telefon.
    """

    def __init__(self, typ, numer):
        """
        Metoda tworząca atrybuty instancyjne opisujące telefon.


        :param typ: rodzaj telefonu (prywatny, służbowy, itp.)
        :param numer: numer telefonu
        """
        self.typ = typ
        self.numer = numer

    def __str__(self):
        """
        Metoda konwersji telefonu na reprezentację tekstową.

        :return: reprezentacja tekstowa
        """
        return f'{self.typ}: {self.numer}'

    def __repr__(self):
        return str(self)
