-- 코드를 입력하세요
SELECT ai.name, ai.datetime
from animal_ins ai left join animal_outs ao
on ai.animal_id = ao.animal_id
where ao.animal_id is null
order by datetime 
limit 3;

-- 입양일 - 보호시작일 +1?