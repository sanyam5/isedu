import Utilities
import numpy as np
import json
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from collections import defaultdict
import tldextract
from urlparse import urlparse

def get_user_features():
    user_features = {}
    with open('annotation_data.json') as data_file:
        user_features = json.load(data_file)
    return user_features


def get_html_data():
    with open('data.json') as data_file:
        html_data = json.load(data_file)
    return html_data


def removeunwanted(string):
    string = string.lower()
    if string == "":
        return ""
    stop_words = []
    stop_words = set(stopwords.words('english'))
    list_of_words = [i.lower() for i in wordpunct_tokenize(string) if i.lower() not in stop_words]
    # final = "$$".join(list_of_words)
    final = list_of_words
    return final


def get_html_features(html_data, user_features):
    X = []
    Y = []
    z = []
    links = []
    for key, val in html_data.iteritems():
        if key not in ["142", "200", "986", "321", "259", "305", "807", ] and user_features.has_key(key):
            X.append(removeunwanted(val["text"]))
            y_array = np.asarray(user_features[key]).astype(int)
            Y.append(y_array[1:-3].tolist())
            z.append(y_array[-1].tolist())
            links.append(val['links'])
    return X, Y, z, links


def write_vocab_bigrams(X):
    dic = defaultdict(int)
    for words in X:
        if len(words) < 2:
            continue
        for i in range(0, len(words) - 1):
            dic[words[i] + ':;:' + words[i + 1]] += 1
    # countdict = defaultdict(int)
    # for key in dic.keys():
    #     countdict[dic[key]]+=1
    #
    # print sorted(countdict.keys(), reverse=1)
    # return

    filtered_bigrams = []

    for key in dic.keys():
        if dic[key] >= 10 and dic[key]<=1000:
            filtered_bigrams.append(key)
    print len(filtered_bigrams), " bigrams in vocab."
    with open('bigrams.json', 'w') as fp:
        json.dump(filtered_bigrams, fp)
        # print "Done"

def write_vocab_links(addresses,subdomains,domains,suffices):
    dic = defaultdict(int)
    for words in addresses:
        if len(words) < 1:
            continue
        for i in range(0, len(words)):
            dic[words[i]] += 1

    # countdict = defaultdict(int)
    # for key in dic.keys():
    #     countdict[dic[key]]+=1
    #
    # print sorted(countdict.keys(), reverse=1)
    # return

    filtered_unigrams = []
    for key in dic.keys():
        if dic[key] >= 3 and dic[key]<=1000:
            filtered_unigrams.append(key)
    print len(filtered_unigrams), " addresses in vocab."
    with open('addresses.json', 'w') as fp:
        json.dump(filtered_unigrams, fp)

    dic = defaultdict(int)
    for words in subdomains:
        if len(words) < 1:
            continue
        for i in range(0, len(words)):
            dic[words[i]] += 1

    # countdict = defaultdict(int)
    # for key in dic.keys():
    #     countdict[dic[key]]+=1
    #
    # print sorted(countdict.keys(), reverse=1)
    # return

    filtered_unigrams = []
    for key in dic.keys():
        if dic[key] >= 3 and dic[key]<=2000:
            filtered_unigrams.append(key)
    print len(filtered_unigrams), " subdomains in vocab."
    with open('subdomains.json', 'w') as fp:
        json.dump(filtered_unigrams, fp)

    dic = defaultdict(int)
    for words in domains:
        if len(words) < 1:
            continue
        for i in range(0, len(words)):
            dic[words[i]] += 1

    # countdict = defaultdict(int)
    # for key in dic.keys():
    #     countdict[dic[key]]+=1
    #
    # print sorted(countdict.keys(), reverse=1)
    # return

    filtered_unigrams = []
    for key in dic.keys():
        if dic[key] >= 3 and dic[key]<=1000:
            filtered_unigrams.append(key)
    print len(filtered_unigrams), " domains in vocab."
    with open('domains.json', 'w') as fp:
        json.dump(filtered_unigrams, fp)

    dic = defaultdict(int)
    for words in suffices:
        if len(words) < 1:
            continue
        for i in range(0, len(words)):
            dic[words[i]] += 1

    # countdict = defaultdict(int)
    # for key in dic.keys():
    #     countdict[dic[key]]+=1
    # print dic
    # print sorted(countdict.keys(), reverse=1)
    # return


    filtered_unigrams = []
    for key in dic.keys():
        if dic[key] >= 3 and dic[key]<=10000:
            filtered_unigrams.append(key)
    print len(filtered_unigrams), " suffices in vocab."
    with open('suffices.json', 'w') as fp:
        json.dump(filtered_unigrams, fp)

def write_vocab_unigrams(X):
    dic = defaultdict(int)
    for words in X:
        if len(words) < 1:
            continue
        for i in range(0, len(words)):
            dic[words[i]] += 1

    # countdict = defaultdict(int)
    # for key in dic.keys():
    #     countdict[dic[key]]+=1
    #
    # print sorted(countdict.keys(), reverse=1)
    # return

    filtered_unigrams = []
    for key in dic.keys():
        if dic[key] >= 5 and dic[key]<=5000:
            filtered_unigrams.append(key)
    print len(filtered_unigrams), " unigrams in vocab."
    with open('unigrams.json', 'w') as fp:
        json.dump(filtered_unigrams, fp)
        # print "Done"


bigrams = []
inv_bigrams = {}
unigrams = []
inv_unigrams = {}
link_addresses = []
link_subdomains = []
link_domains = []
link_suffices = []
inv_link_addresses = {}
inv_link_subdomains = {}
inv_link_domains = {}
inv_link_suffices = {}

def fill_addresses(filename):
    global link_addresses,inv_link_addresses
    with open(filename, 'r') as data_file:
        link_addresses = json.load(data_file)
    inv_link_addresses = {}
    i=0
    for i in range(len(link_addresses)):
        if link_addresses[i]=="":
            continue
        inv_link_addresses[link_addresses[i]] = i

def fill_domains(filename):
    global link_domains,inv_link_domains
    with open(filename, 'r') as data_file:
        link_domains = json.load(data_file)
    inv_link_domains = {}
    i=0
    for i in range(len(link_domains)):
        if link_domains[i]=="":
            continue
        inv_link_domains[link_domains[i]] = i

def fill_subdomains(filename):
    global link_subdomains,inv_link_subdomains
    with open(filename, 'r') as data_file:
        link_subdomains = json.load(data_file)
    inv_link_subdomains = {}
    i=0
    for i in range(len(link_subdomains)):
        if link_subdomains[i]=="":
            continue
        inv_link_subdomains[link_subdomains[i]] = i

def fill_suffices(filename):
    global link_suffices,inv_link_suffices
    with open(filename, 'r') as data_file:
        link_suffices = json.load(data_file)
    inv_link_suffices = {}
    i=0
    for i in range(len(link_suffices)):
        if link_suffices[i]=="":
            continue
        inv_link_suffices[link_suffices[i]] = i

def fill_bigrams(filename):
    global bigrams,inv_bigrams
    with open(filename, 'r') as data_file:
        bigrams = json.load(data_file)
    inv_bigrams = {}
    i=0
    for i in range(len(bigrams)):
        inv_bigrams[bigrams[i]] = i

def fill_unigrams(filename):
    global unigrams,inv_unigrams
    with open(filename, 'r') as data_file:
        unigrams = json.load(data_file)
    inv_unigrams = {}
    i=0
    for i in range(len(unigrams)):
        inv_unigrams[unigrams[i]] = i

def get_unigram_features(x):
    features = np.zeros(len(unigrams))
    for word in x:
        if word in inv_unigrams:
            features[inv_unigrams[word]]+=1
    return list(features)

def get_addresses_features(x):
    features = np.zeros(len(link_addresses))
    for word in x:
        if word in inv_link_addresses:
            features[inv_link_addresses[word]]+=1
    return list(features)

def get_subdomains_features(x):
    features = np.zeros(len(link_subdomains))
    for word in x:
        if word in inv_link_subdomains:
            features[inv_link_subdomains[word]]+=1
    return list(features)

def get_domains_features(x):
    features = np.zeros(len(link_domains))
    for word in x:
        if word in inv_link_domains:
            features[inv_link_domains[word]]+=1
    return list(features)

def get_suffices_features(x):
    features = np.zeros(len(link_suffices))
    for word in x:
        if word in inv_link_suffices:
            features[inv_link_suffices[word]]+=1
    return list(features)

def get_bigram_features(x):
    features = np.zeros(len(bigrams))
    if len(x) < 2:
        return list(features)
    for i in range(len(x)-1):
        big = x[i] + ':;:' + x[i+1]
        if big in inv_bigrams:
            features[inv_bigrams[big]]+=1
    return list(features)

def get_features(X,addresses,subdomains,domains,suffices):
    features = []
    for i in range(len(X)):
        x=X[i]
        xa = addresses[i]
        xs = subdomains[i]
        xd = domains[i]
        xsu = suffices[i]
        feat = []
        feat.extend(get_unigram_features(x))
        feat.extend(get_bigram_features(x))
        feat.extend(get_addresses_features(xa))
        feat.extend(get_subdomains_features(xs))
        feat.extend(get_domains_features(xd))
        feat.extend(get_suffices_features(xsu))
        features.append(feat)
    return features

def getdomainfromurl(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain,tldextract.extract(domain)

def main():
    html_data = get_html_data()
    print html_data['1'].keys()

    user_features = get_user_features()

    X, Y, z, links = get_html_features(html_data, user_features)
    addresses = []
    subdomains = []
    domains = []
    suffices = []
    for ll in links:
        x = defaultdict(list)
        for l in ll:
            try:
                d,t = getdomainfromurl(l)
                x['addresses'].append(d)
                x['subdomains'].append(t.subdomain)
                x['domains'].append(t.domain)
                x['suffices'].append(t.suffix)
            except AttributeError:
                continue
        addresses.append(x['addresses'])
        subdomains.append(x['subdomains'])
        domains.append(x['domains'])
        suffices.append(x['suffices'])

    write_vocab_links(addresses,subdomains,domains,suffices)
    write_vocab_bigrams(X)
    write_vocab_unigrams(X)
    # return
    fill_addresses("addresses.json")
    fill_subdomains("subdomains.json")
    fill_domains("domains.json")
    fill_suffices("suffices.json")
    fill_bigrams("bigrams.json")
    fill_unigrams("unigrams.json")
    # return
    X = get_features(X,addresses,subdomains,domains,suffices)
    # return
    json.dump(X, open('X.json', 'wb'))
    # json.dump(z, open('y.json', 'wb'))
    # json.dump(Y, open('X_manual.json', 'wb'))


if __name__ == '__main__':
    main()
