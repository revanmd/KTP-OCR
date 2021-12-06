import re
class Pretext:
    
    @staticmethod   
    def get_nama(text):
        text = re.sub(r'[0-9]',"",text)
        text = re.sub(r'[^\w\s]', "", text)
        text = re.sub(r'(^nama|^nam|^na.+\s)', "", text.strip())    
        return text.strip()
    
    @staticmethod
    def get_nik(text):
        text = re.sub(r'(^ni|^nik|^n1k|^n1|^n!|^n!k) ', "", text)
        text = re.sub(r'[^\w\s]', "", text)
        text = re.sub(r'[a-z]+', "", text)
        return text.strip()
    
    @staticmethod
    def get_tempat(text):
        text = re.sub(r'[0-9]+.+',"",text)
        text = re.sub(r'[^\w\s]', "", text)
        text = re.sub(r'(^tempat|^tempa|^temp|temp)([\s\S]*?)',"",text)
        text = re.sub(r'(^tgi|^tgl|^tg)',"",text)
        text = re.sub(r'(^lahir|^lah)',"",text.strip())
        text
        return text.strip()
    
    @staticmethod
    def get_tgl_lahir(text):
        text = re.findall(r'[0-9]+-[0-9]+-[0-9]+',text)
        if len(text) > 0:
            return text[0].strip()
        return ""
    
    @staticmethod
    def get_kec(text):
        text = re.sub(r'(^kec[a-z]+) ',"",text)
        text = re.sub(r'[^\w\s]',"",text)
        return text.strip()
    
    @staticmethod
    def get_kel(text):
        text = re.sub(r'(^kel(/|)[a-z]+)',"",text)
        text = re.sub(r'[^\w\s]',"",text)
        return text.strip()