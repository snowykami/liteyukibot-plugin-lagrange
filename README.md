<h1 align="center"><i>✨ Lagrange Python (liteyuki plugin) ✨ </i></h1>

<h3 align="center">基于 Lagrange-Python 的 liteyuki 实现</h3>

## 简介

基于`Lagrange-Python`的`轻雪插件`实现，欢迎[提出Issue](https://github.com/HornCopper/Lagrange-Python.OneBot/issues)或[提出Pull Request](https://github.com/HornCopper/Lagrange-Python.OneBot/pulls)。

- 原项目[LagrangeDev/lagrange-python](https://github.com/LagrangeDev/lagrange-python)
- 支持收发私聊和群聊消息，和轻雪插件互通，不过还有诸多事件回调待完善

## 💿 安装

<details open>
<summary>使用 git 安装</summary>
把仓库clone到本地（目前暂不上传pypi）

    git clone https://github.com/snowykami/liteyukibot-plugin-lagrange

</details>
将包含lagrange和liteyukibot_plugin_lagrange的文件夹放入你项目的插件文件夹中

## 使用
在轻雪配置项中添加
```yaml
liteyuki.plugins: [ "liteyukibot_plugin_lagrange" ]
lagrange:
  sign-url: "https://to_your_sign.com"  # 配置你的签名服务器，请查阅LagrangeDev/Lagrange.Core获取更多信息
```

## 鸣谢

- 感谢[LagrangeDev](https://github.com/LagrangeDev)以及所有的贡献者们

## 许可证LGPL-2.1

- 原项目lagrange-python基于LGPL-2.1协议分发