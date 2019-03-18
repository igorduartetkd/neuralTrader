dados = importdata('dadosTreinamentoAumento-diarioDolarFuturo2002-2012.txt');

n_neuronios_entrada = 30;
n_linhas_treinamento = 1500;

XTrain = zeros(n_linhas_treinamento, n_neuronios_entrada, 'double');
YTrain = zeros(n_linhas_treinamento, 1, 'double');
for i=1:n_linhas_treinamento
    for j=1:n_neuronios_entrada
        XTrain(i, j) = dados(i, j);
    end
    YTrain(i) = 0;
    if dados(i, n_neuronios_entrada + 1) == 1
        YTrain(i) = 1;
    end
end


