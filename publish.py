#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键发布脚本（适配 GitHub Pages「Deploy from a branch + /docs」）

它把原来容易漏掉的三步合成一条命令：
    构建 docs  ->  提交 docs  ->  推送到 GitHub

用法：
    python publish.py                  # 提交说明自动使用当前时间
    python publish.py "新增一篇文章"    # 自定义提交说明

说明：
    - 只提交 docs/（以及 .gitignore、README.md），md/、config.json 等源文件仍不进仓库。
    - 若构建后 docs 没有任何变化，会直接提示并跳过提交，不会产生空提交。
    - 发布后 GitHub 需要 1~3 分钟重新部署，页面缓存约 10 分钟过期。
"""
import os
import sys
import subprocess
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run(cmd):
    """在项目根目录执行命令，实时回显输出。"""
    print("  $ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=BASE_DIR, text=True)


def fail(msg):
    print("\n[X] " + msg)
    sys.exit(1)


def main():
    if not os.path.isdir(os.path.join(BASE_DIR, ".git")):
        fail("当前目录还不是 Git 仓库。请先执行 git init、git remote add origin ... 并完成首次推送。")

    msg = " ".join(sys.argv[1:]).strip() or \
          "更新博客 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    print("[1/4] 构建静态页面 ...")
    if run([sys.executable, "build.py"]).returncode != 0:
        fail("构建失败，已终止发布。请先修复上面的报错。")

    if not os.path.exists(os.path.join(BASE_DIR, "docs", "index.html")):
        fail("构建后找不到 docs/index.html，请检查 build.py 是否正常。")

    print("[2/4] 暂存 docs 产物 ...")
    run(["git", "add", "docs", ".gitignore", "README.md"])

    # 判断是否有实际改动
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=BASE_DIR).returncode == 0:
        print("\n[i] docs/ 没有任何变化，与上次发布内容一致，无需提交。")
        print("    如果你刚写过新文章，请确认：")
        print("      1) md/<ID>/index.md 已保存；")
        print("      2) config.json 的 articles 里已登记该文章及其 title、date。")
        return

    print("[3/4] 提交 ...")
    if run(["git", "commit", "-m", msg]).returncode != 0:
        fail("提交失败。")

    print("[4/4] 推送到 GitHub ...")
    if run(["git", "push"]).returncode != 0:
        fail("推送失败。若远程有新提交，先执行 git pull --rebase 再重试。")

    print("\n[OK] 发布完成。")
    print("     GitHub 收到推送后会重新部署 Pages，约 1~3 分钟生效。")
    print("     若页面仍是旧内容：按 Ctrl+F5 强制刷新，或等约 10 分钟让 CDN 缓存过期。")
    print("     页脚会显示本次「最后构建」时间，可据此确认线上是否已更新。")


if __name__ == "__main__":
    main()
