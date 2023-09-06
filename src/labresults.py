class LabResults:
    def __init__(self):
        self.results = []

    def add(self):
        print('Add lab results')
        print('----------------')
        procedure = input('enter lab procedure: ')
        result = input('enter lab result: ')
        date = input('enter date (dd/mm/yy): ')
        lab = {'procedure': procedure, 'result': result, 'date': date}
        self.results.append(lab)

    def __str__(self):
        str = ''
        for lab in self.results:
            str += f"{lab['procedure']} {lab['result']} {lab['date']}\n"
        return str

    def remove(self):
        print('Remove lab results')
        print('-------------------')
        for lab, i in enumerate(self.results):
            print(f'{i}: {lab}')
        remove = int(input('enter number to remove: '))
        self.results.pop(remove)
