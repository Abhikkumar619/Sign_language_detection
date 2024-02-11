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
    
    

    