# 智学网错题本转PDF
### by 陈暮尘

- 功能：用于将智学网上的错题本转为PDF
- 注意：本应用需要下载`wkhtmltopdf`
- 运行指南：
    - 下载至本地文件夹
    - 打开 `main.py`
    - 修改以下常量值：
        - `WKHTMLTOPDF_PATH` 为本地*wkhtmltppdf*地址
        - `PRARMETER_PATH` 中用于定义参数，如：纸张大小，纸张页边距，页眉页脚
    - 保存 `main.py`
    - 在终端中运行 `python main.py`
    - 按照终端提示输入指定用户名和密码即可
- 致谢：
    - 登录部分代码来源于`https://github.com/anwenhu/zhixuewang-python`

---

## MIT License
Copyright (c) 2020 陈暮尘

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
