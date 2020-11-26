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

### 1.3 Amizades

#### Média de amigos por pessoa (além da família)
8

#### As amizades com mais contato constumam localizar-se geograficamente próximas
#### Vamos considerar a proximidade da residência apenas

## 2. Criando as redes

### 2.1 Criando a rede de famílias

#### Posicionamento das famílias
Tendo o número de famílias esperado para cada zona, elas são alocadas com coordenadas geográficas aleatórias dentro de cada zona.

#### Rede familiar
Dentro da família, o modelo considerado é de todos os nós diretamente conectados.

### 2.2 Criando a rede de empregos

#### Posicionamento das empresas
Dado o número estimado de empresas por zona, elas são alocadas com coordenadas geográficas aleatórias dentro de cada zona.

#### Rede de contato dentro da empresa
Considerando que o contato mais próximo entre os funcionários se dá geralmente no mesmo nível hierárquico, 
pode-se considerar o uso de um lattice para o modelo desta rede de contatos.

### 2.3 Correlacionando emprego e pessoa

#### Cabe aqui considerar dois efeitos: a população em geral costuma trabalhar mais ao centro, onde há mais empregos; ao mesmo tempo, as pessoas tendem a morar perto de onde trabalham, se possível. Por exemplo, pessoas que morem em bairros com muitos cargos de trabalho, e muito caros, portanto, dificilmente trabalham na periferia. Ao mesmo tempo, que os moradores das periferias, são trazidos para o centro pela falta de cargos de trabalho mais próximos a eles.

#### De forma a manter o efeito da localidade, sem perder a atração de mão-de-obra da periferia para o centro, a correlação pessoa-emprego é feita da seguinte forma:
#### - Considera-se os nós correspondentes as pessoas numa ordem aleatória;
#### - Seguindo essa ordem cada pessoa conecta-se ao emprego mais próximo de sua residência que esteja disponível;
#### - Por simplicidade, considera-se que todos trabalham.

## 2.4 Criando a rede de amizades

### Efeito de localidade, análogo ao emprego <-> família - mas cada um é "empregador" 

#### Rede WS baseada num lattice que inicialmente fica conectado


## 3. Evolução dos casos

