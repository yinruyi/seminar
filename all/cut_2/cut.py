#coding=utf-8
import sys
sys.path.append("../")
import jieba
jieba.load_userdict("all_userdic.txt")
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



if __name__=='__main__':
    dataset = pretreatment().read_txt('all.txt')
    print dataset[0]
    words = jieba.cut(dataset[1011])
    print '/'.join(words)
    dataset_string = ','.join(dataset)
    print dataset_string[0:100]
    tag = ('n','nr','ns','nsf','nt','nz','nl','ng','a','ad','an','ag','ag','al')
    # tag = ()
    tfidf = jieba.analyse.extract_tags(dataset_string, topK=1000, withWeight=False, allowPOS=tag)
    print tfidf[0:100]
    tfidf = [[tfidf[i]] for i in range(len(tfidf))]
    print tfidf[0]
    pretreatment().writeMatrix(tfidf, 'all_feature_n_a.txt')
