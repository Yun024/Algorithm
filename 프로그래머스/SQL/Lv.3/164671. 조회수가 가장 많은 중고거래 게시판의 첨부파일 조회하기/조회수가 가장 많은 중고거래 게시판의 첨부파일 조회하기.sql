-- 코드를 입력하세요

-- on을 이용한 join
-- select '/home/grep/src/' || B.board_id || '/' || F.file_id || F.file_name || F.file_ext as file_path
-- from used_goods_file F inner join used_goods_board B
-- on F.board_id = B.board_id
-- where views = (
--                 select max(views)
--                 from used_goods_file F inner join used_goods_board B
--                 on F.board_id = B.board_id
-- )
-- order by file_id desc


-- using을 이용한 join
select '/home/grep/src/' || board_id || '/' || file_id || file_name || file_ext as file_path
from used_goods_file F inner join used_goods_board B
using (board_id)
where views = (
                select max(views)
                from used_goods_file F inner join used_goods_board B
                using (board_id) 
)
order by file_id desc