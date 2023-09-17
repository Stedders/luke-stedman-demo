# Luke Stedman's Python Portfolio


## Python Knowledge

Demonstration of Python knowledge.

1. This repo and project structure demonstrates my best practice for setting up Python projects using poetry
2. You will find a module called [one](stedders/one/__init__.py), this module uses some complex (and slightly naughty)
   techniques to create an importable module that is actually a number
   * To play with this I would recommend using the [python REPL](https://realpython.com/python-repl/#running-the-python-command)
   * Once installed you can import the package using `from stedders import one`
   * You can then use the module as an int `one + 6` and see what happens!
3. You will also find [tests](tests/test_one.py) for the `one` module
   * Again, this uses some advanced techniques to prevent artifacts being left behind by tests
   * Once installed you can run the tests by executing the command `pytest`
   * This will also produce [test coverage reports](reports)
4. The project structure also demonstrates how to separate code depending on use cases
   * The project contains dashboards (next section) and a module
   * By default, only the `one` module is installed when using `poetry install`
   * Building the package `poetry build` will install the dependencies for and build the `one` module
   * The dashboards are in a separate namespace in the package and it's dependencies are installed with `poetry install --with dashboard`

### Installation

This repo uses [poetry](https://python-poetry.org/), my preferred python package manager.

To install the module and tests, run the following command

```shell
poetry install --with dev
```

## Data Science/Engineering

Demonstration of Data Science/Engineering knowledge. I have tried to use several packages to demonstrate my skills - 
numpy, pandas, polars, plotly and streamlit.

1. Uses streamlit to host a couple of dashboards
2. A simple [YFinance Dashboard](stedders/dashboard/pages/1_yfinance_dashboard.py) to look-up NASDAQ stock prices
   * Simple to extend to other exchanges if needed
3. A [random walk dashboard](stedders/dashboard/pages/2_random_walk.py) that implements an efficient algorithm using 
numpy and polars to generate a random, but deterministic, data set
   * The data set contains 1-minute prices between 09:30 and 16:30 every week day
   * Useful for testing of data processing algorithms
4. The code can be run locally or as a container (see below for installation/running instructions)
   * The [Dockerfile](Dockerfile) uses a multi-image build process to optimise the build process

### Local

#### Installation

```shell
poetry install --with dashboard
```

#### Running

```shell
 streamlit run .\stedders\dashboard\Home.py
```

You can then access the dashboards at (http://127.0.0.1:8501)

### Container

#### Building

```shell
docker build . -t luke-stedman-demo
```

#### Running

```shell
docker run -p 8501:8501 luke-stedman-demo
```

You can then access the dashboards at (http://127.0.0.1:8501)

## AWS

Finally, I pulled the above together and deployed it to AWS to demonstrate my knowledge/skills of cloud systems.

1. My AWS account only had AWS Glacier setup, this was all done from scratch
2. All code was managed via CodeCommit and built using CodeBuild and CodePipeline
   * I didn't save the package to CodeArtifact, though could have
3. The Docker container was saved in ECR and deployed to ECS
4. During the process I had to setup several IAM roles and am storing the logs in CloudWatch

### Deployed Dashboard

You can access the dashboard on AWS at http://44.204.243.147:8501/