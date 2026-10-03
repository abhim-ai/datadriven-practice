with lowest_uptime as
(
select svc_name
,min_uptime
from
  (
SELECT svc_name
,uptime min_uptime
,row_number() over (PARTITION BY svc_name order by uptime) rn
from svc_health
where uptime is not NULL
) x
where rn=1
)

select svc_name
,min_uptime
from
  (
select *
,DENSE_RANK() over (order by min_uptime) as pos
from lowest_uptime) x
where pos<11
