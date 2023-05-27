from typing import Text
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

def clean_text(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())

def maximum(pos, neg, neu):
    if pos >= neg and pos >= neu:
        return 'POSITIVE'
    elif neg >= pos and neg >= neu: 
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'

def make_bar(y_axis, module_name):
    x_axis = ["positive", "neutral", "negative"]
    fig = Figure()
    ax = fig.subplots()
    ax.bar(x_axis, y_axis)
    fig.suptitle(f"Sentiments Analysis of {module_name}")
    fig.supylabel("Number of sentiments")
    fig.supxlabel("Sentiments")
    fig.savefig("bar.png", bbox_inches='tight')

def get_sentiments(dataList, provider, module_name):
  
    positives = 0
    negatives = 0
    neutral = 0
    total = len(dataList)

    print('sentiment calculation began..')

    for content in dataList:
        result = TextBlob(clean_text(content))
        
        polarity = result.sentiment.polarity

        if polarity > 0: 
            positives += 1
        elif polarity == 0:
            neutral +=1
        else: 
            negatives += 1

    report = {'positives': positives, 'negatives': negatives, 'neutral': neutral, 'total': total, 
            'overall': maximum(positives, negatives, neutral), 'source': provider}
    
    text_report= '{0} posts were analyzed:\n{1} were classified as being positive\n{2} were classified as negative\n{3} were classified as neutral\nOveral Sentiment: {4}\n\nData Source: {5}'.format(total, positives, negatives, neutral, 
    maximum(positives, negatives, neutral), provider)

    result = [positives, neutral, negatives]
    make_bar(result, module_name)

    print('generating report')
    
    return text_report
            