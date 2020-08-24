## 加阴影:

给一个有单色背景的图标加阴影

### 最简单的调用

#### 在命令行输入:

```
ezpp shadow -i docs/ezpp_t_128.png 
```

#### 输出
```text
shadow file with alpha= 0.5:
docs/ezpp_t_128.png 
to docs/ezpp_t_128_shadow.png
```
#### 结果

|Before|After|
|:---:|:---:|
![A clean background icon](ezpp_t_128.png)|![Shadow added on clean background](ezpp_t_128_shadow.png)

### 控制阴影颜色


#### 在命令行输入:

```
ezpp shadow -i docs/ezpp_t_128.png  -a 0.2
```

#### 输出
```text
shadow file with alpha= 0.2:
docs/ezpp_t_128.png 
to docs/ezpp_t_128_shadow.png
```
#### 结果:

Before| alpha 0.2|Default(0.5)|alpha 0.8
:---:|:---:|:---:|:---:
![A clean background icon](ezpp_t_128.png)|![Shadow added on clean background, shadow alpha 0.2](ezpp_t_128_shadow_0.2.png)|![Shadow added on clean background, shadow alpha 0.5](ezpp_t_128_shadow.png)|![Shadow added on clean background, shadow alpha 0.8](ezpp_t_128_shadow_0.8.png)

