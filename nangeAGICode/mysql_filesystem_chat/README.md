# 1、项目介绍
本期系列相关视频如下，按照发布的先后顺序:                      
**(第一期)[2024.10.10]Claude重大突破！发布MCP(模型上下文协议)，带你在LLM应用程序脚本中感受它，无需使用Claude Desktop桌面软件，支持类OpenAI风格大模型**               
主要内容:MCP介绍、MCP功能测试,LLM(支持OpenAI接口风格的大模型)应用程序调用MCP               
https://www.bilibili.com/video/BV1HBquYbE7t/                          
https://youtu.be/Jmo7rgb_OXQ               
**(第二期)[2024.10.12]Claude MCP应用Text2SQL用例，带你在LLM应用程序中感受它的丝滑，无需使用Claude Desktop桌面软件，支持类OpenAI风格大模型**               
主要内容:使用MCP实现LLM应用程序Text2SQL功能操纵MySQL数据库                   
https://www.bilibili.com/video/BV1ELq4YME8T/                     
https://youtu.be/yaLAqEMz45A                   

**本次分享介绍**                                
使用MCP客户端实现访问多服务器，操纵文件系统和MySQL数据库                   
相关视频:              
https://youtu.be/tG-ZjOgrcSA                 


# 2、项目初始化
## 2.1 下载源码
GitHub或Gitee中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/MCPTest                                                               
https://gitee.com/NanGePlus/MCPTest                             
将文件夹nangeAGICode下的mysql_filesystem_chat文件夹下载到本地                            

## 2.2 将相关代码拷贝到项目工程中           
直接将下载的文件夹中的文件拷贝到MCPTest项目目录中               

## 2.3 安装依赖                        
命令行终端中执行如下命令安装依赖包                    
pip install mysql-connector-python==9.1.0 python-dotenv==1.0.1 requests==2.32.3 mcp==1.1.1 uvicorn==0.32.1 asyncio==3.4.3                              
pip install --upgrade mcp==1.1.1                                      


# 3、功能测试
提供LLM对文件系统和MySQL数据库进行操作                                                                             
**测试内容:**                             
当前可以访问哪些资源                    
当前可以访问哪些表                   
当前可以使用哪些工具                         
创建一个test文件夹                      
在test文件夹下创建一个文件test1.txt，内容为：用户名:NanGe003，密码：6543217890，内容：南哥AGI研习社++。                    
获取nange_agi这个表的内容                    
增加一条数据，数据内容为刚刚创建的test1.txt中的内容                       
获取nange_agi这个表的内容                      
这张表中一共几条数据                                         
新增的那条数据把名称改为test                                    
获取nange_agi这个表的内容                     
把刚新建的那条数据删除                          
获取nange_agi这个表的内容                              




   



















