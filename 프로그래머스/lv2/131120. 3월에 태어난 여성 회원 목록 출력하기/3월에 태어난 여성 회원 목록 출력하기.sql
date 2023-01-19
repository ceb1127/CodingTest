-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_format(DATE_OF_BIRTH,'%Y-%m-%d') as 'DATE_OF_BIRTH'
from member_profile 
where date_format(DATE_OF_BIRTH,'%m') = '03'
and tlno is not null
and gender = 'W'
order by member_id ;