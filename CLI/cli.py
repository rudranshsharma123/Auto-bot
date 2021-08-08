from time import sleep

import inquirer
from inquirer.themes import GreenPassion
from cliutils import (clear_everything, get_ans,
                          type_writer_anim)

clear_everything()
sleep(4)


type_writer_anim("Hello and welcome to Auto-Bot\n Auto-Bot, is a Chat-Bot made with Jina to ans your Automation related question and even teach you python while you are at it \n")

sleep(1.5)

while True:
    questions = [ 
        inquirer.List(
            'ans',
            message = 'Menu',
            choices = ['Start Chatting', 'About Auto-Bot', 'Quit'],
        )
    ]
    ans = inquirer.prompt(questions, theme = GreenPassion()) 

    if ans['ans'] == "Start Chatting":
        while True:
            question = [inquirer.List(
                'chat',
                message = "Auto-Bot",
                choices = ['What would you like to know?', 'Quit']
                
            )]
            ans = inquirer.prompt(question, theme = GreenPassion()) 
            if ans['chat'] == "Quit":
                break
            elif ans['chat'] == "What would you like to know?":
                question = [inquirer.Text('ques',message = "Enter the question you would like to ask" )]

                search_ans = inquirer.prompt(question, theme = GreenPassion())
                search_key = search_ans['ques']
                # search_ans = inquirer.prompt(question, theme = GreenPassion())
                # search_key = search_ans['hashtag']
                type_writer_anim("Searching the ans to your question I am \n")
                get_ans(search_key)
    elif ans['ans'] == 'Quit':
        print('\n')
        type_writer_anim("Quitting!! \n")
        exit(0)
  
    elif ans['ans'] == 'About Auto-Bot':
        text = """Hello and welcome to Auto-Bot. \n Auto-Bot, is a Chat-Bot made with Jina to ans your Automation and python related questions \n The datafile has over 150 questions scraped from best possible sources to help you in your autmation journey \n """
        type_writer_anim(text)
   
