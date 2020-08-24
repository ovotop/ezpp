
## 图片改尺寸
### 1. Resize one by size

#### 在命令行输入:
```text
ezpp resize -i docs/logo_256x256.png -o docs/logo_64.png -s 64
```
#### 输出
```text
resize: (256, 256)->(64, 64)
from:   /Volumes/user/cjf/w/ezpp/docs/logo_256x256.png
to:     /Volumes/user/cjf/w/ezpp/docs/logo_64.png
```
#### 结果:
|修改前|修改后 resize -s 64|
|:---:|:---:|
|![A icon before recolor](logo_256x256.png)|![A icon after recolor](logo_64.png)|

### 2. Resize one by width and height

#### 在命令行输入:
```text
$ ezpp resize -i docs/lego_mc.jpg -s 160x90
```
#### 输出
```text
resize: (286, 197)->(160, 90)
from:   /Volumes/user/cjf/w/ezpp/docs/lego_mc.jpg
to:     /Volumes/user/cjf/w/ezpp/docs/lego_mc_160x90.jpg
```
#### 结果:
|修改前|修改后 resize -s 160x90|
|:---:|:---:|
|![A picture before resize](lego_mc.jpg)|![A picture after resize](lego_mc_160x90.jpg)|


### 3. Resize one by percent

#### 在命令行输入:
```text
$ ezpp resize -i docs/lego_mc.jpg -s 12.5%
```
#### 输出
```text
resize: (286, 197)->(35, 24)
from:   /Volumes/user/cjf/w/ezpp/docs/lego_mc.jpg
to:     /Volumes/user/cjf/w/ezpp/docs/lego_mc_35x24.jpg
```
#### 结果:
|修改前|修改后 resize -s 12.5%|修改后 resize -s 25%|
|:---:|:---:|:---:|
|![A picture before resize](lego_mc.jpg)|![A picture after resize](lego_mc_35x24.jpg)|![A picture after resize](lego_mc_71x49.jpg)|





### 4. 生成应用图标

用一个1024x1024的应用图标，生成安卓和iOS需要的所有大小的图标。

#### 在命令行输入:
```text
$ezpp resize -i playground/logo.png -a
```

#### 输出:
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

#### 结果:
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
