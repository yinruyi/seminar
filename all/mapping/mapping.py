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

def PP_time():
    p = pretreatment()
    raw = p.read_txt('all_raw.txt')
    raw = [raw[i].split('\t') for i in range(len(raw))]
    for i in range(len(raw)):
        raw[i][1] = raw[i][1][0:4]
    # print raw[0]
    pp = p.read_txt('all_pp.txt')
    print pp
    pp_time = []
    for i in range(len(pp)):
    	temp = [pp[i]]
    	pp_time_temp = []
        for j in range(len(raw)):
        	if pp[i] in raw[j][0]:
        		pp_time_temp.append(raw[j][1])
        # pp_time_temp = list(set(pp_time_temp))
        # pp_time_temp = sorted(pp_time_temp)
        temp.extend(sorted(list(set(pp_time_temp))))
        # print temp
        pp_time.append(temp)
        # break
    print pp_time[0:2]
    p.writeMatrix(pp_time,'all_PP_time.txt')

def pp_feature():
    p = pretreatment()
    raw = p.read_txt('all_raw.txt')
    raw = [raw[i].split('\t') for i in range(len(raw))]
    for i in range(len(raw)):
        raw[i][1] = raw[i][1][0:4]
    # print raw[0]
    pp = p.read_txt('all_pp.txt')
    print pp
    feature = p.read_txt('all_feature_n_a.txt')
    print feature
    pp_feature = []
    for i in range(len(pp)):
    	temp = [pp[i]]
        title = [raw[j][0] for j in range(len(raw)) if pp[i] in raw[j][0]]
        title = ''.join(title)
        for j in range(len(feature)):
        	if feature[j] in title:
        		temp.append(feature[j])
        pp_feature.append(temp)
    p.writeMatrix(pp_feature,'all_PP_feature.txt')




    

if __name__ == '__main__':
    pp_feature()
    PP_time()