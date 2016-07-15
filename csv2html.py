# for explicit calling only
def c2h(url):
    anime_name = url.split('http://kissanime.to/Anime/')[1]
    fo = open('anime_links.csv', 'rb')
    fh = open('anime_links.html', 'wb')

    fh_pre_data = '''
                <html>
                <head>
                <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
                <style>
                body{
                font-family:'Raleway',Arial;
                }
                </style>
                </head>

                <body>
                <center><h1> <a href="https://github.com/snbk97/KissAnimeDownloader">Kiss Anime Downloader</a></h1></center>
                <hr></br>
                '''
    fh.write(fh_pre_data)
    fh.write("<center><h2><a href=" + url + ">" + anime_name + "</a></h2><br>")

    l = len(fo.readlines()) - 1
    fo.seek(0, 0)
    for i in fo.readlines()[l::-1]:
        ep = i.split('~')[::2][0]
        link = i.split('~')[::-1][0]
        final = "EP " + ep + ': ' + '<a href=' + '"' + link + '"' + '>Link</a>'
        fh.write(final)
        fh.write('</br>')

    fh.close()
    fo.close()
