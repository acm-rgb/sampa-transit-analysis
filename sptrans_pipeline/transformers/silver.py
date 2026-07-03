import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(data, *args, **kwargs):
    records = []
    extracted_at = data.get('extracted_at')
    hr_api = data.get('hr')
    
    for linha in data.get('l', []):
        for veiculo in linha.get('vs', []):
            records.append({
                'letreiro': linha.get('c'),
                'codigo_linha': linha.get('cl'),
                'sentido': linha.get('sl'),
                'prefixo_veiculo': veiculo.get('p'),
                'acessivel': veiculo.get('a'),
                'latitude': veiculo.get('py'),
                'longitude': veiculo.get('px'),
                'horario_atualizacao_gps': veiculo.get('ta'),
                'horario_api': hr_api,
                'extracted_at': extracted_at
            })
            
    df = pd.DataFrame(records)
    print(f"Transformados {len(df)} registros de veículos individuais.")
    return df