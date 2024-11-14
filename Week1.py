# 导入第三方库
from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels
from llama_index.core.base.llms.types import MessageRole, ChatMessage

# 请确保api已经导入到环境变量中

# 初始化大模型，这里选择的是通义千问MAX模型
dashscope_llm = DashScope(model_name=DashScopeGenerationModels.QWEN_MAX)

# 初始化聊天历史记录，使AI可以结合上下文进行回答
conversation_history = [
    ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant.")
]

exit_list = ['退出', '结束', '再见', '拜拜', 'bye', '不聊了', '停聊', '停止对话', '结束聊天', '我不想和你聊天了',
            '不想继续', '不想聊了', '我累了', '先走了', '离开', '不和你聊了', '我要走了', '不再聊', '挂断', '放弃',
            '打住', '够了', '结束了', '好了', '算了', '停止', '暂停', '我有事', '太晚了', '不能继续', '关闭',
            '断开', '我先走了', '今天不聊了', '我不想再聊了', '无聊', '别再说了', '不想再听了', '没兴趣了', 
            '不想再回应了', '不聊这个了', '决定结束', '给我点时间', '我需要休息', '对话结束', '不想继续这个话题', 
            '结束这段对话', '可以停了吗？', '我想安静一下', '离开一会儿', '结束讨论', '别再说了，我要走', '不想继续交流', 
            '对话结束了', '不想回应了', '不再进行对话', '退出对话', '我累了，停一下', '不想和你继续聊下去', '我要结束对话', 
            '够了，我去忙了', '不想再互动了', '这话题没意思', '我有点累了', '不再对话了']

# 多轮对话
while True:

    # 检测用户输入
    content = input('请输入对话内容：')

    # 检测用户是否有结束聊天的意愿
    if content not in exit_list:
        # 若没有结束聊天的意愿

        # 将用户的输入传入
        user_message = ChatMessage(role=MessageRole.USER, content=content)
        # 添加到聊天历史记录中
        conversation_history.append(user_message)


        # 一轮对话
        # 将聊天历史记录传入
        responses = dashscope_llm.stream_chat(conversation_history)

        # 流式输出
        for response in responses:
            print(response.delta, end="")
        print('\n')

        # 将模型的回复也添加到对话历史
        assistant_message = ChatMessage(role=MessageRole.ASSISTANT, content=response.delta)
        conversation_history.append(assistant_message)

    else:
        # 若有结束聊天的意愿
        print('感谢您的咨询，再见')
        break # 退出程序