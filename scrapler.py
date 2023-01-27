import question as q
import requests
import os
import file_utils

from bs4 import BeautifulSoup
from requests_file import FileAdapter


def scrap_this_page(container, path, file_name):
    count = 1
    s = requests.Session()
    s.mount('file://', FileAdapter())

    path_to_file = path + "/" + file_name
    page = s.get('file:///' + path_to_file)

    soup = BeautifulSoup(page.content, 'html.parser')
    questionGroups = soup.find_all(attrs={"aria-label": "Question"})

    for group in questionGroups:

        question_element = group.find("textarea", class_="textarea_question_text")
        answer_element = group.find_all("div", class_="answer_text")
        correct_answers = group.find_all("div", class_="correct_answer")

        temp_question = q.Question(file_utils.stripPageHtmlTag(str(question_element.text)))
        for each_answer in answer_element:
            temp_question.answers.append(file_utils.stripPageHtmlTag(str(each_answer.text)))
        temp_question.correct_answer = correct_answers[0].find("div", class_="answer_text").text.strip()


        # if "What type of country has the greatest proportion of young individuals?" in temp_question.question:
        #     print(file_name)
        #
        # if "Which characteristic of populations can affect interactions within the population, such as competition?" in temp_question.question:
        #     print(file_name)

        # quick patch because there are questions with wrong keys in the files:
        # these questions have different Correct answer
        if "The maximum growth rate characteristic of a species is called its:" in temp_question.question:
            temp_question.correct_answer = "biotic potential"
        if "A country with zero population growth is likely to be:" in temp_question.question:
            temp_question.correct_answer = "economically developed"

        count+=1
        if temp_question not in container: container.append(temp_question)
        else: print(temp_question.display()) # show duplicates

        # print(temp_question.display())
    return container

def write_to_file(question_set, file):
    for question in question_set:
        file.write(question.display())



def scrape_this_folder(folder_name):

    file_path_destination = folder_name # create new file in same folder
    questionSet = []  # store all Questions object in here

    # create text file if not exist, clean data if exist
    filepath = os.path.join(file_path_destination, os.path.basename(folder_name) + ' result')
    if not os.path.exists(file_path_destination):
        os.makedirs(file_path_destination)
    f = open(filepath, "w")

    # go through all htmls
    all_file_names = file_utils.get_all_file_names(folder_name)
    for file_name in all_file_names:
        if "html" in file_name: scrap_this_page(questionSet, folder_name, file_name)




    write_to_file(questionSet, f)
    f.close()


def show_folder(folder_name):
    os.startfile(folder_name)





