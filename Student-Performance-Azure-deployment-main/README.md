## End to End MAchine Learning Project

1. open anaconda prompt type following command: cd <path of folder> & press enter
2. type following command: code . & vs open
3. type following command: conda create -p venv python==3.8 -y
3.1. type following command: conda activate venv/
4. create a file README.md
5. create a file requirements.txt
6. create a file setup.py
7. create a file .gitignore
8. now open terminal{cmd} and type following command: pip install -r requirement.txt

9. create a folder src 
9.1. create a file inside src folder i.e. __init__.py
9.2. create a folder inside a src folder i.e. componenets
    9.2.1 create a file inside a components folder i.e. __init__.py
    9.2.2 create a file inside a components folder i.e. data_ingestion.py
    9.2.3 create a file inside a components folder i.e. data_transformation.py
    9.2.4 create a file inside a components folder i.e. model_trainer.py
9.3. create a folder inside a src folder i.e. pipeline
    9.3.1 create a file inside a pipline folder i.e. train_pipeline.py
    9.3.2 create a file inside a pipline folder i.e. predict_pipeline.py
    9.3.3 create a file inside a pipline folder i.e. __init__.py
9.4 create a file inside src folder i.e. logger.py
9.5 create a file inside src folder i.e. exception.py
9.6 create a file inside src folder i.e. utlis.py

10. run the following command : python src/logger.py
11. run the following command : python src/exception.py
12. Create a folder i.e. notebook
12.1. create a folder inside a notebook folder i.e. Data
13. create template folder
