<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19  如何使用 Docker Compose 解决开发环境的依赖？.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="00&#32;溯本求源，吃透&#32;Docker！.md">00 溯本求源，吃透 Docker！.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;Docker&#32;安装：入门案例带你了解容器技术原理.md">01  Docker 安装：入门案例带你了解容器技术原理.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;核心概念：镜像、容器、仓库，彻底掌握&#32;Docker&#32;架构核心设计理念.md">02  核心概念：镜像、容器、仓库，彻底掌握 Docker 架构核心设计理念.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;镜像使用：Docker&#32;环境下如何配置你的镜像？.md">03  镜像使用：Docker 环境下如何配置你的镜像？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;容器操作：得心应手掌握&#32;Docker&#32;容器基本操作.md">04  容器操作：得心应手掌握 Docker 容器基本操作.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;仓库访问：怎样搭建属于你的私有仓库？.md">05  仓库访问：怎样搭建属于你的私有仓库？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;最佳实践：如何在生产中编写最优&#32;Dockerfile？.md">06  最佳实践：如何在生产中编写最优 Dockerfile？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;Docker&#32;安全：基于内核的弱隔离系统如何保障安全性？.md">07  Docker 安全：基于内核的弱隔离系统如何保障安全性？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;容器监控：容器监控原理及&#32;cAdvisor&#32;的安装与使用.md">08  容器监控：容器监控原理及 cAdvisor 的安装与使用.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;资源隔离：为什么构建容器需要&#32;Namespace&#32;？.md">09  资源隔离：为什么构建容器需要 Namespace ？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;资源限制：如何通过&#32;Cgroups&#32;机制实现资源限制？.md">10  资源限制：如何通过 Cgroups 机制实现资源限制？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;组件组成：剖析&#32;Docker&#32;组件作用及其底层工作原理.md">11  组件组成：剖析 Docker 组件作用及其底层工作原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;网络模型：剖析&#32;Docker&#32;网络实现及&#32;Libnetwork&#32;底层原理.md">12  网络模型：剖析 Docker 网络实现及 Libnetwork 底层原理.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;数据存储：剖析&#32;Docker&#32;卷与持久化数据存储的底层原理.md">13  数据存储：剖析 Docker 卷与持久化数据存储的底层原理.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;文件存储驱动：AUFS&#32;文件系统原理及生产环境的最佳配置.md">14  文件存储驱动：AUFS 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;文件存储驱动：Devicemapper&#32;文件系统原理及生产环境的最佳配置.md">15  文件存储驱动：Devicemapper 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;文件存储驱动：OverlayFS&#32;文件系统原理及生产环境的最佳配置.md">16  文件存储驱动：OverlayFS 文件系统原理及生产环境的最佳配置.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（上）.md">17  原理实践：自己动手使用 Golang 开发 Docker（上）.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（下）.md">18  原理实践：自己动手使用 Golang 开发 Docker（下）.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;&#32;如何使用&#32;Docker&#32;Compose&#32;解决开发环境的依赖？.md">19  如何使用 Docker Compose 解决开发环境的依赖？.md</a>
                    

                </li>
                <li>

                    
                    <a href="20&#32;&#32;如何在生产环境中使用&#32;Docker&#32;Swarm&#32;调度容器？.md">20  如何在生产环境中使用 Docker Swarm 调度容器？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;如何使&#32;Docker&#32;和&#32;Kubernetes&#32;结合发挥容器的最大价值？.md">21  如何使 Docker 和 Kubernetes 结合发挥容器的最大价值？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;多阶级构建：Docker&#32;下如何实现镜像多阶级构建？.md">22  多阶级构建：Docker 下如何实现镜像多阶级构建？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;DevOps：容器化后如何通过&#32;DevOps&#32;提高协作效能？.md">23  DevOps：容器化后如何通过 DevOps 提高协作效能？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;CICD：容器化后如何实现持续集成与交付？（上）.md">24  CICD：容器化后如何实现持续集成与交付？（上）.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;CICD：容器化后如何实现持续集成与交付？（下）.md">25  CICD：容器化后如何实现持续集成与交付？（下）.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;结束语&#32;&#32;展望未来：Docker&#32;的称霸之路.md">26 结束语  展望未来：Docker 的称霸之路.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>19  如何使用 Docker Compose 解决开发环境的依赖？</h1>
<p>前两个模块，我们从 Docker 的基本操作到 Docker 的实现原理，为你一步一步揭开了 Docker 神秘的面纱。然而目前为止，我们所有的操作都是围绕单个容器进行的，但当我们的业务越来越复杂时，需要多个容器相互配合，甚至需要多个主机组成容器集群才能满足我们的业务需求，这个时候就需要用到容器的编排工具了。因为容器编排工具可以帮助我们批量地创建、调度和管理容器，帮助我们解决规模化容器的部署问题。</p>
<p>从这一课时开始，我将向你介绍 Docker 三种常用的编排工具：Docker Compose、Docker Swarm 和 Kubernetes。了解这些编排工具，可以让你在不同的环境中选择最优的编排框架。</p>
<p>本课时我们先来学习一个在开发时经常用到的编排工具——Docker Compose。合理地使用 Docker Compose 可以极大地帮助我们提升开发效率。那么 Docker Compose 究竟是什么呢？</p>
<h3>Docker Compose 的前世今生</h3>
<p>Docker Compose 的前身是 Orchard 公司开发的 Fig，2014 年 Docker 收购了 Orchard 公司，然后将 Fig 重命名为 Docker Compose。现阶段 Docker Compose 是 Docker 官方的单机多容器管理系统，它本质是一个 Python 脚本，它通过解析用户编写的 yaml 文件，调用 Docker API 实现动态的创建和管理多个容器。</p>
<p>要想使用 Docker Compose，需要我们先安装一个 Docker Compose。</p>
<h3>安装 Docker Compose</h3>
<p>Docker Compose 可以安装在 macOS、 Windows 和 Linux 系统中，其中在 macOS 和 Windows 系统下 ，Docker Compose 都是随着 Docker 的安装一起安装好的，这里就不再详细介绍。 下面我重点介绍下如何在 Linux 系统下安装 Docker Compose。</p>
<h4>Linux 系统下安装 Docker Compose</h4>
<p>在安装 Docker Compose 之前，请确保你的机器已经正确运行了 Docker，如果你的机器还没有安装 Docker，请参考<a href="https://docs.docker.com/engine/install/">官方网站</a>安装 Docker。</p>
<p>要在 Linux 平台上安装 Docker Compose，我们需要到 Compose 的 Github 页面下载对应版本的安装包。这里我以 1.27.3 版本为例，带你安装一个 Docker Compose。</p>
<p>（1）使用 curl 命令（一种发送 http 请求的命令行工具）下载 Docker Compose 的安装包：</p>
<pre><code>$ sudo curl -L &quot;https://github.com/docker/compose/releases/download/1.27.3/docker-compose-$(uname -s)-$(uname -m)&quot; -o /usr/local/bin/docker-compose
</code></pre>
<blockquote>
<p>如果你想要安装其他版本的 Docker Compose，将 1.27.3 替换为你想要安装的版本即可。</p>
</blockquote>
<p>（2）修改 Docker Compose 执行权限：</p>
<pre><code>$ sudo chmod +x /usr/local/bin/docker-compose
</code></pre>
<p>（3）检查 Docker Compose 是否安装成功：</p>
<pre><code>$ docker-compose --version

docker-compose version 1.27.3, build 1110ad01
</code></pre>
<p>当我们执行完上述命令后，如果 Docker Compose 输出了当前版本号，就表示我们的 Docker Compose 已经安装成功。 Docker Compose 安装成功后，我们就可以很方便地使用它了。</p>
<p>在使用 Docker Compose 之前，我们首先需要先编写 Docker Compose 模板文件，因为 Docker Compose 运行的时候是根据 Docker Compose 模板文件中的定义来运行的。</p>
<p>下面我们首先来学习一下如何编写一个 Docker Compose 模板文件。</p>
<h3>编写 Docker Compose 模板文件</h3>
<p>在使用 Docker Compose 启动容器时， Docker Compose 会默认使用 docker-compose.yml 文件， docker-compose.yml 文件的格式为 yaml（类似于 json，一种标记语言）。</p>
<p>Docker Compose 模板文件一共有三个版本： v1、v2 和 v3。目前最新的版本为 v3，也是功能最全面的一个版本，下面我主要围绕 v3 版本介绍一下如何编写 Docker Compose 文件。</p>
<p>Docker Compose 文件主要分为三部分： services（服务）、networks（网络） 和 volumes（数据卷）。</p>
<ul>
<li>services（服务）：服务定义了容器启动的各项配置，就像我们执行<code>docker run</code>命令时传递的容器启动的参数一样，指定了容器应该如何启动，例如容器的启动参数，容器的镜像和环境变量等。</li>
<li>networks（网络）：网络定义了容器的网络配置，就像我们执行<code>docker network create</code>命令创建网络配置一样。</li>
<li>volumes（数据卷）：数据卷定义了容器的卷配置，就像我们执行<code>docker volume create</code>命令创建数据卷一样。</li>
</ul>
<p>一个典型的 Docker Compose 文件结构如下：</p>
<pre><code>version: &quot;3&quot;

services:

  nginx:

    ## ... 省略部分配置

networks:

  frontend:

  backend:

volumes:

  db-data:
</code></pre>
<p>下面我们首先来学习一下如何编写 services 部分的配置。</p>
<h4>编写 Service 配置</h4>
<p>services 下，首先需要定义服务名称，例如你这个服务是 nginx 服务，你可以定义 service 名称为 nginx，格式如下：</p>
<pre><code>version: &quot;3.8&quot;

services:

  nginx: 
</code></pre>
<p>服务名称定义完毕后，我们需要在服务名称的下一级定义当前服务的各项配置，使得我们的服务可以按照配置正常启动。常用的 16 种 service 配置如下。如果你比较了解，可以直接跳过看 Volume 配置和后续实操即可。</p>
<p><strong>build：</strong> 用于构建 Docker 镜像，类似于<code>docker build</code>命令，build 可以指定 Dockerfile 文件路径，然后根据 Dockerfile 命令来构建文件。使用方法如下：</p>
<pre><code>build:

  ## 构建执行的上下文目录

  context: .

  ## Dockerfile 名称

  dockerfile: Dockerfile-name
</code></pre>
<p><strong>cap_add、cap_drop：</strong> 指定容器可以使用到哪些内核能力（capabilities）。使用格式如下：</p>
<pre><code>cap_add:

  - NET_ADMIN

cap_drop:

  - SYS_ADMIN
</code></pre>
<p><strong>command：</strong> 用于覆盖容器默认的启动命令，它和 Dockerfile 中的 CMD 用法类似，也有两种使用方式：</p>
<pre><code>command: sleep 3000
</code></pre>
<pre><code>command: [&quot;sleep&quot;, &quot;3000&quot;]
</code></pre>
<p><strong>container_name：</strong> 用于指定容器启动时容器的名称。使用格式如下：</p>
<pre><code>container_name: nginx
</code></pre>
<p><strong>depends_on：</strong> 用于指定服务间的依赖关系，这样可以先启动被依赖的服务。例如，我们的服务依赖数据库服务 db，可以指定 depends_on 为 db。使用格式如下：</p>
<pre><code>version: &quot;3.8&quot;

services:

  my-web:

    build: .

    depends_on:

      - db

  db:

    image: mysql
</code></pre>
<p><strong>devices：</strong> 挂载主机的设备到容器中。使用格式如下：</p>
<pre><code>devices:

  - &quot;/dev/sba:/dev/sda&quot;
</code></pre>
<p><strong>dns：</strong> 自定义容器中的 dns 配置。</p>
<pre><code>dns:

  - 8.8.8.8

  - 114.114.114.114
</code></pre>
<p><strong>dns_search：</strong> 配置 dns 的搜索域。</p>
<pre><code>dns_search:

  - svc.cluster.com

  - svc1.cluster.com
</code></pre>
<p><strong>entrypoint：</strong> 覆盖容器的 entrypoint 命令。</p>
<pre><code>entrypoint: sleep 3000
</code></pre>
<p>或</p>
<pre><code>entrypoint: [&quot;sleep&quot;, &quot;3000&quot;]
</code></pre>
<p><strong>env_file：</strong> 指定容器的环境变量文件，启动时会把该文件中的环境变量值注入容器中。</p>
<pre><code>env_file:

  - ./dbs.env
</code></pre>
<p>env 文件的内容格式如下：</p>
<pre><code>KEY_ENV=values
</code></pre>
<p><strong>environment：</strong> 指定容器启动时的环境变量。</p>
<pre><code>environment:

  - KEY_ENV=values
</code></pre>
<p><strong>image：</strong> 指定容器镜像的地址。</p>
<pre><code>image: busybox:latest
</code></pre>
<p><strong>pid：</strong> 共享主机的进程命名空间，像在主机上直接启动进程一样，可以看到主机的进程信息。</p>
<pre><code>pid: &quot;host&quot;
</code></pre>
<p><strong>ports：</strong> 暴露端口信息，使用格式为 HOST:CONTAINER，前面填写要映射到主机上的端口，后面填写对应的容器内的端口。</p>
<pre><code>ports:

  - &quot;1000&quot;

  - &quot;1000-1005&quot;

  - &quot;8080:8080&quot;

  - &quot;8888-8890:8888-8890&quot;

  - &quot;2222:22&quot;

  - &quot;127.0.0.1:9999:9999&quot;

  - &quot;127.0.0.1:3000-3005:3000-3005&quot;

  - &quot;6789:6789/udp&quot;
</code></pre>
<p><strong>networks：</strong> 这是服务要使用的网络名称，对应顶级的 networks 中的配置。</p>
<pre><code>services:

  my-service:

    networks:

     - hello-network

     - hello1-network
</code></pre>
<p><strong>volumes：</strong> 不仅可以挂载主机数据卷到容器中，也可以直接挂载主机的目录到容器中，使用方式类似于使用<code>docker run</code>启动容器时添加 -v 参数。</p>
<pre><code>version: &quot;3&quot;

services:

  db:

    image: mysql:5.6

    volumes:

      - type: volume

        source: /var/lib/mysql

        target: /var/lib/mysql
</code></pre>
<p>volumes 除了上面介绍的长语法外，还支持短语法的书写方式，例如上面的写法可以精简为：</p>
<pre><code>version: &quot;3&quot;

services:

  db:

    image: mysql:5.6

    volumes:

      - /var/lib/mysql:/var/lib/mysql
</code></pre>
<h4>编写 Volume 配置</h4>
<p>如果你想在多个容器间共享数据卷，则需要在外部声明数据卷，然后在容器里声明使用数据卷。例如我想在两个服务间共享日志目录，则使用以下配置：</p>
<pre><code>version: &quot;3&quot;

services:

  my-service1:

    image: service:v1

    volumes:

      - type: volume

        source: logdata

        target: /var/log/mylog

  my-service2:

    image: service:v2

    volumes:

      - type: volume

        source: logdata

        target: /var/log/mylog

volumes:

  logdata:
</code></pre>
<h4>编写 Network 配置</h4>
<p>Docker Compose 文件顶级声明的 networks 允许你创建自定义的网络，类似于<code>docker network create</code>命令。</p>
<p>例如你想声明一个自定义 bridge 网络配置，并且在服务中使用它，使用格式如下：</p>
<pre><code>version: &quot;3&quot;

services:

  web:

    networks:

      mybridge: 

        ipv4_address: 172.16.1.11

networks:

  mybridge:

    driver: bridge

    ipam: 

      driver: default

      config:

        subnet: 172.16.1.0/24
</code></pre>
<p>编写完 Docker Compose 模板文件后，需要使用 docker-compose 命令来运行这些文件。下面我们来学习下 docker-compose 都有哪些操作命令。</p>
<h3>Docker Compose 操作命令</h3>
<p>我们可以使用<code>docker-compose -h</code>命令来查看 docker-compose 的用法，docker-compose 的基本使用格式如下：</p>
<pre><code>docker-compose [-f &lt;arg&gt;...] [options] [--] [COMMAND] [ARGS...]
</code></pre>
<p>其中 options 是 docker-compose 的参数，支持的参数和功能说明如下：</p>
<pre><code>  -f, --file FILE             指定 docker-compose 文件，默认为 docker-compose.yml

  -p, --project-name NAME     指定项目名称，默认使用当前目录名称作为项目名称

  --verbose                   输出调试信息

  --log-level LEVEL           日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)

  -v, --version               输出当前版本并退出

  -H, --host HOST             指定要连接的 Docker 地址

  --tls                       启用 TLS 认证

  --tlscacert CA_PATH         TLS CA 证书路径

  --tlscert CLIENT_CERT_PATH  TLS 公钥证书问价

  --tlskey TLS_KEY_PATH       TLS 私钥证书文件

  --tlsverify                 使用 TLS 校验对端

  --skip-hostname-check       不校验主机名

  --project-directory PATH    指定工作目录，默认是 Compose 文件所在路径。
</code></pre>
<p>COMMAND 为 docker-compose 支持的命令。支持的命令如下：</p>
<pre><code>  build              构建服务

  config             校验和查看 Compose 文件

  create             创建服务

  down               停止服务，并且删除相关资源

  events             实时监控容器的时间信息

  exec               在一个运行的容器中运行指定命令

  help               获取帮助

  images             列出镜像

  kill               杀死容器

  logs               查看容器输出

  pause              暂停容器

  port               打印容器端口所映射出的公共端口

  ps                 列出项目中的容器列表

  pull               拉取服务中的所有镜像

  push               推送服务中的所有镜像

  restart            重启服务

  rm                 删除项目中已经停止的容器

  run                在指定服务上运行一个命令

  scale              设置服务运行的容器个数

  start              启动服务

  stop               停止服务

  top                限制服务中正在运行中的进程信息

  unpause            恢复暂停的容器

  up                 创建并且启动服务

  version            打印版本信息并退出
</code></pre>
<p>好了，学习完 Docker Compose 模板的编写和 docker-compose 命令的使用方法，下面我们编写一个 Docker Compose 模板文件，实现一键启动 WordPress 服务（一种博客系统），来搭建一个属于我们自己的博客系统。</p>
<h3>使用 Docker Compose 管理 WordPress</h3>
<h4>启动 WordPress</h4>
<p>第一步，创建项目目录。首先我们在 /tmp 目录下创建一个 WordPress 的目录，这个目录将作为我们的工作目录。</p>
<pre><code>$ mkdir /tmp/wordpress
</code></pre>
<p>第二步，进入工作目录。</p>
<pre><code>$ cd /tmp/wordpress
</code></pre>
<p>第三步，创建 docker-compose.yml 文件。</p>
<pre><code>$ touch docker-compose.yml
</code></pre>
<p>然后写入以下内容：</p>
<pre><code>version: '3'

services:

   mysql:

     image: mysql:5.7

     volumes:

       - mysql_data:/var/lib/mysql

     restart: always

     environment:

       MYSQL_ROOT_PASSWORD: root

       MYSQL_DATABASE: mywordpress

       MYSQL_USER: mywordpress

       MYSQL_PASSWORD: mywordpress

   wordpress:

     depends_on:

       - mysql

     image: wordpress:php7.4

     ports:

       - &quot;8080:80&quot;

     restart: always

     environment:

       WORDPRESS_DB_HOST: mysql:3306

       WORDPRESS_DB_USER: mywordpress

       WORDPRESS_DB_PASSWORD: mywordpress

       WORDPRESS_DB_NAME: mywordpress

volumes:

    mysql_data: {}
</code></pre>
<p>第四步，启动 MySQL 数据库和 WordPress 服务。</p>
<pre><code>$ docker-compose up -d

Starting wordpress_mysql_1 ... done

Starting wordpress_wordpress_1 ... done
</code></pre>
<p>执行完以上命令后，Docker Compose 首先会为我们启动一个 MySQL 数据库，按照 MySQL 服务中声明的环境变量来设置 MySQL 数据库的用户名和密码。然后等待 MySQL 数据库启动后，再启动 WordPress 服务。WordPress 服务启动后，我们就可以通过 <a href="http://localhost:8080/">http://localhost:8080</a> 访问它了，访问成功后，我们就可以看到以下界面，然后按照提示一步一步设置就可以拥有属于自己的专属博客系统了。</p>
<p><img src="assets/Ciqc1F-WuHqAMc6gAAGSco9Zyvc339.png" alt="image.png" /></p>
<p>图 1 WordPress 启动界面</p>
<h4>停止 WordPress</h4>
<p>如果你不再需要 WordPress 服务了，可以使用<code>docker-compose stop</code>命令来停止已启动的服务。</p>
<pre><code>$ docker-compose stop

Stopping wordpress_wordpress_1 ... done

Stopping wordpress_mysql_1     ... done
</code></pre>
<h3>结语</h3>
<p>Docker Compose 是一个用来定义复杂应用的单机编排工具，通常用于服务依赖关系复杂的开发和测试环境，如果你还在为配置复杂的开发环境而烦恼，Docker Compose 可以轻松帮你搞定复杂的开发环境。你只需要把复杂的开发环境使用 Docker Compose 模板文件描述出来，之后无论你在哪里可以轻松的一键启动开发和测试环境，极大地提高了我们的开发效率，同时也避免了污染我们开发机器的配置。</p>
<p>那么，学完本课时的课程，你可以试着使用 Docker Compose 一键启动一个 <a href="https://baike.baidu.com/item/LNMP">LNMP</a> 开发环境吗？</p>
<p>下一课时，我将为你讲解容器的另一个编排系统 Docker Swarm。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;&#32;如何在生产环境中使用&#32;Docker&#32;Swarm&#32;调度容器？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a285a8d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E7%94%B1%E6%B5%85%E5%85%A5%E6%B7%B1%E5%90%83%E9%80%8F%20Docker-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
