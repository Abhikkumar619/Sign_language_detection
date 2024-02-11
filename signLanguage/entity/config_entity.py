from signLanguage.constant.training_pipeline import *
from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class TrainingPipelineConfig: 
    artifacts_dir: str = ARTIFACTS_DIR
    
traing_pipeline_config: TrainingPipelineConfig=TrainingPipelineConfig()


@dataclass(frozen=True)
class DataIngestionConfig: 
    data_ingestion_dir: str=os.path.join(
        traing_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )
    
    feature_store_dir: str=os.path.join(traing_pipeline_config.artifacts_dir, DATA_INGESTION_FEATURE_STORE_DIR)
    
    data_download_url: str=DATA_DOWNLOAD_URL
    
@dataclass(frozen=True)
class DataValidationConfig: 
    data_validation_dir: str=os.path.join(
        traing_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
        
    )
    valid_status_file_dir=os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
    
    resuired_file_list=DATA_VALIDATION_ALL_REQUIRED_FILES
    
    
    
    

    