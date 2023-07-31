from .marks import Marks
from .cookie import RuobrCookies
from .schedule import Schedule

class RuobrParser():
  
  def __init__(self,username : str, password: str) -> None:
    self.__cookies = RuobrCookies(username,password).cookies()
    
  def marks(self) -> Marks:
    return Marks(self.__cookies)

  def schedule(self):
    return Schedule(self.__cookies)
