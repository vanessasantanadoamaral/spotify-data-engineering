import os
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

load_dotenv()

def ingestao_bronze():
    dataset = "vatsalmavani/spotify-dataset"
    pasta_bronze = "bronze"
    os.makedirs(pasta_bronze, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print(f"Baixando dados do Spotify...")
    api.dataset_download_files(dataset, path=pasta_bronze, unzip=True)
    print(f"Arquivos na Bronze: {os.listdir(pasta_bronze)}")

if __name__ == "__main__":
    ingestao_bronze()