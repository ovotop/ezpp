##  图片换色
### 1 图片换色,通过指定色值换色

参数范围：

-u(h**u**e) [0,360]

-s(**s**aturation) [-1.0,1.0]

-v(**v**alue) [-1.0,1.0]

#### 在命令行输入:
```text
$ezpp caojianfeng$ ezpp recolor -i docs/icon.png -c '#ff0000'
```
#### 输出
```text
docs/icon.png + #ff0000 -> docs/icon_0xff0000.png
```
#### 结果:
|修改前|修改后 recolor -c #ff0000 |
|:---:|:---:|
|![A icon before recolor](icon.png)|![A icon after recolor](icon_0xff0000.png)|

#### 在命令行输入: with out -o:
```text
$ ezpp recolor -i docs/logo_256x256.png -o docs/logo_blue.png -c '#3399ff'
```
#### 输出
```text
docs/logo_256x256.png + #3399ff -> docs/logo_blue.png
```

#### 结果:
|修改前|修改后 #recolor -c #3399ff|
|:---:|:---:|
|![picture before recolor](logo_256x256.png)|![picture after recolor](logo_blue.png)|

### 2 图片换色,通过指定HSV值换色


#### 在命令行输入:
```text
$ ezpp recolor -i docs/lego_mc.jpg -h 90
$ ezpp recolor -i docs/lego_mc.jpg -s -1.0
$ ezpp recolor -i docs/lego_mc.jpg -v 1.0
```
#### 输出
```text
docs/lego_mc.jpg + hsv_s(0.5) -> docs/lego_mc_s(0.5).jpg
```
#### 结果:
change s of hsv|effect|change s of hsv|effect|change v of hsv|effect
:---:|:---:|:---:|:---:|:---:|:---:
修改前|![A pic before recolor](lego_mc.jpg)|修改前|![A pic before recolor](lego_mc.jpg)|修改前|![A pic before recolor](lego_mc.jpg)
修改后 -u 0 |![h 0](lego_mc_h(0).jpg)|修改后  -s 1.0 |![s 1.0](lego_mc_s(1.0).jpg)|修改后  -v 0.8 |![v 0.8](lego_mc_v(0.8).jpg)
修改后 -u 60 |![-h 60](lego_mc_h(60).jpg)|修改后  -s 0.5 |![s 0.5](lego_mc_s(0.5).jpg)|修改后  -v 0.5 |![v 0.5](lego_mc_v(0.5).jpg)
修改后 -u 120 |![-h 120](lego_mc_h(120).jpg)|修改后  -s -0.5 |![s -0.5 ](lego_mc_s(-0.5).jpg)|修改后  -v -0.5 |![v -0.5 ](lego_mc_v(-0.5).jpg)
修改后  -u 240 |![-h 240](lego_mc_h(240).jpg)|修改后  -s -1.0 |![s -1.0 ](lego_mc_s(-1.0).jpg)|修改后  -v -0.8 |![v -0.8 ](lego_mc_v(-0.8).jpg)
