
dim_entrada = size(net.IW{1, 1});
dim_entrada = dim_entrada(2);
qtd_camadas = size(net.b);
qtd_camadas = qtd_camadas(1);
dimensoes(1) = dim_entrada;
s = size(net.IW{1, 1});
dimensoes(2) = s(1);
for i=2:qtd_camadas
    s = size(net.LW{i, i-1});
    dimensoes(i+1) = s(1);
end
arq = "redeNeuralExtraidaMatlab2.txt"
dlmwrite(arq, dimensoes, 'delimiter', ' ');
% escrevendo dados da primeira camada
IW = net.IW{1,1};
dlmwrite(arq, IW,'delimiter', ' ', '-append');
% escrevendo dados das outras camadas
for i=2:qtd_camadas
   LW = net.LW{i, i-1};
   dlmwrite(arq, LW,'delimiter', ' ', '-append');
end

% escrevendo biases
for i=1:qtd_camadas
    b = transpose(net.b{i});
    dlmwrite(arq, b, 'delimiter', ' ', '-append');
end