TODO: 

1. localization

https://www.cnblogs.com/ldlchina/p/4708442.html
https://docs.python.org/3/library/gettext.html

2. resize appicons 

1024->sizes{android/ios}

call from terminal
```bash
ezpp resize -f playground/logo.png -a
```


```txt
logo.png.out/
├── android
│   └── res
│       ├── mipmap-hdpi
│       │   └── ic_launcher.png
│       ├── mipmap-mdpi
│       │   └── ic_launcher.png
│       ├── mipmap-xdpi
│       │   └── ic_launcher.png
│       ├── mipmap-xxdpi
│       │   └── ic_launcher.png
│       └── mipmap-xxxdpi
│           └── ic_launcher.png
└── ios
    └── AppIcon.appiconset
        ├── Contents.json
        ├── Icon-App-1024x1024@1x.png
        ├── Icon-App-20x20@1x.png
        ├── Icon-App-20x20@2x.png
        ├── Icon-App-20x20@3x.png
        ├── Icon-App-29x29@1x.png
        ├── Icon-App-29x29@2x.png
        ├── Icon-App-29x29@3x.png
        ├── Icon-App-40x40@1x.png
        ├── Icon-App-40x40@2x.png
        ├── Icon-App-40x40@3x.png
        ├── Icon-App-60x60@2x.png
        ├── Icon-App-60x60@3x.png
        ├── Icon-App-76x76@1x.png
        ├── Icon-App-76x76@2x.png
        └── Icon-App-83.5x83.5@2x.png
```

Call "ezpp resize -f playground/logo.png -a -o logos"
Will output resized logos  to folder "logos"