# coding: utf8

"""
 处理剪贴板相关的文件
"""

import os

from util import (image_path, convert_compress_img, notify)
from AppKit import (NSPasteboard, NSPasteboardTypePNG,
                    NSPasteboardTypeTIFF, NSFilenamesPboardType)

# 只支持上传的图片文件格式
ALLOW_FILE_TYPES = ('png', 'jpeg', 'jpg', 'tiff')

TYPE_MAP = {
    'png': NSPasteboardTypePNG,
    'tiff': NSPasteboardTypeTIFF,
}


def get_pasteboard_file_path():
    """
    获取剪贴板的文件路径
    """

    # 获取系统剪贴板对象
    pasteboard = NSPasteboard.generalPasteboard()
    # 剪贴板里的数据类型
    data_type = pasteboard.types()

    # 如果是直接复制的文件
    if NSFilenamesPboardType in data_type:
        # 获取到这个文件的路径和类型
        file_path = pasteboard.propertyListForType_(NSFilenamesPboardType)[0]
        return file_path, 0

    # 剪贴板是png,tiff文件,生成文件返回文件路径
    for file_type, pastedboard_file_type in TYPE_MAP.items():
        if pastedboard_file_type not in data_type:
            continue

        file_path = image_path(file_type)
        data = pasteboard.dataForType_(pastedboard_file_type)
        ret = data.writeToFile_atomically_(file_path, False)
        if not ret:
            notify('从剪贴板写入文件失败')
            return '', 1

        return file_path, 1

    return '', 0


def get_pasteboard_img_path():
    """获取剪贴板图片文件路径"""

    file_path, remove_raw = get_pasteboard_file_path()
    if not file_path:
        notify('请先截图或者复制一张图片')
        return ''

    print 'path:{0}, remove:{1}'.format(file_path, remove_raw)

    file_name = os.path.split(file_path)[-1]
    file_type = file_name.split('.')[-1]

    # 检查是否是图片类型的文件
    if file_type not in ALLOW_FILE_TYPES:
        notify('文件类型{0}不在支持列表[png、jpeg、jpg、tiff]'.format(file_type))
        return ''

    file_path = convert_compress_img(file_path, remove_raw)

    return file_path


def write_to_pasteboard(text):
    """内容写入剪贴板
    :param text: 写入内容
    """
    os.system('echo \'{}\' | pbcopy'.format(text))
