import datetime


class Hospital():
    '''
    This class represents a hospital.


    '''
    max_patients = 300

    cronic_diseases = ['diabetes',
                       'cancer',
                       'tuberculosis',
                       'HIV',
                       'Alzheimer',
                       'Parkinson',
                       'multiple sclerosis',
                       'amyotrophic lateral sclerosis']

    date = datetime.datetime.now().strftime("%d-%m-%y")

    access_log: dict[str, dict[str, int]] = {}

    def __init__(self):
        '''
        Constructor for Hospital class.

        :param patients: list of patients
        :type patients: list
        :param occupied_beds: number of occupied beds
        :type occupied_beds: int
        '''
        self.__patients = []

    def add_patient(self, patient):
        '''
        Add patient to the hospital.

        :param patient: patient to add
        :type patient: Patient
        '''
        if self.date not in self.access_log:
            self.access_log[self.date] = {"entrance": 0, "exit": 0}
        if len(self.__patients) < self.max_patients:
            self.__patients.append(patient)
            self.access_log[self.date]["entrance"] += 1

        else:
            print('Hospital is full!')

    def remove_patient(self, patient):
        '''
        Remove patient from the hospital.

        :param patient: patient to remove
        :type patient: Patient
        '''
        if self.date not in self.access_log:
            self.access_log[self.date] = {"entrance": 0, "exit": 0}
        if patient in self.__patients:
            self.__patients.remove(patient)
            self.access_log[self.date]["exit"] += 1

    def get_stats(self):
        '''
        Get hospital statistics.

        :return: hospital statistics
        :rtype: dict
        '''
        stats = {}
        stats['num_free_beds'] = self.max_patients - len(self.__patients)
        stats['ratio'] = len(self.__patients) / self.max_patients
        stats['avg'] = self.access_log[self.date]['entrance'] - \
            self.access_log[self.date]['exit']
        stats['entrances'] = self.access_log[self.date]['entrance']
        stats['exits'] = self.access_log[self.date]['exit']
        stats['cronic'] = 0

        for patient in self.__patients:
            if patient.disease in self.cronic_diseases:
                stats['cronic'] += 1

        print(f'''Free beds: {stats['num_free_beds']}
% of occupation: {stats['ratio']}
Average patients per day: {stats['avg']}
Entrances: {stats['entrances']}
Exits: {stats['exits']}
Cronic patients: {stats['cronic']}''')

    def get_patient(self, patient_id):
        '''
        Get patient by id.

        :param patient_id: patient id
        :type patient_id: int
        :return: patient
        :rtype: Patient
        '''
        for patient in self.__patients:
            if patient.id == patient_id:
                return patient
        return None

    def print_patients(self):
        '''
        Print all patients in the hospital.
        '''
        for patient in self.__patients:
            print('--------------------')
            print(patient)
            print('--------------------')

    @property
    def patients(self):
        '''
        Get patients.

        :return: patients
        :rtype: list
        '''
        return self.__patients
