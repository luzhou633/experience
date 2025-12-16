# Python处理《兰亭序》
# homework3.py

# 1. 导入包
import jieba
import jieba.analyse
from collections import Counter

# 2. 读取兰亭序全文
file_path = "d:/luzhou633/repo/experience/课程作业etc/兰亭序.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 3. 统计出现频率最高的字
# 去除非中文字符
text = ''.join(filter(lambda x: '\u4e00' <= x <= '\u9fff', text))

# 统计每个字的频率
char_freq = Counter(text)

# 找出频率最高的字
most_common_char = char_freq.most_common(1)[0]
print(f"出现频率最高的字是：{most_common_char[0]},频率为：{most_common_char[1]}")

# 4. 统计出现频率最高的词
# 使用jieba进行分词
words = jieba.cut(text)

# 去除单字词
filtered_words = [word for word in words if len(word) > 1]

# 使用Counter统计过滤后的词频
filtered_word_freq = Counter(filtered_words)

# 找出频率最高的词
most_common_word = filtered_word_freq.most_common(1)[0]

# 5. 提取关键词
# 使用jieba.analyse提取关键词
keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=False)

# 6. 保存结果到文件
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"出现频率最高的字是:{most_common_char[0]},频率为:{most_common_char[1]}\n")
    f.write(f"出现频率最高的词是:{most_common_word[0]},频率为:{most_common_word[1]}\n")
    f.write(f"提取的关键词为:{keywords}\n")

# 7. 打印输出
print(f"出现频率最高的字是:{most_common_char[0]},频率为:{most_common_char[1]}")
print(f"出现频率最高的词是:{most_common_word[0]},频率为:{most_common_word[1]}")
print(f"提取的关键词为:{keywords}")