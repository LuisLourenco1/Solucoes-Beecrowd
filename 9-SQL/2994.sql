SELECT d.name, ROUND(SUM((a.hours * 150.0) + (((a.hours * 150.0) * w.bonus) / 100.0)), 1) as salary -- seleciona o nome do médico e faz os cálculos do salário
FROM doctors d INNER JOIN attendances a ON d.id = a.id_doctor -- junta a tabela de médicos com a tabela de presença
               INNER JOIN work_shifts w ON w.id = a.id_work_shift -- junta a tabela resultante com a tabela de turnos de trabalho
GROUP BY d.id -- agrupa por id
ORDER BY salary DESC -- ordena o salário do maior pro menor