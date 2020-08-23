## 3.4. Frosted

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
|![A icon before frosted]( lego_mc.jpg)|![A icon after defult frosted](lego_mc_frosted_default.jpg)|

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
|![A icon before frosted]( lego_mc.jpg)|![A icon after frosted](lego_mc_frosted_s5.jpg)|![A icon after defult frosted](lego_mc_frosted_default.jpg)|
