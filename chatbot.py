
from question_classifier import *
from question_parser import *
from answer_search import *

class ChatBot:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def ask(self, quest):
        answer = '您好，我是米喜医药智能助手，请输入健康相关问题，若回答不好，请咨询人工助手，祝您身体健康：）'
        res_classify = self.classifier.classify(quest)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


