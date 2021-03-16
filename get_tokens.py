# -*- encoding: utf-8 -*-
'''
@Func    :   rm stop words & other irrelevant from data
@Time    :   2021/03/12 14:54:35
@Author  :   Yixiao Ma 
@Contact :   mayx20@mails.tsinghua.edu.cn
'''

import os
import json
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords
import nltk.stem
import string

PROOT = '/work/mayixiao/coliee_2021/no_fr'
WDIR = '/work/mayixiao/coliee_2021/tokens'

files = os.listdir(PROOT)

for pfile in tqdm(files[:]):
    with open(os.path.join(PROOT, pfile), 'r') as f:
        jsfile = json.load(f)
    fid = jsfile['id_']
    body = jsfile['body_str']
    wbody = []
    for para in body[:]:

        # 转换大小写
        lower = para.lower()

        # 分词
        tokens = nltk.word_tokenize(lower)

        # 去除标点、停用词
        rm_sw = [w for w in tokens if not w in stopwords.words('english') and w not in string.punctuation]

        # 提取词干
        s = nltk.stem.SnowballStemmer('english')  
        cleaned_text = [s.stem(i) for i in rm_sw]

        wbody.append(cleaned_text)
            
    with open(os.path.join(WDIR, pfile), 'w') as f:
        json.dump({'id_':fid, 'body_str': wbody}, f, ensure_ascii=False)



print(cleaned_text)