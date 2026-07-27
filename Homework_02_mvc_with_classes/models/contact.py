class Contact:
    """
    Class for working with contact data.
    """
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_list(self) -> list:
        """
        Convert contact data to a list.
        
        Args: 
            None
        
        Returns:
            list (list of contact data)    
        """        
        return [self.name, self.phone, self.comment]