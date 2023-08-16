
class VitalSigns():
    '''
    Class that represents the vital signs of a patient.
    '''

    def __init__(self, temperature: float = 36, blood_pressure: float = 120,
                 blood_saturation: float = 95, respiratory_rate: float = 12):
        '''
        Constructor of the VitalSigns class.

        :param temperature: Temperature of the patient in °C.
        :type temperature: float
        :param blood_pressure: Blood pressure of the patient in mmHg.
        :type blood_pressure: float
        :param blood_saturation: Saturation of the patient in % of oxygen.
        :type blood_saturation: float
        :param respiratory_rate: Respiratory rate of the patient.
        :type respiratory_rate: float
        '''
        self.__temperature = temperature
        self.__blood_pressure = blood_pressure
        self.__respiratory_rate = respiratory_rate
        self.__blood_saturation = blood_saturation

    def __str__(self):
        return f''' {{ Temperature: {self.__temperature} °C
                Blood pressure: {self.__blood_pressure} mmHg
                Respiratory rate: {self.__respiratory_rate} breaths per minute
                Blood saturation: {self.__blood_saturation} % }}'''

    @property
    def temperature(self):
        '''
        Returns the temperature of the patient.
        :return: Temperature of the patient in °C.
        :rtype: float
        '''
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        '''
        Sets the temperature of the patient.
        :param value: Temperature of the patient in °C.
        :type value: float
        '''
        self.__temperature = value

    @property
    def blood_pressure(self):
        '''
        Returns the blood pressure of the patient.
        :return: Blood pressure of the patient in mmHg.
        :rtype: float
        '''
        return self.__blood_pressure

    @blood_pressure.setter
    def blood_pressure(self, value: float):
        '''
        Sets the blood pressure of the patient.
        :param value: Blood pressure of the patient in mmHg.
        :type value: float
        '''
        self.__blood_pressure = value

    @property
    def respiratory_rate(self):
        '''
        Returns the respiratory rate of the patient.
        :return: Respiratory rate of the patient.
        :rtype: float
        '''
        return self.__respiratory_rate

    @respiratory_rate.setter
    def respiratory_rate(self, value: float):
        '''
        Sets the respiratory rate of the patient.
        :param value: Respiratory rate of the patient.
        :type value: float
        '''
        self.__respiratory_rate = value

    @property
    def blood_saturation(self):
        '''
        Returns the saturation of the patient.
        :return: Saturation of the patient in % of oxygen.
        :rtype: float
        '''
        return self.__blood_saturation

    @blood_saturation.setter
    def blood_saturation(self, value: float):
        '''
        Sets the saturation of the patient.
        :param value: Saturation of the patient in % of oxygen.
        :type value: float
        '''
        self.__blood_saturation = value
