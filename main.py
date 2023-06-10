import webscrapper, sentimental_analysis, summarizer

url = "###"


if "reddit.com" in url:
    webscrapper.grab_reddit(url)
    
elif "youtube.com" in url:
    webscrapper.grap_youtube(url)
    
else:
    print("error")
    
    
sentimental_analysis.run()

sentimental_analysis.bar_graph()
sentimental_analysis.pie_chart()