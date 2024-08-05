```python
help()

help> keywords
help> quit 
```

```python
dir(__builtins__)
```
```CMD
SET PYTHONPATH='/Users/xieweizhe/Desktop/MacCode/Python-Technical-Manual/Code/ACL059900_python39/samples/CH02'
```
在 zsh 中，環境變數的設定方式與 Windows 的命令提示字元不同。你可以使用 `export` 命令來設定 `PYTHONPATH` 環境變數。以下是正確的命令：
```zsh
export PYTHONPATH='/Users/xieweizhe/Desktop/MacCode/Python-Technical-Manual/Code/ACL059900_python39/samples/CH02'
```

這樣可以在當前的 shell session 中設定 `PYTHONPATH`。如果需要永久設定這個環境變數，可以將這行命令添加到你的 `~/.zshrc` 文件中。修改 `~/.zshrc` 文件可以使用以下命令：
```zsh
nano ~/.zshrc
```

然後在文件末尾添加：
```zsh
export PYTHONPATH='/Users/xieweizhe/Desktop/MacCode/Python-Technical-Manual/Code/ACL059900_python39/samples/CH02'
```

保存並退出編輯器，然後執行以下命令以使更改生效：
```zsh
source ~/.zshrc
```

```python 
import sys
sys.getsizeof(1)
```
```python
oct(10)
hex(10)
```
```python
text = "abc"
text.encode('utf-8).decode('utf-8)

```
```python
import sys
x = [1, 3, 3]
sys.getrefcount(x)
```
