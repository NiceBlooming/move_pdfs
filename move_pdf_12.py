import os
import sys

import xlrd
from xlutils.copy import copy
import datetime
from os.path import join
import shutil


def main(rootdir=r'文件夹a', resdir=r'文件夹b'):
    """
        1. 原文件位置 rootdir = '原文件夹'
        2. 现文件位置 resdir ='现文件夹'
    """

    # 查看现文件夹下所有子文件夹名称
    for parent, dirnames, filenames in os.walk(resdir):
        # 通过文件夹名称寻找对应的文件
        for dir in dirnames:
            # 确定是否查找到文件
            num = 0
            # 根据空格来分割关键词
            # print('\ndir:', dir)
            keypoint_list = dir.split(" ")
            # print('keypoint:', keypoint_list)
            # 对每个关键词进行寻找
            for keypoint in keypoint_list:
                # 确定keypoint后续存不存在-MMH
                if keypoint[-4:] == '-MMH':
                    keypoint = keypoint[:-4]
                print('关键词: {}'.format(keypoint))
                # 查找 文件夹a 下的所有pdf文件
                for parent_a, dirnames_a, filenames_a in os.walk(rootdir):
                    for file_a in filenames_a:
                        # 确定pdf文件中是否含有关键词
                        if keypoint in file_a:
                            # 移动文件
                            shutil.copy(join(parent_a, file_a), join(parent, dir, file_a))
                            print('移动 {} 到 {} 成功'.format(join(parent_a, file_a), join(parent, dir, file_a)))
                            # print('移动成功')
                            num += 1
            if num == 0:
                print('文件夹 {} 未发现任何文件'.format(join(parent, dir)))
            else:
                print("\n")





if __name__ == '__main__':
    # main(sys.argv[1], int(sys.argv[2]))
    main()
    print("Finish")
