from whatsapp_analyzer.read import read_txt
from whatsapp_analyzer.preprocessor import preprocess
from whatsapp_analyzer.stats import create_wordcloud

data = read_txt("#################")
df = preprocess(data)

create_wordcloud(df)
