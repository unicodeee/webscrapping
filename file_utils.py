import os


def print_all_file_names_in_folder(path):
    with os.scandir(path) as entries:
        for entry in entries:
            print(entry.name)


def get_all_file_names(path):
    names = set()
    with os.scandir(path) as entries:
        for entry in entries:
            names.add(entry.name)
    return names


def stripPageHtmlTag(string):  # strip <p> tag and </p>, sometimes it happens
    return  string.strip().replace("<p>", "").replace("</p>", "").replace("&nbsp;", "")
    # return string.strip().removeprefix("<p>").removesuffix("</p>") #  ">p/<" so that rstrip work

#
# print(stripPageHtmlTag("<p>4.&nbsp; The sticky ends of the foreign and host DNA anneal</p>     "))
# print(stripPageHtmlTag("Molecular cloning is a multi-step process.&nbsp; Put the following steps in order from first to last.</p><p>1.&nbsp; DNA ligase glues the backbone of the foreign and host DNA together</p><p>2.&nbsp; The foreign and host DNA are cut with restriction enzymes</p><p>3.&nbsp; The plasmid is taken up by a bacterium</p><p>4.&nbsp; The sticky ends of the foreign and host DNA anneal"))

# print(stripPageHtmlTag(" asd     <p>4.&nbsp; The sticky ends of the foreign and host DNA anneal</p>       "))
#
# # print("<p>4.&nbsp; The sticky ends of the foreign and host DNA anneal</p>".lstrip("<p>").rstrip("</p>").strip())
# #
# # print("</p>" [::-1])