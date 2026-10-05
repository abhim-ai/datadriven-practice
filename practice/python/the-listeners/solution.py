from collections import defaultdict

class EventEmitter:
  def __init__(self):
    self.listener_state=defaultdict(list)#{"click":["log_click"]}
   
  def on(self,event:str,listener:str)->None:
   self.listener_state[event].append(listener)

  def off(self,event:str,listener:str)->None:
    if listener in self.listener_state[event]:
       self.listener_state[event].remove(listener) 

  def emit(self,event:str,payload:str)->None:
   return [payload]*len(self.listener_state[event])


def event_broadcaster(op_names: list[str], op_args: list[list]) -> list:
  collected,res=[],[]
  op_arg,op_name,emitter=[],None,None

  for i in range(len(op_names)):
    op_arg=op_args[i]
    op_name=op_names[i]
    
    if op_name=="EventEmitter":
      emitter=EventEmitter()
      collected.append(None)
    elif op_name=="on":
      emitter.on(op_arg[0],op_arg[1])
      collected.append(None)
    elif op_name=="off":
      emitter.off(op_arg[0],op_arg[1])
      collected.append(None)
    else:
      res=emitter.emit(op_arg[0],op_arg[1])
      collected.append(res)
      
  return collected
  

  '''
  op_args
  :
  [
  [],
  ["click","log_click"],
  ["click","log_click_1"],
  ["click","event1"],
  ["click","log_click"],
  ["click","event2"],
  ]

  op_names
  :
  ["EventEmitter","on","on","emit","off","emit"]

  [null,null.null,["event1","event1"]]

  '''
