import sys 
import os 
import pathlib


class RawClear:
    def __init__(self):
        self.path = self.get_path()
        self.parent = self.get_parent_path()
        self.folder_name = self.get_folder_name()
        self.new_path = self.create_new_path()

    def get_path(self):
        path = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path("null")
        if not path.exists():
            path = self.prompt_path()
            if not path.exists():
                print("Invalid path")
                sys.exit(1)
        return path

    def prompt_path(self):
        path = input("Enter path to photos: ")
        path = pathlib.Path(path) if os.path.exists(path) else pathlib.Path("Null")
        return path 
    
    def get_parent_path(self):
        if self.path.exists():
            parent = self.path.parent.absolute()
            return parent

    def get_folder_name(self):
        if self.path.exists() and self.path.is_dir():
            return self.path.name
        return "null"

    def create_new_path(self):
        name = f"{self.folder_name}-raw-clear"
        parts = list(self.path.parts)
        parts[-1] = name
        # This part will need to redo to handle error for fileExist or fileNotFound 
        try:
            new_path = pathlib.Path(*parts).mkdir()
            return new_path
        except Exception as e: 
            print(e)
            return pathlib.Path("Null")
    
        
    def get_var(self):
        print(self.path)
        print(self.parent)
        print(self.folder_name)
        print(self.new_path)
            

if __name__ == '__main__':
    raw_clear = RawClear()
    raw_clear.get_var()


