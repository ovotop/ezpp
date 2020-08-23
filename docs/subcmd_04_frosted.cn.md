## 毛玻璃效果

#### 在命令行输入:
```text
ezpp frosted -i docs/lego_mc.jpg 
```
#### 输出
```text
docs/lego_mc.jpg frosted(size = 10) -> docs/lego_mc_frosted.jpg
```
#### 结果:
|修改前|修改后 frosted default(-s 10)|
|:---:|:---:|
|![A icon before frosted]( lego_mc.jpg)|![A icon after defult frosted](lego_mc_frosted_default.jpg)|


#### 在命令行输入: with '-s 5':

default -s is 10
-s = 5 will be clearly


```text
$ ezpp frosted -i docs/lego_mc.jpg  -s 5
```
#### 输出
```text
docs/lego_mc.jpg frosted(size = 5) -> docs/lego_mc_frosted.jpg
```
#### 结果
|修改前|修改后 frosted(-s 5)|修改后 frosted(-s 10) default|
|:---:|:---:|:---:|
|![A icon before frosted]( lego_mc.jpg)|![A icon after frosted](lego_mc_frosted_s5.jpg)|![A icon after defult frosted](lego_mc_frosted_default.jpg)|

