import cv2

# 获取视频
video = cv2.VideoCapture('007.mp4')

# 生成椭圆结构元素
es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 4))
# 设置背景帧
background = None

while True:
    # 读取视频每一帧
    ret, frame = video.read()

    # 获取背景帧
    if background is None:
        # 将视频的第一帧图像转为灰度图
        background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 对灰度图进行高斯模糊,平滑图像
        background = cv2.GaussianBlur(background, (21, 21), 0)
        continue

    # 将视频的每一帧图像转为灰度图
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 对灰度图进行高斯模糊,平滑图像
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # 获取当前帧与背景帧之间的图像差异,得到差分图
    diff = cv2.absdiff(background, gray_frame)

    # 利用像素点值进行阈值分割,得到一副黑白图像
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    # 膨胀图像,减少错误
    diff = cv2.dilate(diff, es, iterations=2)

    # 得到图像中的目标轮廓
    image, cnts, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 1500:
            continue
        # 绘制目标矩形框
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x+2, y+2), (x+w, y+h), (0, 255, 0), 2)

    # 显示检测视频
    cv2.namedWindow('contours', 0)
    cv2.resizeWindow('contours', 600, 400)
    cv2.imshow('contours', frame)

    # 显示差异视频
    cv2.namedWindow('diff', 0)
    cv2.resizeWindow('diff', 600, 400)
    cv2.imshow('diff', diff)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# 结束
cv2.destroyAllWindows()
video.release()
