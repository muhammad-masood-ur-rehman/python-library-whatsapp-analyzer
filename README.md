# Whatsapp Analyzer

A data science-based package that aims to provide insights and analysis on your WhatsApp chat data. Using this package, you can easily import your WhatsApp chat history and visualize the data through various charts and graphs. The package allows you to analyze the most active users in the chat, the most common words used, and the frequency of messages sent at different times.
<br>
Whether you're interested in analyzing your personal chat history or conducting research on communication patterns, the WhatsApp Analyzer package provides a user-friendly platform to visualize and interpret your chat data.






# Installation

    pip install whatsapp-analyzer




# Getting Started

The library is intended to perform data analysis on your group chats or individual chats that can be downloaded from WhatsApp using the proceedure below:

    Go to WhatsApp Chat > tap More options (⋮) > then More > Now tap on Export chat > Choose whether to export without media > your chat history as a .txt document will be available

##  *Reading the Data from .txt File:*

    from whatsapp_analyzer.read import read_txt
    
    data = read_txt("ENTER THE PATH OF THE CHAT FILE")
    
    """ To visualize the data in file"""

    print(data)

##  *Pre-processing the Data from .txt File:*

In order to perform data analysis and visualization on the data it needs to be pre-processed in a way it is understandable to derive the relationships amongst the parameters.

    from whatsapp_analyzer.preprocessor import preprocess
    
    preprocessed_data = preprocess(data)
    
    print(preprocessed_data)`





##  *Visualizing the Data from .txt File:*

There is wide range of options provided to analyze the chat history:

+ Number of Messages: <br>

        from whatsapp_analyzer.stats import message_count

        message_count(preprocessed_data)

+ Number of Media:<br>

        from whatsapp_analyzer.stats import media_count

        media_count(preprocessed_data)

+ Number of Words:<br>

        from whatsapp_analyzer.stats import word_count

        word_count(preprocessed_data)

+ Number of Links:<br>

        from whatsapp_analyzer.stats import links_count

        links_count(preprocessed_data)

+ Most Busy User:<br>

        from whatsapp_analyzer.stats import most_busy_users

        most_busy_users(preprocessed_data)

+ Word Cloud:<br>

        from whatsapp_analyzer.stats import create_wordcloud

        create_wordcloud(preprocessed_data)

+ Frequently Used Words:<br>

        from whatsapp_analyzer.stats import most_common_words

        most_common_words(preprocessed_data)

+ Frequently used Emoji:<br>

        from whatsapp_analyzer.stats import emoji

        emoji(preprocessed_data)

+ Monthly Timeline:<br>

        from whatsapp_analyzer.stats import monthly_timeline

        monthly_timeline(preprocessed_data)

+ Daily Timeline:<br>

        from whatsapp_analyzer.stats import daily_timeline

        daily_timeline(preprocessed_data)

+ Weekly Activity Map:<br>

        from whatsapp_analyzer.stats import week_activity_map

        week_activity_map(preprocessed_data)

+ Monthly Activity Map:<br>

        from whatsapp_analyzer.stats import month_activity_map

        month_activity_map(preprocessed_data)

+ Activity Heat Map:<br>

        from whatsapp_analyzer.stats import activity_heatmap

        activity_heatmap(preprocessed_data)



