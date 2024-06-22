import json
import requests

from login import SankhyaLogin

class SankhyaParceiro:
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

        
        serviceName = "CRUDServiceProvider.loadRecords"
        baseUrl = "https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json "
        #baseUrl = f"{baseUrl}?serviceName={serviceName}&outputType=json&requestBody={''}"
                
        sankhyaLogin = SankhyaLogin()
        bearer_token = sankhyaLogin.get_bearer_token()
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        
        #headers = { Authorization: 'Bearer ' + this.securityUtil.token };
        
        args = {
             #'serviceName': serviceName,
             #'outputType': 'json',
             "requestBody": requestBodyJson
        }
                
        
        #response = requests.post(baseUrl, params=args, headers=headers, timeout=300)
        #response_json = response.json()
        #response.close()
        
        urlx = "https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json"
        jsonx =  {
            "serviceName": "CRUDServiceProvider.loadRecords",
            "requestBody": {
                "dataSet": {
                    "rootEntity": "Banco",
                    "includePresentationFields": "N",
                    "offsetPage": "0",
                    "criteria": {
                        "expression": {
                            "$": "this.ABREVIATURA = ?"
                        },
                        "parameters": [
                            {
                                "$": "BB",
                                "type": "S"
                            }
                        ]
                    },
                    "entity": {
                        "fieldset": {
                            "list":"CODBCO,ABREVIATURA,NOMEBCO"
                        }
                    }
                }
            }
        }
        
        response = requests.post(urlx, params=jsonx, headers=headers, timeout=300)
        response_json = response.json()
        print(response_json)
        response.close()
        
        
    except Exception as ex:        
        raise ex