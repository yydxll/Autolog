import os
import shutil


def copy(mubanpath, addressmonth, copymubanpath, realmubanpath):
    source = mubanpath
    target = addressmonth

    try:
        shutil.copy(source, target)
        print("模板复制成功")
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:")

    srcFile = copymubanpath
    dstFile = realmubanpath

    try:
        os.rename(srcFile, dstFile)
        print('命名成功')
    except Exception as e:
        print(e)
        print('命名失败')


