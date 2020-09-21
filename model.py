

from heapq import nlargest
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
text = "India is known for diversity in the region, diversity in languages, diversity in food, diversity in clothing, diversity in the festival, diversity in states, diversity in everything that represents the world. country and its people. India is a country of the republic that is for the people, by the people and by the people. People run their county, people choose their own leader, and people are independent of everything. India is a country where people are changed according to their location. Each state has its incredible beauty of heritage as well as the nation. Each state has its own history of religion. In the fields of literature and science, my country has produced a prominent personality such as Rabindranath Tagore, Premchand , Sara Chandra, Raman CV, Jagadish Chandra Bose and Dr. Abdul Kalama. These big names make me proud of my country. My country is a land of villages and fields full of bodies. I am proud of his village from which the Indian civilization flourished. Most of the great leaders of our country came from villages. Our fields are fed by mighty rivers like Ganges, Yamuna, Brahmaputra, Godavari, Narmada, Krishna and Kavery. The   Gangetic Valley is the most fertile region of our country. The oceans bathing its shores on three sides and the mighty Himalayas to the north have given my country natural boundaries. Once again, the attraction of the mountain has attracted many adventures to this land of rich culture. Our state is secular. On his knees breathe the happy disciples of the different religions of the world. We have a unique culture that has vested throughout the centuries. There is a lot of diversity among our people. We speak several languages, we worship many gods and yet we have the same spirit, the spirit of India, which crosses all parts of our country and binds us all together. We have a great unity in diversity. Basically, Indian culture is tolerant and absorbing. His nature is assimilative. The democratic installation facilitates the process. Diversity in all aspects of society serves as a source of strength and wealth. The different ways of worshiping and believing represent the underlying uniformity      . They promote a spirit of harmony and fraternity. This goes beyond all considerations of religious, regional, linguistic diversity. India is rich in dialects and languages. Twenty-two languages constitutionally enjoy official language status, but Hindi is recognized as the lingua franca of the nation. From Kashmir to Kanyakumari and from Nagaland to Mumbai, Hindi is understood as the national language of India. Although different regions have different regional affiliations, they are all Indian. People are called Bihari , Punjabi, Kashmiri, Marathi, Gujarati, but they are proud to say that they are Indians. Indian dance and theatre are brilliant examples of unity in diversity. The country is full of tribal dances, folk dances, and classical dances of great virtuosity. They are considered as the mode of aesthetic expression but they all symbolize India. The expression is different but the theme is the same. "


stopWords = list(STOP_WORDS)

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)
tokens = [token.text for token in doc]


# new line is not available
# add new line in punctuation
punctuation = punctuation+'\n'


word_freq = {}
for word in doc:
    if word.text.lower() not in stopWords:
        if word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1


# normalization of frequency
# formula = each word frequency / max_freq
max_freq = max(word_freq.values())
for word in word_freq.keys():
    word_freq[word] = word_freq[word]/max_freq


sentence_tokens = [sent for sent in doc.sents]

# Calculating  sentence scores
sentence_score = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_freq.keys():
            if sent not in sentence_score.keys():
                sentence_score[sent] = word_freq[word.text.lower()]
            else:
                sentence_score[sent] += word_freq[word.text.lower()]


select_len = int(len(sentence_tokens)*0.05)
summary = nlargest(select_len, sentence_score, key=sentence_score.get)


final_summary = [word.text for word in summary]
Summary = ' '.join(final_summary)
print(Summary)
