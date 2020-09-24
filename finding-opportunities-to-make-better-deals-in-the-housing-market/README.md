<img src="https://dm2302files.storage.live.com/y4mjoWpKezUd7ykYnOn2t6DRjIbYWcBHM85Ytuw7XSxiRSUEwiSvjuPRw7Me4ioJwJCbghN1JQuDwXuiCM0uV4m_KiIyj9LcX5rm_HwC460BlCQ03mfCqauISbZxpasUFIpxBafTRyPGfzznlUkoiZgARXGoEn7nbhmRUVd6kz94VRNTJ5JDej-kMzBZLaTk4RvAuTGb169kTLgN0TLsYe68w/cidades-coloridas_bo-kaap.png?psid=1&width=1024&height=418"></img>

<center>
<h1>
Encontrando oportunidades de negócio no mercado de imóveis
</h1>
</center>

O CEO da InteliHouse gostaria de maximizar a receita da empresa encontrando melhores oportunidades de negócio no ramo de imóveis.

A principal estratégia da empresa é comprar boas casas em ótimas localizações com preços baixos, torna-las inteligentes, isto é equipa-las com tecnologia de ponta para proporcionarem mais segurança, conforto e praticidade aos seus moradores, e depois revendê-las posteriormente à preços mais altos.

Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e portanto maior sua receita.

Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores e a localização e o período do ano também podem influenciar os preços.

Para maximizar a receita, o CEO acredita que as seguintes perguntas devem ser respondidas:

- Quais casas a InteliHouse deveria comprar e por qual preço de compra?

- Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?

- A InteliHouse deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma?


## _Sobre os dados_

O conjunto de dados que representa o contexto está disponível na plataforma do [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction). E foram obtidos a partir da venda de casas em King County, um dos 39 condados do estado de Washington.


_Disclaimer: o contexto apresentado, a empresa, o CEO e as perguntas de negócio são ficticios e existem somente para a elaboração de um problema._

_Nota: Este projeto foi sugerido por [Meigarom Lopes](https://www.linkedin.com/in/meigarom) em seu blog [sejaumdatascientist.com](https://sejaumdatascientist.com)_

## Resumo da conclusão realizada pela análise
<img src="https://0rtu3q.dm.files.1drv.com/y4mQ-GVlbNI1NFxNPuOE3kO8zLKhNs7wnbDnQYep8zKhBacdEXAKlh0-brIes4yPKJ7phoOKAQof3twEdLVv7lBTmO0zgzOAQEHW5951XsiWEhZIz8MKddAjrqXZGDfSskDGqOVjh8iFHGbRpMCvjZn5YB8bApHgitHkNRjeWhJcoGuqO4v6GfltV3Wj8PtlWJCBFnNbLYIA8m662wA9P63qg/Tomada-de-Decis%C3%B5es.png?psid=1"></img>

- __Quais casas o CEO da InteliHouse deveria comprar e por qual preço?__

Dentre as questões levantadas para a compra de imóvel, foram levadas em consideração a __localização__, __valorização__ e outras __condições__ do imóvel, além da diferença de tempo entre a compra e venda ser o menor possível afim de diminuir os efeitos de um imóvel/passivo. 

Baseado na análise realizada, é possível estipular o m² mais barato e mais caro por região, sendo a região de Bellevue apresentando bons indicativos de compra já que possui um dos m² mais barato em relação a área livre (que pode ser construída), mas tem um dos m² construídos mais caros, mesmo sendo um local com um alto padrão (casas acima de 1M em média) a compra de casas de visando a valorização futura com uma reforma possui indicativos de bons lucros.

Em relação a setores que possuem uma valorização anual, o de Seattle é um dos mais altos. Visando este quesito, a recomendação de compra ocorre para o setor Sul, que possui uma valorização próxima ao do setor Norte, porém com casas mais baratas (indicando que há uma inflação em relação ao setor Norte). Seguido desses dois setores o próximo é o de Bellevue, reforçando o argumento acima em relação a compra para valorização através de uma reforma/melhoria. Em relação ao setor que menos valoriza ao ano (o de Preston), não é recomendável a compra visando a valorização anual, já que possui uma média de venda alta. A diferença de valorização entre o setor Sul de Seattle, com casas mais baratas podem apresentar um melhor negócio, já que é possível atingir a mesma média de valores considerando a valorização, mas com um investimento bem menor.

Em questão das condições do imóvel, os que apresentam melhores dados em relação a compra são os de condição 2 e 3, o aumento de preço em relação a condições superiores a esta não é significativo, enquanto que a condição 3 apresenta grande variância, ou seja, é possível vender casas nessas condições por valores mais acessíveis a até valores na casa de milhões. Os imóveis com condição 2 apresentam uma queda significativa de preço em relação aos de condição 3 e podem apresentar um bom negócio visando melhorias/reformas, já que possui uma certa concentração de valor em relação ao preço, indicando por exemplo que clientes com perfis com um maior poder aquisitivo preferem obter casas com condição igual ou superior a 3, portanto, melhorando a condição abrangerá mais perfis de clientes.

Em relação a vista, as casas com vista para o lago em sua maioria são sobrevalorizadas, portanto a recomendação de compra não é indicada, já que sugere também um perfil de cliente especifico. 

Baseando-se que a empresa assuma bons negócios e tentando abranger o maior número de perfis de clientes, além de considerar menores valores de investimento, o perfil de casas a serem adquiridas são as que podem ser vendidas entre a faixa de `$84.000` até `$3.400.000,00`. Que em sua maioria se enquadra no padrão de 2 a 6 quartos com até 5 banheiros, condições intermediárias (2 e 3) e sem vista para o mar.
<br>
<br>

- __Uma vez a casa em posse da empresa, qual o melhor momento para vendê-las e qual seria o preço da venda?__

Os dados nos mostram que o melhor período de venda ocorre entre a Primavera e o Verão, onde ocorre também um aumento da procura. Neste período, as casas podem ser vendidas em média por um valor superior de 3% por m². Em relação a um período em que a procura é baixa, que ocorre no Inverno, a diferença entre esses dois períodos pode ser em média de 6% por m².
<br>
<br>

- __A InteliHouse deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma?__

Sim, a reforma é interessante para o aumento do preço da venda, principalmente em casas que podem ser compradas com frente para rios/lagos e que se enquadram nos padrões estabelecidos, pois nesses casos há uma sobrevalorização. Em nossa análise foi possível verificar casas que possuiam frente para rios e lagos e que foram vendidas por preços relativamente baixos, mesmo tendo uma qualidade de vista 4 e estando em setores que são valorizados, como Seattle. Dentre os atributos que podem ser classificados para uma reforma, como qtd de banheiros, quartos, melhora na condição do imóvel e do ranking, o atributo que mais contribui é o ranking, tendo um aumento médio de 30% no valor do imóvel a cada `grade` aumentado. Seguido pela quantidade de quartos, com um incremento no preço de 14.84% e de 14.12% para cada banheiro completo adicionado, por último a condição do imóvel tem um aumento médio de 7.25% no preço de venda.