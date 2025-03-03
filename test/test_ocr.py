# import easyocr

# # 创建阅读器对象，指定识别语言
# reader = easyocr.Reader(['en', 'ch_sim'])
# # 进行文字提取
# result = reader.readtext('example.jpg')
# for (bbox, text, prob) in result:
#     print(f'Text: {text}, Probability: {prob}')


from paddleocr import PaddleOCR

# 创建OCR对象
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# 进行OCR识别
result = ocr.ocr('example.jpg', cls=True)

# 提取识别结果中的文本
for line in result:
    for res in line:
        print(res[1][0])
    




