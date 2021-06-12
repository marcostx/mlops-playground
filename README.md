# Machine Learning Train/Serve Pipeline - ML Engineer Case

### Deliverables

There are two goals for this exercise. The first one is to create an automated ML model training process.

The second one is to create a Rest API documented with Swagger that serves a ML model predictions.

### Data Description
Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges the competitors to predict the final price of each home. It is your job to predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable. 

The full data description is available in datasets/data_description.txt. These descriptions were extracted from [kaggle webpage](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview)

### Usage

The first thing is to build the container:

```
make build
```

Then the training step is triggered by running:

```
make run-train
```
Once trained the model is then served using the Flask API

```
make run-serve
```

Optionally, run these two previous steps together using the following command:

```
make run-pipeline
```

The documentation is available at:
```
http://localhost:5000/apidocs
```

Once the server started, the predictions are obtained in the following URL

```
http://localhost:5000/predict/regression
```

The inputs for prediction follow the following format :

```json
[
    {
        "Id":1461,
        "MSSubClass":20,
        "MSZoning":"RH",
        "LotFrontage":80.0,
        "LotArea":11622,
        "Street":"Pave",
        "Alley":null,
        "LotShape":"Reg",
        "LandContour":"Lvl",
        "Utilities":"AllPub",
        "LotConfig":"Inside",
        "LandSlope":"Gtl",
        "Neighborhood":"NAmes",
        "Condition1":"Feedr",
        "Condition2":"Norm",
        "BldgType":"1Fam",
        "HouseStyle":"1Story",
        "OverallQual":5,
        "OverallCond":6,
        "YearBuilt":1961,
        "YearRemodAdd":1961,
        "RoofStyle":"Gable",
        "RoofMatl":"CompShg",
        "Exterior1st":"VinylSd",
        "Exterior2nd":"VinylSd",
        "MasVnrType":"None",
        "MasVnrArea":0.0,
        "ExterQual":"TA",
        "ExterCond":"TA",
        "Foundation":"CBlock",
        "BsmtQual":"TA",
        "BsmtCond":"TA",
        "BsmtExposure":"No",
        "BsmtFinType1":"Rec",
        "BsmtFinSF1":468.0,
        "BsmtFinType2":"LwQ",
        "BsmtFinSF2":144.0,
        "BsmtUnfSF":270.0,
        "TotalBsmtSF":882.0,
        "Heating":"GasA",
        "HeatingQC":"TA",
        "CentralAir":"Y",
        "Electrical":"SBrkr",
        "1stFlrSF":896,
        "2ndFlrSF":0,
        "LowQualFinSF":0,
        "GrLivArea":896,
        "BsmtFullBath":0.0,
        "BsmtHalfBath":0.0,
        "FullBath":1,
        "HalfBath":0,
        "BedroomAbvGr":2,
        "KitchenAbvGr":1,
        "KitchenQual":"TA",
        "TotRmsAbvGrd":5,
        "Functional":"Typ",
        "Fireplaces":0,
        "FireplaceQu":null,
        "GarageType":"Attchd",
        "GarageYrBlt":1961.0,
        "GarageFinish":"Unf",
        "GarageCars":1.0,
        "GarageArea":730.0,
        "GarageQual":"TA",
        "GarageCond":"TA",
        "PavedDrive":"Y",
        "WoodDeckSF":140,
        "OpenPorchSF":0,
        "EnclosedPorch":0,
        "3SsnPorch":0,
        "ScreenPorch":120,
        "PoolArea":0,
        "PoolQC":null,
        "Fence":"MnPrv",
        "MiscFeature":null,
        "MiscVal":0,
        "MoSold":6,
        "YrSold":2010,
        "SaleType":"WD",
        "SaleCondition":"Normal"
    }
]
```

Additionally, is also possible to test the api using pytest, running the following command:

```
make run-tests
```
