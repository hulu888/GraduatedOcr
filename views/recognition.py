import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import paddlehub as hub


def reg_image(img_path):
    # 待预测图片
    test_img_path = ['./images/000559.jpg', ]

    # 展示其中广告信息图片
    # img1 = mpimg.imread(test_img_path[0])
    # plt.figure(figsize=(10,10))
    # plt.imshow(img1)
    # plt.axis('off')
    # plt.show()

    ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")
    # images = [cv2.imread(img) for img in test_img_path]
    images = [cv2.imread(img) for img in img_path]
    results = ocr.recognize_text(
        images=images,  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
        use_gpu=False,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
        output_dir='static/ocr_result',  # 图片的保存路径，默认设为 ocr_result；
        visualization=True,  # 是否将识别结果保存为图片文件；
        box_thresh=0.5,  # 检测文本框置信度的阈值；
        text_thresh=0.5)  # 识别中文文本置信度的阈值；

    # for result in results:
    #     data = result['data']
    #     save_path = result['save_path']
    #     for infomation in data:
    #         print('text: ', infomation['text'], '\nconfidence: ', infomation['confidence'], '\ntext_box_position: ',
    #               infomation['text_box_position'])
    return results
