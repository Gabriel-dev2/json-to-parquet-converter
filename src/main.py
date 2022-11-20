from service.json_to_parquet_conversor import JsonToParquetService

if  __name__ == '__main__':
    jps = JsonToParquetService()
    
    jps.criar_arquivo_parquet('../arquivo.json')
    
    data = jps.ler_arquivo_parquet()
    
    print(data)