# Preparation of the environment
* If you have Docker on the machine <br>
    Open the console in the project folder and run the following commands:
    ```
    docker build -t chsponciano/stock-learning-news-analyser .
    docker run --name news-analyser chsponciano/stock-learning-news-analyser python /service-news-analyser/__init__.py start
    ```
* If it is for development, follow the steps below:
    * Install [Python 3.8](https://www.python.org/downloads/)
    * Install the python dependency manager [Pip](https://pip.pypa.io/en/stable/installing/)
    * Install [Anaconda](https://anaconda.org/)
    * Install [Git](https://git-scm.com/download)
    * Clone the repository for the machine, executing the commands below:
    ```
    git clone https://github.com/stock-learning/stock-learning-news-analyser
    cd stock-learning-news-analyser
    ```
    * Create the .env file inside the folder with the following content:
    ```
    MONGO_HOST = *MONGODB_HOST*
    MONGO_PORT = *MONGODB_PORT*
    DATABASE = *MONGODB_DATABSE*
    ```
    * Create a new environment within anaconda and execute the following commands:
    ```
    activate *ENVIRONMENT_NAME*
    pip install -r requirements.txt
    ```
