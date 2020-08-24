

## Shadow:

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
![A clean background icon](ezpp_t_128.png)|![Shadow added on clean background](ezpp_t_128_shadow.png)

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
![A clean background icon](ezpp_t_128.png)|![Shadow added on clean background, shadow alpha 0.2](ezpp_t_128_shadow_0.2.png)|![Shadow added on clean background, shadow alpha 0.5](ezpp_t_128_shadow.png)|![Shadow added on clean background, shadow alpha 0.8](ezpp_t_128_shadow_0.8.png)
