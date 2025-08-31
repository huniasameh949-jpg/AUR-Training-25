from random import randint
import copy
class Employee:
    def __init__(self,name,family,manager=None):
        self.name=name
        self._family=copy.deepcopy(family)
        self._id=randint(1000,9999)
        self._manager=manager
        self.salary=2500
    @property
    def id(self)->int:
        return self._id
    @property 
    def family(self)->dict:
        return copy.deepcopy(self._family)
    def apply_raise(self,managed_employee:'Employee', raise_percent:int):
        if(managed_employee._manager is self):
            managed_employee.salary=managed_employee.salary*(1+(raise_percent/100))
            print(managed_employee.salary)
            return True
        else :
            return False
    
        
