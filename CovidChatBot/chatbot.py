from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.8
        },
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation",

        },
    ],

    database_uri='sqlite:///database.sqlite3'
)

# Training with Personal Ques & Ans & Corona Assessment
training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()
training_data_covid = open('training_data/corona_q.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal + training_data_covid

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)
