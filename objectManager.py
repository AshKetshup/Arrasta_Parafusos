class Objects():
    """
    Classe encarregue de armazenar os objetos encontrados pelo robô sem repetição.
    """
    _people         = list()
    _objects        = list()
    _lastTwoFemales = (None, None)

    # OBJETOS: Identifica segundo os nomes dados pelo robô
    OBJ = {
        "ADULT"    : "adulto",
        "CHILD"    : "criança",
        "EMPLOYEE" : "funcionario",
        "CART"     : "carrinho",
        "ZONE"     : "zona",
        "CASHIER"  : "caixa"
    }

    # CATEGORIAS: Agrupa os varios objetos para identificação nos algoritmos correspondentes
    CATEGORY = {
        "OBJECT": [OBJ["CART"], OBJ["CASHIER"]],                   # Objetos
        "PEOPLE": [OBJ["EMPLOYEE"], OBJ["ADULT"], OBJ["CHILD"]],   # Pessoas
        "LOCALS": [OBJ["ZONE"]]                                    # Locais
    }
    
    ERROR_NOT_ENOUGH_FEMALES = "Não foram avistadas pelo menos 2 pessoas do sexo feminino até ao momento"

    class NotEnoughFemalesException(Exception):
        def __init__(self, error) -> None:
            self.msg = error

        def what(self) -> str:
            return self.msg

        
    @staticmethod
    def add(category, name) -> None:
        """
        * Adiciona o par (categoria, nome) se o objeto for novo.
        * Atualiza, caso necessario a queue das 2 ultimas pessoas do sexo feminino.

        Args:
            category (str): categoria indicada do objeto.
            name (str): nome indicado do objeto.
        """
        # Se o objeto não foi ainda encontrado:
        if not Objects.isIn(category, name): 
            # Se a categoria for de pessoa:
            if category in Objects.CATEGORY["PEOPLE"]:
                # Vamos adicionar ao à lista de pessoas.
                Objects._people.append((category, name))
            # Se a categoria for de objetos:
            else:
                # Vamos adicionar ao à lista de objetos.
                Objects._objects.append((category, name))
        
        
        # Se o objeto for uma pessoa do sexo feminino: 
        if Objects.sexCheck(name) == "female":
            # Se não for a ultima pessoa do sexo feminino a ser encontrada:
            if not Objects.isLastFemale(category, name):
                # Vamos dar swap aos elementos retirando o mais antigo
                Objects._lastTwoFemales = ((category, name), Objects._lastTwoFemales[0])

                    
    @staticmethod
    def isIn(category, name) -> bool:
        """
        * Retorna verdadeiro se o objeto já tiver sido previamente encontrado.

        Args:
            category (str): categoria do objeto
            name (str): nome do objeto

        Returns:
            bool: foi previamente encontrado
        """
        return ((category, name) in Objects._people + Objects._objects)
    
    
    @staticmethod
    def sexCheck(name) -> str:
        """
        * Indica se o sexo do objeto pelo nome.

        Args:
            name (str): nome do objeto

        Returns:
            str: sexo do nome do objeto = "female" | "male".
        """
        return "female" if name[-1] == 'a' else "male"
    
    
    @staticmethod
    def isLastFemale(category, name) -> bool:
        """
        * Indica se o objeto é a ultima pessoa do sexo feminino vista.

        Args:
            category (str): categoria do objeto
            name (str): nome do objeto

        Returns:
            bool: É a ultima pessoa do sexo feminino encontrado pelo robô
        """
        return (category, name) == Objects._lastTwoFemales[0]
    
    
    @staticmethod
    def getPenultSawFemale() -> tuple[str, str]:
        """
        * Devolve o objeto da penultima pessoa do sexo feminino avistada.

        Raises:
            Objects.NotEnoughFemalesException: levantado quando não são avistadas pessoas do sexo feminino suficientes

        Returns:
            tuple[str, str]: (categoria do objeto, nome do objeto)
        """        
        if None in Objects._lastTwoFemales:
            raise Objects.NotEnoughFemalesException(Objects.ERROR_NOT_ENOUGH_FEMALES)
        else:
            return Objects._lastTwoFemales[1]