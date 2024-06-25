import sys 
import os 
import pathlib
import shutil


class RawClear:
    def __init__(self):
        """
        Initialise the RawClear class
        """
        self.path = self.get_path() # Get the path to the target directory 
        self.parent = self.get_parent_path() # Get the parent path of the target directory
        self.folder_name = self.get_folder_name() # Get the name of the target directory 
        self.new_path = self.create_new_path() # Create a new directory with a modified name

    def get_path(self):
        """
        Get the path to the directory provided as a comamnd-line argument or prompt the user.
        :return pathlib.Path: The validated path to the target directory.
        """
        # Check if the path is provided as a command-line argument 
        path = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path("null")

        # If the provided path does not exist, prompt the user for a valid path
        if not path.exists():
            path = self.prompt_path()
            if not path.exists():
                print("Invalid path")
                sys.exit(1)
        return path

    def prompt_path(self):
        """
        Prompt the user to enter a path to the photos directory.
        :returns pathlib.Path: The user-provided path.
        """
        path = input("Enter path to photos: ")
        path = pathlib.Path(path) if os.path.exists(path) else pathlib.Path("Null")
        return path 
    
    def get_parent_path(self):
        """
        Get the parent directory of the target path.
        :return pathlib.Path: The parent directory path.
        """
        if self.path.exists():
            parent = self.path.parent.absolute()
            return parent

    def get_folder_name(self):
        """
        Get the name of the target directory.
        :return str: the name of the directory or "null" if the path is invalid.
        """
        if self.path.exists() and self.path.is_dir():
            return self.path.name
        return "null"

    def create_new_path(self):
        """
        Create a new directory with the name "{original_name}-raw-clear"
        :return: pathlib.Path: the path to the new directory or "Null if an error occurs.
        """
        name = f"{self.folder_name}-raw-clear"
        parts = list(self.path.parts)
        parts[-1] = name
        try:
            # attempt to create a new directory if exist else set self.new_path as new path
            new_path = pathlib.Path(*parts)
            if new_path.exists():
                return new_path
            else:
                pathlib.Path(*parts).mkdir()
                return new_path
        except Exception as e: 
            # Handles any errors that occur during directory creation
            print(e)
            return pathlib.Path("Null")
    
    
    def tsf_jpg(self):
        """
        Transfer JPG files from target directory to the new directory specified
        """
        jpg_photos = [p.name for p in self.path.glob("*.jpg")]
        
        for photo in jpg_photos:
            # get full path of file from target directory
            ori_path = self.path.joinpath(photo)
            # get full path of file from new directory
            jpg_path = self.new_path.joinpath(photo)
            shutil.copy(ori_path, jpg_path)

        print("JPG Photos Copied Completed!")


    def get_var(self):
        """
        print the class variables for debugging purposes.
        """
        print(self.path)
        print(self.parent)
        print(self.folder_name)
        print(self.new_path)
        
            

if __name__ == '__main__':
    raw_clear = RawClear()
    # raw_clear.get_var()
    raw_clear.tsf_jpg()


