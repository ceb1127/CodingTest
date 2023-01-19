-- 코드를 입력하세요
SELECT MCDP_CD as '진료과코드', count(apnt_no) as '5월예약건수'
from appointment
where APNT_YMD like '2022-05%'
group by MCDP_CD
order by count(apnt_no), MCDP_CD;