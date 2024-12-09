# 1、项目介绍
## 1.1、本次分享介绍                      
(1)MCP介绍                                                                             
(2)MCP功能测试,LLM(支持OpenAI接口风格的大模型)应用程序调用MCP                                                                      

## 1.2 MCP介绍                             
MCP(模型上下文协议)是Claude开源的一种开放协议，可实现LLM应用程序与外部数据源和工具之间的无缝集成                              
该架构非常简单:开发人员可以通过MCP服务器公开数据，也可以构建连接到这些服务器的AI应用程序(MCP客户端)                  
目前MCP还算是一个测试版，一个本地的服务，运行在你自己的电脑上的                        
MCP官方简介:https://www.anthropic.com/news/model-context-protocol                                                                                  
MCP文档手册:https://modelcontextprotocol.io/introduction                                              
MCP官方服务器列表:https://github.com/modelcontextprotocol/servers                      
PythonSDK的github地址:https://github.com/modelcontextprotocol/python-sdk                          
### (1)PythonSDK版本           
截止当前(12.9),当前的稳定版本为1.1.0                                          
### (2)MCP工作原理                  
MCP遵循客户端-服务器架构(client-server)，其中主机应用程序可以连接到多个服务器                             
<img src="./01.png" alt="" width="600" />                               
**MCP主机(MCP Host):** 是发起连接的LLM应用程序(Claude Desktop、IDE或AI应用等)                                             
**MCP客户端(MCP Client):** 在主机应用程序内部与服务器保持1:1连接                                    
**MCP服务器(MCP Servers):** 服务器向客户端提供上下文、工具和提示词(context, tools, and prompts)                                                           
### (3)核心组件
**Protocol layer 协议层**                           
协议层处理消息帧、请求/响应链接和高级通信模式。关键类:Protocol、Client、Server                                   
**Transport layer 传输层**                         
传输层处理客户端和服务器之间的实际通信                              
Stdio(standard input/output):使用标准输入/输出进行通信                        
SSE(Server-Sent Events):使用服务器发送的事件来发送服务器到客户端的消息                         
所有传输都使用JSON-RPC2.0 来交换消息                         
**Message types 消息类型**            
Requests:请求期望来自另一方的响应                       
Notifications:通知是一种不期望响应的单向消息                    
Results:结果是对请求的成功响应                          
Errors:错误表明请求失败                         
### (4)连接生命周期
**Initialization 初始化**                
<img src="./02.png" alt="" width="600" />                
客户端发送带有协议版本和功能的initialize请求                                         
服务器响应其协议版本和功能                     
客户端发送initialized通知作为确认                                   
正常消息交换开始                        
**Message exchange 消息交换**                  
初始化后，支持以下模式:                        
请求-响应(Request-Response)：客户端或服务器发送请求，对方响应                       
通知(Notifications)：任何一方发送单向消息                      
**Termination 终止**                 
定义了这些标准错误代码:                
ParseError = -32700                     
InvalidRequest = -32600                         
MethodNotFound = -32601                        
InvalidParams = -32602                           
InternalError = -32603                        
### (5)核心功能
**Resources 资源**             
资源是模型上下文协议 (MCP) 中的核心功能，允许服务器公开可供客户端读取并用作LLM交互上下文的数据和内容                 
File contents 文件内容             
Database records 数据库记录            
API responses API 响应               
Live system data 实时系统数据               
Screenshots and images 屏幕截图和图像             
Log files 日志文件                  
And more 还有更多                  
每个资源都由唯一的 URI 标识，并且可以包含文本或二进制数据                  
**Prompts 提示**             
服务器能够定义可重用的提示模板和工作流程，客户端可以轻松地向用户和LLMs展示这些模板和工作流程。它们提供了一种强大的方法来标准化和共享常见的LLM交互                     
接受动态参数                    
包括资源中的上下文              
指导具体工作流程            
**Tools 工具**           
工具是MCP中的强大功能，工具被设计为LLMs控制的，这意味着工具从服务器公开给客户端，目的是让LLMs能够自动调用它们（有人在循环中授予批准）                                   
工具的关键方面包括:                                    
发现(Discovery):客户端可以通过tools/list端点列出可用的工具                             
调用(Invocation):使用tools/call端点调用工具，服务器在其中执行请求的操作并返回结果                                   
灵活性(Flexibility):工具范围从简单的计算到复杂的API交互               
**Sampling 采样**               
采样是一项强大的MCP功能，允许服务器通过客户端请求LLM完成，从而在保持安全和隐私的同时实现复杂的代理行为                      
服务器向客户端发送sampling/createMessage请求                       
客户端审查请求并可以修改它             
LLM采样的客户端样本           
客户端审核完成情况              
客户端将结果返回给服务器                      
这种人机交互设计可确保用户保持对LLM所看到和生成的内容的控制                        
**Transports 传输**                     
MCP的传输为客户端和服务器之间的通信提供了基础。传输处理消息发送和接收的底层机制               
MCP使用JSON-RPC 2.0作为其格式。传输层负责将MCP协议消息转换为JSON-RPC格式进行传输，并将接收到的JSON-RPC消息转换回MCP协议消息           


# 2、前期准备工作
## 2.1 开发环境搭建:anaconda、pycharm
anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可                                      
pycharm:提供集成开发环境，官网下载社区版本安装包安装即可                                               
可参考如下视频进行安装，【大模型应用开发基础】集成开发环境搭建Anaconda+PyCharm                                                          
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                             
https://youtu.be/myVgyitFzrA          

## 2.2 大模型相关配置
(1)GPT大模型使用方案              
(2)非GPT大模型(国产大模型)使用方案(OneAPI安装、部署、创建渠道和令牌)                 
(3)本地开源大模型使用方案(Ollama安装、启动、下载大模型)                         
可参考如下视频:                         
提供一种LLM集成解决方案，一份代码支持快速同时支持gpt大模型、国产大模型(通义千问、文心一言、百度千帆、讯飞星火等)、本地开源大模型(Ollama)                       
https://www.bilibili.com/video/BV12PCmYZEDt/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                 
https://youtu.be/CgZsdK43tcY           


# 3、项目初始化
## 3.1 下载源码
GitHub或Gitee中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/MCPTest                                                               
https://gitee.com/NanGePlus/MCPTest                                     

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境               
项目名称：MCPTest                                                     

## 3.3 将相关代码拷贝到项目工程中           
直接将下载的文件夹中的文件拷贝到新建的项目目录中               

## 3.4 安装项目依赖                        
命令行终端中执行如下命令安装依赖包                               
pip install -r requirements.txt                      
     

# 4、测试
**核心演示示例介绍:Filesystem**                                       
**描述:** 提供文件系统操作功能，包括读写文件、目录管理和文件搜索                 
**工具:** read_file, write_file, create_directory, list_directory, move_file, search_files, get_file_info             
**工具描述:**                  
read_file: 读取文件内容，参数:path (文件路径)                 
read_multiple_files 读取多个文件内容，参数:paths (文件路径数组)              
write_file: 创建或覆写文件，参数: path (文件路径), content (文件内容)                           
create_directory: 创建目录，参数: path (目录路径)                              
list_directory: 列出目录内容，参数: path (目录路径)                          
move_file: 移动/重命名文件，参数: source (源路径), destination (目标路径)                                
search_files: 递归搜索文件，参数: path (起始路径), pattern (搜索模式)                               
get_file_info: 获取文件元数据，参数: path (文件路径)                          
对应的链接:https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem                

**代码目录**                  
脚本均放置在nangeAGICode目录内,运行对应脚本进行测试              
   



















