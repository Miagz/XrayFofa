# XrayFofa
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
>>> input_file_type - xray输出方式 为空的话则默认为html格式输出
 <br>
 
>>> file_path - xray结果的输出位置,为空则默认在当前目录下生成一个以 input_file_type 中所填写的输出方式作为名称的目录名称
 <br>
 
