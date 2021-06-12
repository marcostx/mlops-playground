from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import sys 

from src.model.datasets import *
import src.model.datasets.preprocessors as prep
from src.model.configs import configs

model_pipeline = Pipeline(
    [
        (
            "categorical_imputer",
            prep.CategoricalImputer(variables=configs.CATEGORICAL_VARS_WITH_NA),
        ),
        (
            "numerical_inputer",
            prep.NumericalImputer(variables=configs.NUMERICAL_VARS_WITH_NA),
        ),
        (
            "temporal_variable",
            prep.TemporalVariableEstimator(
                variables=configs.TEMPORAL_VARS, reference_variable=configs.DROP_FEATURES
            ),
        ),
        (
            "categorical_encoder",
            prep.CategoricalEncoder(variables=configs.CATEGORICAL_VARS),
        ),
        ("log_transformer", prep.LogTransformer(variables=configs.NUMERICALS_LOG_VARS)),
        ( "drop_features", prep.DropUnecessaryFeatures(variables_to_drop=configs.DROP_FEATURES)),
        ("scaler", MinMaxScaler()),
        ("model", ElasticNet(configs.ALPHA, configs.L1_RATIO, random_state=0)),
    ]
)

