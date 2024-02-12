import sys, os
from signLanguage.logger import log
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.entity.config_entity import (DataIngestionConfig, 
                                               DataValidationConfig, 
                                               ModelTainerConfig)

from signLanguage.entity.artifacts_entity import (DataIngestionArtifacts,
                                                  DataValidationArtifacts,
                                                  ModelTrainerArtifacts)

from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer



class TrainPipeline: 
    def __init__(self): 
        self. data_ingestion_config= DataIngestionConfig()
        self. data_validation_config=DataValidationConfig()
        self. model_trainer_config=ModelTainerConfig()
        
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

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifacts)-> DataValidationArtifacts: 
        try: 
            log.info("Entered In Data Vlidation Pipeline")
            
            data_validation=DataValidation(dataingestion_artifact=data_ingestion_artifact, 
                                                    datavalidation_config=self.data_validation_config)
            data_validation_artifact=data_validation.initate_data_validation()
            
            log.info("Perfomed the data validation operation")
            
            log.info("Exited from data validation")
            
            return data_validation_artifact
        
            
        except Exception as e: 
            raise e
        
    def start_model_trainer(self):
        model_train=ModelTrainer(model_trainer_config=self.model_trainer_config) 
        model_train.initate_data_model_trainer()
        
        
         
         
    def run_pipeline(self)-> None: 
        try: 
            data_ingestion_artifacts=self.start_data_ingstion()
            log.info(f"Data Ingestion artifacts: {data_ingestion_artifacts}")
            
            data_validation_artifacts=self.start_data_validation(data_ingestion_artifacts)
            
            self.start_model_trainer()
            
        except Exception as e: 
            raise e      
        