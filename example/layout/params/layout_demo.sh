cd example/layout/params
ezpp layout -i params.yaml -p '{"icon":"logo_64.png","title":"Hello"}' -o hello.png
ezpp layout -i params.yaml -p '{"icon":"logo_64.png","title":"EzPP"}' -o ezpp.png
ezpp layout -i params.yaml -p '{"icon":"logo_64.png","title":"Hello EzPP"}' -o hello_ezpp.png
cd ../../../