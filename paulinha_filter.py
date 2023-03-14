import data_collection as dt
import json

musicTypes = [' homophonic ', ' polyphonic ', ' monophonic ', ' heterophonic ', ' a cappella ', ' instrumental ', ' vocal ',
              ' choral ', 'orchestral', ' chamber ', ' symphonic ', ' folk ', ' blues ', ' jazz ', ' rock ', ' classical ',
              ' electronic ', 'hip-hop', ' reggae ', ' country ', ' r&b ', ' heavy metal ', ' punk ', ' alternative ', ' k-pop ',
            ' pop ', ' ambient ', ' gospel ', ' soul ', ' funk ', ' disco ', ' techno ', ' dubstep ', ' opera ',
              ' bluegrass ', ' flamenco ', ' rock ', '-rock ']
#architectures = ['RNN', 'Recurrent Neural Network', 'VAE', 'Variational Autoencoder', 'GAN', 'Generative Adversarial Network',
#                 'Transformer-based', 'Tranformer', 'Hierarchical', 'Neural Autoregressive', 'NAM', 'Deep Belief Network', 'DBN',
#                 'Markov Chain Monte Carlo', 'MCMC', 'Boltzmann Machines', 'BM', 'Hopfield Network']

architectures = ['RNN', 'Recurrent Neural Network', 'VAE', 'Variational Autoencoder', 'GAN', 'Generative Adversarial Network',
                 'Transformer-based', 'Tranformer']

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
    # dt.generateDataCollection(musicTypes,'musicTypesFiltered')
    f = open('musicTypesFiltered.json', encoding='utf-8')
    data = json.load(f)
    dataCounts = {}
    for group in data['data_collection']:
        for type in group:
            if type != 'title' and group[type] != []:
                if not type in dataCounts:
                    dataCounts[type] = 1
                else:
                    dataCounts[type] = dataCounts[type] + 1

    with open("Results/musicTypeResults" + ".json", 'w') as f:
        json.dump(dataCounts, f, indent=4)

def getNumberOfArticlesByArchitecture():
    dt.generateDataCollection(architectures,'architecturesFiltered')
    f = open('architecturesFiltered.json', encoding='utf-8')
    data = json.load(f)
    dataCounts = {}
    for group in data['data_collection']:
        for type in group:
            if type != 'title' and group[type] != []:
                if not type in dataCounts:
                    dataCounts[type] = 1
                else:
                    dataCounts[type] = dataCounts[type] + 1

    with open("Results/architecturesResults" + ".json", 'w') as f:
        json.dump(dataCounts, f, indent=4)

# getNumberOfArticlesByLocation()
# getNumberOfArticlesByMusicType()
getNumberOfArticlesByArchitecture()