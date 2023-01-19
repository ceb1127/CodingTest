-- 코드를 입력하세요
SELECT 
floor(price/10000) * 10000
as 'PRICE_GROUP' , count(PRODUCT_ID) as 'products'
from product
group by PRICE_GROUP
order by PRICE_GROUP 
