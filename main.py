from urllib.request import Request, urlopen
import gzip
import json

def download_dati():
    print('Beginning file download')
    url = 'https://data.gharchive.org/2020-01-01-16.json.gz'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()

    github_gzip = open("github_gzip.json", "wb")
    github_gzip.write(web_byte)
    github_gzip.close()

    file_git = gzip.open("github_gzip.json", "rb")
    contents = file_git.read()
    #print(contents)

    github_gzip = open("github.json", "wb")
    github_gzip.write(contents)
    github_gzip.close()

    print("\ncontents",  type(contents))
    print("github_gzip", type(github_gzip))
    print("github.json", type("github.json"))

def parse_json ():
    f = open("github.json", "r", encoding='UTF-8')
    git = (f.readlines())

    '''
    print(git.count("commit "))
    print(git.find('User'))
    '''

    json_data = []
    #print(type(git))

    for jsonObj in git:
        #print(type(jsonObj))
        jsonDistinct = json.loads(jsonObj)
        json_data.append(jsonDistinct)

    messagi_totali=0
    messagi_fix_bug=0
    messagi_vuoti=0
    flag=1

    print("Printing each JSON Decoded Object")
    for github in json_data:
        try:

            #print(github)
            #print(github["payload"]["commits"])
            #print(type(((github["payload"]["commits"]))))

            if github["type"]=="PushEvent":
                scomponi=github["payload"]["commits"]
                flag=1
            else:
                scomponi=""
                flag=0

            for s in scomponi:
                #print(s['message'])
                trova_message=(s['message'])
                #print(type(trova))
                if flag==1:
                    messagi_totali+=1

                if  trova_message.find("fix")!=-1 and trova_message.find("bug")!=-1:
                    print(trova_message)
                    print()
                    print()
                    messagi_fix_bug+=1
                '''
                if trova_message.find("update gitignore")!=-1:
                    print(trova_message)
                    messagi_vuoti+=1

                
                trova_author=(s['author'])
                #print(trova_author)
                name_author=trova_author['name']
                email_author=trova_author['email']
                if name_author.find("kyuhsim")!=-1 and email_author.find("5c2115d366f8a4eff8970563e42b1185072c4994@naver.com")!=-1:
                    print(trova_author)
                '''

            '''
            funziona:
            print(github)
            print(github["actor"]["id"])
            print(github["id"])
            print(github["payload"]["push_id"])
            (github["payload"]["distinct_size"])
            print(github["payload"]["ref"]) 
            print(github["payload"]["head"])
            print(github["payload"]["before"])
            print(github["payload"]["commits"])
            print(github["payload"]["size"])

            non funziona:
            print(github["payload"]["action"])
            print(github["payload"]["author"])
            print(github["payload"]["message"])
            print(github["payload"]["distinct"])
            print(github["payload"]["url"])
            '''
        except KeyError:
            c=0

    print("messagi_fix/messagi_totali:", messagi_fix_bug,"/", messagi_totali)
    print("messagi vuoti: ",messagi_vuoti)

if __name__ == '__main__':
    #download_dati()
    parse_json()
