# -*- coding: utf-8
import os
import subprocess
import time
import platform
import config


CONFIG_FILE = 'config.py'

def check_config():
    if not all((config.LOCAL_PATH, config.GITHUB_NAME, config.REPO_NAME, config.IMAGE_RELATIVE_PATH, config.BRANCH)):
        notify('请先设置相关参数!')
        open_with_editor()
        return False
    local_path = full_path(config.LOCAL_PATH)
    if not os.path.exists(local_path):
        notify('{}路径不存在'.format(local_path))
        return False

    image_save_path = '{}/{}'.format(local_path, config.IMAGE_RELATIVE_PATH)
    if not os.path.exists(image_save_path):
        os.makedirs(image_save_path)
        # notify('{}路径不存在'.format(image_save_path))
        # return False

    return True


def open_with_editor():
    """ open file with apple's text editor"""
    os.system('open -b "com.apple.TextEdit" "./{}"'.format(CONFIG_FILE))


def full_path(path):
    first = path[0]
    if first == '~':
        return '{0}{1}'.format(os.path.expanduser('~'), path[1:])
    else:
        return path


def image_path(image_type):
    return '{0}/{1}/{2}.{3}'.format(full_path(config.LOCAL_PATH),
                                    config.IMAGE_RELATIVE_PATH,
                                    int(time.time() * 1000),
                                    image_type)


def time_now_str():
    time_sec = time.time()
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_sec))


def compress_png(raw_img):
    """ use pngquant to compress:https://github.com/pornel/pngquant"""
    print 'start compress_png:%s' % raw_img
    if not os.path.exists(raw_img):
        notify('压缩图片源不存在', '压缩图片失败')

    compress_img = image_path('png')
    if not subprocess.call('pngquant/pngquant --force {0} -o {1}'.format(raw_img, compress_img), shell=True):
        os.remove(raw_img)
        return compress_img
    else:
        return raw_img


def convert_compress_img(raw_img, remove_raw):
    file_type = raw_img.split('.')[-1]
    img_path = raw_img

    if 0 != cmp(file_type, 'png'):
        img_path = convert_to_png(raw_img, remove_raw)

    return compress_png(img_path)


""" 下面的方法是mac相关的"""
def check_is_mac():
    return 0 == cmp(platform.system(), 'Darwin') or 0 == cmp(platform.system(), 'mac')

def notify(text, title='上传Github'):
    os.system('''
              osascript -e 'display notification "{}" with title "{}"'
              '''.format(text, title))


def convert_to_png(raw_img, remove_raw):
    # convert it to png file
    print 'start convert_to_png:%s' % raw_img
    png_img = image_path('png')
    width, height = get_img_size(raw_img)
    if remove_raw and check_is_mac():
        width /= 2
        height /= 2
    os.system('sips -z {2} {3}  -s format png {0} --out {1}'.format(raw_img, png_img, height, width))
    if remove_raw:
        os.remove(raw_img)
    return png_img


def get_img_size(img_path):
    """获取图片尺寸
    :param img_path: 图片路径
    """
    print 'get_img_size %s' % img_path
    width = os.popen("sips -g pixelWidth %s | awk -F: '{print $2}'" % img_path).read()
    height = os.popen("sips -g pixelHeight %s | awk -F: '{print $2}'" % img_path).read()

    width = int(width.strip())
    height = int(height.strip())

    return width, height
