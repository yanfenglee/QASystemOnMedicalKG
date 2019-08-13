
from question_classifier import *
from question_parser import *
from answer_search import *
import random

jokes = [
    '''  据说，有一位外国朋友，上厕所的时候无聊，拿起一瓶洁厕剂，阅读背面的说明书，居然在里面看到这么一句话：“如果你在阅读本产品的说明书，说明你没带手机，被我猜对了吧？”
      后来这位朋友把这个图片就发到了网上，据说很多人都成了这个洁厕剂品牌的粉丝，因为它有趣。''',

    '''这个世界上有10种人，
    一种懂二进制，还有一种不懂。''',

    '''一道闪光，你身着华丽的服装出现在一间装修奢华的房间里，房间中放置着很多奇妙的钟表，你发现桌子上有一个日记本，你翻开日记本，发现日记最新的一页上写着“今日无事”''',

    '''  两程序员向同一个MM求爱，MM说：“去环游世界后再来找我！”码农A立即收拾行李出发。码农B绕MM一圈，然后说：“Hello world！”立即感动了MM。
      其实他只是习惯在做任何新事情前先确定Hello World能跑通而已。''',

    '''一个妻子想让她的丈夫早回家，于是规定：晚于11点回家就锁门。
    第一周奏效，第二周丈夫又晚归，妻子按制度把门锁了，于是丈夫干脆不回家了。
    妻子郁闷，后经高人指点，修改规定：23点前不回家，我就开着门睡觉。丈夫大惊，从此准时回家。
    有时候直觉反过来才有效''',

    '''早上小侄女说难受不想去幼儿园，老妈问她哪儿难受，小侄女有气无力的说：浑身头疼。。。
    这个理由直接给我笑喷了：你几个头？
    小侄女撅着小嘴伸出手指头数：头疼，额头疼，鼻头疼，舌头疼，手指头疼，还有脚趾头也疼。。。
    我去！！'''    
]

m = '您好，我是米喜医药智能助手，请输入医疗相关问题, 如：疾病症状，治疗方式，如何预防，需检查项目，用什么药，饮食禁忌，为什么会得，易感人群等'
default_ans = [m,m,m,m,m,m,m
    '有点难以回答，让我思考下。。。',
    '正在进行思考。。。'
    '我还经验不足，请海涵...',
    '您好，这个问题暂时回答不了，请咨询医家人工助手，祝您身体健康：）'
]

class ChatBot:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def ask(self, quest):
        qu = str.strip(quest)
        if qu == '头痛' or qu == '头疼':
            return jokes[random.randrange(len(jokes))]

        answer = default_ans[random.randrange(len(default_ans))]
        res_classify = self.classifier.classify(quest)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


