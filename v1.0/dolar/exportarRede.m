IW = net.IW{1,1}; 
LW = net.LW{2,1}; 
b1 = net.b{1}; 
b2 = net.b{2};
dim_entrada = size(IW);
dim_entrada = dim_entrada(2);

dlmwrite("saidaRedeMatlab.txt", IW, 'delimiter', ' ');
entrada = zeros(dim_entrada, 'double');
for i=1:dim_entrada
    for j=1:dim_entrada
        entrada(i, j) = 1;
    end
end
dlmwrite("primeiracamada.txt", entrada, 'delimiter', ' ');
dlmwrite("segundacamada.txt", IW, 'delimiter', ' ');
dlmwrite("camadasaida.txt", LW, 'delimiter', ' ');
dlmwrite("b1.txt", b1, 'delimiter', ' ');
dlmwrite("b2.txt", b2, 'delimiter', ' ');

%qtd_camadas = size(net.b);
%qtd_camadas = qtd_camadas(1);
%dimensoes = [dim_entrada]
%for i=1:qtd_camadas
    
%end