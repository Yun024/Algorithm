/* https://solvesql.com/problems/critic-scores-by-genre-and-year/ */

select 
  genre.name as genre,
  round(avg(case when year = 2011 then critic_score end),2) score_2011,
  round(avg(case when year = 2012 then critic_score end),2) score_2012,
  round(avg(case when year = 2013 then critic_score end),2) score_2013,
  round(avg(case when year = 2014 then critic_score end),2) score_2014,
  round(avg(case when year = 2015 then critic_score end),2) score_2015
from games game
inner join genres genre on game.genre_id = genre.genre_id
group by genre.name