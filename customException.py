class SimpleException(Exception):
    def __init__(self, errorMsg: str) -> None:
        """
        Construtor da SimpleException.

        Args:
            errorMsg (str): Mensagem enviada como payload.
        """
        self.payload = errorMsg

    def what(self) -> str:
        """
        Devolve o payload.

        Returns:
            str: Payload da exceção.
        """        
        return self.payload