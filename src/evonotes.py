class EvoNotes:
    def __init__(self):
        self.notes = []

    def add(self):
        print('Add notes')
        print('--------------------')
        date = input('enter date: ')
        note = input('enter note: ')
        state = input('enter patient state: ')
        notes = {'date': date, 'note': note, 'state': state}
        self.notes.append(notes)

    def print(self):
        for note in self.notes:
            print(note)
