import random
import sys
import threading
import time
import tkinter
import tkinter.messagebox

import easyocr
import numpy
import pyautogui
import win32gui

# from pynput import keyboard
#
#
# def on_activate_o():
#     print('<ctrl>+<alt>+o pressed')
#
# def on_activate_i():
#     print('<ctrl>+<alt>+i pressed')


# import pynput

from pynput import keyboard

def on_press(key):
    '按下按键时执行。'
    try:
        if key.char=='o':
          print("o")
          openCallBack()
        elif key.char == 'p':
          print("p")
          stopCallBack()
    except AttributeError:
      print('.')
    #通过属性判断按键类型。

def on_release(key):
    '松开按键时执行。'
    if key == keyboard.Key.esc:
        # Stop listener
        return False





exStatus = 0

def clickReady():
  print('点击准备')
  try:
    pyautogui.moveTo((2*w_start_d+w_d)/2+(w_d/3), (2*h_start_d+h_d)/2)  # 移动到 (100,100)
    pyautogui.mouseDown()  # 鼠标左键按下再松开
    time.sleep(0.5)
    pyautogui.mouseUp()
    pyautogui.mouseUp()
    time.sleep(0.1)
  except:
    print('点击失败')

def clickTaskFinsh():
  print('点击插件')
  try:
    pyautogui.moveTo(500, 300)  # 移动到 (100,100)
    pyautogui.mouseDown()  # 鼠标左键按下再松开
    time.sleep(0.3)
    pyautogui.mouseUp()
    pyautogui.mouseUp()
    time.sleep(0.1)
  except:
    print('点击失败')

def movePlayer():
  time.sleep(0.1) # 准备时间
  print('移动鸭子')
  try:
    pyautogui.keyDown('W')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('W')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyDown('D')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('D')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyDown('S')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('S')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyDown('A')
    time.sleep(random.uniform(0.05, 0.1))
    pyautogui.keyUp('A')
    time.sleep(random.uniform(0.05, 0.1))
  except:
    print('任务移动失败')



def getScreen():
  print('截屏')
  try:
    img = pyautogui.screenshot(region=(w_start_d, h_start_d, w_d ,h_d))
    print(w_start_d, h_start_d, w_d ,h_d)
    img.save("goose.jpg")
    im =  numpy.array(img)
    return im
  except:
    print('截屏失败')


def getGameStatus(img):
  time.sleep(0.1) # 准备时间
  print('获取状态')
  try:
    print("开始识别")
    results = reader.readtext(img)
    if len(results) != 0 :
      for result in results:
        print(result[1])
        if "你" in result[1]:
          print("你已经准备好了")
        elif "已" in result[1]:
          print("你已经准备好了")
        elif "经" in result[1]:
          print("你已经准备好了")
        elif "好" in result[1]:
          print("你已经准备好了")
        elif "了" in result[1]:
          print("你已经准备好了")
        elif "开" in result[1] :
          print("开始游戏")
          clickReady()
        elif "始" in result[1]:
          print("开始游戏")
          clickReady()
        elif "游" in result[1]:
          print("开始游戏")
          clickReady()
        elif "戏" in result[1]:
          print("开始游戏")
          clickReady()
        elif "点" in result[1] :
          print("点击准备")
          clickReady()
        elif "击" in result[1]:
          print("点击准备")
          clickReady()
        elif "准" in result[1]:
          print("点击准备")
          clickReady()
        elif "备" in result[1]:
          print("点击准备")
          clickReady()
        elif "观" in result[1]:
          print("观察者")
          clickReady()
        elif "察" in result[1]:
          print("观察者")
          clickReady()
        elif "者" in result[1]:
          print("观察者")
          clickReady()
        else:
          print("识别有误")
          movePlayer()
          # clickTaskFinsh()
          time.sleep(0.5)
    else:
      print("空闲时间")
      movePlayer()
      #点击任务完成,这个位置需要调整
      # clickTaskFinsh()
      time.sleep(0.3)



  except:
    print('游戏状态获取失败')


# 角色挂机检测 准备识别 开始识别 任务警告识别 挂机识别

def testCallBack():
  print('截屏')
  try:
    # img = pyautogui.screenshot()
    # img.save("all.jpg")
    # im = numpy.array(img)
    # results = reader.readtext(im)
    # if len(results) != 0:
    #   for result in results:
    #     if "开始游戏" == result[1]:
    #       print(result)
    # else:
    #   print("失败")
    txt = '窗口的左上角坐标为：（%s,%s）\n窗口的高度为：%s窗口的宽度为：%s' \
          % (top.winfo_x(), top.winfo_y(), top.winfo_width(), top.winfo_height())
    tkinter.messagebox.showinfo("窗口覆盖",txt)

    global w_start_d
    w_start_d = top.winfo_x()
    global h_start_d
    h_start_d = top.winfo_y()
    global w_d
    w_d = top.winfo_width()
    global h_d
    h_d = top.winfo_height()
    print(w_start_d)
    print(h_start_d)
    print(w_d)
    print(h_d)
    print(type(h_d))

    w_start.delete(0,6)
    w_start.insert(0,w_start_d)
    h_start.delete(0,6)
    h_start.insert(0, h_start_d)
    w.delete(0,6)
    w.insert(0, w_d)
    h.delete(0,6)
    h.insert(0, h_d)
    # txt = '窗口的左上角坐标为：（%s,%s）\n窗口的高度为：%s窗口的宽度为：%s' \
    #       % (w_start_d, h_start_d,w_d , h_d)
    # tkinter.messagebox.showinfo("窗口覆盖", txt)

  except:
    print('截屏失败')

def openCallBack():
  print("开启程序")
  if hwnd != 0:
    win32gui.SetForegroundWindow(hwnd)  # 设置前置窗口
    # win32gui.SetFocus(hwnd)  # 设置聚焦窗口
  global exStatus
  exStatus = 1


def stopCallBack():
  print("停止程序")
  global exStatus
  exStatus =0

def closeCallBack():
  print("关闭程序")
  global exStatus
  exStatus =-1
  sys.exit(0)


def selection():
  print("选择")
  print(radio)

# def task():
#   print(".",end='')
#   # print(exStatus)
#   # if exStatus == 1:
#   #   img = getScreen()
#   #   getGameStatus(img)
#   top.after(1000, task)  # reschedule event in 2 seconds

def mainFun():
  img = getScreen()
  getGameStatus(img)

exitFlag = 0

def den():
  print("den")

  # Collect events until released
  with keyboard.Listener(
          on_press=on_press,
          on_release=on_release) as listener:
    listener.join()

  # with keyboard.GlobalHotKeys({
  #   '<ctrl>+<alt>+o': on_activate_o,
  #   '<ctrl>+<alt>+i': on_activate_i}) as h:
  #   h.join()


  # while 1:
  #   with pynput.keyboard.Events() as event:
  #     for i in event:
  #       # 迭代用法。
  #       key_event = i
  #       break
  #
  #     key_event = event.get()
  #     # get用法。
  #     # 可以提供一个实数作为最长等待时间（单位秒），超过这个时间没有事件，
  #     # 就会报错。错误类型是queue模块的Empty，而非TimeoutError。
  #
  #   # 判断事件情况：
  #   if isinstance(key_event, pynput.keyboard.Events.Press):
  #     print('按下按键', end='')
  #   elif isinstance(key_event, pynput.keyboard.Events.Release):
  #     print('松开按键', end='')
  #
  #   # 判断按键：
  #
  #   # *这个事件的`key`属性*对应才是*Listener方法获得的按键`'key'`*。
  #
  #   try:
  #     print(key_event.key.name)
  #   except AttributeError:
  #     # 说明这个是普通按键。
  #     print(key_event.key.char)
  #   else:
  #     # 两种判断方式，第一种是我自创的，第二种是官网上的。`
  #     if key_event.key is pynput.keyboard.Key.o:
  #       print('发生了o键事件。')


def cen():
  print("cen")
  while 1:
    if exStatus == 1:
      # th = threading.Thread(target=mainFun)
      # th.daemon(daemon=True)  # 守护线程
      # th.start()
      # myWindow = win32gui.FindWindow("TkTopLevel", "tk")
      # if myWindow :
      #   win32gui.SetForegroundWindow(myWindow)  # 设置前置窗口
      hwnd = win32gui.FindWindow("UnityWndClass", "Goose Goose Duck")  # 类名，标题
      #onScreen = win32gui.GetForegroundWindow()
      #if  hwnd and onScreen==hwnd:
      time.sleep(0.2)
      if hwnd :
        img = getScreen()
        getGameStatus(img)
      else :
        print(".")



print("本台计算机分辨率为：",pyautogui.size(),type(pyautogui.size()))

# 获取当前鼠标位置
x, y = pyautogui.position()
print("目前光标的位置：",pyautogui.position(),type(pyautogui.position()))

hwnd = win32gui.FindWindow("UnityWndClass", "Goose Goose Duck")
threads = []     #定义一个线程池

t1=threading.Thread(target=den,daemon=True)
threads.append(t1)    #把t1线程装到线程池里

t2=threading.Thread(target=cen,daemon=True)
threads.append(t2)


# model_storage_directory("./model", default = None)
reader = easyocr.Reader(['ch_sim', 'en'],model_storage_directory=".\model")  # this needs to run only once to load the model into memory

top = tkinter.Tk()
# top.geometry("300x160")
radio = 0


O = tkinter.Button(top, text="测试程序", command=testCallBack)
O.pack()
A = tkinter.Button(top, text="开始程序", command=openCallBack)
A.pack()
B = tkinter.Button(top, text="停止程序", command=stopCallBack)
B.pack()
C = tkinter.Button(top, text="关闭程序", command=closeCallBack)
C.pack()

w_start_d=850
h_start_d=1230
w_d=500
h_d=70
w_label = tkinter.Label(top, text="文字识别坐标")
w_label.pack()
w_start = tkinter.Spinbox(top, from_=0, to=5000)
w_start.pack()
h_start = tkinter.Spinbox(top, from_=0, to=3000)
h_start.pack()
w = tkinter.Spinbox(top, from_=0, to=1000)
w.pack()
h = tkinter.Spinbox(top, from_=0, to=500)
h.pack()

w_start.delete(0, 6)
w_start.insert(0, w_start_d)
h_start.delete(0, 6)
h_start.insert(0, h_start_d)
w.delete(0, 6)
w.insert(0, w_d)
h.delete(0, 6)
h.insert(0, h_d)

# R1 = tkinter.Radiobutton(top, text="3214", variable=radio, value=1,command=selection)
# R1.pack()
# R2 = tkinter.Radiobutton(top, text="1323", variable=radio, value=2, command=selection)
# R2.pack()
# 进入消息循环

for t in threads:
  t.start()
# for t in threads:
#   t.join()
  #   time.sleep(0.5)


top.mainloop()

  #   img = pyautogui.screenshot(region=(900, 1230, 400 ,70))
  #   im =  numpy.array(img)
  #   print(img)
    # img.save("goose.jpg")
  # reader = easyocr.Reader(['ch_sim', 'en'])  # this needs to run only once to load the model into memory
  # print("开始识别")
  # a = datetime.now()
  # result = reader.readtext("goose.jpg")
  # b = datetime.now()
  # print(len(result))
  # print(result)
  # print(result[0])
  # print(result[len(result)-1][1])
  # for ret in result:
  #   print(ret[1])
  # print((b-a).seconds)

    # get_mouse_positon()
    # width, height = pyautogui.size()  # 屏幕的宽度和高度
    # print(width, height)

    # currentMouseX, currentMouseY = pyautogui.position()  # 鼠标当前位置
    # print(currentMouseX, currentMouseY)
    # pyautogui.moveTo(1000, 1000, duration=0.25)  # 移动到 (100,100)
    # pyautogui.click()

    # pyautogui.mouseDown()  # 鼠标左键按下再松开
    # pyautogui.mouseUp()

    # pyautogui.keyDown('shift')  # 按下`shift`键
    # pyautogui.keyUp('shift')  # 松开`shift`键

    # img = pyautogui.screenshot()
    # print(img)
    # img.show()

    #pyautogui.screenshot(r'C:\Users\ZDH\Desktop\PY\my_screenshot.png')  # 截全屏并设置保存图片的位置和名称
    #im = pyautogui.screenshot(r'C:\Users\ZDH\Desktop\PY\my_screenshot.png')  # 截全屏并设置保存图片的位置和名称
    #print(im)  # 打印图片的属性

