SELECT p.name  -- seleciona o nome do produto
FROM products p INNER JOIN providers f ON  -- junta a tabela products com a tabela providers
    p.id_providers = f.id
WHERE SUBSTRING(f.name, 1, 1) = 'P' AND p.amount > 10 AND p.amount < 20  -- seleciona os produtos cujo nome do fornecedor começa com 'P' e a quantidade de produtos é maior que 10 e menor que 20