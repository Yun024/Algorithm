## Url : https://solvesql.com/problems/artists-without-artworks/

select a.artist_id, a.name
from artists a
left join artworks_artists b on a.artist_id = b.artist_id
where death_year is not null
and artwork_id is null