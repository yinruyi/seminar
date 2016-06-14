#coding:utf-8
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

if __name__ == '__main__':
    p = pretreatment()
    male = p.read_txt('male_userdic.txt')
    female = p.read_txt('female_userdic.txt')
    all_ = male + female
    print len(all_)
    all_ = list(set(all_))
    print len(all_)
    pp = [[all_[i]] for i in range(len(all_)) if ' pp' in all_[i]]
    print pp,len(pp)
    an = [[all_[i]] for i in range(len(all_)) if ' pp' not in all_[i]]
    p.writeMatrix(pp,'all.txt')
    p.writeMatrix(an,'all.txt')