### file and filename
file 绝对路径
filename 相对与当前yaml的路径

## layer types
### import 
约束 import只能用相对位置查找，且位于当前目录下。
import layer 引用yaml时只能用 filename

```yaml
items:
-
  type: "import"
  filename: "ezpp_slogan_top.yaml"
  pos:
    x: 0
    y: 0
```