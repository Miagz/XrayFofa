# XrayFofa
🎉
一款将xray和fofa结合运行的脚本,配置方法参考了piaolin大佬写的<a href="https://github.com/piaolin/fofa2Xray">fofa2Xray</a>
增加了一些自己的想法(望指正)🌹🌹🌹
# scan_config.yaml
  ~~~yaml
#xray配置
  xray:
          #扫描结果存储路径
          file_path: 

          #xray文件位置,不填则为默认路径
          xray_file_path:

          #xray 结果输出方式默认是 html|xray输入出方式仅有html,json,text
          input_file_type: 

  #fofa配置
  fofa:
          #fofa登录邮箱
          Fofa_email: 

          #fofa key值
          Fofa_key:  

          #fofa搜索语法,可直接在后面添加
          fofaQuerysyntax:
                  - status_code=200
                  - country="CN"

  #全局配置
  global:

          #是否只扫描域名,如果需要请修改为yes
          scan_domain_name: no

          #多线程数量
          threads: 5
 ~~~
### xray配置 ✔
> input_file_type 
<p>xray输出方式 为空的话则默认为html格式输出</p>

> file_path 
<p>xray结果的输出位置,为空则默认在当前目录下生成一个以 input_file_type 中所填写的输出方式作为名称</p>

>xray_file_path
<p>xray所在的路径(包含xray文件名) 为空则默认xray在当前目录下</p>

### fofa配置 ✔
> Fofa_email
<p>fofa登录邮箱</p>

> Fofa_key
<p>fofa api key 可在fofa个人资料中查看</p>
 
> fofaQuerysyntax
<p>fofa查询语法 跟fofa使用差不多 更多搜索语法可在后面追加</p>

  ~~~
  fofaQuerysyntax:
          - status_code=200
          - country="CN"
          - title="后台管理系统"
  ~~~

### 全局配置 ✔
> scan_domain_name
<p>开启后xray只会扫描fofa扫描出的域名,ip直接过滤 默认为关闭状态</p>

> threads
<p>多线程大小</p>
### 环境
运行脚本前请安装pyfofa,pyyaml模块
~~~
  python3 -m pip install pyfofa,pyyaml
~~~
# demo
<img src="https://raw.githubusercontent.com/Miagz/image/master/na25n-7yu0i.gif">
