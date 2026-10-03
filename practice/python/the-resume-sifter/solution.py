def filter_new_resumes(urls: list[str], existing_ids: set[str]) -> list[list[str]]:
    '''
    
    urls:["https://resumes.io/abhishek_muthange_82"],[["abhishek_muthange","82"]]
    Constraints:
    each url always the same url prefix
    Edge case:
    urls:[],[]
    
    '''
    result=[]
    #loop over urls list
    for url in urls:
      #slice out url
      split_string=url[19:]
      #split the string on _
      candidate=split_string.rsplit("_",1)
      #if split_string[2] in existing_ids add name,id to result
      if candidate[1] not in existing_ids:
        result.append([candidate[0],candidate[1]])
    return result
   
    
 
