import pyautogui

# pyautogui.size() # 화면 해상도
# pyautogui.position() # 마우스 현재 커서 (x,y)리턴
# pyautogui.onScreen(x, y) # 스크린 상에 x,y 위치 좌표가 해당하는지 확인 있으면 True

#  마우스
# pyautogui.moveTo(100, 200)
# pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
# pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.

# pyautogui.click(clicks=2)  # double-click the left mouse button
# pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
# pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks
# # 드래그+ 이동
# pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.

# 키보드, *핫키 : 특정 기능 실행시 이용 * 

# pyautogui.keyDown('shift')  # hold down the shift key
# pyautogui.press('left')     # press the left arrow key
# #pyautogui.press(['ctrl', 'shift', 'esc']) 아래의 hotkey와는 다르다.
# pyautogui.hotkey('shift','ctrl','esc') # 핫키 : 작업관리자 인데 pyautogui.press([]) 에선 안됨

# # 키 누른 상태  + 'left' 3번+ 키 누른 상태 때기
# with pyautogui.hold('shift'):
#         pyautogui.press(['left', 'left', 'left'])
# # 위와 동일하게 하려면...
# pyautogui.keyDown('shift')  # hold down the shift key
# pyautogui.press('left')     # press the left arrow key
# pyautogui.press('left')     # press the left arrow key
# pyautogui.press('left')     # press the left arrow key
# pyautogui.keyUp('shift')    # release the shift key

# 메세지 박스(팝업창, )

# pyautogui.alert(text='', title='', button='ok')
# pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])

# dafault는 입력란에 들어가는 문자. 
# 아래처럼 객체로 지정해서 print(input) 해야 입력값이 터미널에 표출 / 객체로 표출안해도 팝업 창이 뜨긴함
# input=pyautogui.prompt(text='test', title='what is title', default='write sth')
# print("input data is ", input)        # 터미널에 입력내용 표출
# pyautogui.alert(text='OK')            # 입력값에 대한 피드백을 팝업창으로...

# 똑같은데 password 팝업창. mask는 입력 될때 보이는 문자. 비번이라 감춰준것
# pw=pyautogui.password(text='Entering PW', title='PW Pop UP', default='password', mask='*')
# print("PW is ", pw)      # 이렇게 해도 나오네. 그런데 None으로 리턴이 오면 안됨


# 스크린 샷
#im1=pyautogui.screenshot('job management.png', region=(0,0,1920,1080))  # 특정 범위, 
pyautogui.hotkey('shift','ctrl','esc') # 핫키 : 작업관리자 

im2=pyautogui.screenshot('job management.png')  # 약 100ms 후 찍는게 default

# 특정 이미지가 있을 때 이미지의 좌표 찾기. 'confidence' 옵션은 
# button7location = pyautogui.locateOnScreen('xxx.png') 
# x,y = pyautogui.locateCenterOnScreen('xxx.png')   # 이미지 위치와 중심 찾기 
# pyautogui.click(x,y)
# 이를 이용해 모르는 위치나 변경된 위치에 있어도 좌표 찾고 -> 해당 좌표를 지정해 액션 명령 

# pixel에 grey scale하면 좀더 빨리 처리가능. 픽셀당 색구분도 가능 
# 더 상세한건 document 참고



