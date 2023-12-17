#!/bin/bash

#criando da pasta com o ambiente virtual
python3 -m venv .venv

#iniciando o ambiente virtual
source .venv/bin/activate

#Instalando dependências no ambiente
pip install reportlab