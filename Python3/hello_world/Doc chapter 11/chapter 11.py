class AnonymousSurvey():
    """存储一个问题，并为存储答案作准备"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问题"""
        print(self.question)

    def get_responses(self, response):
        """获取多个答案并显示答案"""
        print(response)


question = "What's your pants?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print('Enter \'q\' at any time to quit.\n')
while True:
    response = input('You answer')
    if response == 'q':
        break
    my_survey.get_responses(response)
