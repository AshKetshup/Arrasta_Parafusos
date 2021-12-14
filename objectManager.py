import csv

from utils import SimpleException
from zone import Zone


class Objects():
    """
    Classe encarregue de armazenar os objetos encontrados pelo robô sem repetição.

    Raises:
        `Objects.NotEnoughFemalesException`: Excepção usada para descrever quando não foram avistadas pessoas do sexo 
        feminino suficientes.
        
    CheckList:
    [X]: Inicializar as variaveis de classe:
        * [X] _people
        * [X] _objects
        * [X] _last2Females
        * [X] SIZE
        * [X] OBJ
        * [X] CATEGORY
        * [X] SPLITTER
    [X]: Preparar Exceção de falta de pessoas encontradas do sexo feminino
    [X]: Implementa Funções de management: 
        * [X] add()
        * [X] isIn()
        * [X] isLastFemale()
        * [X] sexCheck()
        * [X] getPenultSawFemale()
        * [X] getListOfPeople()
        * [X] getListOfObjects()
    [X]: Completa a documentação: 
        * [X] add()
        * [X] isIn()
        * [X] isLastFemale()
        * [X] sexCheck()
        * [X] getPenultSawFemale()
        * [X] getListOfPeople()
        * [X] getListOfObjects()
    """
    _people         = list()
    _objects        = list()
    _lastTwoFemales = (None, None)
    
    # SIZE: Tamanho de cada tipo de objecto que compõe o mundo
    SIZE = {
        "OBJECT": 25,
        "WALL"  : 15
    }

    # OBJETOS: Identifica segundo os nomes dados pelo robô
    OBJ = {
        "ADULT"    : "adulto",
        "CHILD"    : "criança",
        "EMPLOYEE" : "funcionário",
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
    
    SPLITTER = "_"

    ERROR_NOT_ENOUGH_FEMALES = "Não foram avistadas pelo menos 2 pessoas do sexo feminino até ao momento"
    class NotEnoughFemalesException(SimpleException):
        """
        Excepção usada para descrever quando não foram avistadas pessoas do sexo feminino suficientes.

        Inherits:
            `SimpleException` (class): Very basic exception
        """        
        pass
    

    @staticmethod
    def add(obj: tuple[str, str], currentZone: Zone) -> None:
        """
        * Adiciona o par (categoria, nome) se o objeto for novo.
        * Atualiza, caso necessario a queue das 2 ultimas pessoas do sexo feminino.

        Args:
            `category` (str): categoria indicada do objeto.
            `name` (str): nome indicado do objeto.
        """
        # Se o objeto não foi ainda encontrado:
        if not Objects.isIn(obj): 
            # Se a categoria for de pessoa:
            if obj in Objects.CATEGORY["PEOPLE"]:
                # Vamos adicionar ao à lista de pessoas.
                Objects._people.append(obj)
            # Se a categoria for de objetos:
            else:
                # Vamos adicionar ao à lista de objetos.
                Objects._objects.append(obj)
                # Se a categoria for uma zona:
                if obj[0] in Objects.CATEGORY["LOCALS"]:
                    # Vamos dar set na zona atual
                    currentZone.setType(obj[1])
        
        # Se o objeto for uma pessoa do sexo feminino: 
        if obj[0] in Objects.CATEGORY["PEOPLE"] and Objects.sexCheck(obj[1]) == "female":
            # Se não for a ultima pessoa do sexo feminino a ser encontrada:
            if not Objects.isLastFemale(obj):
                # Vamos dar swap aos elementos retirando o mais antigo
                Objects._lastTwoFemales = (obj, Objects._lastTwoFemales[0])


    @staticmethod
    def isIn(obj: tuple[str, str]) -> bool:
        """
        * Retorna verdadeiro se o objeto já tiver sido previamente encontrado.

        Args:
            `obj` (tuple[str, str]): objeto

        Returns:
            bool: foi previamente encontrado
        """
        # Verdadeiro se o objeto já tiver sido avistado.
        return (obj in Objects._people + Objects._objects)

    
    @staticmethod
    def sexCheck(name: str) -> str:
        """
        * Indica se o sexo do objeto se o nome estiver dentro do dataset do registo de nomes proprios femininos do anos de 2017 em Portugal.

        Args:
            `name` (str): nome do objeto

        Returns:
            str: sexo do nome do objeto = "female" | "male".
        """
        with open('res/nomesfeminino.up.csv', encoding="cp1252") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if name == row[1]:
                    return 'female'

        return 'male'
    
    
    @staticmethod
    def isLastFemale(obj: tuple[str, str]) -> bool:
        """
        * Indica se o objeto é a ultima pessoa do sexo feminino vista.

        Args:
            `obj` (tuple[str, str]): objeto

        Returns:
            bool: É a ultima pessoa do sexo feminino encontrado pelo robô
        """
        # Verificamos se a categoria e o nome dados correspondem aos dados da ultima pessoa do sexo feminino avistada.
        return obj == Objects._lastTwoFemales[0]

    
    @staticmethod
    def getPenultSawFemale() -> tuple[str, str]:
        """
        * Devolve o objeto da penultima pessoa do sexo feminino avistada.

        Raises:
            `Objects.NotEnoughFemalesException`: levantado quando não são avistadas pessoas do sexo feminino suficientes

        Returns:
            tuple[str, str]: (categoria do objeto, nome do objeto)
        """
        # Se estiver algum None no tuplo:
        if None in Objects._lastTwoFemales:
            print(Objects._lastTwoFemales)
            # Levantamos a exceção de que ainda não avistamos mais que 2 pessoas.
            raise Objects.NotEnoughFemalesException(Objects.ERROR_NOT_ENOUGH_FEMALES)
        # Caso não encontremos nenhum None:
        else:
            # Significa que já avistamos pelo menos 2 pessoas do sexo feminino e portanto devolvemos a penultima avistada. 
            return Objects._lastTwoFemales[1]
        
    @staticmethod
    def getListOfPeople():
        """
        Devolve a lista de pessoas encontradas.

        Returns:
            list[tuple[str, str]]: Pessoas encontradas
        """
        return Objects._people
    
    @staticmethod
    def getListOfObjects():
        """
        Devolve a lista de objetos encontrados.

        Returns:
            list[tuple[str, str]]: Objetos encontrados
        """
        return Objects._objects