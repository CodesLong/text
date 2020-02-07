# _*_ coding utf-8 _*_
# 开发时间：2020/2/421:07
# 开发人员：Administrator
# 文件名称：th_ku
import jieba
# a = jieba.lcut('你好就这样没问题')
# print(a)
from wordcloud import WordCloud
a = """
sjjgjg
sjgig是
世界冠军
哥几个
赛季的冠军而
就是刚刚手机附件二
就覅结果i金额为
经过加工后
"""
list = jieba.lcut(a) # 分词
new_str = ' '.join(list) # 拼接
word_cloud = WordCloud(font_path='msyh.ttc').generate(new_str)
word_cloud.to_file('zj.png')
