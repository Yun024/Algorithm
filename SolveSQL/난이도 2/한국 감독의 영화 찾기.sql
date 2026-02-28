/* https://solvesql.com/problems/find-movies-by-korean-artists/ */
select b.name as artist, c.title as title
from artworks_artists as a
inner join artists b on a.artist_id = b.artist_id
inner join artworks c on a.artwork_id = c.artwork_id
where b.nationality = 'Korean'
and c.classification like 'Film%'