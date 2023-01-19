-- 코드를 입력하세요
SELECT ao.animal_id, ao.name
from animal_ins ai right join animal_outs ao
on ai.animal_id = ao.animal_id
order by datediff(ao.datetime,ai.datetime) desc
limit 2;