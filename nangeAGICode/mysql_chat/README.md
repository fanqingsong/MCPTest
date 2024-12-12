# 1、项目介绍
本期系列相关视频如下，按照发布的先后顺序:                      
**(第一期)[2024.10.10]Claude重大突破！发布MCP(模型上下文协议)，带你在LLM应用程序脚本中感受它，无需使用Claude Desktop桌面软件，支持类OpenAI风格大模型**               
主要内容:MCP介绍、MCP功能测试,LLM(支持OpenAI接口风格的大模型)应用程序调用MCP               
https://www.bilibili.com/video/BV1HBquYbE7t/                          
https://youtu.be/Jmo7rgb_OXQ                                       
B站、YouTube搜索“**南哥AGI研习社**”关注我                   
<img src="../../logo.png" alt="" width="1400" />            

**本次分享介绍**          
本期视频:                    
https://www.bilibili.com/video/BV1ELq4YME8T/                          
https://youtu.be/yaLAqEMz45A                      
使用MCP实现LLM应用程序Text2SQL功能操纵MySQL数据库                      
**(1)列举可用资源**               
**(2)获取某资源内容**                  
**(3)列举可用工具**                       
**(4)查询数据**                                           
**(5)增加数据**                    
**(6)修改数据**         
**(7)删除数据**                              
**(8)统计数据量**                                              


# 2、项目初始化
## 2.1 下载源码
GitHub或Gitee中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/MCPTest                                                               
https://gitee.com/NanGePlus/MCPTest                             
将文件夹nangeAGICode下的mysql_chat文件夹下载到本地                            

## 2.2 将相关代码拷贝到项目工程中           
直接将下载的文件夹中的文件拷贝到MCPTest项目目录中               

## 2.3 安装依赖                        
命令行终端中执行如下命令安装依赖包                               
pip install mysql-connector-python==9.1.0                                         
     

# 3、功能测试
提供LLM对MySQL数据库操作功能，增、删、改、查                                                        
**测试内容:**         
**(1)列举可用资源**                    
当前可以访问哪些数据表            
**(2)获取某资源内容**            
获取nange_agi这个表的内容            
**(3)列举可用的工具**                               
当前可以使用哪些工具                        
**(4)查询**                   
调用工具获取nange_agi这个表的内容                            
**(5)增加**                  
随机帮我增加一条数据           
调用工具获取nange_agi这个表的内容      
**(6)修改**         
新增的那条数据把名称改为test             
调用工具获取nange_agi这个表的内容      
**(7)删除**                 
把刚新建的那条数据删除                                 
调用工具获取nange_agi这个表的内容                     
**(8)统计数据量**               
这张表中一共几条数据                                       
          
   



















