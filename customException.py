import inspect

myself = lambda: inspect.stack()[1][3]

class SimpleException(Exception):
    def __init__(self, errorMsg: str, funName: str = "" ) -> None:
        """
        Construtor da SimpleException.

        Args:
            errorMsg (str): Mensagem enviada como payload.
        """
        self.payload = f"{funName} | {errorMsg}"

    def what(self) -> str:
        """
        Devolve o payload.

        Returns:
            str: Payload da exceção.
        """        
        return self.payload