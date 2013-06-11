SELECT
	COUNT(m.id) AS 'costarred',
	csa.last_name AS 'Last Name',
	csa.first_name AS 'First Name'
FROM
	movies as m
	JOIN roles as kbr ON kbr.actor_id = 22591 AND kbr.movie_id = m.id
	JOIN roles as csr ON csr.movie_id = m.id
	JOIN actors as csa ON csr.actor_id = csa.id
GROUP BY
        csa.id
