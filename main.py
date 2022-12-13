
class Laboratories:

    
    labs = [] 

    def __init__(self, name = "", cost = ""):
        self.name = name
        self.cost = cost
        
   
    def read_lab_file(self):
        
        with open("laboratories.txt", "r") as lab_file:
            file_content = lab_file.readlines()
            for line in file_content:
                values = line.split("_")
                lab = lab(values[0], values[1])
                self.labs.append(lab)
        print("Finished loading laboratories.txt to labs list")

    def write_list_of_labs_to_file(self):
       
        with open("laboratories.txt", "w") as lab_file:
            for lab in self.labs:
                formatted_lab = self.format_lab_info(lab)
                lab_file.write(formatted_lab)
        print("Finished writing data from the list to Laboratories.txt.")

    def format_lab_info(self, lab):
    
        return (f"{lab.name}_{lab.cost}")


    def enter_lab_info(self):

        print("Enter Laboratory facility:")
        name = input()
        print("Enter Laboratory cost:")
        cost = input()
        lab = Laboratories(name, cost)

       
        return lab

    def display_labs_list(self):
        
        for lab in self.labs:
            print ("{:<4} {:<22}".format(lab.name, lab.cost))


    def add_lab_to_file(self):
        with open("labratories.txt", "a") as lab_file:
            new_lab = self.enter_lab_info()
            self.labs.append(new_lab)
            formatted_lab = self.format_lab_info(new_lab)
            lab_file.write(f"\n{formatted_lab}")
        print("Finished adding a new lab to laboratories.txt.")


