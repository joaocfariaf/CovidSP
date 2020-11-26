# CovidSP

## 1. Definindo os parâmetros de simulação

### Número de pessoas envolvidas
n <- parametrizado pelo número de nós presentes de forma a se obter uma simulação factível
### Distribuição geográfica de zonas da cidade
Zonas num modelo simplificado do mapa da cidade

### 1.1 Famílias

#### Proporção populacional em cada zona
Valor absoluto do IBGE
#### Média de pessoas por família na zona
Valor absoluto do IBGE
#### Número estimado de famílias em cada zona
Calculado pela razão dos dois nros anteriores

### 1.2 Trabalho

#### Proporção de empregados em cada zona
Valor absoluto do IBGE
#### Número médio de empresas em cada zona
Aproximado por meio de uma regra de três entre o número total de empresas e empregados e o número de empregados em cada zona

## 2. Criando as redes

### 2.1 Criando a rede de famílias

#### A rede de famílias é basicamente uma rede GN, com Zext = 0, < Zin > = Média de pessoas por família

#### Para cada família criada naquela zona, gera um par de coordenadas aleatórias para aquela zona


### 2.2 Criando a rede de empregos

### Tinhamos falado de Lattice

#### Podemos criar um Lattice grande de todos os empregados da zona, e considerar o local de emprego
#### é no centro dela. Não acho pouco razoável não. Mas daí tem que ver a medida de dsitância.

### Podemos usar BA

#### Outra coisa que se pode fazer é criar uma rede BA, com gamma = 2.5 -> o Verri falou em aula
#### que as redes BA, com 2 < gamma < 3 geralmente são as que melhor descrevem as redes sociais reais.
#### E daí, distribuir os hubs aleatoriamente no espaço de cada zona
#### Os hubs poderiam ser definidos como nós com grau maior que a média.

## Correlacionando emprego e família

### Efeito de Localidade considerado

#### Dada uma vaga de emprego, ela vai estar relacionada com uma pessoa com probabilidade inversamente
#### proporcional a distância do emprego a casa da pessoa. 
#### Acho que daria pra pegar uma pessoa de forma aleatória e conectá-la ao emprego mais próximo e 
#### disponível, ou contrário. Isso daria o mesmo efeito de localidade, diminuindo o custo de gerar
#### vários números aleatórios - um pra cada emprego - até que dê um maior que 1/d

## Criando a rede de amizades

### Efeito de localidade, análogo ao emprego <-> família - mas cada um é "empregador" 

#### Rede WS baseada num lattice que inicialmente fica conectado

