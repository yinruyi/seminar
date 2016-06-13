#coding=utf-8
import sys
sys.path.append("../")
import jieba
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg
import jieba.analyse

# jieba.add_word('石墨烯')
# jieba.add_word('凱特琳')
# jieba.del_word('自定义词')

# test_sent = (
# "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
# "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
# "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
# )
# words = jieba.cut(test_sent)
# print('/'.join(words))
# print 'hh'
import os
import sys
import string
import codecs
reload(sys)
import math
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

class pretreatment():
    """预处理"""
    def __init__(self):
        pass
    def read_txt(self, txtPath, coding = 'utf-8'):
        import codecs
        f = codecs.open(txtPath,'r',coding).readlines()
        f[0] = f[0].replace(u"\ufeff",u"")
        dataset = []
        for line in f:
            line = line.replace("\r\n","")
            line = line.replace("\n","")
            dataset.append(line)
        return dataset

    def writeMatrix(self, dataset, Path, coding = "utf-8"):
        for i in xrange(len(dataset)):
            temp = dataset[i]
            temp = [str(temp[j]) for j in xrange(len(temp))]
            temp = ",".join(temp)
            dataset[i] = temp
        string = "\n".join(dataset)
        f = open(Path, "a+")
        line = f.write(string+"\n")
        f.close()


class Methods():
    pass

class DataAnalysis(pretreatment, Methods):
    pass

def counts(List):
    result = {}
    for i in range(len(List)):
        if List[i] in result:
            result[List[i]] += 1
        else:
            result[List[i]] = 1
    return result

if __name__=='__main__':
    dataset = pretreatment().read_txt('male.txt')
    print dataset[0]
    # words = jieba.cut(dataset[1011])
    # print '/'.join(words)
    # dataset_string = ','.join(dataset)
    words = []
    comment = []
    for i in range(len(dataset)):
        word = jieba.cut(dataset[i])
        word_string = '/'.join(word)
        word = word_string.split('/')
        # print word
        # break
        words.extend(word)
        comment.append(word)
    words_dic = counts(words)
    length = len(words)
    words = list(set(words))
    print length
    for i in range(len(words)):
        num = words_dic[words[i]]
        # print num
        pi = num*1.0/length
        entropy = -pi*math.log(pi)
        # print entropy
        words_dic[words[i]] = entropy
        # break
    result = []
    for i in range(len(dataset)):
        entropy = 0
        for j in range(len(comment[i])):
            entropy += words_dic[comment[i][j]]
        temp_result = [dataset[i], entropy]
        # print temp_result
        result.append(temp_result)
        # break
    pretreatment().writeMatrix(result,'entropy.txt')

    
