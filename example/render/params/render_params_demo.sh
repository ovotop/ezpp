cd example/render/params
ezpp render -i params.yaml -p '{"icon":"logo_64.png","title":"Hello"}' -o hello.png
ezpp render -i params.yaml -p '{"icon":"logo_64.png","title":"EzPP"}' -o ezpp.png
ezpp render -i params.yaml -p '{"icon":"logo_64.png","title":"Hello EzPP"}' -o hello_ezpp.png
cd ../../../