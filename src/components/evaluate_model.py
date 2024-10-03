import os
import sys
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.utils.utils import load_object
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from src.logger import logging
from src.exception import customexception
from dataclasses import dataclass

@dataclass
class EvaluationModelconfig:
    pass

class EvaluationModel:
    def __init__(self):
        pass
   
   
    def initiate_evaluate_model(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)