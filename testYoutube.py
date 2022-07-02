from googleapiclient.discovery import build
import json

class YoutubeScraper:
    def __init__(self):
        self.links = []
        self.channelId=[]
        self.channelTitle=[]
        self.publishTime=[]
        self.title=[]
        self.likes=[]
        
    def open_new(self,keyword,results):
        
        #enter your api key here
        api_key='API-KEY'
        youtube=build('youtube','v3',developerKey=api_key)
        request = youtube.search().list(
                        part='snippet',
                        maxResults=results,
                        q=keyword
                    )
        response = request.execute()
        for item in response['items']:
            self.links.append("https://www.youtube.com/watch?v="+item['id']['videoId'])
            self.channelId.append(item['snippet']['channelId'])
            self.channelTitle.append(item['snippet']['channelTitle'])
            self.publishTime.append(item['snippet']['publishedAt'])
            self.title.append(item['snippet']['title'])
        
        for i in self.links:
            response = youtube.videos().list(
                part='statistics',
                id=i.replace("https://www.youtube.com/watch?v=","")
            )
            response = response.execute()
            for item in response['items']:
                self.likes.append(item['statistics']['likeCount'])
        

        print(self.links,self.channelId,self.channelTitle,self.publishTime,self.title,self.likes)

if __name__ == "__main__":
    scraper = YoutubeScraper()
    
    #enter the keyword you want to search
    keyword = "Python"
    
    #enter the number of results you want to get
    results = 1
    scraper.open_new(keyword,results) 