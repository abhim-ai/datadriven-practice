def run_length_encoding(s: str):
  # l=r=0
  # res=str()
  # while r<len(s):
  #   while r<len(s) and s[l]==s[r]:
  #     r+=1
  #   res=res+s[l]+str(r-l)
  #   l=r
  # return res
  if len(s)<1:
    return ""
  count=1
  res=[]
  for i in range(1,len(s)):
    if s[i]==s[i-1]:
      count+=1
    else:
      res.append(s[i-1]+str(count))
      count=1
  res.append(s[-1]+str(count))
  return "".join(res)
