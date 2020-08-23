# Examples of ezpp layout command

## 1. hello_ezpp

This example show basically using of ezpp layout. 
1. How to use canvas.
2. How to use item with type "text".

#### Call from terminal
```text
ezpp layout -i example/layout/hello_ezpp/hello.yaml
```
#### Output
```text
FROM: example/layout/hello_ezpp/hello.yaml
TO: example/layout/hello_ezpp/hello.png
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
ezpp layout -i example/layout/params/params.yaml  -p '{"icon":"logo_256x256.png","title":"Hello EzPP"}' -o example/layout/params/hello_ezpp.png
```
#### Output
```text
FROM: example/layout/params/params.yaml
TO: example/layout/params/hello_ezpp.png
```

#### Result:

![](params/hello_ezpp.png)

#### Power of params!

You can also make a *.sh file like this.
```bash
cd example/layout/params
ezpp layout -i params.yaml -p '{"icon":"logo_64.png","title":"Hello"}' -o hello.png
ezpp layout -i params.yaml -p '{"icon":"logo_64.png","title":"EzPP"}' -o ezpp.png
ezpp layout -i params.yaml -p '{"icon":"logo_64.png","title":"Hello EzPP"}' -o hello_ezpp.png
cd ../../../
```

This shell will create these:

![](params/hello.png)
![](params/ezpp.png)
![](params/hello_ezpp.png)

Or batch processing of datas. And call 'ezpp layout ***' automatically.

## 3. slogan

This example show how to setup complex layout.
1. How to use item with type "import"
2. How to use item with type "nested"

#### Call from terminal:
```text
ezpp layout -i example/layout/params/params.yaml  -p '{"icon":"logo_256x256.png","title":"Hello EzPP"}' -o example/layout/params/hello_ezpp.png
```

#### Output
```text
FROM: example/layout/slogan/ezpp_slogan.yaml
TO: example/layout/slogan/ezpp_slogan.png
```

#### Result:

![](slogan/ezpp_slogan.png)
