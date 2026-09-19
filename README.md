# 李宗翰 · 工程作品集

网站：https://lizonghan24-prog.github.io/

面向嵌入式系统、运动控制与设备软件的个人作品集。首页展示七个精选项目，支持按专业方向筛选；每个项目有独立静态详情页，介绍问题、系统组成、工程重点、产物和当前阶段。

## 内容与生成

- `content/projects.json`：七个项目的公开介绍、技术标签、进展及边界。
- `build.py`：用 Python 标准库生成首页、项目页、站点地图和 robots.txt。
- `dist/styles.css`：响应式样式。
- `dist/script.js`：渐进增强的项目筛选；关闭 JavaScript 仍能浏览全部内容。
- `dist/favicon.svg`：站点图标。

修改内容后运行 `python build.py`，将生成的 `dist` 文件一起提交。页面不依赖外部字体、CDN、数据库或运行时框架。概念插图由 SVG 绘制，已标注为示意图，不代表产品实拍、实测波形或实际软件截图。

## 预览与发布

```powershell
python build.py
python -m http.server 4173 --bind 127.0.0.1 --directory dist
```

推送到 `main` 后，`.github/workflows/pages.yml` 部署 `dist` 到 GitHub Pages。仓库仅包含公开作品介绍与网页源码，不包含本地工程、内部交付文件或历史聊天。

## 表达与设计参考

参考以专业方向组织能力、通过具体项目展开的表达方式，本站重新制作布局、文案与概念图：

- [Curt Henrichs Portfolio](https://curthenrichs.github.io/)
- [Pankaja Malshan Portfolio](https://pankaja2328.github.io/PortFolio/)

项目背景保留在详情页；首页侧重工程问题与实现。进展按已有工程和交付记录描述，未验证的指标不作为成果展示。
