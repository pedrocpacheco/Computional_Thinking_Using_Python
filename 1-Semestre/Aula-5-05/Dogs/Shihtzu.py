import Dog

class Shihtzu(Dog):
    
    def bark(self, sound="Au au"):
        return f"{self.name} barks {sound}"