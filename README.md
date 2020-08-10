
![](docs/slogan.png)

[中文文档](读我.md)

# Install

```bash
pip install ezpp
```

# What ezpp can

Function |Before|After
:---:|:---:|:---:
Frosted|![A icon before frosted]( docs/lego_mc.jpg)|![A icon after defult frosted](docs/lego_mc_frosted_default.jpg)
ReColor|![picture before recolor](docs/logo_256x256.png)|![picture after recolor](docs/logo_blue.png)
ReSize|![A icon before recolor](docs/logo_256x256.png)|![A icon after recolor](docs/logo_64.png)
ReFormat|lego_mc_l.jpg(203k)|lego_mc_l.webp(109k)|
Text2Icon| "EzPP"|![Simplest call of text2icon](docs/ezpp_t_128.png)
Shadow|![A clean background icon](docs/ezpp_t_128.png)|![Shadow added on clean background](docs/ezpp_t_128_shadow.png)


# How
## 1. Recolor

### 1.1 Recolor Hue of a pic by color.
#### Call from terminal:
```text
$ ezpp recolor -i docs/icon.png -c '#ff0000'
```
#### Output
```text
docs/icon.png + #ff0000 -> docs/icon_0xff0000.png
```
#### Result:
|Before|After recolor -c #ff0000 |
|:---:|:---:|
|![A icon before recolor](docs/icon.png)|![A icon after recolor](docs/icon_0xff0000.png)|

#### Call from terminal with out -o:
```text
ezpp caojianfeng$ ezpp recolor -i docs/logo_256x256.png -o docs/logo_blue.png -c '#3399ff'
```
#### Output
```text
docs/logo_256x256.png + #3399ff -> docs/logo_blue.png
```

Result:
|Before|After #recolor -c #3399ff|
|:---:|:---:|
|![picture before recolor](docs/logo_256x256.png)|![picture after recolor](docs/logo_blue.png)|

### 1.2 Recolor Hue of a pic by hsv.
params：

-u(h**u**e) [0,360]

-s(**s**aturation) [-1.0,1.0]

-v(**v**alue) [-1.0,1.0]

#### Call from terminal:
```text
$ ezpp recolor -i docs/lego_mc.jpg -h 90
$ ezpp recolor -i docs/lego_mc.jpg -s -1.0
$ ezpp recolor -i docs/lego_mc.jpg -v 1.0
```
#### Output
```text
docs/lego_mc.jpg + hsv_s(0.5) -> docs/lego_mc_s(0.5).jpg
```
#### Result:
change s of hsv|effect|change s of hsv|effect|change v of hsv|effect
:---:|:---:|:---:|:---:|:---:|:---:
Before|![A pic before recolor](docs/lego_mc.jpg)|Before|![A pic before recolor](docs/lego_mc.jpg)|Before|![A pic before recolor](docs/lego_mc.jpg)
After recolor -u 0 |![h 0](docs/lego_mc_h(0).jpg)|After recolor -s 1.0 |![s 1.0](docs/lego_mc_s(1.0).jpg)|After recolor-v 0.8 |![v 0.8](docs/lego_mc_v(0.8).jpg)
After recolor -u 60 |![-h 60](docs/lego_mc_h(60).jpg)|After recolor -s 0.5 |![s 0.5](docs/lego_mc_s(0.5).jpg)|After recolor -v 0.5 |![v 0.5](docs/lego_mc_v(0.5).jpg)
After recolor -u 120 |![-h 120](docs/lego_mc_h(120).jpg)|After recolor -s -0.5 |![s -0.5 ](docs/lego_mc_s(-0.5).jpg)|After recolor -v -0.5 |![v -0.5 ](docs/lego_mc_v(-0.5).jpg)
After recolor -u 240 |![-h 240](docs/lego_mc_h(240).jpg)|After recolor -s -1.0 |![s -1.0 ](docs/lego_mc_s(-1.0).jpg)|After recolor -v -0.8 |![v -0.8 ](docs/lego_mc_v(-0.8).jpg)

## 2. Resize
### 2.1. Resize one by size

#### Call from terminal
```text
ezpp resize -i docs/logo_256x256.png -o docs/logo_64.png -s 64
```
#### Output
```text
resize: (256, 256)->(64, 64)
from:   /Volumes/user/cjf/w/ezpp/docs/logo_256x256.png
to:     /Volumes/user/cjf/w/ezpp/docs/logo_64.png
```
#### Result:
|Before|After resize -s 64|
|:---:|:---:|
|![A icon before recolor](docs/logo_256x256.png)|![A icon after recolor](docs/logo_64.png)|

### 2.2. Resize one by width and height

#### Call from terminal
```text
$ ezpp resize -i docs/lego_mc.jpg -s 160x90
```
#### Output
```text
resize: (286, 197)->(160, 90)
from:   /Volumes/user/cjf/w/ezpp/docs/lego_mc.jpg
to:     /Volumes/user/cjf/w/ezpp/docs/lego_mc_160x90.jpg
```
#### Result:
|Before|After resize -s 160x90|
|:---:|:---:|
|![A picture before resize](docs/lego_mc.jpg)|![A picture after resize](docs/lego_mc_160x90.jpg)|


### 2.3. Resize one by percent

#### Call from terminal
```text
$ ezpp resize -i docs/lego_mc.jpg -s 12.5%
```
#### Output
```text
resize: (286, 197)->(35, 24)
from:   /Volumes/user/cjf/w/ezpp/docs/lego_mc.jpg
to:     /Volumes/user/cjf/w/ezpp/docs/lego_mc_35x24.jpg
```
#### Result:
|Before|After resize -s 12.5%|After resize -s 25%|
|:---:|:---:|:---:|
|![A picture before resize](docs/lego_mc.jpg)|![A picture after resize](docs/lego_mc_35x24.jpg)|![A picture after resize](docs/lego_mc_71x49.jpg)|





### 2.4. Resize for App

Resize a Logo 1024x1024 to all sizes you need in android and iOS Application

1024->sizes{android/ios}

#### Call from terminal
```text
ezpp resize -i playground/logo.png -a
```

#### Output:
```text
[1/24]--------- RESIZE ----------
resize: (1024, 1024)->(40, 40)
from:   /Volumes/user/cjf/w/ezpp/playground/logo.png
to:     /Volumes/user/cjf/w/ezpp/playground/logo.png.out/ios/AppIcon.appiconset/Icon-App-20x20@2x.png
[2/24]--------- RESIZE ----------
resize: (1024, 1024)->(60, 60)
from:   /Volumes/user/cjf/w/ezpp/playground/logo.png
to:     /Volumes/user/cjf/w/ezpp/playground/logo.png.out/ios/AppIcon.appiconset/Icon-App-20x20@3x.png

...

[24/24]--------- RESIZE ----------
resize: (1024, 1024)->(192, 192)
from:   /Volumes/user/cjf/w/ezpp/playground/logo.png
to:     /Volumes/user/cjf/w/ezpp/playground/logo.png.out/android/res/mipmap-xxxdpi/ic_launcher.png
[1/1]--------- COPY ----------
from:    /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/ezpp-0.0.3-py3.6.egg/ezpp/resize_cfg/Contents.json
copy to: /Volumes/user/cjf/w/ezpp/playground/logo.png.out/ios/AppIcon.appiconset/Contents.json
```

#### Result:
```text
logo.png.out/
├── android
│   └── res
│       ├── mipmap-hdpi
│       │   └── ic_launcher.png
│       ├── mipmap-mdpi
│       │   └── ic_launcher.png
│       ├── mipmap-xhdpi
│       │   └── ic_launcher.png
│       ├── mipmap-xxhdpi
│       │   └── ic_launcher.png
│       └── mipmap-xxxhdpi
│           └── ic_launcher.png
├── android_stores
│   ├── 1024.png
│   ├── 16.png
│   ├── 216.png
│   ├── 256.png
│   └── 512.png
└── ios
    └── AppIcon.appiconset
        ├── Contents.json
        ├── Icon-App-1024x1024@1x.png
        ├── Icon-App-20x20@1x.png
        ├── Icon-App-20x20@2x.png
        ├── Icon-App-20x20@3x.png
        ├── Icon-App-29x29@1x.png
        ├── Icon-App-29x29@2x.png
        ├── Icon-App-29x29@3x.png
        ├── Icon-App-40x40@1x.png
        ├── Icon-App-40x40@2x.png
        ├── Icon-App-40x40@3x.png
        ├── Icon-App-60x60@2x.png
        ├── Icon-App-60x60@3x.png
        ├── Icon-App-76x76@1x.png
        ├── Icon-App-76x76@2x.png
        └── Icon-App-83.5x83.5@2x.png
```

call from terminal
```bash
ezpp resize -i playground/logo.png -a -o playground/logos
```
Will output resized logos  to folder "playground/logos"

## 3. ReFormat

#### Call from terminal:
```text
$ezpp caojianfeng$ ezpp refmt -i playground/lego_mc_l.jpg  -f WEBP
```
#### Output
```text
comvert: WEBP
from:   /Volumes/user/cjf/w/ezpp/playground/lego_mc_l.jpg
to:     /Volumes/user/cjf/w/ezpp/playground/lego_mc_l.webp
```

#### Result:
|Before|After refmt -f WEBP|
|:---:|:---:|
|lego_mc_l.jpg(203k)|lego_mc_l.webp(109k)|



## 4. Frosted

#### Call from terminal:
```text
$ezpp frosted -i docs/lego_mc.jpg 
```
#### Output
```text
docs/lego_mc.jpg frosted(size = 10) -> docs/lego_mc_frosted.jpg
```
#### Result:
|Before|After frosted default(-s 10)|
|:---:|:---:|
|![A icon before frosted]( docs/lego_mc.jpg)|![A icon after defult frosted](docs/lego_mc_frosted_default.jpg)|

#### Call from terminal with '-s 5':

default -s is 10
-s = 5 will be clearly


```text
$ ezpp frosted -i docs/lego_mc.jpg  -s 5
```
#### Output
```text
docs/lego_mc.jpg frosted(size = 5) -> docs/lego_mc_frosted.jpg
```
#### Result:
|Before|After frosted(-s 5)|After frosted(-s 10) default|
|:---:|:---:|:---:|
|![A icon before frosted]( docs/lego_mc.jpg)|![A icon after frosted](docs/lego_mc_frosted_s5.jpg)|![A icon after defult frosted](docs/lego_mc_frosted_default.jpg)|

## 5. Text to icon:

### Simplest call

#### Call from terminal:

```
ezpp text2icon -t "EzPP" -o playground/ezpp_t.png
```

#### Output
```text
text2icon:[title:EzPP,subtitle:None,color:#ffffff,bgcolor:#3399ff]
```
#### Result:

![Simplest call of text2icon](docs/ezpp_t_128.png)


### Setting subtitle and colors
#### Call from terminal:
```
ezpp text2icon -t "EzPP" -s"ovo.top" -o playground/ezpp_c.png -c "#543" -b "#f93" 
```

#### Output
```text
text2icon:[title:EzPP,subtitle:ovo.top,color:#543,bgcolor:#f93]
```

#### Result:

![Setting subtitle and colors](docs/ezpp_c_128.png)


## 6. Shadow:

Add shadow to a picture which has clean background

### Simplest call

#### Call from terminal:

```
ezpp shadow -i docs/ezpp_t_128.png 
```

#### Output
```text
shadow file with alpha= 0.5:
docs/ezpp_t_128.png 
to docs/ezpp_t_128_shadow.png
```
#### Result:

|Before|After|
|:---:|:---:|
![A clean background icon](docs/ezpp_t_128.png)|![Shadow added on clean background](docs/ezpp_t_128_shadow.png)

### Config shadow alpha


#### Call from terminal:

```
ezpp shadow -i docs/ezpp_t_128.png  -a 0.2
```

#### Output
```text
shadow file with alpha= 0.2:
docs/ezpp_t_128.png 
to docs/ezpp_t_128_shadow.png
```
#### Result:

Before| alpha 0.2|Default(0.5)|alpha 0.8
:---:|:---:|:---:|:---:
![A clean background icon](docs/ezpp_t_128.png)|![Shadow added on clean background, shadow alpha 0.2](docs/ezpp_t_128_shadow_0.2.png)|![Shadow added on clean background, shadow alpha 0.5](docs/ezpp_t_128_shadow.png)|![Shadow added on clean background, shadow alpha 0.8](docs/ezpp_t_128_shadow_0.8.png)

## Recursive for subcommands

### Use -r to  process your images recursively。

The support for recursive calls for each subcommand is as follows：

subcommand|support recursive
:---:|:---:
frosted|yes
recolor|yes
refmt|yes
resize -s|yes
resize -a|no
text2icon |no
shadow |yes

------ 

### Use --overwrite to override the original images

The following command walks through the docs for images and turns them into frosted effects, directly overwriting the original image
```text
$ ezpp frosted -r --overwrite -i docs
```

# ROADMAP
## 1. Ignore colors when recolor a pic.

Recolor with -i flag

## 2. Recolor/Resize all picture under a floder


## 3. Localization help and output

https://www.cnblogs.com/ldlchina/p/4708442.html

https://docs.python.org/3/library/gettext.html

## 4. Control whether to  show preview after tranform picture.