-- a) Faça um agrupamento para descobrir o total de clientes por Sexo.
SELECT Sexo, COUNT(Sexo) FROM clientes
GROUP BY Sexo;

-- b) Faça um agrupamento para descobrir quantos produtos existem por categoria.
-- Resposta 1
SELECT Categoria, COUNT(produtos.ID_Categoria) AS 'Qtd de produtos'
FROM produtos
INNER JOIN categorias ON produtos.ID_Categoria=categorias.ID_Categoria
GROUP BY produtos.ID_Categoria;

-- Resposta 2
SELECT Categoria,COUNT(*) AS 'Qtd de produtos'
FROM produtos
INNER JOIN categorias ON produtos.ID_Categoria=categorias.ID_Categoria
GROUP BY Categoria;

-- c) Faça um agrupamento para descobrir a soma total de receita por Loja.
-- Resposta 1
SELECT Loja,SUM(Receita_Venda) AS 'Receita total'
FROM pedidos
INNER JOIN lojas ON pedidos.ID_Loja = lojas.ID_Loja
GROUP BY pedidos.ID_Loja;

-- Resposta 2
SELECT Loja,SUM(Receita_Venda) AS 'Receita total'
FROM pedidos
INNER JOIN lojas ON pedidos.ID_Loja = lojas.ID_Loja
GROUP BY loja;