from time import time
from rich.console import Console
console=Console()
def send_Msg(msg):
    if isinstance(msg,BaseMsg):
        console.print(msg,style=msg.style)
    else:
        print(msg)
class BaseMsg:
    def __init__(self,data:str):
        self._data=data

    @property
    def style(self)->str:
        return ''
    
    @property
    def data(self):
        return self._data
    
    def __str__(self):
        return self._data
    def __len__(self):
        return len(str(self))
 
    def __eq__(self, other):
        return str(self)==str(other)

    def __add__(self,other):
        new_data= str(self)+str(other)
        return self.__class__(new_data)
class LogMsg(BaseMsg):
    def __init__(self, data: str):
        super().__init__(data)
        self._timestamp:int=int(time())
    @property
    def style(self) ->str:
        return "black on yellow"
    def __str__(self):
        return f"[{self._timestamp}] {self._data}"

class WarnMsg(LogMsg):
    def __init__(self,data:str):
        super().__init__(data)
    @property
    def style(self) ->str:
        return "white on red"
    def __str__(self):
        return f"[!WARN][{self._timestamp}] {self._data}"

from task2_2 import BaseMsg,LogMsg,WarnMsg,send_Msg
if __name__=='__main__':
    msg1=BaseMsg('Normal Message')
    msg2=LogMsg('Log')
    msg3=WarnMsg('Warning')

    send_Msg(msg1)
    send_Msg(msg2)
    send_Msg(msg3)
    
    #test
    msg4 = msg1+ "Extra Message"
    send_Msg(msg4)

    print("length of msg4 is:",len(msg4))
    print("type of msg4 is:", type(msg4))
    print("msg1==msg4",msg1==msg4)

