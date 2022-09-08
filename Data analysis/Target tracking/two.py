import cv2

# 获取视频
video = cv2.VideoCapture('traffic.flv')
# KNN背景分割器,设置阴影检测
bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)

while True:
    # 读取视频每一帧
    ret, frame = video.read()
    # 计算视频的前景掩码
    fgmask = bs.apply(frame)
    # 图像阈值化
    th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
    # 膨胀图像,减少错误
    dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)

    # 得到图像中的目标轮廓
    image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) > 1600:
            # 绘制目标矩形框
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

    # 显示差异视频
    cv2.imshow('mog', fgmask)
    # cv2.imshow('thresh', th)
    # 显示检测视频
    cv2.imshow('detection', frame)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()