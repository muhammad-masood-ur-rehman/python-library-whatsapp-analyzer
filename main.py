from whatsapp_analyzer.read import read_txt
from whatsapp_analyzer.preprocessor import preprocess
from whatsapp_analyzer.stats import create_wordcloud

data = read_txt(r"E:\WhatsApp Chat with NED SE boys.txt")
df = preprocess(data)
# #st = stats(df)
# #print(st)
# #print(df)
create_wordcloud(df)
