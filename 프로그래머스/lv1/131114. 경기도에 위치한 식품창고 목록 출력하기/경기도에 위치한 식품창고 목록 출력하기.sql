-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, 
    case 
    when freezer_yn is null or freezer_yn = 'N' then 'N'
    when freezer_yn = 'Y' then 'Y'
    end 
    as 'Freezer_yn'
from food_warehouse
where warehouse_name like '%경기%'
order by warehouse_id asc;
