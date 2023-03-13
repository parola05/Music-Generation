import data_collection as dt
import json

keywords = []

def articleTalkAbout(article):
    for key in article.keys():
        if key in keywords and len(article[key]) > 0:
            return True

def getNumberOfArticlesByLocation():
    allMetadata = dt.getAllMetaData()
    dataCounts = {}
    metadatas = allMetadata["content"]
    for metadata in metadatas:
        if not metadata["location"] == None:
            for location in metadata["location"]:
                if not location in dataCounts:
                    dataCounts[location] = 1
                else:
                    dataCounts[location] = dataCounts[location] + 1
    
    with open("Results/locationResults" + ".json", 'w') as f:
        json.dump(dataCounts, f, indent=4)

def getNumberOfArticlesByMusicType():
    allMetadata = dt.getAllMetaData()
    dataCounts = {}
    metadatas = allMetadata["content"]
    for metadata in metadatas:
        print("\n\n\n\n\n\nmetadata: ",metadata)
        if not metadata["location"] == None:
            for location in metadata["location"]:
                if not location in dataCounts:
                    dataCounts[location] = 1
                else:
                    dataCounts[location] = dataCounts[location] + 1
    
    with open("Results/locationResults" + ".json", 'w') as f:
        json.dump(dataCounts, f, indent=4)

getNumberOfArticlesByMusicType()