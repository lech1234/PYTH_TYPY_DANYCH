class Contact:
    def __init__(self, first_name, last_name, phones):
        self.first_name = first_name
        self.last_name = last_name
        self.phones = phones

    def __str__(self):
        return f'{self.first_name} {self.last_name}, phones: {self.phones}'


class Phone:
    def __init__(self, phone_type, phone_number):
        self.phone_type = phone_type
        self.phone_number = phone_number

    def __str__(self):
        return f'{self.phone_type}: {self.phone_number}'

    def __repr__(self):
        return str(self)


# przykładowe dane
ph1 = Phone('work', '123456789')
ph2 = Phone('private', '987654321')

ct1 = Contact('Jan', 'Kowalski', [ph1, ph2])
