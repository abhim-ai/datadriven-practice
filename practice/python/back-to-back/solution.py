def merge_overlapping_time_ranges(intervals: list[list[int]]):
  '''
  intervals: [[1,6],[2,6],[6,10],[8,10],[15,18]]
  output:[[1,10],[15,18]]
  
  Assumptions:
  - the list will contain valid start end values
  
  Cases to handle:
  - Isolated windows i.e no overlap, or adjacent window
  - overlapping windows
  - adjacent windows, win1[len]==win2[0]
  '''
  #create a new result list
  res=[]
  #sort the input
  sorted_ip=sorted(intervals)
  #loop over the sorted input
  for start,end in sorted_ip:
    #check if the curr win's start is within the running window accordingly add to result
    if res and start<=res[-1][1]:
      res[-1][1]=max(end,res[-1][1])
    #if not add a new running window to result
    else:
      res.append([start,end])
  return res
