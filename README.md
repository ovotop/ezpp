
![](docs/ezpp_slogan.png)

[中文文档](README.CN.md)

# 1. Install

```bash
pip3 install ezpp
```

# 2. What ezpp can and how

## 2.1 Picture process

What |Before|After|How to
:---:|:---:|:---:|:---
Frosted|![A icon before frosted]( docs/ezpp_slogan_256x128.png)|![A icon after defult frosted](docs/ezpp_slogan_256x128_frosted.png)|[🔗How to Frosted](docs/subcmd_04_frosted.md)
ReColor|![picture before recolor](docs/logo_256x256.png)|![picture after recolor](docs/logo_blue_hsv_v(-0.5).png)|[🔗How to ReColor](docs/subcmd_01_recolor.md)
ReSize|![A icon before recolor](docs/logo_256x256.png)|![A icon after recolor](docs/logo_64.png)|[🔗How to ReSize](docs/subcmd_02_resize.md)
ReFormat|lego_mc_l.jpg(203k)|lego_mc_l.webp(109k)|[🔗How to ReFormat](docs/subcmd_03_reformat.md)
Text2Icon| "EzPP"|![Simplest call of text2icon](docs/ezpp_t_128.png)|[🔗How to Text2Icon](docs/subcmd_05_text2icon.md)
Shadow|![A clean background icon](docs/ezpp_t_128.png)|![Shadow added on clean background](docs/ezpp_t_128_shadow.png)|[🔗How to Shadow](docs/subcmd_06_shadow.md)
Render|ezpp_slogan.yaml|![slogan](docs/ezpp_slogan_256x128.png)|[🔗How to Render](examples/render/examples_render.md)


## 2.2 ListFonts 
Display preview for font selection。

```shell
ezpp listfonts -s
ezpp listfonts -u
ezpp listfonts -d ./fonts_dir
```
-s  system fonts (/System/Library/fonts) 

-u  user fonts (~/Library/fonts)

-d  fonts in input dir

You can use -c/--imgcat for iterm2.And show preview in iterm2 directly.

```shell
ezpp listfonts -s -c
ezpp listfonts -s --imgcat 
```


# 3. Common params

## Input file
### Use '-i' or '--infile' provide a input file.

Only text2icon sub command not support -i

## Output file
### Use '-o' or '--outfile' provide a output file.
                            
If you provide a '-p' or '--preview' flag . Output file will be ignored.

## Recursive for subcommands

### Use -r to  process your images recursively。

The support for recursive calls for each subcommand is as follows：

subcommand|support recursive
:---:|:---:
frosted|yes
recolor|yes
refmt|yes
resize -s|yes
resize -a|no
text2icon |no
shadow |yes
render |no
listfonts |no

### Use --overwrite to override the original images

The following command walks through the docs for images and turns them into frosted effects, directly overwriting the original image
```text
$ ezpp frosted -r --overwrite -i docs
```

### Use --preview to show your results directly

The following command walks through the docs for images and turns them into frosted effects, directly overwriting the original image
```text
$ ezpp text2icon -t "EzPP" -c "#93f" -b "#543" --preview
```
------ 
# ROADMAP
- [ ] 1. Ignore colors when recolor a pic.

Recolor with -i flag

- [Done] 2. Recolor/Resize all picture under a floder 


- [ ] 3. Localization help and output

https://www.cnblogs.com/ldlchina/p/4708442.html

https://docs.python.org/3/library/gettext.html

[GNU gettext utilities](https://www.gnu.org/software/gettext/manual/gettext.html)

[关于操作系统中英文切换的.po和.mo介绍](https://www.cnblogs.com/linux-wang/p/9001368.html)


- [Done] 4. Control whether to  show preview after tranform picture.

- [Done] 5. Layout support postion.
- [ ] 6. Layout support Row and Column flex mode.
- [ ] 7. Gif Animation.