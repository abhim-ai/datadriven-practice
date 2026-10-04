with unioned as
(SELECT region,svc_name, amount from cloud_costs
union all
SELECT region,svc_name, amount from cost_allocs
)
,
ranked as
(
select region
,svc_name
,row_number() over(partition by region order by amount) lo_rn
,row_number() over(partition by region order by amount desc) hi_rn
from unioned
)

select a.region
,b.svc_name most_expensive
,a.svc_name cheapest
from ranked a
join ranked b
using (region)
where a.lo_rn =1 and b.hi_rn=1
