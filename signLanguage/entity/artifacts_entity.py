from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionArtifacts: 
    data_zip_file_path: str
    feature_store_path: str
    
    
    
@dataclass(frozen=True)
class DataValidationArtifacts: 
    validation_status: bool
