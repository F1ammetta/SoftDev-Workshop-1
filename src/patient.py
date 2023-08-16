from vitalsigns import VitalSigns


class Patient():

    def __init__(self, name: str = "", birthdate: str = "", id: int = 0,
                 vital_signs: VitalSigns = VitalSigns(),
                 evolution_notes: list = [],
                 diagnostic_images: list = [],
                 lab_results: list = [],
                 prescriptions: list = []):
        '''
        Constructor of the Patient class

        :param name: name of the patient
        :type name: str
        :param birthdate: birthdate of the patient
        :type birthdate: str
        :param id: id of the patient
        :type id: int
        :param vital_signs: vital signs of the patient
        :type vital_signs: VitalSigns
        :param evolution_notes: evolution notes of the patient
        :type evolution_notes: list
        :param diagnostic_images: diagnostic images of the patient
        :type diagnostic_images: list
        :param lab_results: lab results of the patient
        :type lab_results: list
        '''
        self.__name = name
        self.__birthdate = birthdate
        self.__id = id
        self.__vital_signs = vital_signs
        self.__evolution_notes = evolution_notes
        self.__diagnostic_images = diagnostic_images
        self.__lab_results = lab_results
        self.__prescriptions = prescriptions

    def __str__(self):
        '''
        Returns the string representation of the patient

        :return: string representation of the patient
        :rtype: str
        '''
        return f'Patient: {self.__name}'

    @property
    def name(self):
        '''
        Returns the name attribute

        :return: name of the patient
        :rtype: str
        '''
        return self.__name

    @name.setter
    def name(self, name: str):
        '''
        Sets the name attribute

        :param name: name of the patient
        :type name: str
        '''
        self.__name = name

    @property
    def birthdate(self):
        '''
        Returns the birthdate attribute

        :return: birthdate of the patient
        :rtype: str
        '''
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate: str):
        '''
        Sets the birthdate attribute

        :param birthdate: birthdate of the patient
        :type birthdate: str
        '''
        self.__birthdate = birthdate

    @property
    def id(self):
        '''
        Returns the id attribute

        :return: id of the patient
        :rtype: int
        '''
        return self.__id

    @id.setter
    def id(self, id: int):
        '''
        Sets the id attribute

        :param id: id of the patient
        :type id: int
        '''
        self.__id = id

    @property
    def vital_signs(self):
        '''
        Returns the vital_signs attribute

        :return: vital signs of the patient
        :rtype: VitalSigns
        '''
        return self.__vital_signs

    @vital_signs.setter
    def vital_signs(self, vital_signs: VitalSigns):
        '''
        Sets the vital_signs attribute

        :param vital_signs: vital signs of the patient
        :type vital_signs: VitalSigns
        '''
        self.__vital_signs = vital_signs

    @property
    def evolution_notes(self):
        '''
        Returns the evolution_notes attribute

        :return: evolution notes of the patient
        :rtype: list
        '''
        return self.__evolution_notes

    @evolution_notes.setter
    def evolution_notes(self, evolution_notes: list):
        '''
        Sets the evolution_notes attribute

        :param evolution_notes: evolution notes of the patient
        :type evolution_notes: list
        '''
        self.__evolution_notes = evolution_notes

    @property
    def diagnostic_images(self):
        '''
        Returns the diagnostic_images attribute

        :return: diagnostic images of the patient
        :rtype: list
        '''
        return self.__diagnostic_images

    @diagnostic_images.setter
    def diagnostic_images(self, diagnostic_images: list):
        '''
        Sets the diagnostic_images attribute

        :param diagnostic_images: diagnostic images of the patient
        :type diagnostic_images: list
        '''
        self.__diagnostic_images = diagnostic_images

    @property
    def lab_results(self):
        '''
        Returns the lab_results attribute

        :return: lab results of the patient
        :rtype: list
        '''
        return self.__lab_results

    @lab_results.setter
    def lab_results(self, lab_results: list):
        '''
        Sets the lab_results attribute

        :param lab_results: lab results of the patient
        :type lab_results: list
        '''
        self.__lab_results = lab_results

    @property
    def prescriptions(self):
        '''
        Returns the prescriptions attribute

        :return: prescriptions of the patient
        :rtype: list
        '''
        return self.__prescriptions

    @prescriptions.setter
    def prescriptions(self, prescriptions: list):
        '''
        Sets the prescriptions attribute

        :param prescriptions: prescriptions of the patient
        :type prescriptions: list
        '''
        self.__prescriptions = prescriptions
