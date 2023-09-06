from hospital import Hospital
from vitalsigns import VitalSigns
from patient import Patient

# Create a new hospital
hospital = Hospital()

print("Welcome to the Hospital Management System")


def select_patient():
    id = int(input("Please enter the patient id: "))
    patient = hospital.get_patient(id)
    if patient is None:
        print("Patient not found")
        return
    return patient


def manage_patient():
    patient = select_patient()
    if patient is None:
        return
    print("Please select an option from the menu below: ")
    print("1. Manage Vital Signs")
    print("2. Manage Medication")
    print("3. Manage Evolution notes")
    print("4. Manage Diagnostic images")
    print("5. Manage Lab results")
    print("6. Exit")

    op = int(input())

    while op not in range(1, 7):
        print("Invalid option")
        op = int(input())

    {1: manage_vital_signs, 2: manage_medication, 3: manage_evolution_notes,
        4: manage_diagnostic_images, 5: manage_lab_results,
     6: exit}[op](patient)


def manage_diagnostic_images(patient):
    print("Please select an option from the menu below: ")
    print("1. Add diagnostic image")
    print("2. Show diagnostic images")
    print("3. Exit")

    op = int(input())

    while op not in range(1, 4):
        print("Invalid option")
        op = int(input())

    if op == 1:
        print("Please enter the image url: ")
        url = input()
        patient.add_diagnostic_image(url)
    elif op == 2:
        patient.show_diagnostic_images()
    else:
        return


def manage_vital_signs(patient):
    print("Please select an option from the menu below: ")
    print("1. Edit vital signs")
    print("2. Show vital signs")
    print("3. Exit")

    op = int(input())

    while op not in range(1, 4):
        print("Invalid option")
        op = int(input())

    if op == 1:
        temp = float(input("Please enter the temperature: "))
        blood_pressure = float(input("Please enter the blood pressure: "))
        respiratory_rate = float(input("Please enter the respiratory rate: "))
        blood_oxygen_saturation = float(
            input("Please enter the blood oxygen saturation: "))

        patient.vital_signs = VitalSigns(
            temp, blood_pressure, respiratory_rate, blood_oxygen_saturation)

    elif op == 2:
        print(patient.vital_signs)

    elif op == 3:
        return


def manage_evolution_notes(patient):
    print("Please select an option from the menu below: ")
    print("1. Add evolution note")
    print("2. Remove evolution note")
    print("3. Show evolution notes")
    print("4. Exit")

    op = int(input())

    while op not in range(1, 5):
        print("Invalid option")
        op = int(input())

    if op == 1:
        patient.clinical_records.evolution_notes.add()

    elif op == 2:
        patient.clinical_records.evolution_notes.remove()

    elif op == 3:
        print(patient.clinical_records.evolution_notes)

    elif op == 4:
        return

    manage_evolution_notes(patient)


def manage_lab_results(patient):
    print("Please select an option from the menu below: ")
    print("1. Add lab result")
    print("2. Remove lab result")
    print("3. Show lab results")
    print("4. Exit")

    op = int(input())

    while op not in range(1, 5):
        print("Invalid option")
        op = int(input())

    if op == 1:
        patient.clinical_records.lab_results.add()

    elif op == 2:
        patient.clinical_records.lab_results.remove()

    elif op == 3:
        print(patient.clinical_records.lab_results)

    elif op == 4:
        return


def manage_medication(patient):
    print("Please select an option from the menu below: ")
    print("1. Add medication")
    print("2. Remove medication")
    print("3. Show medications")
    print("4. Exit")

    op = int(input())

    while op not in range(1, 5):
        print("Invalid option")
        op = int(input())

    if op == 1:
        patient.clinical_records.prescriptions.add()

    elif op == 2:
        patient.clinical_records.prescriptions.remove()

    elif op == 3:
        print(patient.clinical_records.prescriptions)

    elif op == 4:
        return


def menu():
    print("Please select an option from the menu below:")
    print("1. Add a patient")
    print("2. remove a patient")
    print("3. Manage a patient")
    print("4. Show hospital stats")
    print("5. Show all patients")
    print("6. Exit")

    op = int(input())

    while op not in range(1, 7):
        print("Invalid option")
        op = int(input())

    if op == 1:
        name = input("Please enter the patient's name: ")
        birth_date = input(
            "Please enter the patient's birth date (dd/mm/yy): ")
        id = int(input("Please enter the patient's id: "))
        disease = input("Please enter the patient's disease: ")

        patient = Patient(name, birth_date, id=id, disease=disease)

        hospital.add_patient(patient)

    elif op == 2:
        id = int(input("Please enter the patient's id: "))
        patient = hospital.get_patient(id)

        if patient is None:
            print("Patient not found")
            return

        hospital.remove_patient(patient)

    elif op == 3:
        manage_patient()

    elif op == 4:
        hospital.get_stats()

    elif op == 5:
        hospital.print_patients()

    elif op == 6:
        return


def main():
    while True:
        menu()


if __name__ == '__main__':
    main()
