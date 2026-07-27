import csv

class FileReader:
    """
    Class for reading data from a file.
    """
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_file(self) -> list:
        """
        Read data from the file.
        
        Args: 
            None
        
        Returns:
            list (list of data from the file)    
        """        
        with open(self.file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
        return data