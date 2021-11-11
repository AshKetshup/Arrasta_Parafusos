# Arrasta Parafusos


## Boundaries
!["Boundaries Identifiers"](./docs/imgs/Boundaries.jpg)

|   No.    |   (X1, X2)   |   (Y1, Y2)   |
|----------|--------------|--------------|
|  **01**  | `(030, 135)` | `(165, 435)` |
|  **02**  | `(135, 285)` | `(165, 285)` |
|  **03**  | `(135, 285)` | `(330, 285)` |
|  **04**  | `(285, 435)` | `(165, 435)` |
|  **05**  | `(435, 770)` | `(165, 285)` |
|  **06**  | `(435, 770)` | `(330, 285)` |
|  **07**  | `(030, 135)` | `(030, 135)` |
|  **08**  | `(180, 285)` | `(030, 135)` |
|  **09**  | `(330, 435)` | `(030, 135)` |
|  **10**  | `(480, 585)` | `(030, 135)` |
|  **11**  | `(630, 770)` | `(030, 135)` |
|  **12**  | `(630, 770)` | `(435, 570)` |
|  **13**  | `(480, 585)` | `(435, 570)` |
|  **14**  | `(330, 435)` | `(435, 570)` |
|  **15**  | `(180, 285)` | `(435, 570)` |
|  **16**  | `(030, 135)` | `(435, 570)` |

---
## Questões

#### 1. Qual foi a penúltima pessoa do sexo feminino que viste?

##### Sugestão de solução:
Distinguir sexo feminino pelo ultimo caracter.
Se 'a' então feminino.

Irmos dando append a uma lista o nome de cada pessoa que encontramos.
Quando for requesitada a resposta é percorrer a lista do fim para o inicio e a resposta será a segunda pessoa do sexo feminino.

Outra solução seria fazer uma lista para cada sexo. E assim seria apenas aceder ao elemento de indice -2 da lista de pessoas do sexo feminino.



#### 2. Em que tipo de zona estás agora?

##### Sugestão de solução:
Durante o uso do robô se ele encontrar um item de "Zona" vai atraves das coordenadas atuais descobrir em que "sala" está e atribuir o tipo de zona.

Quando for requesitada a resposta é apenas necessario descobrir a sala em que estamos e se já tivermos encontrado que zona estamos então dá print a isso. Caso contrario dá print que ainda não temos essa resposta.

#### 3. Qual o caminho para a papelaria?

##### Sugestão de solução:
Um Grafo com cada aresta de onde estamos para onde passamos.
Utilizar Pesquisa de Primeiro em Profundidade (PPP) ou Pesquisa de Primeiro em Largura (PPL).

#### 4. Qual a distância até ao talho?

##### Sugestão de solução:
Aberto a sugestões.

#### 5. Quanto tempo achas que demoras a ir de onde estás até à caixa?

##### Sugestão de solução:
Calcular em media a velocidade. Pela distancia percorrida desde o inicio do programa. (Talvez pausar quando o bixo não se mexe)

#### 6. Quanto tempo achas que falta até ficares com metade da bateria que tens agora?

##### Sugestão de solução:
Fazendo uma regressão linear. E no momento em que for pedido seria apenas buscar em y = (bateria atual / 2).
y -> bateria
x -> tempo

(talvez reiniciar sempre que a bateria estiver a 100%)

#### 7. Qual é a probabilidade da próxima pessoa a encontrares ser uma criança?

##### Sugestão de solução:
Deve ser uma rede Bayesiana ou uma Condicional. Esta deixo contigo @CRISphantom04

#### 8. Qual é a probabilidade de encontrar um adulto numa zona se estiver lá uma criança mas não estiver lá um carrinho?

##### Sugestão de solução:
Deve ser uma rede Bayesiana ou uma Condicional. Esta deixo contigo @CRISphantom04

---
## Dependências

```bash
pip3 install pygame networkx numpy scipy scikit-learn pyAgrum
```