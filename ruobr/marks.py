import asyncio
import aiohttp
from bs4 import BeautifulSoup

from .cookie import RuobrCookies
from .extra import crop, headers

class Marks():
  
  def __init__(self, __data : dict) -> None:
    self.__cookies = RuobrCookies(*__data.values()).cookies()

  def __marks(self) -> list:

    async def pagination(session : aiohttp.ClientSession) -> int:
      response = await session.get('https://cabinet.ruobr.ru//student/progress/',cookies = self.__cookies,headers=headers)
      soup = BeautifulSoup(await response.text(), 'lxml')
      href_list = soup.find('ul',class_='pagination noprint').find_all('a')[-1]
      number = crop(str(href_list),'?page=', '"')
      return int(number)
    
    async def catch_page(url: str ,session : aiohttp.ClientSession):
      async with session.get(url=url,headers=headers,cookies = self.__cookies) as response:
        return await response.text()
        
    async def pages(timeout: float):
      tasks = []
      async with aiohttp.ClientSession() as session:
        pagination_num = await pagination(session)
        for num in range(1,pagination_num+1):
          url = f"https://cabinet.ruobr.ru//student/progress/?page={num}"
          tasks.append(asyncio.create_task(catch_page(url,session))) 
          await asyncio.sleep(timeout)
          
        return await asyncio.gather(*tasks)
    
    async def sorter():
      all_marks = []
      for page in await pages(0.0065):
        soup = BeautifulSoup(page, 'html.parser')
        data = list(map(str, soup.find_all('tr')))
        for t in data:
          cleantext = BeautifulSoup(t, 'html.parser').text.split('\n')[3:6]
          header = ['Дата', 'Дисциплина', 'Отметка']
          if cleantext != header:
            cleantext[2] = {'отлично': 5,'хорошо': 4,'удовлетворительно': 3,'неудовлетворительно': 2}[cleantext[2]]
            all_marks.append(cleantext)
            
      return all_marks
    
    async def main():
      return await sorter()
    
    return asyncio.run(main())

  def get_all(self) -> list:
    return self.__marks()

  