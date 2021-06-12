# Future Works

Here are some possible next steps to improve the project:
* Implement a robust CI/CD pipeline to automate the stages of app development
* Increment the monitor module with different other performance reports in addition to data drift. Additionally, include other monitoring stats: RAM, CPU, network, etc.
* Improve the data versioning feature: change from MLFlow + config file to [DVC](https://pypi.org/project/dvc/) + MLFlow
* Create automated triggers to retrain the model based on the performance degration in production
* Add a parameter tuning module for models with more parameters than ElasticNet
* Increment the tests with pytest

