import cv2
image_folder = 'DeepFashion2/train/example_small/image'
id_sample = '/001928'
image_file = image_folder + id_sample + '.jpg'
lowThreshold = 0
max_lowThreshold = 100


def sobel_edge():   # Sobel边缘检测算子
    img_gray = cv2.imread(image_file, 0)
    x = cv2.Sobel(img_gray, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img_gray, cv2.CV_16S, 0, 1)
    # cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
    # 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
    Scale_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
    Scale_absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
    cv2.imshow('gray_img', img_gray)
    cv2.imshow('Scale_absX', Scale_absX)
    cv2.imshow('Scale_absY', Scale_absY)
    cv2.imshow('result', result)
    cv2.waitKey(0)


def scharr_edge() :       # Scharr算子
    img = cv2.imread(image_file, 0)
    x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=-1)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=-1)
    # ksize=-1 Scharr算子
    # cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
    # 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
    Scharr_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
    Scharr_absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(Scharr_absX, 0.5, Scharr_absY, 0.5, 0)
    cv2.imshow('img', img)
    cv2.imshow('Scharr_absX', Scharr_absX)
    cv2.imshow('Scharr_absY', Scharr_absY)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def laplace_edge():
    img = cv2.imread(image_file, 0)
    laplacian = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
    dst = cv2.convertScaleAbs(laplacian)
    cv2.imshow('laplacian', dst)
    blur = cv2.GaussianBlur(img, (3, 3), 0)
    laplacian2 = cv2.Laplacian(blur, cv2.CV_16S, ksize=3)
    dst2 = cv2.convertScaleAbs(laplacian2)
    cv2.imshow('laplacian_gauss', dst2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def CannyThreshold(lowThreshold):
    img = cv2.imread(image_file, 0)
    ratio = 3
    kernel_size = 3
    detected_edges = cv2.GaussianBlur(img,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold, lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)


def canny_edge():
    img = cv2.imread(image_file, 0)
    img = cv2.GaussianBlur(img, (3, 3), 0)  # 用高斯滤波处理原图像降噪
    cv2.namedWindow('canny demo')
    cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)
    CannyThreshold(0)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()


if __name__ == '__main__':
    method = int( input( "> " ) )
    if( method == 1):
        sobel_edge()
    elif(method == 2):
        scharr_edge()
    elif(method == 3):
        laplace_edge()
    elif(method == 4):
        canny_edge()