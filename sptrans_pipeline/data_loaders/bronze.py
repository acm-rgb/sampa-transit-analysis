import requests
import os
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

BASE_URL = 'http://api.olhovivo.sptrans.com.br/v2.1'

@data_loader
def load_data(*args, **kwargs):
    API_KEY = os.environ.get('SPTRANS_API_KEY')
    session = requests.Session()
    
    auth_response = session.post(f'{BASE_URL}/Login/Autenticar?token={API_KEY}', timeout=10)
    if auth_response.text != 'true':
        raise Exception(f"Falha na autenticação: {auth_response.text}")
    
    response = session.get(f'{BASE_URL}/Posicao', timeout=10)
    if response.status_code != 200:
        raise Exception(f"Erro: {response.status_code}")
        
    data = response.json()
    data['extracted_at'] = datetime.utcnow().isoformat()
    
    print(f"Sucesso! {len(data.get('l', []))} linhas capturadas.")
    return data