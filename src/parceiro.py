import json

from base.database import Database
from base.entity import Entity

class SankhyaParceiro(Entity):
    def __init__(self):        
        super().__init__()
        self.base_url = 'https://api.sankhya.com.br/gateway/v1/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json'
        self.database = Database()
               
    def get_parceiro(self):
        try:            
            df = self.get()
            self.database.sql_query('')
        except Exception as ex:        
            raise ex
        
    def get_body(self):
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
                                "list": "CODEND, TIPO, NOMEEND"
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
        json_data_str = json.dumps(requestBodyJson)
        return json_data_str