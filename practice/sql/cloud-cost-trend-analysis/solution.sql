select svc_name,bill_date,amount
,amount-lag(amount,1) over (PARTITION BY svc_name order by bill_date) price_change
from cloud_costs
-- where
