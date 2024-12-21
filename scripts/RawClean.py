import pathlib
import shutil
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm 
from .config import DEFAULT_FOLDER_NAME

class PathError(Exception):
    """Custom Exception for Path-related errors."""
    pass

class RawClear: 
    def __init__(self, path: str, extensions: list[str]=None):
        self.path = self.get_path(path)
        self.parent = self.path.parent 
        self.folder_name = self.path.name
        self.new_path = self.create_new_path()
        self.extensions = extensions or ['jpg']

    def get_path(self, path: str) -> pathlib.Path:
        path = pathlib.Path(path) 
        if not path.exists() or not path.is_dir():
            raise PathError(f"Invalid path: {path}")
        logging.info(f"Validated path: {path}")
        return path 
        
    def create_new_path(self) -> pathlib.Path: 
        new_path = self.path.parent / f"{self.folder_name}-{DEFAULT_FOLDER_NAME}"
        if not new_path.exists():
            new_path.mkdir(parents=True)
            logging.info(f"Created directory: {new_path}")
            return new_path 
        logging.warning(f"Directory already exists: {new_path}")
        return new_path

    def tsf_files(self) -> int:
        files_to_copy = list()
        for ext in self.extensions:
            files_to_copy.extend(self.path.glob(f"*.{ext}"))

        if not files_to_copy:
            logging.warning("No matching files found to transfer.")
            return 0
        
        logging.info(f"Transferring {len(files_to_copy)} files...")

        successful_transfer = 0 
        with ThreadPoolExecutor() as executer: 
            futures = [executer.submit(self.copy_file, file) for file in files_to_copy]
            for future in tqdm(futures, desc="Copying Files", unit="file"):
                if future.result():
                    successful_transfer += 1 
        
        logging.info(f"File transder completed: {successful_transfer}/{len(files_to_copy)} files copied.")
        return successful_transfer

    def copy_file(self, file: pathlib.Path) -> bool:
        target_path = self.new_path / file.name
        try: 
            shutil.copy(file, target_path)
            logging.info(f"Copied {file} to {target_path}")
            return True
        except Exception as e: 
            logging.error(f"Failed to copy {file}: {e}")
            return False
    
    def get_summary(self) -> dict: 
        return {
            "source_path": str(self.path),
            "parent_path": str(self.parent),
            "folder_name": self.folder_name,
            "destination_path": str(self.new_path),
            "extensions": self.extensions
        }
