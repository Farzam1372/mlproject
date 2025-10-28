import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformer_object(self):
        try:
           # df.columns = (
            #    df.columns
             #   .str.strip()                            # remove extra spaces
              #  .str.lower()                            # lowercase
               # .str.replace('[^a-z0-9]+', '_', regex=True)  # replace special chars with underscore
            #)
        
            numeric_features = ['writing_score', 'reading_score']
            categorical_features = [
                'gender', 'race_ethnicity', 
                'parental_level_of_education',
                'lunch', 'test_preparation_course'
            ]
            
        num_pipeline = Pipeline(
            steps = [
            ("imputer", SimpleImputer(strategy="median")),    
            ("scaler", StandardScaler())    
            
            ]
        )    
        except:
            pass
        