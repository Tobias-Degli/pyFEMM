# Unit[m]
problemDepth = 3*1e-3

P = 100 # W                         (Potência do equipamento)
η = 0.95 #                          (Eficiência do equipamento)
P_loss = (1-0.95)*100 # W           (Dissipação térmica considerando que todas as perdas são por aquecimento)
V = 10*1e-3 * 10*1e-3 * 5*1e-3 # m³ (Considerando que o elemento gerador de calor tem 5mm de espessura)
Q_ger = P_loss/V # W/m³            (Se tiver mais de um elemento, multiplicar o número de elementos no denominador Q_ger = P_loss/(V*N)

# Definição das coordenadas (A separação por vértices auxilia no momento de definir as condições de contorno e os materiais)
# Vale lembrar, que diferente do caso do eletromagnetismo que sempre vai trabalhar como o motor ou geometria circular, a análise térmica é aplicada a dispositivos de geometrias diversas..

x1 = 5 *1e-3; y1 = 0
x2 = 45*1e-3; y2 = 0
x3 = 50*1e-3; y3 = 5*1e-3; angle_2_3 = 90
x4 = x3; y4 = 25*1e-3
x5 = x2; y5 = 30*1e-3
x6 = x1; y6 = y5
x7 = 0;  y7 = y4
x8 = x7; y8 = y3; angle_8_1 = 90
x9 = 30*1e-3; y9 = 20*1e-3
x11 = 35*1e-3; y11 = 25*1e-3

