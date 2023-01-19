-- 코드를 입력하세요
SELECT CAR_TYPE, count(CAR_ID) as cars
from CAR_RENTAL_COMPANY_CAR
where OPTIONS REGEXP '통풍시트|열선시트|가죽시트'
group by car_type
order by car_type;