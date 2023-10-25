-- 코드를 입력하세요
SELECT apnt_no , pt_name, A.pt_no, B.mcdp_cd, dr_name, apnt_ymd
from patient A, Doctor B, appointment C
where A.pt_no = C.pt_no 
and C.mddr_id = b.dr_id
and c.mcdp_cd = B.mcdp_cd 
and B.mcdp_cd = 'CS'
and apnt_ymd between to_date('2022-04-13 01','YYYY-MM-DD HH24') and to_date('2022-04-13 23','YYYY-MM-DD HH24')
and apnt_cncl_yn = 'N'
order by apnt_ymd 


