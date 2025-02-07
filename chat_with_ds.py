# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

# 请将 <DeepSeek API Key> 替换为你自己的 DeepSeek API Key
client = OpenAI(api_key="sk-bd4f42a599ef430abd05aff9de50b5d1", base_url="https://api.deepseek.com")

# 初始化消息列表，包含系统消息
messages = [
    {"role": "system", "content": "You are a helpful assistant"}
]
stream_mode = True

print("开始对话！输入 '退出' 结束对话。")

while True:
    # 获取用户输入
    user_input = input("你: ")

    # 检查用户是否想要退出对话
    if user_input.lower() == "退出":
        break

    # 将用户输入添加到消息列表中
    messages.append({"role": "user", "content": user_input})

    try:
        # 调用 DeepSeek 模型
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=stream_mode
        )

        if stream_mode:
            print("助手: ", end="")
            for chunk in response:
                chunk_content = chunk.choices[0].delta.content
                print(chunk_content, end="", flush=True)
            print(' ')
        else:
            # 获取模型的回复
            assistant_reply = response.choices[0].message.content

            # 将模型的回复添加到消息列表中
            messages.append({"role": "assistant", "content": assistant_reply})

            # 打印模型的回复
            print(f"助手: {assistant_reply}")

    except Exception as e:
        print(f"发生错误: {e}")

print("对话结束。")
