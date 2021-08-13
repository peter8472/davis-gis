'''extract listings from the DDBA. 



'''
import json
import re
import html.parser


class mystate:
    SKIPPING=1
    READINGROW=2
class myparser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.state = mystate.SKIPPING
    def handle_starttag(self, tag,attrs):
        if self.state == mystate.SKIPPING:
            if tag != "div":
                return
            for line in attrs:
                if line[0] == "class":
                    if line[1] == 'sabai-row':
                        print("row start")
                    if line[1] == 'sabai-directory-location':
                        print("location start")
                    if line[1] == 'sabai-directory-contact':
                        print("direcotry contact")
                    if line[1] == 'sabai-directory-social':
                        print("sabai-directory-social")
                    
    def handle_data(self,data):
        if self.state == mystate.SKIPPING:
            pass
        else:
            print(data)
    
            

def jdump(i):
    print(json.dumps(i,indent=4))

if __name__ == "__main__":
    
    f = open("Data/ddba.html")
    g = f.read()
    u = myparser()
    u.feed(g)


        
    