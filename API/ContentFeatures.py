from urllib.parse import urlparse
from pyquery import PyQuery


class ContentFeatures:
    def __init__(self, url):
        self.url = url
        self.urlparse = urlparse(self.url)
        self.response = ""
        # self.html = self.__get_html()
        self.pq = self.__get_pq()
        self.scripts = self.__get_scripts()
    # def __get_html(self):
    #     try:
    #         print("open")
    #         self.response = urlopen(self.url, timeout=10)
    #         print("closed")
    #         html = self.response.read().decode()
    #     except:
    #         html = ""
    #     return html

    def __get_pq(self):
        try:
            pq = PyQuery(self.html) if self.html else None
            return pq
        except:
            return None

    def __get_scripts(self):
        scripts = self.pq('script') if self.pq else None
        return scripts
    
    # extract content-based features
    
    #HtmlLen
    # def length_of_html(self):
    #     return len(self.html) if self.html else 0

    #NumHtmlTags
    def number_of_html_tags(self):
        return len(self.pq('*')) if self.pq else 0

    #NumHiddenTags
    def number_of_hidden_tags(self):
        if self.pq:
            hidden1, hidden2 = self.pq('.hidden'), self.pq('#hidden')
            hidden3, hidden4 = self.pq('*[visibility="none"]'), self.pq('*[display="none"]')
            hidden = hidden1 + hidden2 + hidden3 + hidden4
            return len(hidden)
        else:
            return 0
    
    #NumScriptTags
    def number_of_script_tags(self):
        return len(self.scripts) if self.scripts else 0

    #NumIframes
    def number_iframes(self):
        if self.pq:
            iframes = self.pq('iframe') + self.pq('frame')
            return len(iframes)
        else:
            return 0
    
    #NumEmbeds
    def number_embeds(self):
        if self.pq:
            objects = self.pq('embed')
            return len(objects)
        else:
            return 0

    #NumHyperLinks
    def number_of_hyperlinks(self):
        if self.pq:
            hyperlinks = self.pq('a')
            return len(hyperlinks)
        else:
            return 0
    
    #NumEvalFuncs
    def number_of_eval_functions(self):
        if self.pq:
            scripts = self.pq('script')
            scripts = ['eval' in script.text().lower() for script in scripts.items()]
            return sum(scripts)
        else:
            return 0

    #WebForwards   
    def forwarding(self):
        return int(self.url == self.response.geturl()) if self.response else -1
