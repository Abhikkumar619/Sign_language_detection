import sys, os
from signLanguage.logger import log
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.entity.artifacts_entity import DataIngestionArtifacts


class TrainPipeline: 
    def __init__(self): 
        self. data_ingestion_config= DataIngestionConfig()
        
    def start_data_ingstion(self)->DataIngestionArtifacts:
        try: 
            log.info("Entered TrainPipeline class for Data Ingestion")
            
            data_ingestion=DataIngestion(Data_ingestion_config=self.data_ingestion_config)
            
            data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()
            
            log.info("Got data URL\n\n")
            log.info(f"Exist from TrainPipeline Class")
            
            return data_ingestion_artifacts
        
        except Exception as e:
            raise e
    def run_pipeline(self)-> None: 
        try: 
            data_ingestion_artifacts=self.start_data_ingstion()
        except Exception as e: 
            raise e        