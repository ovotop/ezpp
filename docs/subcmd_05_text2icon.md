
## Text to icon:

### Simplest call

#### Call from terminal:

```
ezpp text2icon -t "EzPP"
```

#### Output
```text
text2icon:[title:EzPP,subtitle:None,color:#ffffff,bgcolor:#3399ff]
```
#### Result:

![Simplest call of text2icon](ezpp_t_128.png)


### Setting color font and subtitle 

option|function
:---|:---
-t or --title  | set title
-s or --subtitle | set subtitle
-c or --color  |set color of the title
-b or --bgcolor |set background color 
-F or --font |set font of the title
-f or --subfont |set font fo the subtitle


You can find fonts under these directories.
```
/System/Library/fonts
~/Library/Fonts
/Library/Fonts
```

#### Call from terminal:
```
ezpp text2icon -t "EzPP" -s "ovo.top" -o playground/ezpp_cm.png -c "#543" -b "#f93" -F /System/Library/fonts/Courier.dfont -f /System/Library/fonts/Monaco.dfont
```

#### Output
```text
text2icon:
[
        title:(EzPP,font:/System/Library/fonts/Courier.dfont),
        subtitle:(ovo.top,subfont:/System/Library/fonts/Monaco.dfont),
        color:#543,
        bgcolor:#f93
]
```

#### Result:

![Setting font color and subtitle](ezpp_cm_128.png)

