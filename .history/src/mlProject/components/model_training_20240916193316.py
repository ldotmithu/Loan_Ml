from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class ModelTraining:
    def __init__(self,config:ModelTrainingConfig) -> None:
        self.config=config
        
    def preprocess_method(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        target_col='Loan_Status'
        
        X_train=train_data.drop(columns=[target_col])
        X_test=test_data.drop(columns=target_col)
        y_train=train_data[target_col]
        y_test=test_data[target_col]
        
        num_col=['ApplicantIncome', 'LoanAmount']
        cat_col=['Gender', 'Married', 'Education', 'Property_Area']
        
        num_pipeline=Pipeline([
            ('scaler',StandardScaler())
        ])

        cat_pipeline=Pipeline([
            ('ordinal',OrdinalEncoder())
        ])

        preprocess=ColumnTransformer([
            ('num_pipeline',num_pipeline,num_col),
            ('cat_pipeline',cat_pipeline,cat_col)
])
        
        
        
        
           