class Lab:
    def __init__(self,room_number):
        self.room_number = room_number
        
class Technician:
    
    def __init__(self,name):
        self.assigned_lab = None
        self.name = name
        
        
    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj

mr_cruz=Technician("Mr. Cruz")

room_num=input("Enter keycard number: ")

chem_lab=Lab(room_num)

mr_cruz.assign_lab(chem_lab)

print(mr_cruz.assigned_lab.room_number)
