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
                'latitude': float(veiculo.get('py', 0)),
                'longitude': float(veiculo.get('px', 0)),
                'horario_atualizacao_gps': veiculo.get('ta'),
                'horario_api': hr_api,
                'extracted_at': extracted_at
            })
            
    df = pd.DataFrame(records)
    
    # Remove GPS falho (0,0)
    df = df[(df['latitude'] != 0.0) & (df['longitude'] != 0.0)]
    
    # Cria coluna apenas com a data (YYYY-MM-DD) para particionamento
    df['data_extracao'] = pd.to_datetime(df['extracted_at']).dt.date.astype(str)
    
    return df