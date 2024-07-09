import requests
from base.login import SankhyaLogin
from base.pivot import Pivot
from abc import ABC, abstractmethod

class Entity:
    def __init__(self):
        self.base_url = ''
        self.setup_login()
    
    def setup_login(self):
        login = SankhyaLogin()
        bearer_token = login.get_bearer_token()
        self.headers = {
            "Authorization": f"Bearer {bearer_token.strip()}",
            "Content-Type": "application/json"
        }
    
    def get(self):
        try:
            requestBodyJson = self.get_body()
            response = requests.get(self.base_url, headers=self.headers, data=requestBodyJson, timeout=300)
            response_json = response.json()
            response.close()
            
            pivot = Pivot()            
            df = pivot.to_pivot(response_json)
            
            filename = requestBodyJson['requestBody']['dataSet']['rootEntity'] if requestBodyJson and 'rootEntity' in requestBodyJson['requestBody']['dataSet']['rootEntity'] else ''
            if filename:
                df.to_csv(f'src/csv/{filename}.csv', index=False)
            
            return df
            
        except Exception as ex:
            raise ex
    
    @abstractmethod
    def get_body(self):
        pass