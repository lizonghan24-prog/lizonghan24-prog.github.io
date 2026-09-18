# 李宗翰 · 个人网站

适合 GitHub Pages 的静态个人主页，包含介绍、作品、关于和 GitHub 联系入口。没有构建依赖，不需要数据库或付费服务。支持手机屏幕、键盘导航和系统减少动画偏好；所有网页资源随仓库提供，不依赖外部字体/CDN。

## 修改资料

- `dist/profile.js`：站点名称、问候语、介绍、GitHub 和邮箱。邮箱留空不会显示。
- `dist/index.html`：首页结构、作品和无需 JavaScript 时显示的内容；修改资料后建议同步这里的标题与介绍，以便搜索引擎直接读取。
- `dist/styles.css`：颜色与布局。

目前个人介绍是可修改的初稿；作品仅展示这个已实现的网站，没有填写虚构的经历或项目。

## 发布到 GitHub Pages

目标仓库：`lizonghan24-prog/lizonghan24-prog.github.io`。

1. 在 GitHub 上创建上述公开仓库，将本目录内的文件（包括 `.github`）推送到 `main` 分支。
2. 进入仓库 **Settings → Pages → Build and deployment → Source**，选择 **GitHub Actions**。
3. 在 **Actions → Publish personal website** 中运行工作流；之后每次推送到 `main` 都会自动更新。
4. 工作流成功后访问 `https://lizonghan24-prog.github.io/`。

只有 `dist` 中的公开网页会被部署，不会公开本机其他文件。仓库本身的源码在公开仓库中可见。

官方说明：https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## 本地预览

在本目录执行：

```powershell
python -m http.server 4173 --bind 127.0.0.1 --directory dist
```

然后打开 http://127.0.0.1:4173/ 。也可以直接双击 `dist/index.html` 预览。
