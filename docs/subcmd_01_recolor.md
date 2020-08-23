## Recolor

### 1. Recolor Hue of a pic by color.
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
|![A icon before recolor](icon.png)|![A icon after recolor](icon_0xff0000.png)|

#### Call from terminal with out -o:
```text
$ezpp recolor -i docs/logo_256x256.png -o docs/logo_blue.png -c '#3399ff'
```
#### Output
```text
docs/logo_256x256.png + #3399ff -> docs/logo_blue.png
```

#### Result:
|Before|After #recolor -c #3399ff|
|:---:|:---:|
|![picture before recolor](logo_256x256.png)|![picture after recolor](logo_blue.png)|

### 2. Recolor Hue of a pic by hsv.
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
Before|![A pic before recolor](lego_mc.jpg)|Before|![A pic before recolor](lego_mc.jpg)|Before|![A pic before recolor](lego_mc.jpg)
After recolor -u 0 |![h 0](lego_mc_h(0).jpg)|After recolor -s 1.0 |![s 1.0](lego_mc_s(1.0).jpg)|After recolor-v 0.8 |![v 0.8](lego_mc_v(0.8).jpg)
After recolor -u 60 |![-h 60](lego_mc_h(60).jpg)|After recolor -s 0.5 |![s 0.5](lego_mc_s(0.5).jpg)|After recolor -v 0.5 |![v 0.5](lego_mc_v(0.5).jpg)
After recolor -u 120 |![-h 120](lego_mc_h(120).jpg)|After recolor -s -0.5 |![s -0.5 ](lego_mc_s(-0.5).jpg)|After recolor -v -0.5 |![v -0.5 ](lego_mc_v(-0.5).jpg)
After recolor -u 240 |![-h 240](lego_mc_h(240).jpg)|After recolor -s -1.0 |![s -1.0 ](lego_mc_s(-1.0).jpg)|After recolor -v -0.8 |![v -0.8 ](lego_mc_v(-0.8).jpg)
