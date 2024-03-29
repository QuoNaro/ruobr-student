class RuobrException(Exception):
  ...

class AuthorizationError(RuobrException):
  ...
  
class IncorrectDateError(RuobrException):
  ...

class EmptyDateError(RuobrException):
  ...

class RequestError(RuobrException):
  ...
  
class DateNotFoundError(RuobrException):
  ...