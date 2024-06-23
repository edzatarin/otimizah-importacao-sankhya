import json
import requests

from login import SankhyaLogin

class SankhyaParceiro:
    def __init__(self):
        sankhyaLogin = SankhyaLogin()
        bearer_token = sankhyaLogin.get_bearer_token()
        self.headers = {
            "Authorization": f"Bearer {bearer_token.strip()}",
            "Content-Type": "application/json"
        }
    
    def get_parceiro(self):
        try:
            requestBodyJson = {
                "serviceName": "CRUDServiceProvider.loadRecords",
                "requestBody": {
                    "dataSet": {
                        "rootEntity": "Parceiro",
                        "includePresentationFields": "N",
                        "tryJoinedFields": "true",
                        "parallelLoader": "true",
                        "offsetPage": "0",
                        "criteria": {
                            "expression": {
                            "$": "CLIENTE = ?"
                            },
                            "parameter": [
                                {
                                    "$": "S",
                                    "type": "S"
                                }
                            ]
                        },
                        "entity": [
                            {
                                "path": "",
                                "fieldset": {
                                    "list": "CODPARC, NOMEPARC, NUMEND, COMPLEMENTO, CEP"
                                }
                            },
                            {
                                "path": "Endereco",
                                "fieldset": {
                                    "list":"CODEND, TIPO, NOMEEND"
                                }
                            },
                            {
                                "path": "Bairro",
                                "fieldset": {
                                    "list": "CODBAI, NOMEBAI"
                                }
                            },
                            {
                                "path": "Cidade",
                                "fieldset": {
                                    "list": "CODCID, NOMECID, UF"
                                }
                            }
                        ]
                    }
                }
            }

            baseUrl = "https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json"
                            
            json_data_str = json.dumps(requestBodyJson)

            response = requests.get(baseUrl, headers=self.headers, data=json_data_str, timeout=300)
            response_json = response.json()
            response.close()
            
            print(response_json)
            
        except Exception as ex:        
            raise ex