select log_id, server_name, log_level, message, response_time_ms, log_timestamp
from 
(
select *
,row_number() over (partition by server_name,message order by log_timestamp) rn
from server_logs

) x 
where rn=1
and date(current_date- interval '90' days)<=date(log_timestamp)
order by log_timestamp desc
