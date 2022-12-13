class Facility:
    facility = []

    def __init__ (self, facility_name=""):
        self.facility_name = facility_name

    # Adds and writes the facility name to the file
    def add_facility(self):
        with open ("facilities.txt", "a") as facility_file:
            print ("Enter facility name:")
            new_facility = input()  
            facility_file.write(f"\n{new_facility}")
        print("Finished adding a new facility to facilities.txt.")

    # Displays the list of facilities
    def display_facility(self):
        with open("facilities.txt", "r") as facility_file:
            for facility_line in facility_file:
                print(facility_line,end="" + "\n")

    # Writes the facilities list to facilities.txt
    def write_list_of_facilities_to_file (self):
        with open ("facilities.txt", "w") as facility_file:
            for facility_line in self.facility:
                facility_file.write(facility_line)
        return
