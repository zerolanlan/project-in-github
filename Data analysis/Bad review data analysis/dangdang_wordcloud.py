from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba

df = pd.read_excel('alive.xlsx', header=None, names=["name", "score", "comment", "date", "up_number", "down_number", "reply_number"])

text = ''
for line in df['comment']:
    text += ' '.join(jieba.cut(line, cut_all=False))
backgroud_Image = plt.imread('book.jpg')
stopwords = set('')
stopwords.update(['没有', '什么', '不是', '知道', '怎么', '就是', '本书', '当当', '这个 商品', '一个', '自己', '真的', '商品 不太好', '一本', '这样', '但是', '现在', '你们', '一直', '以后', '这个', '商品'])

wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    max_words=2000,
    max_font_size=150,
    random_state=30,
    stopwords=stopwords
)
wc.generate_from_text(text)
# 看看词频高的有哪些,把无用信息去除
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e:e[1], reverse=True)
print(sort[:50])
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
wc.to_file("活着.jpg")
print('生成词云成功!')

