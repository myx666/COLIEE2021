# -*- encoding: utf-8 -*-
'''
@Func    :   remove french sentence from data
@Time    :   2021/03/10 20:55:44
@Author  :   Yixiao Ma 
@Contact :   mayx20@mails.tsinghua.edu.cn
'''

import os
import json
from tqdm import tqdm

import langdetect
from langdetect import detect
from langdetect import detect_langs
from langdetect import DetectorFactory
DetectorFactory.seed = 0

PROOT = '/work/mayixiao/coliee_2021/task1_processed_files 3'
WDIR = '/work/mayixiao/coliee_2021/no_fr'
files = os.listdir(PROOT)
# print(len(os.listdir(PROOT)))

for pfile in tqdm(files[:]):
    with open(os.path.join(PROOT, pfile), 'r') as f:
        jsfile = json.load(f)
    fid = jsfile['id_']
    body = jsfile['body_str']
    wbody = []
    for para in body[:]:
        wpara = ''
        for j in para:
            try:
                if len(j) >= 8 and str(detect_langs(j.lower())[0])[:6]=='fr:0.9':
                    pass
                    # print(j)
                    # print(detect_langs(j.lower()))
                else:
                    wpara = wpara + j + ' '
            except langdetect.lang_detect_exception.LangDetectException:
                pass
        wbody.append(wpara[:-1])
    with open(os.path.join(WDIR, pfile), 'w') as f:
        json.dump({'id_':fid, 'body_str': wbody}, f, ensure_ascii=False)


# s = '\"112. Le permis de travail ne peut être délivré à l\'étranger qui cherche à entrer au Canada au titre de la catégorie des aides familiaux que si l\'étranger se conforme aux exigences suivantes:  <FRAGMENT_SUPPRESSED>'.lower()
# print(detect_langs(s))

# with open('test.json', 'w') as f:
#     json.dump('Enquête',f, ensure_ascii=False)
