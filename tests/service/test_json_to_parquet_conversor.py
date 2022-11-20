import pytest
import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from src.service.json_to_parquet_conversor import JsonToParquetService

json_conversor = JsonToParquetService()

def test_criar_arquivo_parquet():
    json_conversor.criar_arquivo_parquet('../../arquivo.json')
    
    assert os.path.exists('/tmp/out.parquet') == True
    
def test_ler_arquivo_parquet():
    data = json_conversor.ler_arquivo_parquet()
    
    assert not data.empty