
# What is ezpp

![](docs/logo_256x256.png)

Ezpp is a commandline tool to process your pictures.

ezpp = Easy Process Pictures

# What ezpp can

## 1. ReColor a picture

## 2. ReSize a picture

## 3. Filter a picture

# How
## 1. Recolor



#### Call from terminal:
```text
$ezpp caojianfeng$ ezpp recolor -f docs/icon.png -c '#ff0000'
```
#### Output
```text
docs/logo_256x256.png + #00ff00 -> docs/logo_256x256_0x3399ff.png
```
#### Result:
|Before|After|
|:---:|:---:|
|![A icon before recolor](docs/icon.png)|![A icon after recolor](docs/icon_0xff0000.png)|

#### Call from terminal with out -o:
```text
ezpp caojianfeng$ ezpp recolor -f docs/logo_256x256.png -o docs/logo_blue.png -c '#3399ff'
```
#### Output
```text
docs/logo_256x256.png + #3399ff -> docs/logo_blue.png
```

Result:
|Before|After|
|:---:|:---:|
|![picture before recolor](docs/logo_256x256.png)|![picture after recolor](docs/logo_blue.png)|

## Resize
### 2. Resize one

#### Call from terminal
```text
ezpp resize -f docs/logo_256x256.png -o docs/logo_64.png -s 64
```
#### Output
```text
resize: (256, 256)->(64, 64)
from:   /Volumes/user/cjf/w/ezpp/docs/logo_256x256.png
to:     /Volumes/user/cjf/w/ezpp/docs/logo_64.png
```
#### Result:
|Before|After|
|:---:|:---:|
|![A icon before recolor](docs/logo_256x256.png)|![A icon after recolor](docs/logo_64.png)|


### 2. Resize for App

Resize a Logo 1024x1024 to all sizes you need in android and iOS Application

1024->sizes{android/ios}

#### Call from terminal
```text
ezpp resize -f playground/logo.png -a
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
│       ├── mipmap-xdpi
│       │   └── ic_launcher.png
│       ├── mipmap-xxdpi
│       │   └── ic_launcher.png
│       └── mipmap-xxxdpi
│           └── ic_launcher.png
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
ezpp resize -f playground/logo.png -a -o playground/logos
```
Will output resized logos  to folder "playground/logos"

------

#ROADMAP
## 1. Ignore colors when recolor a pic.

Recolor with -i flag
```bash

```

## 2. Recolor/Resize all picture under a floder


## 3. Localization help and output

https://www.cnblogs.com/ldlchina/p/4708442.html
https://docs.python.org/3/library/gettext.html
