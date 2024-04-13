### 说明
说来话长，此脚本来自[#转换脚本](http://blog.xandery.top/archives/78cbabaa.html#%E8%BD%AC%E6%8D%A2%E8%84%9A%E6%9C%AC)

简单说一下：
Hexo 官方的数学公式渲染插件 [hexo-math](https://github.com/hexojs/hexo-math) 只支持行内公式，且使用如下包裹方式：
```markdown
{% mathjax '{options}' %}
content
{% endmathjax %}
```
使用此脚本可以实现将含有由 `$...$` 和 `$$...$$` 包裹的数学公式的 md 文件转换为支持 hexo-math 的文件