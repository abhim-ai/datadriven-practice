SELECT svc_name
,checked
,latency
,avg(latency) over (
  PARTITION BY svc_name
  ORDER BY checked
  ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) rolling_avg
from svc_health
