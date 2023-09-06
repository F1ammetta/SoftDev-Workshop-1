class Prescriptions():
    def __init__(self):
        self.prescriptions = []

    def add(self):
        print('Add prescriptions')
        print('--------------------')
        name = input('enter medicine name: ')
        prescription = input('enter prescription (i.e 1x4h): ')
        med = {'name': name, 'prescription': prescription}
        self.prescriptions.append(med)

    def __str__(self):
        str = ''
        for prescription in self.prescriptions:
            str += f'{prescription["name"]}: {prescription["prescription"]}\n'
        return str

    def remove(self):
        print('Remove prescriptions')
        print('--------------------')
        for prescription, i in enumerate(self.prescriptions):
            print(f'{i}: {prescription}')
        remove = int(input('enter number to remove: '))
        self.prescriptions.pop(remove)
