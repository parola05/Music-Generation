import data_collection as dt
import helpers as hp

keywords = [' homophonic ', ' polyphonic ', ' monophonic ', ' heterophonic ', ' a cappella ', ' instrumental ', ' vocal ',
              ' choral ', 'orchestral', ' chamber ', ' symphonic ', ' folk ', ' blues ', ' jazz ', ' rock ', ' classical ',
              ' electronic ', 'hip-hop', ' reggae ', ' country ', ' r&b ', ' heavy metal ', ' punk ', ' alternative ', ' k-pop ',
            ' pop ', ' ambient ', ' gospel ', ' soul ', ' funk ', ' disco ', ' techno ', ' dubstep ', ' opera ',
              ' bluegrass ', ' flamenco ', ' rock ', '-rock ']

dt.generateDataCollection(keywords,"Results/types_of_music_extraction.json")
hp.getNumberOfEachKeywords('Results/types_of_music_extraction.json', 'Results/types_of_music_extraction(2).json', keywords)