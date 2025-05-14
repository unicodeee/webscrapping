import scrapler

if __name__ == '__main__':

    # put the absolute path of the folder containing the htmls
    source_folder: str = r'/Users/Thang/Documents/SJSU materials/CMPE 131/quizlet/'
    # scrape

    scrapler.scrape_this_folder(source_folder)

    # open the newly created text file
    scrapler.show_folder(source_folder)

