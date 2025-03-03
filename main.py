from img_cls import is_malicious_email
from read_mail_with_img import process_eml_file

def process_and_detect_email(eml_file_path):
    # 处理 .eml 文件
    sender, receiver, subject, date, html_body_with_ocr = process_eml_file(eml_file_path)
    if sender is None:
        print("无法处理该 .eml 文件，请检查文件路径或文件格式。")
        return None

    # 打印邮件信息
    print(f"发件人: {sender}")
    print(f"收件人: {receiver}")
    print(f"主题: {subject}")
    print(f"日期: {date}")
    print("包含图片 OCR 识别结果的邮件正文:")
    print(html_body_with_ocr)

    # 组合邮件内容
    full_email_content = f"主题: {subject}\n正文: {html_body_with_ocr}"

    # 进行恶意邮件检测
    is_malicious = is_malicious_email(full_email_content)

    return is_malicious

def print_detection_result(is_malicious):
    if is_malicious is None:
        return
    if is_malicious:
        print("该邮件被判定为恶意邮件。")
    else:
        print("该邮件不是恶意邮件。")


if __name__ == "__main__":
    eml_file_path = "ham.eml"
    result = process_and_detect_email(eml_file_path)
    print_detection_result(result)

    eml_file_path = "nham.eml"
    result = process_and_detect_email(eml_file_path)
    print_detection_result(result)

