/* https://solvesql.com/problems/correlation-penguin/ */

-- WITH
--   temp AS (
--     SELECT
--       species,
--       flipper_length_mm,
--       avg(flipper_length_mm) OVER (PARTITION BY species) avg_fl,
--       body_mass_g,
--       avg(body_mass_g) OVER (PARTITION BY species) avg_bm
--     FROM penguins
--   )

-- select
--   species,
--   round(
--     sum( (flipper_length_mm - avg_fl) * (body_mass_g - avg_bm)) 
--       /
--     sqrt( sum( power(flipper_length_mm - avg_fl,2)) *
--       sum( power(body_mass_g - avg_bm,2)))
--   ,3) as corr
-- from temp
-- group by species

SELECT
  species,
  round(cast(corr(flipper_length_mm,body_mass_g) as numeric),3) as corr
from
  penguins
group by species
