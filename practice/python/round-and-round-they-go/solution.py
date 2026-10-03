from collections import Counter

def distribute(values: list[int], containers: list[str]) -> list[dict]:
    '''
    Assumptions:
    values and containers will never be empty
    
    Constraints:
    0<values<1001
    containers: ["set,"list","tuple"]
    
    '''
    cnts= Counter(values)
    result=[]
    for idx,val in enumerate(sorted(cnts)):
      container_idx=idx%len(containers)
      if containers[container_idx]=='set':
        values=[val]
      else:
        values = [val]*cnts[val]
      result.append({"values":values,"container":containers[container_idx]})
    return result
      
    
    
