# -*- coding: utf-8

import git
from util import (time_now_str)
import config

branch = config.BRANCH


def check_branch_exist(all_branch_str, exist_branch):
    is_exist = [0, 0]
    branchs = all_branch_str.split('\n')
    # find local branch
    for item in branchs:
        if 0 == cmp(item[2:], exist_branch):
            is_exist[0] = 1
            break

    # find remote branch
    for item in branchs:
        if -1 != item.find('remotes/origin/'):
            if 0 == cmp(item[item.rfind('/') + 1:], exist_branch):
                is_exist[1] = 1

    return is_exist


def switch_branch(git_repo):
    branch_str = git_repo.git.branch('-a')
    is_branch_exist = check_branch_exist(branch_str, branch)
    if 1 == is_branch_exist[0]:
        git_repo.git.checkout(branch)
    else:
        git_repo.git.branch(branch)
        git_repo.git.checkout(branch)

    if 1 == is_branch_exist[1]:
        print 'pull...'
        print git_repo.git.pull('origin', branch)
        print 'pull complete'


def commit(git_repo, comment):
    print git_repo.git.add('.')
    print git_repo.git.commit(m=comment)
    print 'push origin...'
    push_result = git_repo.git.push('origin', branch)
    if not push_result:
        print 'push complete'
    else:
        print 'push err: {}'.format(push_result)
    return push_result


def image_url(file_name):
    return 'https://raw.githubusercontent.com/{0}/{1}/{2}/{3}/{4}'.format(config.GITHUB_NAME,
                                                                          config.REPO_NAME,
                                                                          branch,
                                                                          config.IMAGE_RELATIVE_PATH,
                                                                          file_name)


def upload2github():
    try:
        git_repo = git.Repo(config.LOCAL_PATH)
    except Exception, e:
        print Exception, ":", e
        return '本地路径不是一个git仓库'

    switch_branch(git_repo)
    return commit(git_repo, '{0} auto upload by python'.format(time_now_str()))
