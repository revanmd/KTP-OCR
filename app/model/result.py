import re
from .person import Person

class Result:
    @staticmethod
    def regex_nama(string):
        return re.search ("(.+nama.+|^nam|^na.+) ([\s\S]*?)",string)
    
    @staticmethod    
    def regex_nik(string):
        return re.search("^ni", string)
    
    @staticmethod   
    def regex_tempat(string):
        return re.search("(^tempat|^tempa|^temp|temp)([\s\S]*?)",string)

    @staticmethod
    def regex_tgl_lahir(string):
        return re.search("(^tempat|^tempa|^temp|temp)([\s\S]*?)",string)
    
    @staticmethod
    def regex_kec(string):
        return re.search("(^kec|^ke.+tan\s)",string)
    
    @staticmethod
    def regex_kel(string):
        return re.search("(^kel|^ke.+han\s)",string)
    
    @staticmethod
    def prepare_result(list_of_string):
        person = Person()
        for item in list_of_string:
            item = item.lower()
            if Result.regex_nama(item):
                person.nama = item
            if Result.regex_nik(item):
                person.nik = item
            if Result.regex_tempat(item):
                person.tempat = item
            if Result.regex_tgl_lahir(item):
                person.tgl_lahir = item
            if Result.regex_kec(item):
                person.kec = item
            if Result.regex_kel(item):
                person.kel = item
        return person