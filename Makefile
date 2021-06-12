NAME=test
GPU=false
GPU_DOCKER_IMAGE=marcos/ml-docker
PYTHON_COMMAND=python
PYTEST_COMMAND=pytest
HOST_CPU_SOURCE_PATH=$(shell pwd)/ml_app/
IMAGE_SOURCE_PATH=/app/ml_app/

HOST_CPU_DATASETS_PATH=$(shell pwd)/ml_app/data/
HOST_CPU_MODELS_PATH=$(shell pwd)/ml_app/models/
HOST_CPU_REPORTS_PATH=$(shell pwd)/ml_app/reports/
IMAGE_DATASETS_PATH=/app/ml_app/data/
IMAGE_REPORTS_PATH=/app/ml_app/reports/
IMAGE_MODELS_PATH=/app/ml_app/models/

CPU_DOCKER_VOLUMES = --volume=$(HOST_CPU_SOURCE_PATH):$(IMAGE_SOURCE_PATH) \
				     --volume=$(HOST_CPU_REPORTS_PATH):$(IMAGE_REPORTS_PATH) \
					 --volume=$(HOST_CPU_MODELS_PATH):$(IMAGE_MODELS_PATH) \
				     --workdir=$(IMAGE_SOURCE_PATH) \
				     --shm-size 8G

train_pipeline tr:
	@$(PYTHON_COMMAND) train_main.py

build:
	docker build -t $(GPU_DOCKER_IMAGE) -f Dockerfile .

run-train:
	docker run -it $(CPU_DOCKER_VOLUMES) $(GPU_DOCKER_IMAGE) bash -c "$(PYTHON_COMMAND) src/model/train.py";

run-serve:
	docker run -it -p 5000:5000 $(CPU_DOCKER_VOLUMES) $(GPU_DOCKER_IMAGE) bash -c "$(PYTHON_COMMAND) src/api/run.py";

run-pipeline: 
	docker run -it -p 5000:5000 $(CPU_DOCKER_VOLUMES) $(GPU_DOCKER_IMAGE) bash -c "$(PYTHON_COMMAND) src/model/train.py && $(PYTHON_COMMAND) src/api/run.py";

run-tests: 
	docker run -it -p 5000:5000 $(CPU_DOCKER_VOLUMES) $(GPU_DOCKER_IMAGE) bash -c "$(PYTEST_COMMAND) src/api/tests";