import os
from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi

load_dotenv()

def ingestao_raw():
    dataset = "vatsalmavani/spotify-dataset"
    pasta_bronze = "raw"
    os.makedirs(pasta_raw, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print(f"Baixando dados do Spotify...")
    api.dataset_download_files(dataset, path=pasta_raw, unzip=True)
    print(f"Arquivos raw: {os.listdir(pasta_raw)}")

if __name__ == "__main__":
    ingestao_raw()