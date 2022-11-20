import pandas as pd

class JsonToParquetService(object):
    
    def __init__(self, parquet_path = '/tmp'):
        self.parquet_path = parquet_path
    
    
    def __data_frame(self, record):
       return pd.read_json(record)
    
    
    def __criar_data_frame_endereco(self, data_frame):
        enderecos = pd.DataFrame()
        
        for i, row in data_frame.iterrows():
            try:
                temp = pd.json_normalize(data_frame['endereços'].values[i])
                temp['parent_flag'] = row['flag_vingador']
                enderecos = enderecos.append(temp)
            except:
                pass

        del data_frame['endereços']

        merged_data = pd.merge(
            data_frame,
            enderecos, 
            left_on='flag_vingador', 
            right_on='parent_flag', 
            how='left')

        return merged_data


    def __criar_data_frame_telefones(self, data_frame):
        telefones = pd.DataFrame()

        for i, row in data_frame.iterrows():

            try:
                temp = pd.json_normalize(data_frame['telefones'].values[i])
                telefones=telefones.append(temp, ignore_index=True)
            except:
                pass

        telefones['comercial'] = telefones['comercial'].dropna()
        telefones['tipo'] = telefones['tipo'].fillna(telefones.keys()[2])
        telefones['numero'] = telefones['numero'].fillna(telefones['comercial'].loc[2])
        telefones['celular'] = telefones['celular'].fillna(telefones['celular'].loc[3])

        del telefones['comercial']

        telefones.drop_duplicates(inplace = True)

        data_frame_final=pd.merge(data_frame, telefones, on='tipo', how='inner')
        del data_frame_final['telefones']
        del data_frame_final['parent_flag']

        data_frame_final.drop_duplicates(inplace = True)
        return data_frame_final
    
    
    def criar_arquivo_parquet(self, record):
        data_frame = self.__data_frame(record)
        
        df_endereco = self.__criar_data_frame_endereco(data_frame)
        
        df_completo = self.__criar_data_frame_telefones(df_endereco)
        
        df_completo.to_parquet(f'{self.parquet_path}/out.parquet')
        
    
    def ler_arquivo_parquet(self):
        data = pd.read_parquet(f'{self.parquet_path}/out.parquet')
        return data
        