SELECT res.id Reserva, user.name as Usuario, des.name as Destino
FROM reservations as res
INNER JOIN users as user ON res.user_id = user.id
INNER JOIN destiny as des ON res.destiny_id = des.id
WHERE user.id < 4
group by res.id, user.name, des.name;

SELECT * FROM users us                           -- Retorna todos os dados de users e
LEFT JOIN reservations rs ON rs.user_id = us.id; -- se não houver correspondencia em reservations
												 -- os campos ficam NULL
                                                 
SELECT * FROM reservations rs					 -- Retorna todos os dados de destiny e 
RIGHT JOIN destiny ds ON rs.destiny_id = ds.id;  -- os campos não correspondentes ficam NULL

-- FULL OUTER JOIN gambiarra kkk
SELECT * FROM reservations rs					
LEFT JOIN destiny ds ON rs.destiny_id = ds.id
LEFT JOIN users us ON rs.user_id = us.id
UNION                                            -- Retorna todos os dados de todas as tabelas
SELECT * FROM reservations rs					 -- incluindo os sem correspondência
RIGHT JOIN destiny ds ON rs.destiny_id = ds.id
RIGHT JOIN users us ON rs.user_id = us.id;

-- Substrings
SELECT * FROM destiny
WHERE id NOT IN (SELECT destiny_id 
				 FROM reservations);
                 
SELECT name, (SELECT COUNT(*) FROM reservations
			  WHERE user_id = users.id) as Total_Reservas
FROM users;

-- Funções agregadoras
SELECT MAX(TIMESTAMPDIFF(YEAR, birthDate, CURRENT_DATE())) as Maior_Idade
FROM users;

SELECT COUNT(*) QTD_Reservas, destiny_id
FROM reservations
GROUP BY destiny_id;






