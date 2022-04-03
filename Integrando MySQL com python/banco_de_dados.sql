-- CRIANDO O BANCO DE DADOS
CREATE DATABASE PYTHONSQL;

-- USANDO O BANCO DE DADOS CRIADO ANTES, CRIE UMA TABELA COM O NOME VENDAS
USE PYTHONSQL;
CREATE TABLE VENDAS(
	id_venda int,
    cliente varchar(50),
    produto varchar(50),
    data_venda date,
    preco decimal(6,2),
    quantidade int
);

-- INSERINDO VALORES NA TABELA CRIADA
INSERT INTO VENDAS(id_venda,cliente,produto,data_venda,preco,quantidade)
VALUES
	(1,'Fábio','PC','2022/04/01',6000,1);
    
-- VISUALIZANDO A TABELA CRIADA
SELECT * FROM VENDAS;

