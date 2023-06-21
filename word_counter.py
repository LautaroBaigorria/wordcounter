# paragraph = "The Zen of Python, by Tim Peters Beautiful is better than ugly.Explicit is better than implicit. Simple is better than complex."
from collections import Counter
import re

class ContadordePalabras(object):

    def __init__(self) -> None:
        self.demo(True)

    def check_if_in_list_en(self, words):
        words_en = ["the","of","and","to","a","in","for","is","on","that","by","this","with","i","you","it","not","or","be","are","from","at","as","your","all","have","new","more","an","was","we","will","home","can","us","about","if","page","my","has","search","free","but","our","one","other","do","no","information","time","they","site","he","up","may","what","which","their","news","out","use","any","there","see","only","so","his","when","contact","here","business","who","web","also","now","help","get","pm","view","online","c","e","first","am","been","would","how","were","me","s","services","some","these","click","its","like","service","x","than","find"]
        return words not in words_en

    def check_if_in_list_sp(self, words):
        words_sp = ["que","de","no","a","la","el","es","y","en","lo","un","por","qué","me","una","te","los","se","con","para","mi","está","si","bien","pero","yo","eso","las","sí","su","tu","aquí","del","al","como","le","más","esto","ya","todo","esta","vamos","muy","hay","ahora","algo","estoy","tengo","nos","tú","nada","cuando","ha","este","sé","estás","así","puedo","cómo","quiero","sólo","soy","tiene","gracias","o","él","bueno","fue","ser","hacer","son","todos","era","eres","vez","tienes","creo","ella","he","ese","voy","puede","sabes","hola","sus","porque","dios","quién","nunca","dónde","quieres","casa","favor","esa","dos","tan","señor","tiempo","verdad","estaba"]
        return words not in words_sp    

    def word_counter(self, paragraph, omitCommonWords=False):
        
        paragraph = re.sub(r"[¡!“”#$%&'()*+,-./:;<=>¿?@[\]^_`{|}~]","",paragraph)
        paragraph_list = paragraph.lower().split()
        if (omitCommonWords == True):
            paragraph_list = list(filter(self.check_if_in_list_en, paragraph_list))
            paragraph_list = list(filter(self.check_if_in_list_sp, paragraph_list))
        self.print_ascii_bar_chart(paragraph_list)

    def print_ascii_bar_chart(self, data, symbol="#"):
        counter = Counter(data).most_common()
        chart = {category: symbol * frequency for category, frequency in counter}
        max_len = max(len(category) for category in chart)
        print (f"Cantidad de palabras contabilizadas: {len(data)}")
        for category, frequency in chart.items():
            percentage = round ((len(frequency) / len(data) *100),2) 
            padding = (max_len - len(category)) * " "
            print(f"{category}{padding} |{frequency} {len(frequency)} | {percentage}%")

    def demo(self,bol=False):
        with open("zen_of_python.txt") as my_file:
            paragraph_file=my_file.read()
        self.word_counter(paragraph_file,bol)

    def open_file(self,file,bol=False):
        with open(file) as my_file:
            paragraph_file=my_file.read()
        self.word_counter(paragraph_file,bol)