'''Desenvolva uma rotina que apresente os valores de conversão de graus
Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 0º
Celsius e finalizando em 100º Celsius. A rotina deverá exibir tanto o
valor em Celsius quanto em Fahrenheit e a seguinte fórmula deverá ser
adotada: ºF = ºC x 1,8 + 32.'''

C = 0
F = 0
for c in range(0, 101, 10):

    F = c * 1.8 + 32
    C = (c - 32) / 1.8
    print(f'{c:>3} ºCelsius =  {F:>5}ºFahrenheit.{"-":^9}{c:>3}ºFahrenheit =  {C:>8.4f}ºCelsius.)')
