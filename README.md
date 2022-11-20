# Json to Parquet Python Script

## Overview

- Este é um repositorio de um script python que realiza a conversão de um arquivo Json (nested)
para um arquivo .parquet(flat)

## Pré-requisitos
- Python 3.10 
- (Opcional) pipenv

## Instruções para executar o script
**Para executar esse script é necessário a instalação de algumas dependências:**

### (Opção 1) Para executar o script diretamente utilizando o python primeiro deve-se instalar a lib pandas (necessário ter o pip instalado)
- Caso não tenha o pip seguir tutorial do link abaixo
    [pip doc](https://pip.pypa.io/en/stable/installation/)

**Para instalar o pandas executar o comando abaixo:**
        
        pip install pandas

**Após instalação o projeto poderá ser executado com o comando abaixo (terminal) dentro do diretório src:**

        python3 main.py

### (Opção 2) Para executar o script utilizando um virtualenv primeiro deve-se o pipenv


**Para instalar o pandas executar o comando abaixo:**
        
        pip install pipenv

**Para executar a instalação das dependências que estão no Pipfile pode-se usar o comando**

        pipenv install --dev

**E para executar o script via pipenv basta usar o comando dentro do diretório src:**

        pipenv run python main.py

### (Opção 3) Para executar o script utilizando docker:


**Fazer build do Dockerfile:**
        
        docker build -t "json_to_parquet:Dockerfile" . 

**Executar a imagem docker criada:**

        docker run json_to_parquet:Dockerfile


## Execução de testes unitários

**Para a execução dos testes unitários é necessário a instalação da lib pytest**

        pip install pytest

**Para executar os testes basta digitar o seguinte comando no terminal (dentro do diretório root do projeto)**
        
        pytest

## Authors

* **Gabriel Lucas** - *Initial work* - [Gabriel](mailto:gabriel23costalima@outlook.com)