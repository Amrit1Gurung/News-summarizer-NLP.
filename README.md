# News-summarizer-NLP.
Newspaper articles is  extracted from the [The kathmandu Post](https://kathmandupost.com/). Only 9 news categories have been  extraced and and each category conatains 20 news articles(today's and last few days news).  

There are two types of summarization in NLP domain, **Extractive** and **Abstractive** summarization. In extractive  summarization We identify the important sentences or phrases from the original text and extract only those from the text whereas in abstractive summarization we generate the new sentences from the original text and the generated sentences through this approach might not be present in the original text. the approach i used here is the former one,  

In this repository there are 2 notebooks, one uses **TfidfVectorizer** and another uses pre-trained **Wikipedia 2014 + Gigaword 5** GloVe vectors with **TextRank** algorithmn. The reason for writing 2 notebooks is to compare the results from 2 notebooks.The summary results were almost camparable and precise. Beside above mentioned approach there are also other approach of text summarization.
