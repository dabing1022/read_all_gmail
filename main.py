import pyautogui
import time

choose_action_button_region1 = None
choose_action_button_region2 = None
read_action_button_region = None

def read_all(inbox_loc):
	global choose_action_button_region1
	global choose_action_button_region2
	global read_action_button_region
	pyautogui.moveTo(inbox_loc.x, inbox_loc.y, 0.4, pyautogui.easeInQuad)  
	pyautogui.doubleClick()
	print("click inbox {loc}, then sleep 3 seconds.".format(loc=inbox_loc))
	time.sleep(3)
	if not choose_action_button_region1:
		choose_action_button_region1 = pyautogui.locateOnScreen('choose_action_button.png')
	if choose_action_button_region1:
		choose_action_button_loc1 = pyautogui.center(choose_action_button_region1)
		pyautogui.moveTo(choose_action_button_loc1.x, choose_action_button_loc1.y, 0.4, pyautogui.easeInQuad)  
		pyautogui.click()
		print("click choose action1.")
		pyautogui.moveTo(choose_action_button_loc1.x - 100, choose_action_button_loc1.y, 0)
		pyautogui.click()
		time.sleep(0.5)
	
	choose_action_button_region2 = pyautogui.locateOnScreen('choose_action_button2.png')
	if choose_action_button_region2:
		choose_action_button_loc2 = pyautogui.center(choose_action_button_region2)
		pyautogui.moveTo(choose_action_button_loc2.x - 5, choose_action_button_loc2.y, 0.4, pyautogui.easeInQuad)  
		pyautogui.click()
		print("click choose action2.")
		print("choose_action_button_location2 {loc}".format(loc=choose_action_button_loc2))
		time.sleep(0.5)
		
		read_action_button_region = pyautogui.locateOnScreen('read_action_button.png')
		if read_action_button_region:
			read_action_loc = pyautogui.center(read_action_button_region)
			pyautogui.moveTo(read_action_loc.x, read_action_loc.y, 0.4, pyautogui.easeInQuad)  
			pyautogui.click()
			print("click read action {loc}, then sleep 2 seconds".format(loc=read_action_loc))
			time.sleep(1.5)
	
	

if __name__ == "__main__":
	inbox_region = pyautogui.locateOnScreen('inbox.png')
	if inbox_region:
		inbox_location = pyautogui.center(inbox_region)
		while True:
			read_all(inbox_location)
	else:
		print("执行时确保Gmail可以看到")