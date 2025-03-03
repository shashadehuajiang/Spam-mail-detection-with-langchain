import email
from email.parser import Parser
from paddleocr import PaddleOCR
import os

# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

def read_eml_file(eml_file_path):
    """
    读取 .eml 文件内容
    :param eml_file_path: .eml 文件的路径
    :return: 文件内容
    """
    try:
        with open(eml_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件 {eml_file_path} 未找到。")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

def parse_email(eml_content):
    """
    解析邮件内容，提取发件人、收件人、主题、日期和正文
    :param eml_content: 邮件内容
    :return: 发件人、收件人、主题、日期、邮件正文
    """
    parser = Parser()
    msg = parser.parsestr(eml_content)
    sender = msg["From"]
    receiver = msg["To"]
    subject = msg["Subject"]
    date = msg["Date"]
    html_body = ""
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            html_body = part.get_payload(decode=True).decode('utf-8')
            break
    return sender, receiver, subject, date, html_body, msg

def extract_images_and_ocr(msg):
    """
    提取邮件中的图片并进行 OCR 识别
    :param msg: 解析后的邮件对象
    :return: 图片 Content-ID 与 OCR 识别结果的映射
    """
    image_cid_mapping = {}
    for part in msg.walk():
        if part.get_content_maintype() == 'image':
            # 获取图片的 Content-ID
            content_id = part.get('Content-ID').strip('<>')
            # 保存图片到临时文件
            image_filename = f"{content_id}.jpg"
            try:
                with open(image_filename, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                # 进行 OCR 识别
                result = ocr.ocr(image_filename, cls=True)
                ocr_text = ""
                for line in result[0]:
                    ocr_text += line[1][0] + "\n"
                image_cid_mapping[content_id] = ocr_text
            except Exception as e:
                print(f"处理图片 {content_id} 时发生错误: {e}")
            finally:
                # 删除临时图片文件
                if os.path.exists(image_filename):
                    os.remove(image_filename)
    return image_cid_mapping

def insert_ocr_results(html_body, image_cid_mapping):
    """
    将 OCR 识别结果插入到邮件正文的对应位置
    :param html_body: 邮件正文
    :param image_cid_mapping: 图片 Content-ID 与 OCR 识别结果的映射
    :return: 包含 OCR 识别结果的邮件正文
    """
    for cid, text in image_cid_mapping.items():
        placeholder = f'<img src="cid:{cid}">'
        ocr_text_html = f'<p>图片 OCR 识别结果:</p><pre>{text}</pre>'
        html_body = html_body.replace(placeholder, placeholder + ocr_text_html)
    return html_body

def process_eml_file(eml_file_path):
    """
    处理 .eml 文件，完成邮件信息提取和图片 OCR 识别
    :param eml_file_path: .eml 文件的路径
    :return: 发件人、收件人、主题、日期、包含 OCR 识别结果的邮件正文
    """
    eml_content = read_eml_file(eml_file_path)
    if eml_content is None:
        return None, None, None, None, None
    sender, receiver, subject, date, html_body, msg = parse_email(eml_content)
    image_cid_mapping = extract_images_and_ocr(msg)
    html_body_with_ocr = insert_ocr_results(html_body, image_cid_mapping)
    return sender, receiver, subject, date, html_body_with_ocr

# 示例调用
if __name__ == "__main__":
    eml_file_path = "ham.eml"
    sender, receiver, subject, date, html_body_with_ocr = process_eml_file(eml_file_path)
    if sender is not None:
        print(f"发件人: {sender}")
        print(f"收件人: {receiver}")
        print(f"主题: {subject}")
        print(f"日期: {date}")
        print("包含图片 OCR 识别结果的邮件正文:")
        print(html_body_with_ocr)
        

