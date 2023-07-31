import requests
from .extra import headers
from .exceptions import AuthorizationError

class RuobrCookies:
  
  """Класс для получения куки cabinet.ruobr.ru"""
  def __init__(self, username : str, password : str) -> None:
    self.username = username
    self.password = password
     
    cookies = self.cookies().values()
    if len(cookies) < 2:
      raise AuthorizationError(f"Invalid credantials in username or password")
    self.csrftoken,self.sessionid = self.cookies().values()

  def cookies(self) -> dict:
    """Cookie необходимые для авторизации"""
    data = {'username' : self.username, 'password' : self.password}
    session = requests.Session()
    
    session.get('https://cabinet.ruobr.ru/login/', headers=headers)
    data |= {'csrfmiddlewaretoken': dict(session.cookies)['csrftoken']}
    
    session.post('https://cabinet.ruobr.ru/login/', headers=headers, data=data)
    return dict(session.cookies)
