import os
import gdown
import zipfile
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            logger.info(f"Downloading data from {self.config.source_URL} into file {self.config.local_data_file}")
            gdown.download(url=self.config.source_URL, output=self.config.local_data_file, quiet=False, fuzzy=True)
            logger.info(f"Downloaded data from {self.config.source_URL} into file {self.config.local_data_file}")
        except Exception as e:
            raise e

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_dir
            target_folder = os.path.join(unzip_path, "kidney-ct-scan-image")

            # Remove target folder if it exists
            if os.path.exists(target_folder):
                import shutil
                shutil.rmtree(target_folder)

            os.makedirs(target_folder, exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(target_folder)

            # Optional cleanup of __MACOSX or .DS_Store files
            for root, dirs, files in os.walk(target_folder):
                for dir_name in dirs:
                    if dir_name == "__MACOSX":
                        import shutil
                        shutil.rmtree(os.path.join(root, dir_name))
                for file_name in files:
                    if file_name == ".DS_Store":
                        os.remove(os.path.join(root, file_name))

        except Exception as e:
            raise e

    def initiate_data_ingestion(self):
        self.download_file()
        self.extract_zip_file()