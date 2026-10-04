with error_count as
(
select cast(first_at as date) error_date
,count(*) error_count
from err_tracks
group by 1
order by 1
)

select *
,error_count-prev_count day_over_day_change
from
  (
SELECT error_date
,error_count
,lag(error_count,1) over (order by error_date) prev_count
from error_count
) x
