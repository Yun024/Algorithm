/* https://solvesql.com/problems/species-and-mass-of-penguins/ */

select species, body_mass_g
from penguins
/* where species is not null and body_mass_g is not null */
where num_nonnulls(species, body_mass_g) = 2
order by body_mass_g desc, species
;