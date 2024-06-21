SELECT c.name -- seleciona o nome do cliente
FROM customers c INNER JOIN legal_person l ON -- junta a tabela de clientes com a tabela de pessoas jurídicas
    l.id_customers = c.id