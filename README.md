# rickroll诈骗检测

#### 介绍
本项目仅供娱乐整活。这个项目可以帮你检测一个网址里面有没有rickroll诈骗，让你从此以后告别《never gonna give you up》。

#### 使用说明

1.  安装`python环境`，这应该不用我多说了吧，不懂就去百度
2.  用`pip工具`安装`requests库`，执行`pip install requests'，如果出现报错，请自行百度解决
3.  下载本仓库发行版，并解压
4.  切换到解压目录下，通过执行`python main.py`来运行`main.py`
5.  输入要鉴定的网址

#### 注意事项

1.  如果输入网址后出现报错，请先检查网址是否正确，再检查网络状态，最后重新运行本程序，再次输入网址
2.  本项目依赖关键词检测，所以可能无法正确检测，您可以自行修改关键词列表（关键词列表位于`main.py`的`check函数`内，列表名为`ls`，您可以通过修改来检测其他内容）
3.  本项目仅供娱乐整活，请勿用于重大场合