import cv2
import numpy as np
from PIL import Image


def inverse_color(image, col_range):
    # 读取图片，0意味着图片变为灰度图
    image = cv2.imread(image, 0)
    # 图片二值化，100为设置阀值，255为最大阀值，1为阀值类型，当前点值大于阀值，设置为0，否则设置为255。ret是return value缩写，代表当前的阀值
    ret, image = cv2.threshold(image, 110, 255, 1)
    # 图片的高度和宽度
    height, width = image.shape
    # 图片反色处理，原因：上面的处理只能生成白字黑底的图片，而我们需要的是黑字白底的图片
    img2 = image.copy()
    for i in range(height):
        for j in range(width):
            img2[i, j] = (255 - image[i, j])
    img = np.array(img2)
    # 对处理后的图片做截取
    height, width = img.shape
    new_image = img[0:height, col_range[0]:col_range[1]]
    cv2.imwrite('handle_one.png', new_image)
    image = Image.open('handle_one.png')
    return image


def clear_noise(img):
    # 图片降噪处理
    x, y = img.width, img.height
    for i in range(x):
        for j in range(y):
            if sum_9_region(img, i, j) < 2:
                # 改变像素点颜色，白色
                img.putpixel((i, j), 255)
    img = np.array(img)
    cv2.imwrite('handle_two.png', img)
    img = Image.open('handle_two.png')
    return img


def sum_9_region(img, x, y):
    """
    田字格
    """
    # 获取当前像素点的颜色值
    cur_pixel = img.getpixel((x, y))
    width = img.width
    height = img.height

    if cur_pixel == 255:  # 如果当前点为白色区域,则不统计邻域值
        return 10

    if y == 0:  # 第一行
        if x == 0:  # 左上顶点,4邻域
            # 中心点旁边3个点
            sum_1 = cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
            return 4 - sum_1 / 255
        elif x == width - 1:  # 右上顶点
            sum_2 = cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1))
            return 4 - sum_2 / 255
        else:  # 最上非顶点,6邻域
            sum_3 = img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
            return 6 - sum_3 / 255

    elif y == height - 1:  # 最下面一行
        if x == 0:  # 左下顶点
            # 中心点旁边3个点
            sum_4 = cur_pixel + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x, y - 1))
            return 4 - sum_4 / 255
        elif x == width - 1:  # 右下顶点
            sum_5 = cur_pixel + img.getpixel((x, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y - 1))
            return 4 - sum_5 / 255
        else:  # 最下非顶点,6邻域
            sum_6 = cur_pixel + img.getpixel((x - 1, y)) + img.getpixel((x + 1, y)) + img.getpixel((x, y - 1)) + img.getpixel((x - 1, y - 1)) + img.getpixel((x + 1, y - 1))
            return 6 - sum_6 / 255

    else:  # y不在边界
        if x == 0:  # 左边非顶点
            sum_7 = img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
            return 6 - sum_7 / 255
        elif x == width - 1:  # 右边非顶点
            sum_8 = img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1))
            return 6 - sum_8 / 255
        else:  # 具备9领域条件的
            sum_9 = img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y)) + img.getpixel((x - 1, y + 1)) + img.getpixel((x, y - 1)) + cur_pixel + img.getpixel((x, y + 1)) + img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y)) + img.getpixel((x + 1, y + 1))
            return 9 - sum_9 / 255


def main():
    img = '1.jpeg'
    img = inverse_color(img, (0, 160))
    clear_noise(img)


if __name__ == '__main__':
    main()
