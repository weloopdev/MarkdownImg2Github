# -*- coding: utf-8

import os
from clipboard import (get_pasteboard_img_path, write_to_pasteboard)
from github import (upload2github, image_url)
from util import (notify, get_img_size, check_config)

# IMG_TPL = '<img src=\"{}\" width=\"{}\" height=\"{}\" />'
IMG_TPL = '![image]({})'

def upload_img2github():
    if not check_config():
        return

    img_path = get_pasteboard_img_path()

    if img_path:
        notify("开始上传图片到github，请稍等")
        result = upload2github()
        if result:
            notify(result)
            os.remove(img_path)
        else:
            # width, height = get_img_size(img_path)
            image_name = os.path.split(img_path)[-1]
            # markdown_img = IMG_TPL.format(image_url(image_name), width, height)
            markdown_img = IMG_TPL.format(image_url(image_name))
            print markdown_img
            write_to_pasteboard(markdown_img)
            notify('Markdown格式Image已在Clipboard')


def main():
    """main"""
    upload_img2github()

if __name__ == '__main__':
    main()