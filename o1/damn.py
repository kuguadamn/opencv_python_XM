# import cv2 as cv
# # logo = cv.imread('3_1.jpg')
# # print(logo[190,168])
# # 210,148,108
# # logo = cv.imread('3_1.jpg')
# # blue = logo[190,168,0]
# # green = logo[190,168,1]
# #
# # red = logo[190,168,2]
# # # print(red,green,blue)
#
# import numpy as np
# # canvas = np.zeros((500,500,3),np.uint8)
# # cv.imshow('canvas',canvas)
#
# class Canvas:
#     def __init__(self):
#         self._win = 'canvas'
#         self._bar_value_red = 0
#         self._bar_value_green = 0
#         self._bar_value_blue = 0
#         self._bar_name_red = 'red'
#         self._bar_name_green = 'green'
#         self._bar_name_blue = 'blue'
#         self._canvas = np.zeros((500,500,3),np.uint8)
#
#
#     def _setBarConfig(self):
#         cv.namedWindow(self._win)
#         cv.createTrackbar(self._bar_name_red,self._win,0,255,self._callback)
#         cv.createTrackbar(self._bar_name_green, self._win, 0, 255, self._callback)
#         cv.createTrackbar(self._bar_name_blue, self._win, 0, 255, self._callback)
#     def _changeColor(self):
#         self._canvas[:] = (self._bar_value_blue,self._bar_value_green,self._bar_value_red)
#     def _callback(self,input):
#         self._bar_value_red = cv.getTrackbarPos(self._bar_name_red,self._win)
#         self._bar_value_green = cv.getTrackbarPos(self._bar_name_green, self._win)
#         self._bar_value_blue = cv.getTrackbarPos(self._bar_name_blue, self._win)
#         self._changeColor()
#     def run(self):
#         self._setBarConfig()
#         while True:
#             cv.imshow(self._win,self._canvas)
#             if cv.waitKey(1) == ord('q'):
#                 break
