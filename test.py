import pyautogui
import matplotlib.pyplot as plt
# im = pyautogui.screenshot(region=(301,39, 1197-301, 73-39))
# imgplot = plt.imshow(im)
# plt.show()
import tkinter as tk
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
x, y = canvas1.winfo_rootx(), canvas1.winfo_rooty()
w, h = canvas1.winfo_width(), canvas1.winfo_height()
pyautogui.screenshot('screenshot.png', region=(x, y, w, h))
root.mainloop()