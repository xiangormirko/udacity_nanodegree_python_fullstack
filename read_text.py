import urllib.request

def read_text():

    quotes= open("/Users/xiangormirko/Desktop/movie_quotes.txt")
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url=("http://www.wdyl.com/profanity?q="+text_to_check)
    connection = urllib.request.urlopen(url)
    output =connection.read()
    print(output)
    connection.close()
    

read_text()
