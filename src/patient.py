from vitalsigns import VitalSigns
from clinical import ClinicalRecords


class Patient():

    def __init__(self, name: str = "", birthdate: str = "", id: int = 0,
                 vital_signs: VitalSigns = VitalSigns(), gender: str = "",
                 clinical_records: ClinicalRecords = ClinicalRecords(),
                 disease: str = ""):
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
        :param gender: gender of the patient
        :type gender: str
        :param clinical_records: clinical records of the patient
        :type clinical_records: ClinicalRecords
        '''
        self.__name = name
        self.__birthdate = birthdate
        self.__id = id
        self.__vital_signs = vital_signs
        self.__clinical_records = clinical_records
        self.__disease = disease
        self.__gender = gender

    def __str__(self):
        '''
        Returns the string representation of the patient

        :return: string representation of the patient
        :rtype: str
        '''
        return f'''Patient: {self.__name}
Gender: {self.__gender}
id: {self.__id}
Disease: {self.__disease}
Vital Signs: {self.__vital_signs}
Evolution Notes: {self.__clinical_records.evolution_notes}
Lab Results: {self.__clinical_records.lab_results}
Diagnostic Images: {self.__clinical_records.diagnostic_images}
Prescriptions: {self.__clinical_records.prescriptions}'''

    @ property
    def name(self):
        '''
        Returns the name attribute

        : return: name of the patient
        : rtype: str
        '''
        return self.__name

    @ name.setter
    def name(self, name: str):
        '''
        Sets the name attribute

        : param name: name of the patient
        : type name: str
        '''
        self.__name = name

    @ property
    def gender(self):
        '''
        Returns gender of the patient

        : return: gender of the patient
        : rtype: str
        '''
        return self.__gender

    @ property
    def birthdate(self):
        '''
        Returns the birthdate attribute

        : return: birthdate of the patient
        : rtype: str
        '''
        return self.__birthdate

    @ birthdate.setter
    def birthdate(self, birthdate: str):
        '''
        Sets the birthdate attribute

        : param birthdate: birthdate of the patient
        : type birthdate: str
        '''
        self.__birthdate = birthdate

    @ property
    def id(self):
        '''
        Returns the id attribute

        : return: id of the patient
        : rtype: int
        '''
        return self.__id

    @ id.setter
    def id(self, id: int):
        '''
        Sets the id attribute

        : param id: id of the patient
        : type id: int
        '''
        self.__id = id

    @ property
    def vital_signs(self):
        '''
        Returns the vital_signs attribute

        : return: vital signs of the patient
        : rtype: VitalSigns
        '''
        return self.__vital_signs

    @ property
    def clinical_records(self):
        '''
        Returns the clinical_records attribute

        : return: clinical records of the patient
        : rtype: ClinicalRecords
        '''
        return self.__clinical_records

    @ property
    def disease(self):
        '''
        Returns the disease attribute

        : return: disease of the patient
        : rtype: str
        '''
        return self.__disease
