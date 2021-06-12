from src.model.configs import configs

import pandas as pd


def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for unprocessable values."""

    num_na_not_allowed = [
        feature
        for feature in configs.FEATURES if feature not in configs.CATEGORICAL_VARS + configs.NUMERICAL_VARS_WITH_NA
    ]

    cat_na_not_allowed = [
        feature for feature in configs.CATEGORICAL_VARS if feature not in configs.CATEGORICAL_VARS_WITH_NA
    ]

    validated_data = input_data.copy()

    # check for numerical variables with NA not seen during training
    if input_data[num_na_not_allowed].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=num_na_not_allowed
        )

    # check for categorical variables with NA not seen during training
    if input_data[cat_na_not_allowed].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=cat_na_not_allowed
        )

    return validated_data
