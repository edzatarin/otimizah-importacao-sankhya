import pandas as pd

class Pivot:
    def to_pivot(self, response_json):
        result = []
        metadata = response_json['responseBody']['entities']['metadata']['fields']['field']
        entities = response_json['responseBody']['entities']['entity']        
        for rowx, rowv in enumerate(entities):
            for colx, colv in enumerate(metadata):
                col_met = colv['name']
                col_ent = f'f{colx}'
                value = rowv[col_ent]['$'] if '$' in rowv[col_ent] else None
                new_obj = {
                    'row': rowx,
                    'column_entity': col_ent,
                    'column_metadata': col_met,
                    'value': value
                }
                result.append(new_obj)
                    
        df = pd.DataFrame(result)
        df_pivot = df.pivot(index='row', columns='column_metadata', values='value')
        return df_pivot
        
        
