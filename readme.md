# Simulação de BER vs SNR com Modulação BPSK

Este projeto implementa uma simulação para analisar a relação entre a Taxa de Erro de Bits (BER) e a Relação Sinal-Ruído (SNR) em uma comunicação digital utilizando modulação BPSK (Binary Phase Shift Keying). A simulação é realizada inteiramente em software, com uma interface gráfica interativa para ajustar parâmetros e observar como a qualidade do sinal influencia a taxa de erro.

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/Bit_Error_Rate.git
```


### Instalação das Dependências

Se ainda não tiver as bibliotecas instaladas, use:

```
pip install numpy matplotlib
```

### Executando o Projeto

Para iniciar o simulador, execute:

```
python3 main.py
```
<div align="center">
<img src=print.png width=80%>
</div>

## Fundamentos Teóricos

### 1. Modulação BPSK (Binary Phase Shift Keying)

BPSK é uma técnica de modulação digital onde cada bit de informação é representado por uma mudança de fase de 180° em uma portadora. Em termos simples:

- Um bit `1` é representado por uma onda com fase de 0°.
- Um bit `0` é representado por uma onda com fase de 180°.

Essa modulação é robusta e simples, sendo amplamente utilizada em sistemas de comunicação digital. No entanto, como todo sistema, o desempenho da BPSK é afetado pela presença de ruído no canal.

### 2. Ruído AWGN (Additive White Gaussian Noise)

O ruído no canal de comunicação é modelado como AWGN (Ruído Gaussiano Branco Aditivo), que representa uma interferência aleatória com características estatísticas gaussianas. Esse tipo de ruído é comumente utilizado em simulações de comunicação digital.

### 3. Relação Sinal-Ruído (SNR)

SNR é uma medida da relação entre a potência do sinal desejado e a potência do ruído presente no canal. Ela é expressa em decibéis (dB) e afeta diretamente a taxa de erro de bits (BER). Quanto maior a SNR, menor será a quantidade de erros, pois o sinal estará mais "forte" em relação ao ruído.

### 4. Taxa de Erro de Bits (BER)

A BER é uma métrica usada para avaliar a qualidade da transmissão de dados. Ela representa a fração de bits que foram incorretamente recebidos em relação ao total de bits transmitidos. A relação entre SNR e BER é essencial em sistemas de comunicação, pois ajuda a determinar a eficiência do sistema sob diferentes condições de ruído.

### Simulação

O simulador implementa a seguinte cadeia de comunicação:

1. **Geração de Bits Aleatórios**: Uma sequência de bits (0s e 1s) é gerada.
2. **Modulação BPSK**: Os bits são mapeados para sinais de -1 e 1.
3. **Adição de Ruído AWGN**: Um ruído proporcional ao valor de SNR especificado é adicionado ao sinal.
4. **Demodulação**: O sinal recebido é decodificado de volta para 0s e 1s.
5. **Cálculo da BER**: A BER é calculada comparando os bits originais com os bits recebidos.

A simulação é realizada para diferentes valores de SNR e a BER correspondente é calculada.

## Interpretação do Gráfico

O gráfico gerado mostra a relação entre a SNR (em dB) e a BER, em uma escala semilogarítmica (BER no eixo y e SNR no eixo x). A escala semilogarítmica é utilizada para destacar as diferenças na BER em diferentes níveis de SNR.

### Análise

- **Regiões de Alta SNR (à direita)**: Em níveis elevados de SNR, a BER tende a ser baixa, indicando uma comunicação confiável com poucos erros.
- **Regiões de Baixa SNR (à esquerda)**: Em níveis baixos de SNR, a BER aumenta significativamente, refletindo a dificuldade do sistema em discernir o sinal no meio do ruído.

Esse gráfico é fundamental para entender o desempenho de sistemas de comunicação digital sob diferentes condições de ruído.
