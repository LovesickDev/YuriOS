from enum import Enum
from datetime import datetime
import time

class LogTypes(Enum):
    DEFAULT = 0
    WARNING = 1
    ERROR = 2
    LOGSYSTEM = 4



class LoggingSystem: #Static Class
    '''Simple complete logging system usable anywhere within the program. (Static)'''
    recordedLogs = []
  
    def log(logmsg, level=LogTypes.DEFAULT):
        '''Append a new log.'''
        logInstance = LogInstance(logmsg, level)
        LoggingSystem.recordedLogs.append(logInstance)

    def error(errorMsg, kill=False):
        LoggingSystem.log(errorMsg, LogTypes.ERROR)
        if kill:    
            LoggingSystem.log("An error caused the program to panic and kill itself. Take a screenshot of the logs or note them. Everything will now shutdown in 30 seconds.", LogTypes.LOGSYSTEM)
            time.sleep(30)

    
    def clean(percentage: float):
        '''Delete a certain percentage of all logs starting by the oldest recorded.'''
        
        amountOfLogsToClear = int(len(LoggingSystem) * percentage)
        for time in range(0, amountOfLogsToClear):
            LoggingSystem.recordedLogs.pop(0)

    

class LogInstance:
    _msg, _type, _time = None

    def __init__(self, message, type: LogTypes) -> None:
        _msg = str(message)
        _type = type
        _time = datetime.now().strftime("%H:%M:%S")
