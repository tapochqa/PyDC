# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 0 Название 1 Тип 2 Суть 3 Партнёр 4 Сумма 5 Дедлайн

mas = []

def upmas():
    mas = []
    with open ('DC', 'r') as dc:
        for line in dc:
            line = line.decode('utf-8').replace('\n', '')
            item = line.split('#')
            mas.append(item)
    return mas

def downmas():
    with open ('DC', 'w') as dc:
        for item in mas:
            dc.write ('#'.join(item)+'\n')

def addnew(name, typ, ess, part, summ, deadl):
    mas.append ([name.decode('utf-8'), typ.decode('utf-8'), ess.decode('utf-8'), part.decode('utf-8'), summ.decode('utf-8'), deadl.decode('utf-8')])

def delselected (name):
    for item in mas:
        if item[0] == name:
            mas.remove(item)
            
