from .marks import Marks
from .cookie import RuobrCookies

class RuobrParser():
  
  def __init__(self,username,password) -> None:
    self.__data = {'username' : username,
                   'password' : password}
    
  def marks(self) -> Marks:
    return Marks(self.__data)



