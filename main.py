
def main():
    # Import libraries
    from bs4 import BeautifulSoup as bs
    import requests
    import os.path
    from os import path

    DOMAIN = 'http://'
    # You can put url that you want to download from.
    URL = ''
    # You can put any file type what you want.
    FILETYPE = '.tar.gz'
    link_array = []

    def get_soup(URL):
        return bs(requests.get(URL).text, 'html.parser')

    for link in get_soup(URL).find_all('a'):
        file_linki = link.get('href')
        link_array.append(URL + file_linki)

    for link in link_array:
        # I put len() func because there were different types of files that I did not want to download in the link
        # It was sorter. So you don't have to put len() func here.
        if len(link) >= 135 and path.exists(link) == False:
            file_name = link.split('/')[-1]
            print(file_name)
            with open(file_name, 'wb') as file:
                response = requests.get(link)
                file.write(response.content)
        else:
            continue


if __name__ == '__main__':
    main()


