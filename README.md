# README for Malicious Email Detection Project

## Project Overview

This project aims to implement a malicious email detection system based on a large language model. By parsing email files in `.eml` format, it extracts key information of the email (such as sender, recipient, subject, date, and body content), converts images to text using OCR, and combines with a large language model to determine whether the email is malicious.

## Project Structure



```
project\_root/

├── img\_cls.py              # Contains functions for malicious email detection

├── read\_mail\_with\_img.py   # Contains functions for processing .eml files

├── main.py                 # Main program entry

├── config.py               # Configuration file, containing API keys and other information

├── ham.eml                 # Example email file

└── README.md               # Project description document
```

## Environment Requirements

Python 3.x

Install the required Python libraries using the following command:



```
pip install langchain langchain-openai pydantic
```

## Configuration Instructions

In the `config.py` file, you need to configure the `ARK_API_KEY`, which is used to access the large language model API. An example is as follows:



```
API\_URL = "your api url here"

ARK\_API\_KEY = "your\_api\_key\_here"
```

## Usage Steps

**Prepare the email file**: Place the `.eml` file to be detected in the project directory, or modify the `eml_file_path` variable in `main.py` to the actual file path.

**Run the main program**: Execute the following command in the terminal to run the main program:



```
python main.py
```

**View the results**: The program will output the key information of the email and give the detection result of whether the email is malicious.

## Code Explanation

### `img_cls.py`

`is_malicious_email(email_content)`** function**: Accepts the email content as input, calls the large language model to determine whether the email is malicious, and returns a boolean value.

### `read_mail_with_img.py`

`process_eml_file(eml_file_path)`** function**: Processes the `.eml` file, extracts the sender, recipient, subject, date, and the email body with OCR recognition results of images, and returns this information.

### `main.py`

Calls the `process_eml_file` function to process the `.eml` file and extract email information.

Combines the email subject and body content, and calls the `is_malicious_email` function for malicious email detection.

Outputs the email information and the detection result.

## Notes

Ensure that the `ARK_API_KEY` in the `config.py` file is valid, otherwise the large language model cannot be called normally.

The judgment results of the large language model may be affected by various factors, such as the training data of the model and the complexity of the email content, so the results are for reference only.

If the processing of the `.eml` file fails, the program will output the corresponding error message. Please check the file path or file format.

## 恶意邮件检测项目 README

### 项目概述

本项目旨在实现一个基于大语言模型的恶意邮件检测系统，通过解析 `.eml` 格式的邮件文件，提取邮件的关键信息（如发件人、收件人、主题、日期和正文内容），使用 ocr 将图片转为文本，并结合大语言模型判断邮件是否为恶意邮件。

### 项目结构



```
project\_root/

├── img\_cls.py              # 包含恶意邮件检测函数

├── read\_mail\_with\_img.py   # 包含处理 .eml 文件的函数

├── main.py                 # 主程序入口

├── config.py               # 配置文件，包含 API 密钥等信息

├── ham.eml                 # 示例邮件文件

└── README.md               # 项目说明文档
```

### 环境要求

Python 3.x

安装所需的 Python 库，可以使用以下命令进行安装：



```
pip install langchain langchain-openai pydantic
```

### 配置说明

在 `config.py` 文件中，需要配置 `ARK_API_KEY`，该密钥用于访问大语言模型 API。示例如下：



```
API\_URL = "your api url here"

ARK\_API\_KEY = "your\_api\_key\_here"
```

### 使用步骤

**准备邮件文件**：将需要检测的 `.eml` 文件放在项目目录下，或者修改 `main.py` 中的 `eml_file_path` 变量为实际的文件路径。

**运行主程序**：在终端中执行以下命令运行主程序：



```
python main.py
```

**查看结果**：程序将输出邮件的关键信息，并给出该邮件是否为恶意邮件的检测结果。

### 代码说明

#### `img_cls.py`

`is_malicious_email(email_content)`** 函数**：接受邮件内容作为输入，调用大语言模型判断邮件是否为恶意邮件，并返回布尔值。

#### `read_mail_with_img.py`

`process_eml_file(eml_file_path)`** 函数**：处理 `.eml` 文件，提取发件人、收件人、主题、日期和包含图片 OCR 识别结果的邮件正文，并返回这些信息。

#### `main.py`

调用 `process_eml_file` 函数处理 `.eml` 文件，提取邮件信息。

组合邮件主题和正文内容，调用 `is_malicious_email` 函数进行恶意邮件检测。

输出邮件信息和检测结果。

### 注意事项

确保 `config.py` 文件中的 `ARK_API_KEY` 是有效的，否则无法正常调用大语言模型。

大语言模型的判断结果可能受到多种因素的影响，如模型的训练数据、邮件内容的复杂性等，因此结果仅供参考。

若处理 `.eml` 文件失败，程序将输出相应的错误信息，请检查文件路径或文件格式。


