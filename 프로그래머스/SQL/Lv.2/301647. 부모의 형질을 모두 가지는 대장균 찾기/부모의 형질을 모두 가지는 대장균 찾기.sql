-- 코드를 작성해주세요
select a.id, a.genotype, b.genotype parent_genotype
from ecoli_data a, ecoli_data b
where a.parent_id = b.id 
and a.genotype & b.genotype = b.genotype 
order by id