from collections import defaultdict
def hourly_event_counts(logs: list[tuple[str, str]]) -> dict[str, dict[str, int]]:
  '''
  - It's always sorted

  Assumptions:
  - It's always a valid tuple
  Constraints:
  - 0<=len(logs)<=10^3


  '''

  #Approach 1
  # res={}
  # for i in range(len(logs)):
  #   ts=logs[i][0]
  #   ts_h=ts[:13]
  #   event=logs[i][1]
  #   #create or fetch event_count in res for ts_h
  #   if ts_h not in res:
  #     res[ts_h]={}
  #   event_count=res[ts_h]

  #   #If Event in event_count then increment else add 1 as count
  #   if event in event_count:
  #     event_count[event]+=1
  #   else:
  #     event_count[event]=1
  # return res
        
  # if event in event_count: event_count.add(event_count.get(event)+1)
  # else: event_count={event,1}
  # res={ts_h,event_count}
  
  res=defaultdict(lambda: defaultdict(int))
  for i in range(len(logs)):
    ts_h=logs[i][0][:13]
    event=logs[i][1]
    #increment the event couunt in the res defaultdict
    res[ts_h][event]+=1
    
  return res
    
    
  
