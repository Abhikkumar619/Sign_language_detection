import os, sys
import shutil
from signLanguage.logger import log
from signLanguage.entity.config_entity import DataValidationConfig
from signLanguage.entity.artifacts_entity import (DataIngestionArtifacts,
                                                  DataValidationArtifacts)



class DataValidation:
    def __init__(self, dataingestion_artifact: DataIngestionArtifacts,
                 datavalidation_config: DataValidationConfig) -> None:
        
    
        try: 
            self.data_ingestion_artifact=dataingestion_artifact
            self.data_validation_config=datavalidation_config
        except Exception as e:
           raise e
            
    def validate_all_file(self)-> bool: 
        try: 
            validation_status=None
            all_files=os.listdir(self.data_ingestion_artifact.feature_store_path)
            
            for file in all_files: 
                if file not in self.data_validation_config.resuired_file_list: 
                    validation_status=False
                    
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation state : {validation_status}")
                else: 
                    validation_status=True
                    
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f: 
                        f.write(f"validation state: {validation_status}")
            
            return validation_status
        
        except Exception as e: 
            raise e
    def initate_data_validation(self): 
        
        try: 
            status=self.validate_all_file()
            log.info(f"From initate data validation validation status : {status}")
            data_validation_artifact=DataValidationArtifacts(validation_status=status)
            
            if status: 
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
              
            return data_validation_artifact  
            
            
        except Exception as e: 
            raise e