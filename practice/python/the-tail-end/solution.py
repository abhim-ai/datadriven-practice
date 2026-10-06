# class MinStack:
#   def __init__(self):
#     self.stk=[]
#   def push(self, value):
#     self.stk.append(value)
#   def pop(self):
#     return self.stk.pop() if self.stk else None
#   def peek(self):
#     # print("stk peeked: ",self.stk[-1])
#     return self.stk[-1] if self.stk else None
#   def is_empty(self):
#     return False if self.stk else True
#   def min(self):
#     return min(self.stk) if self.stk else None
# def the_tail_end(operations):
#   '''
#   '''
#   minstk=MinStack()
#   # print("MinStack Initialised:",minstk,"stk:",minstk.stk)
#   res=[]
#   for op_call in operations:
#     op=op_call[0]
#     val=op_call[1] if len(op_call)>1 else None
#     # print(op,val)
#     if op=='push':
#       minstk.push(val)
#       # print(minstk.stk)
#       res.append(None)
#     elif op=='pop':
#       res.append(minstk.pop())
#     elif op=='min':
#       res.append(minstk.min())
#     elif op=='peek':
#       res.append(minstk.peek())
#     elif op=='is_empty':
#       res.append(minstk.is_empty())
#   return res


class MinStack:
  def __init__(self):
    self.stk=[]
  def push(self, value):
    self.stk.append(value)
  def pop(self):
    return self.stk.pop() if self.stk else None
  def peek(self):
    # print("stk peeked: ",self.stk[-1])
    return self.stk[-1] if self.stk else None
  def is_empty(self):
    return False if self.stk else True
  def min(self):
    return min(self.stk) if self.stk else None
def the_tail_end(operations):
  '''
  '''
  minstk=MinStack()
  # print("MinStack Initialised:",minstk,"stk:",minstk.stk)
  res=[]
  for op,*val in operations:
    if op=='push':
      minstk.push(val[0])
      # print(minstk.stk)
      res.append(None)
    elif op=='pop':
      res.append(minstk.pop())
    elif op=='min':
      res.append(minstk.min())
    elif op=='peek':
      res.append(minstk.peek())
    elif op=='is_empty':
      res.append(minstk.is_empty())
  return res
