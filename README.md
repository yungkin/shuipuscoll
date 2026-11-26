
## 目录结构

```
wlblog-static/
├── build.py              生成器主程序（本地运行，不提交）
├── config.json           站点信息、友情链接、文章目录（本地保留，不提交）
├── md/                   文章源文件（Markdown，本地保留，不提交）
│   ├── 1/index.md
│   ├── 2/index.md
│   └── 3/index.md
├── static/               静态资源（本地保留，不提交）
│   ├── image/            图片，构建时复制到 docs/static/image/
│   └── js/search.js      搜索脚本，构建时复制到 docs/static/js/
├── templates/            Jinja2 模板（本地保留，不提交）
│   ├── base.html         公共骨架与样式（换主题只需改这里）
│   ├── index.html        首页
│   ├── post.html         文章详情页
│   ├── collections.html  合集列表页
│   ├── collection.html   合集详情页
│   ├── search.html       搜索页
│   ├── archive.html      归档页
│   ├── 404.html          404 页
│   └── feed.xml          RSS / Atom 订阅源
├── .gitignore            只放行 docs/，其余源文件全部忽略
└── docs/                 构建产物 —— 仓库里唯一被提交的内容
    ├── index.html  collections.html  search.html  archive.html  404.html
    ├── 1.html  2.html  3.html
    ├── collection-blog-tutorial.html
    ├── search-index.json
    ├── feed.xml  .nojekyll
    └── static/js/search.js
```

