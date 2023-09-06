from evonotes import EvoNotes
from diagnostic import DiagnosticImages
from prescriptions import Prescriptions
from labresults import LabResults


class ClinicalRecords():
    def __init__(self, evolution_notes: EvoNotes = EvoNotes(),
                 diagnostic_images: DiagnosticImages = DiagnosticImages(),
                 lab_results: LabResults = LabResults(),
                 prescriptions: Prescriptions = Prescriptions()):
        '''
        Constructor of the class ClinicalRecords class


        :param evolution_notes: evolution notes of the patient
        :type evolution_notes: EvoNotes
        :param diagnostic_images: diagnostic images of the patient
        :type diagnostic_images: DiagnosticImages
        :param lab_results: lab results of the patient
        :type lab_results: LabResults
        :param prescriptions: prescriptions of the patient
        :type prescriptions: Prescriptions
        '''
        self.__evolution_notes = evolution_notes
        self.__diagnostic_images = diagnostic_images
        self.__lab_results = lab_results
        self.__prescriptions = prescriptions

    @ property
    def evolution_notes(self):
        '''
        Returns the evolution_notes attribute

        :return: evolution notes of the patient
        :rtype: EvoNotes
        '''
        return self.__evolution_notes

    @ property
    def diagnostic_images(self):
        '''
        Returns the diagnostic_images attribute

        :return: diagnostic images of the patient
        :rtype: DiagnosticImages
        '''
        return self.__diagnostic_images

    @ property
    def lab_results(self):
        '''
        Returns the lab_results attribute

        :return: lab results of the patient
        :rtype: LabResults
        '''
        return self.__lab_results

    @ property
    def prescriptions(self):
        '''
        Returns the prescriptions attribute

        :return: prescriptions of the patient
        :rtype: Prescription
        '''
        return self.__prescriptions
