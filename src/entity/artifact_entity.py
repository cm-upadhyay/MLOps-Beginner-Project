from dataclasses import dataclass

# Data Ingestion Outputs
@dataclass
class DataIngestionArtifact:
    trained_file_path: str  
    test_file_path: str     

# Data Validation Results
@dataclass
class DataValidationArtifact:
    validation_status: bool  # True if validation passed
    message: str            # Validation summary message
    validation_report_file_path: str  

# Data Transformation Outputs
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str  # Path to preprocessing pipeline
    transformed_train_file_path: str  
    transformed_test_file_path: str   

# Model Performance Metrics
@dataclass
class ClassificationMetricArtifact:
    f1_score: float        
    precision_score: float 
    recall_score: float   

# Model Training Outputs
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str  # Path to saved model
    metric_artifact: ClassificationMetricArtifact  # Model metrics

# Model Evaluation Results
@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool  # True if new model is better
    changed_accuracy: float  # Accuracy difference vs current model
    s3_model_path: str       # Model path in S3
    trained_model_path: str  # Local model path

# Model Deployment Info
@dataclass
class ModelPusherArtifact:
    bucket_name: str   # S3 bucket name
    s3_model_path: str 