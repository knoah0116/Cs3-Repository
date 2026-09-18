class Glassware:
    
    def __init__(self,material="Glass"):
        self.material="Glass"
        
class Beaker(Glassware):
    def __init__(self,material="Glass"):
        super().__init__(material)
        
class Tray:
    def __init__(self,material="Glass"):
        self.beakers =[Beaker(material) for i in range(5)]
        
        
        
        
my_tray=Tray(material="Glass")

print(f"{len(my_tray.beakers)} {my_tray.beakers[0].material}")
