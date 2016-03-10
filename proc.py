from bs4 import BeautifulSoup
import re
import pickle
import subprocess


def parse_title(file_name):
    data = ""
    with open(file_name, "r") as myfile:
        data = myfile.read()
    # print data
    soup = BeautifulSoup(data, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return str(soup.title)[len("<title>"):-len("</title>")], links


def main():
    data_dict = {}
    with open("html_files") as f:
        for line in f.readlines():
            line = line.strip()
            print "hola", line
            title, links = parse_title(line)
            text = subprocess.check_output([ "elinks", line, "-no-references", "-dump", "-no-numbering" ])
            number = line.split("/")[-1].split(".")[0]
            data_dict[int(number)] = {'title' :title, 'links' :links, 'text' :text}
    pickle.dump(data_dict, open("./outputs/data_dict.pickle", "wb"))

if __name__ == '__main__':
    main()
# the files with id 142 200 986 321 259 305 807 are defective !!
