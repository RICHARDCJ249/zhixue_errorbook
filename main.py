from zhixuewang.zxw import Zhixuewang
import jinja2
import os
from zhixuewang.Student.models import exceptionsModel
import sys
import pygal
import datetime

WKHTMLTOPDF_PATH = r'.\wkhtmltopdf\bin\wkhtmltopdf.exe' # wkhtmltopdf 地址
# PDF参数
PRARMETER_PDF = '--page-size "B5" --margin-top "0.25in" --margin-right "0.25in" --margin-bottom "0.25in" --margin-left "0.3in" --encoding "UTF-8" --no-outline --footer-center "·[page]·"'


class fullModel():
    """
    填充模板
    """

    def __init__(self, name, subjectName, examName, rank, errorbook):
        self.name = name
        self.subjectName = subjectName
        self.examName = examName
        self.rank = rank
        self.errorbooks = errorbook


def showInformation():
    print('''


    *********************************************************
    *               Name：智学网错题本合成工具              *
    *                   Auther:陈半夏                       *
    *                  Time：2019-12-12                     *
    *********************************************************


    ''')


def fullTemplate(model):
    env = jinja2.Environment(
        loader=jinja2.PackageLoader('zhixuewang', 'templates'))
    tep = env.get_template("templates.html")
    return tep.render(model=model)


def htmlToPdf(f,subject):
    command = f'{WKHTMLTOPDF_PATH} {PRARMETER_PDF} {f} {getFileName(subject)}'
    print('run-- '+command)
    os.system(command)


def getGradeCode(s):
    return {
        'E': 1,
        'D5': 2,
        'D4': 3,
        'D3': 4,
        'D2': 5,
        'D1': 6,
        'C5': 7,
        'C4': 8,
        'C3': 9,
        'C2': 10,
        'C1': 11,
        'B5': 12,
        'B4': 13,
        'B3': 14,
        'B2': 15,
        'B1': 16,
        'A5': 17,
        'A4': 18,
        'A3': 19,
        'A2': 20,
        'A1': 21
    }[s]


def drawGraphy(mLostTopic, mLevelTrend):
    def drawLevelTrend():
        LevelTrend = pygal.Line(js=(), width=750, height=400)
        LevelTrend.x_labels = [x["Time"] for x in mLevelTrend]
        LevelTrend.y_labels = [x for x in range(0, 20)]
        LevelTrend.add("rank", [getGradeCode(x["level"]) for x in mLevelTrend])
        LevelTrend.render_to_file("zhixuewang/templates/img/gradechange.svg")

    def drawLostTopic():
        LostTopic = pygal.HorizontalBar(
            margin_left=60, js=(), width=750, height=400)
        for x in mLostTopic:
            LostTopic.add(x["Name"], float(x["Score"]))
        LostTopic.render_to_file("zhixuewang/templates/img/losttopic.svg")
    drawLevelTrend()
    drawLostTopic()


def deletCatch():
    print('清除暂存文件······')
    os.remove('html.html')
    os.remove('zhixuewang/templates/img/gradechange.svg')
    os.remove('zhixuewang/templates/img/losttopic.svg')
    print('清除成功。')


def getFileName(subject: str):
    return '"{0}-{1}-错题本.pdf"'.format(datetime.datetime.now().strftime('%Y-%m-%d'),subject)


if __name__ == "__main__":
    try:
        showInformation()
        LoginName = input('LoginName: ')
        LoginPassword = input('LoginPassword: ')
        print('尝试登陆中······')
        zxw = Zhixuewang(LoginName, LoginPassword)
        print('登陆成功')
        while True:
            exams = zxw.get_exams()
            print('考试名称：  \r\n')
            for i in range(0, len(exams)):
                print(str(i) + '.' + ' ' + exams[i].name)
            examId = int(input('请输入您要生成错题本的考试：   '))
            subjects = zxw.get_exam_subject(exams[examId].id)
            for i in range(0, len(subjects)):
                print(str(i) + '.' + ' ' + subjects[i]['subjectName'])
            subjectId = int(input('请输入您要生成错题本的学科：   '))
            print('获取信息中······')
            mark = zxw.get_level_trend(exams[examId], subjects[subjectId]['subjectName'])[-1]["level"]
            print("获取成绩成功")
            full_model = fullModel(zxw.name, subjects[subjectId]['subjectName'], exams[examId].name,mark , zxw.get_errorbook(exams[examId], subjects[subjectId]['subjectName']))
            print('生成图片······')
            drawGraphy(zxw.get_lost_topic(exams[examId], subjects[subjectId]['subjectName']), zxw.get_level_trend(
                exams[examId], subjects[subjectId]['subjectName']))
            print('生成成功')
            print('获取成功，正在合成中······')
            errorbookHtml = fullTemplate(full_model)
            with open("html.html", 'w', encoding='utf-8') as f:
                f.write(errorbookHtml)
            htmlToPdf("html.html",subjects[subjectId]['subjectName'])
            print('合成成功')
            deletCatch()
            ifOk = input("是否生成其他错题本（Y/N）:")
            if ifOk in ["Y","y"]:
                continue
            elif ifOk in ["N","n"]:
                exit("退出")
            exit("退出")
    except Exception as e:
       print(repr(e))
