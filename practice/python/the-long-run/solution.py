def run_length_encoding(s: str):
  l=r=0
  res=str()
  while r<len(s):
    while r<len(s) and s[l]==s[r]:
      r+=1
    res=res+s[l]+str(r-l)
    l=r
  return res
