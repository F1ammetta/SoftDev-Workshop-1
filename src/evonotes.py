class EvoNotes:
    def __init__(self):
        self.notes = []

    def add(self):
        '''
        Add notes
        '''
        print('Add notes')
        print('--------------------')
        date = input('enter date: ')
        note = input('enter note: ')
        state = input('enter patient state: ')
        notes = {'date': date, 'note': note, 'state': state}
        self.notes.append(notes)

    def get_last(self):
        '''
        Returns most recent note
        '''
        return self.notes[-1]

    def __str__(self):
        str = ''
        for note in self.notes:
            str += f"{note['date']} {note['note']} {note['state']}\n"
        return str
