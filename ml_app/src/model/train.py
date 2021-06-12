import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from src.model.datasets.datasets import *
from src.model.configs import configs
import pipeline
import mlflow
import mlflow.sklearn

mlflow.set_experiment("train")

def eval_metrics(target: np.array, predictions: np.array) -> float:
    output = np.exp(predictions)

    rmse = mean_squared_error(target, output)
    return rmse

def run_training() -> None:
    """Train the model."""

    with mlflow.start_run():
        # read training data
        data = load_dataset(file_name=configs.TRAINING_DATA_FILE)

        # logging data artifacts
        mlflow.log_param('data_path', configs.TRAINING_DATA_FILE)
        mlflow.log_param('data_version', configs.TRAIN_DATA_VERSION)
        mlflow.log_param('input_rows', data.shape[0])
        mlflow.log_param('input_cols', data.shape[1])

        # divide train and test
        X_train, X_test, y_train, y_test = train_test_split(
            data[configs.FEATURES], data[configs.TARGET], test_size=0.1, random_state=0
        )  # we are setting the seed here

        # logging the columns used for training
        columns_x = pd.DataFrame(list(X_train.columns))
        columns_y = pd.DataFrame(list(y_train.name))
        columns_x.to_csv(configs.TRAIN_X_COLUMNS, header=False, index=False)
        columns_y.to_csv(configs.TRAIN_Y_COLUMNS, header=False, index=False)
        mlflow.log_artifact(configs.TRAIN_X_COLUMNS)
        mlflow.log_artifact(configs.TRAIN_Y_COLUMNS)

        # transform the target
        y_train = np.log(y_train)

        pipeline.model_pipeline.fit(X_train[configs.FEATURES], y_train)

        predictions = pipeline.model_pipeline.predict(X_test)

        rmse = eval_metrics(y_test, predictions)

        mlflow.log_metric("rmse", rmse)
        mlflow.sklearn.log_model(rmse, "model")

        save_pipeline(pipeline_to_persist=pipeline.model_pipeline)

    mlflow.end_run()

if __name__ == "__main__":
    run_training()