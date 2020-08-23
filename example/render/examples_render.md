# Examples of ezpp render command

## 1. hello_ezpp

This example show basically using of ezpp render. 
1. How to use canvas.
2. How to use item with type "text".

#### Call from terminal
```text
ezpp render -i example/render/hello_ezpp/hello.yaml
```
#### Output
```text
FROM: example/render/hello_ezpp/hello.yaml
TO: example/render/hello_ezpp/hello.png
```

#### Result:

![](hello_ezpp/hello.png)


## 2. params

This example show how to use params to reuse your *.yaml file.
1. How to use item with type "image"
2. How to use item with type  "shadow"
3. How to use params

#### Call from terminal:
```text
ezpp render -i example/render/params/params.yaml  -p '{"icon":"logo_256x256.png","title":"Hello EzPP"}' -o example/render/params/hello_ezpp.png
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

## 3. slogan

This example show how to setup complex render.
1. How to use item with type "import"
2. How to use item with type "nested"

#### Call from terminal:
```text
ezpp render -i example/render/params/params.yaml  -p '{"icon":"logo_256x256.png","title":"Hello EzPP"}' -o example/render/params/hello_ezpp.png
```

#### Output
```text
FROM: example/render/slogan/ezpp_slogan.yaml
TO: example/render/slogan/ezpp_slogan.png
```

#### Result:

![](slogan/ezpp_slogan.png)
