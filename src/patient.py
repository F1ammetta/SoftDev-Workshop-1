from vitalsigns import VitalSigns


class Patient():

    def __init__(self, name: str = "", birthdate: str = "", id: int = 0,
                 vital_signs: VitalSigns = VitalSigns()):
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
        '''
        self.__name = name
        self.__birthdate = birthdate
        self.__id = id
        self.__vital_signs = vital_signs

    def __str__(self):
        '''
        Returns the string representation of the patient

        :return: string representation of the patient
        :rtype: str
        '''
        return f'Patient: {self.__name}'

    @ property
    def name(self):
        '''
        Returns the name attribute

        :return: name of the patient
        :rtype: str
        '''
        return self.__name

    @ name.setter
    def name(self, name: str):
        '''
        Sets the name attribute

        :param name: name of the patient
        :type name: str
        '''
        self.__name = name

    @ property
    def birthdate(self):
        '''
        Returns the birthdate attribute

        :return: birthdate of the patient
        :rtype: str
        '''
        return self.__birthdate

    @ birthdate.setter
    def birthdate(self, birthdate: str):
        '''
        Sets the birthdate attribute

        :param birthdate: birthdate of the patient
        :type birthdate: str
        '''
        self.__birthdate = birthdate

    @ property
    def id(self):
        '''
        Returns the id attribute

        :return: id of the patient
        :rtype: int
        '''
        return self.__id

    @ id.setter
    def id(self, id: int):
        '''
        Sets the id attribute

        :param id: id of the patient
        :type id: int
        '''
        self.__id = id

    @ property
    def vital_signs(self):
        '''
        Returns the vital_signs attribute

        :return: vital signs of the patient
        :rtype: VitalSigns
        '''
        return self.__vital_signs
