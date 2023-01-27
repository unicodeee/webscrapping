import scrapler

if __name__ == '__main__':

    # put the absolute path of the folder containing the htmls
    chapter19_folder_path: str = r"C:/Users/Thang/Desktop/BIO 010/Exam3/chapter19"
    # scrape
    scrapler.scrape_this_folder(chapter19_folder_path)

    # open the newly created text file
    scrapler.show_folder(chapter19_folder_path)

