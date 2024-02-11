from signLanguage.logger import log
from signLanguage.entity.artifacts_entity import  DataIngestionArtifacts
from signLanguage.entity.config_entity import DataIngestionConfig
import os
import gdown
import zipfile
import sys

class DataIngestion:
    def __init__(self, Data_ingestion_config:DataIngestionConfig=DataIngestionConfig):
        
        try:  
            self.config=Data_ingestion_config  
        except Exception as e: 
            raise e
        
    def download_url(self): 
        """
        Fetch data
        """
        try: 
            data_url=self.config.data_download_url
            zip_download_dir=self.config.data_ingestion_dir
            
            os.makedirs(zip_download_dir, exist_ok=True)
            
            dataFail_name="data.zip"
            zip_file_path=os.path.join(zip_download_dir, dataFail_name)
            
            log.info(f"Directories is created for data: {zip_file_path}")
            
            
            file_id=data_url.split('/')[-2]
            prefix='https://drive.google.com/uc?id='+file_id
            gdown.download(prefix, zip_file_path)
            
            log.info(f"Download Data from: {file_id} into file {zip_file_path}")
            
            return zip_file_path
                
        except Exception as e: 
            raise e
        
    def Extract_zip_file(self, zip_file_path: str)->str: 
        try: 
            features_store_file=self.config.feature_store_dir
            os.makedirs(features_store_file, exist_ok=True)
            
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref: 
                zip_ref.extractall(features_store_file)
                
            log.info(f"From zip file extract all file {features_store_file}")
            
            return features_store_file
        except Exception as e: 
            raise e
        
    def initiate_data_ingestion(self)-> DataIngestionArtifacts: 
        log.info(f"Initiate Data InGestion from DataIngestion Class\n\n")
        try: 
            zip_file_path=self.download_url()
            extract_file_path=self.Extract_zip_file(zip_file_path)
            
            data_ingestion_artifact=DataIngestionArtifacts(data_zip_file_path=zip_file_path,
                                   feature_store_path=extract_file_path)
              
              
            log.info(f"Data Ingestion is Completed.\n\n")
            log.info(f"Data Ingestion artifacts are: {data_ingestion_artifact}")
            
            return data_ingestion_artifact

        except Exception as e:
            raise e
        
        
        