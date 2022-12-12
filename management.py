class Management:
    
    def __init__(self):
        self.option = -1

    def DisplayMenu(self):

        self.option = 0

        print('Welcome to the Alberta Hospital (AH) Managment system ')
        print('Select from the following options, or select 0 to stop: ')
        print('1 - 	Doctors')
        print('2 - 	Facilities')
        print('3 - 	Laboratories')
        print('4 - 	Patients ')
        self.option = int(input())

        while (self.option != 0):
            if self.option == 1:
                self.doctor_menu()
            if self.option == 2:
                self.facility_menu()
            if self.option == 3:
                self.laboratory_menu()
            if self.option == 4:
                self.patient_menu()
            if self.option == 0:
                print("This program is now closing...")
                exit()
        return

    def doctor_menu(self):
        doctor_object = Doctor()
        doctor_object.read_doctors_file()
        doctor_option = -1

        doctor_method = {
        1: doctor_object.display_doctors_list,
        2: doctor_object.search_doctor_by_id,
        3: doctor_object.search_doctor_by_name,
        4: doctor_object.add_dr_to_file,
        5: doctor_object.edit_doctor_info,
        }

        while (doctor_option != 6):
            print('1 - Display Doctors list')
            print('2 - Search for doctor by id')
            print('3 - Search for doctor by name')
            print('4 - Add doctor')
            print('5 - Edit doctor info')
            print('6 - Back to the Main Menu')
            doctor_option = int(input())
            doctor_method.get(doctor_option, self.doctor_menu)()
            
        else:
            print('Back to the previous Menu')
            self.DisplayMenu()
            return
                

    def facility_menu(self):
        facility_object = Facility()
        facility_object.read_facilities_file()
        facility_option = -1

        facility_method = {
        1: facility_object.display_facilities_list,
        2: facility_object.add_facility_to_file,
        }

        while (facility_option != 3):
            print('1 - Display Facilities list')
            print('2 - Add Facility')
            print('3 - Back to the Main Menu')
            facility_option = int(input())
            facility_method.get(facility_option, self.facility_menu)()
                     
        else:
            self.DisplayMenu()
            print('Back to the previous Menu')
            return

    def laboratory_menu(self):
        laboratory_object = Laboratory()
        laboratory_object.read_lab_file()
        laboratory_option = -1

        laboratory_method = {
        1: laboratory_object.display_labs_list,
        2: laboratory_object.add_lab_to_file,
        }

        while (laboratory_option != 3):
            print('1 - Display laboratories list')
            print('2 - Add laboratory')
            print('3 - Back to the Main Menu')
            laboratory_option = int(input())
            laboratory_method.get(laboratory_option, self.laboratory_menu)()
                    
        else:
            self.DisplayMenu()
            print('Back to the previous Menu')
            return

    def patient_menu(self):
        patient_object = Patient()
        patient_object.read_patients_file()
        patient_option = -1

        patient_method = {
        1: patient_object.display_patients_list,
        2: patient_object.search_patient_by_id,
        3: patient_object.add_patient_to_file,
        4: patient_object.edit_patient_info,
        }

        while (patient_option != 5):
            print('1 - Display patients list')
            print('2 - Search for patient by id')
            print('3 - Add patient')
            print('4 - Edit patient info')
            print('5 - Back to the Main Menu')
            patient_option = int(input())
            patient_method.get(patient_option, self.patient_menu)()
                    
        else:
            self.DisplayMenu()
            print('Back to the previous Menu')
            return
    
menu_object = Management()
menu_object.DisplayMenu()
