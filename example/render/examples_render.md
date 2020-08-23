# Examples of ezpp render command

## 1. hello_ezpp

This example show basically using of ezpp render. 
1. How to use canvas.
2. How to use item type "text".
3. How to custom font by filename.
4. How to custom font by path.

#### Call from terminal
```text
ezpp render -i example/render/hello_ezpp/hello.yaml
ezpp render -i example/render/hello_ezpp/hello_custom_font.yaml
```

example/render/hello_ezpp/hello.yaml
```yaml
# ezpp render -i example/render/hello_ezpp/hello.yaml
canvas:
  width: 240
  height: 80
  color: "#f93"  # "#RGBA" or "#RRGGBBAA"

items:
- 
  type: "text"
  title: "Hello, EzPP"
  pos:
    x: "center"
    y: "center"
  font:
    path: "/System/Library/fonts/Monaco.dfont"
    # filename: "ZhenyanGB.ttf"
    size: 24
    color: "#543"
```
#### Output
```text
FROM: example/render/hello_ezpp/hello.yaml
TO: example/render/hello_ezpp/hello.png
FROM: example/render/hello_ezpp/hello_custom_font.yaml
TO: example/render/hello_ezpp/hello_custom_font.png
```

#### Result:

![](hello_ezpp/hello.png)
![](hello_ezpp/hello_custom_font.png)

## 2. params

This example show how to use params to reuse your *.yaml file.
1. How to use item type "image".
2. How to use item type  "shadow".
3. How to use params.

#### Call from terminal:
```text
ezpp render -i example/render/params/params.yaml  -p '{"icon":"logo_256x256.png","title":"Hello EzPP"}' -o example/render/params/hello_ezpp.png
```
example/render/params/params.yaml
```yaml
# params defines
params: 
  - "title"
  - "icon"

canvas:
  width: 256
  height: 80
  color: "#f93" 

items:
-
  type: "image"
  filename: "__icon__" # params using
  pos:
    x: 16
    y: "center"
- 
  title: "__title__" # params using
  type: "text"
  visible: true
  pos:
    x: 96
    y: "center"
  font:
    path: "/System/Library/fonts/Monaco.dfont"
    size: 24
    color: "#543"
        
-
  type: "shadow"
  alpha: 0.1 # 0.0-1.0  shadow color is #000a

```
#### Output
```text
FROM: example/render/params/params.yaml
TO: example/render/params/hello_ezpp.png
```

#### Result:

![](params/hello_ezpp.png)

#### Power of params!

You can also make a *.sh file like this.

example/render/params/render_params_demo.sh:
```bash
cd example/render/params
ezpp render -i params.yaml -p '{"icon":"logo_64.png","title":"Hello"}' -o hello.png
ezpp render -i params.yaml -p '{"icon":"logo_64.png","title":"EzPP"}' -o ezpp.png
ezpp render -i params.yaml -p '{"icon":"logo_64.png","title":"Hello EzPP"}' -o hello_ezpp.png
cd ../../../
```

This shell will create these:

![](params/hello.png)
![](params/ezpp.png)
![](params/hello_ezpp.png)

Or batch processing of datas. And call 'ezpp render ***' automatically.

## 3. mask
This example show how to use params to reuse your *.yaml file.
1. How to use item type "image".
2. How to use item type  "shadow".
3. How to use item type  "nested".
4. How to use canvas prop color.
5. How to use canvas prop antialias_size.

#### Call from terminal:
```text
ezpp render -i example/render/mask/mask.yaml 
ezpp render -i example/render/mask/mask_antialias.yaml 
```

example/render/mask/mask.yaml 
```yaml
canvas:
#...

items:
-
  type: "image"
#...
-
  type: "shadow"
  alpha: 0.1
  
-
  type: "nested" # Just like a inline yaml file
  pos:
    x: 48
    y: "center"
  canvas:
    width: 204
    height: 72 
    antialias_size: 4 # 1,2,4,8,16 antialias range,The bigger the slower
    color: "#0006" # "#RGB6" means alpha = 6/16
  items:      
  - 
    type: "text"
    title: "EzPP"
    pos:
      x: "center"
      y: "center"
    font:
      path: "/System/Library/fonts/Monaco.dfont"
      size: 32
      color: "#543"
```
#### Output
```text
FROM: example/render/mask/mask.yaml
TO: example/render/mask/mask.png
FROM: example/render/mask/mask_antialias.yaml
TO: example/render/mask/mask_antialias.png
```

#### Result:

![](mask/mask_text.png) bing nested to below:

![](mask/mask.png)
![](mask/mask_antialias.png)

## 4. slogan

This example show how to setup complex render.
1. How to use item type "image".
2. How to use item type  "shadow".
3. How to use item type "import" to reuse you .yaml file.

#### Call from terminal:
```text
ezpp render -i example/render/slogan/ezpp_slogan.yaml          
```

example/render/slogan/ezpp_slogan.yaml 
```yaml
#...
items:
-
  type: "import"
  filename: "ezpp_slogan_top.yaml"
  pos:
    x: 0
    y: 0
#...
```

#### Output
```text
FROM: example/render/slogan/ezpp_slogan.yaml
TO: example/render/slogan/ezpp_slogan.png
```

#### Result:

![](slogan/ezpp_slogan.png)
