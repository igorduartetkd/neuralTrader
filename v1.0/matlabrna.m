dados = importdata('dadosTreinamentoAumento.txt');

XTrain = zeros(2000, 20, 'double');
YTrain = zeros(2000, 1, 'double');
for i=1:2000
    for j=1:20
        XTrain(i, j) = dados(i, j);
    end
    YTrain(i) = 0;
    if dados(i, 21) == 1
        YTrain(i) = 1;
    end
end


