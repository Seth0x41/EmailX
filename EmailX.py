import requests,re,argparse


print (r"""
                     _____                 _ _           
                    | ____|_ __ ___   __ _(_) |    __  __
                    |  _| | '_ ` _ \ / _` | | |____\ \/ /
                    | |___| | | | | | (_| | | |_____>  < 
                    |_____|_| |_| |_|\__,_|_|_|    /_/\_\

                    """)
        
rgx = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com"
email_list = []


parser = argparse.ArgumentParser(description='Extract Emails From Html Content')
parser.add_argument('-w','--wordlist', help='Import wordlist')
parser.add_argument('-u','--url', help='Collect Emails from url [HTML Page]')
parser.add_argument('-o','--output', help='Save Results')
args = parser.parse_args()

if args.wordlist:
    try:
        Word_List = open(args.wordlist,"r")
        for url in Word_List:
            url = url.strip()
    except FileNotFoundError:
        print("Some Thing Wrong")

elif args.url:
    url = args.url

req = requests.get(url)
email = re.findall(rgx,req.text)
email_list.extend(email)
for line in email_list:
    print(line)


if args.output:
    Out = open(args.output+".txt","w")
    for line in email_list:
        Out.write(line+"\n")

    
