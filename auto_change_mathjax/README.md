### 说明
此脚本来自 [Hexo 数学公式支持（任意主题）](http://blog.xandery.top/archives/78cbabaa.html)

简单说一下：
Hexo 官方的数学公式渲染插件 [hexo-math](https://github.com/hexojs/hexo-math) 只支持行内公式，且使用如下包裹方式：
```markdown
{% mathjax '{options}' %}
content
{% endmathjax %}
```
使用此脚本可以实现将含有由 `$...$` 和 `$$...$$` 包裹的数学公式的 md 文件转换为支持 hexo-math 的文件