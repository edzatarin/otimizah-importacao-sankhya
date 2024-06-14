import requests

class SankhyaLogin:
  def __init__(self, ):
    self.headers = {
        'token': "f7d833f5-3e89-4341-811a-682f0427e6a6",
        'appkey': "1a5aaf86-7e23-4704-97a5-c0e74da30d9d",
        'username': "edzatarin@gmail.com",
        'password': "PGJdE6.dLzNgW"
    }
  
  def get_bearer_token(self):
    try:
      url = 'https://api.sankhya.com.br/login'
      response = requests.post(url, headers=self.headers)
      response_json = response.json()
      response.close()
      return response_json['bearerToken']
    except Exception as ex:
      raise ex