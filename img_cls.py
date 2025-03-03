from langchain_openai import ChatOpenAI
from config import ARK_API_KEY
from config import API_URL
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


def is_malicious_email(email_content):
    # 配置大语言模型
    llm = ChatOpenAI(
        temperature=0,
        openai_api_base=API_URL,
        openai_api_key=ARK_API_KEY,  # app_key
        model_name="deepseek-v3-241226",  # 模型名称
    )

    # 定义输出解析器
    response_schemas = [
        ResponseSchema(name="is_malicious", description="判断邮件是否为恶意邮件，返回True或False", type="bool")
    ]
    parser = StructuredOutputParser.from_response_schemas(response_schemas)

    # 定义提示模板
    prompt_template = """
    判断以下邮件是否为恶意邮件。请按照指定的JSON格式返回结果。

    邮件内容: {email_content}

    {format_instructions}
    """
    prompt = ChatPromptTemplate.from_template(template=prompt_template)

    # 格式化提示
    _input = prompt.format_prompt(email_content=email_content, format_instructions=parser.get_format_instructions())

    # 调用大语言模型并解析输出
    output = llm(_input.to_messages())
    result = parser.parse(output.content)

    return result["is_malicious"]


# 示例调用
if __name__ == "__main__":
    test_email = "这是一封测试邮件，不包含任何恶意信息。"
    result = is_malicious_email(test_email)
    print(f"该邮件是否为恶意邮件: {result}")


    