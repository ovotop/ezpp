
## 纯文本图标:

### 最简单的调用
#### 在命令行输入:


```
ezpp text2icon -t "EzPP"
```

#### 输出
```text
text2icon:[title:EzPP,subtitle:None,color:#ffffff,bgcolor:#3399ff]
```
#### 结果:

![最简单的text2icon结果](ezpp_t_128.png)


### 指定颜色、字体和副标题

选项|功能
:---|:---
-t 或者 --title|指定主标题
-s 或者 --subtitle|指定副标题
-c 或者 --color|指定前景色
-b 或者 --bgcolor|指定背景色
-F 或者 --font|指定主标题字体
-f 或者 --subfont|指定副标题字体

你可以在以下目录找到你需要的字体
```
/System/Library/fonts
~/Library/Fonts
/Library/Fonts
```

#### 在命令行输入:
```
ezpp text2icon -t "EzPP" -s "ovo.top" -o playground/ezpp_cm.png -c "#543" -b "#f93" -F /System/Library/fonts/Courier.dfont -f /System/Library/fonts/Monaco.dfont
```

#### 输出
```text
text2icon:
[
        title:(EzPP,font:/System/Library/fonts/Courier.dfont),
        subtitle:(ovo.top,subfont:/System/Library/fonts/Monaco.dfont),
        color:#543,
        bgcolor:#f93
]
```

#### 结果

![指定颜色和副标题结果](ezpp_cm_128.png)

