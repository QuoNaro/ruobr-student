from .marks import Marks
from .cookie import RuobrCookies

class RuobrParser():
  
  def __init__(self,username : str, password: str) -> None:
    self.__cookies = RuobrCookies(username,password).cookies()
    
  def marks(self) -> Marks:
    return Marks(self.__cookies)



