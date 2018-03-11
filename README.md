# jsbox_sublime
A ST3 plugin for Jsbox

在SublimeText3下开发Jsbox脚本的插件

### 插件下载

1. **git clone** 或者 **下载** 仓库中 **Jsbox** 文件夹
2. 将 **Jsbox** 文件夹拷贝到 **Sublime Text 3/Packages** 目录下

### 配置Host

修改 **Jsbox/Jsbox.sublime-settings** 文件，将host字段改为APP中对应的字段。

```json
{
  "host": "192.168.xxx.xxx"
}
```

### 加载插件依赖

1. 打开 **Sublime Text 3**
2. **Ctrl + Shift + P** 呼出 **Package Control**
3. 输入 **Satisfy Dependencies** 安装插件依赖

### 命令简介

![](https://github.com/Fndroid/jsbox_sublime/blob/master/imgs/jsbox_plugin.png?raw=true)

1. Download File: 从手机中下载脚本
2. Sync File: 同步脚本文件或安装包（将安装包或js文件发送到APP）

### 保存推送

当脚本或应用中有文件触发保存，将触发一次 **Sync File** 命令

### 最后

1. 暂时没做补全（我基本不用代码提示。。。），有人乐意可以自己做一下
2. 快捷键只有Windows下的，有兴趣可以自己加
