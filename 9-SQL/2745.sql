SELECT name, ROUND(0.1 * salary, 2) as tax  -- seleciona o nome e calcula a taxa a ser paga
FROM people  -- da tabela de pessoas
WHERE salary > 3000  -- onde o salário for maior que 3000
