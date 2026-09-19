# 李宗翰的个人主页

网站：https://lizonghan24-prog.github.io/

首页为个人介绍和七个项目的文字索引。每个项目有独立页面，说明实现内容、调试工作和目前的进展。

## 内容与生成

- `content/projects.json`：项目摘要、技术信息和正文。
- `build.py`：用 Python 标准库生成首页、项目页、站点地图和 robots.txt。
- `dist/styles.css`：响应式样式。
- `dist/favicon.svg`：站点图标。

修改内容后运行 `python build.py`，将生成的 `dist` 文件一起提交。所有页面直接使用 HTML 与 CSS，不需要 JavaScript、外部字体、CDN、数据库或运行时框架。样式链接带文件内容摘要，避免改版后仍使用旧缓存。

## 预览与发布

```powershell
python build.py
python -m http.server 4173 --bind 127.0.0.1 --directory dist
```

推送到 `main` 后，`.github/workflows/pages.yml` 部署 `dist` 到 GitHub Pages。仓库仅包含公开作品介绍与网页源码，不包含本地工程、内部交付文件或历史聊天。

## 表达与设计参考

参考以下主页的文字排版和项目介绍方式。本站文案与样式独立编写，没有复制其代码或内容：

- [Ben Kuhn](https://www.benkuhn.net/)：短介绍、明确的内容列表、适合阅读的行宽。
- [Andrej Karpathy](https://karpathy.ai/)：以具体经历和项目为主的个人介绍。
- [Bartosz Ciechanowski](https://ciechanow.ski/)：技术文章的正文层级与段落间距。

首页去掉了装饰示意图、口号、筛选按钮、状态徽章和流程介绍。项目背景保留在详情页；进展按已有工程和交付记录描述。
