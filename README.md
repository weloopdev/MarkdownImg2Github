# MarkdownImg2Github

Mac下自动上传图片到`Github`，并把`Markdown`格式的图片`url`复制到`clipboard`

> 该项目供远峰运动团队使用，目前只有Mac版本

## 使用方法

### 第三方库

- 安装`GitPython`

```ruby
# 安装pip
$sudo easy_install pip
# 安装GitPython
$pip install GitPython
```

- 如果没有安装`Aflred`自行安装

### Github仓库

我们的图床仓库在`weloopdev`账号下的`yfimg`仓库，没有加入到该项目的同学请提供`github`账号

- 把`yfimg` `clone`到本地，如果遇到问题请到`TAPD`上去看下[Github的配置](https://www.tapd.cn/20084761/markdown_wikis/view/#1120084761001000712)

```ruby
$ git clone git@github.com:weloopdev/yfimg.git
Cloning into 'yfimg'...
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), 4.68 KiB | 0 bytes/s, done.
```

### Alfred workflow设置

- 下载`MarkdownImg2Github`仓库下的`MarkdownImg2Github.alfredworkflow`双击导入`workflow`
- 双击`HotKey`设置一个快捷键，比如 `command+shift+v`

![image](https://raw.githubusercontent.com/weloopdev/yfimg/yangxi/tapd/1489334346502.png)

- 第一次使用会让配置参数，配置好之后保存下就ok，如下图:
  - LOCAL_PATH：从`Github` `git clone`到本地的路径
  - GITHUB_NAME：接入`Github`账号名称，目前我们都放在`weloopdev`这个账号下
  - REPO_NAME：仓库名称，目前我们放在`yfimg`这个仓库下
  - IMAGE_RELATIVE_PATH：图片在仓库下面的相对路径，目前我们统一放到`tapd`下面
  - BRANCH：自己的分支，这个我们强制每个人使用自己的分支

![image](https://raw.githubusercontent.com/weloopdev/yfimg/yangxi/tapd/1489334473397.png)

- 配置填好之后，在`Aflred`输入`mdimgconfig`可以修改配置

![image](https://raw.githubusercontent.com/weloopdev/yfimg/yangxi/tapd/1489335067854.png)

- 复制一张图片或者截图后，使用快捷键`command+shift+v`上传到`github`看到下图提示后，`command+v`即可拿到`markdown`格式的`url`

![image](https://raw.githubusercontent.com/weloopdev/yfimg/yangxi/tapd/1489335617663.png)



## 参考资料

- [第三方库GitPython](http://stackoverflow.com/questions/1456269/python-git-module-experiences)
- 两个自动上传到七牛的的例子，[例子1](https://github.com/tiann/markdown-img-upload) [例子2](https://github.com/kaito-kidd/markdown-image-alfred)