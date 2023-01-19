-- 코드를 입력하세요
SELECT  b.author_id, a.author_name, b.category, sum( bs.sales * b.price ) as total_sales
from book b, author a, book_sales bs
where b.author_id = a.author_id and b.book_id = bs.book_id
and DATE_FORMAT(sales_DATE, '%Y-%m') = '2022-01'
group by a.author_id, b.category
order by a.author_id, b.category desc;