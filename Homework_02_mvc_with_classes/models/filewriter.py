import csv

class FileWriter:
    """
    Class for writing data to a file.
    """
    def __init__(self, file_name: str):
        self.file_name = file_name

    def write_file(self, data: list):
        """
        Write data to the file.
        
        Args: 
            data (list): The data to write to the file.
        
        Returns:
            None    
        """        
        print(data)
        with open(self.file_name, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)