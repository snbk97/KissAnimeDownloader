def c2h(url):
    anime_name = url.split('http://kissanime.to/Anime/')[1]
    fo = open('anime_links.csv', 'rb')  # csv file
    fh = open('anime_links.html', 'wb')  # html fileb')

    fh_pre_data = '''
<html>
<head>
<link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
<style>
body{

font-family:'Raleway',Arial;
color:green;
}
td{
    padding:10px

}
#main_table{
    -webkit-box-shadow: 0px 13px 21px -7px rgba(0,0,0,0.6);
    -moz-box-shadow: 0px 13px 21px -7px rgba(0,0,0,0.6);
    box-shadow: 0px 13px 21px -7px rgba(0,0,0,0.6);
    border-radius:12px;
}
</style>
</head>

<body>
<center><h1> <a href="https://github.com/snbk97/KissAnimeDownloader">Kiss Anime Downloader</a></h1></center>
<hr></br>

                '''
    fh.write(fh_pre_data)
    fh.write("<center><h2><a href=" + url + ">" + anime_name + "</a></h2><br>")
    fh.write('<table id="main_table">')
    l = len(fo.readlines()) - 1
    fo.seek(0, 0)
    for i in fo.readlines()[l::-1]:
        ep = i.split('~')[::2][0]
        link = i.split('~')[::-1][0]
        final = "<td>" + ep + '<td><td>' + '<a href=' + \
            '"' + link + '"' + '>Link</a></td>'
        fh.write("<tr>")
        fh.write(final)
        fh.write("</tr>")

    fh.write("</table></center></body></html>")
    fh.close()
    fo.close()

# c2h(url) #test
