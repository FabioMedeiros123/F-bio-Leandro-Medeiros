-- a) Descubra o total de custo da tabela de pedidos.
SELECT Custo_Unit AS 'Custo' FROM pedidos;
SELECT SUM(Custo_Unit) AS 'Custo Total' FROM pedidos;

-- b) Descubra a quantidade total de lojas.
SELECT COUNT(Loja) AS "Qtd. Lojas" FROM lojas;

-- c) Descubra o custo médio dos produtos (de acordo com a tabela de produtos).
SELECT AVG(Custo_Unit) AS 'Custo médio' FROM produtos;

-- d) Descubra a quantidade mínima e máxima de funcionários das lojas (faça isso em um único SELECT).
SELECT MIN(Num_Funcionarios),MAX(Num_Funcionarios) FROM Lojas;