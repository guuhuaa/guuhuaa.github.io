<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>03  镜像使用：Docker 环境下如何配置你的镜像？.md</title>
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

                    <a class="current-tab" href="03&#32;&#32;镜像使用：Docker&#32;环境下如何配置你的镜像？.md">03  镜像使用：Docker 环境下如何配置你的镜像？.md</a>
                    

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

                    
                    <a href="19&#32;&#32;如何使用&#32;Docker&#32;Compose&#32;解决开发环境的依赖？.md">19  如何使用 Docker Compose 解决开发环境的依赖？.md</a>

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
                        <div><h1>03  镜像使用：Docker 环境下如何配置你的镜像？</h1>
<p>今天我将围绕 Docker 核心概念镜像展开，首先重点讲解一下镜像的基本操作，然后介绍一下镜像的实现原理。首先说明，咱们本课时的镜像均指 Docker 镜像。</p>
<p>你是否还记得镜像是什么？我们先回顾一下。</p>
<p>镜像是一个只读的 Docker 容器模板，包含启动容器所需要的所有文件系统结构和内容。简单来讲，镜像是一个特殊的文件系统，它提供了容器运行时所需的程序、软件库、资源、配置等静态数据。即<strong>镜像不包含任何动态数据，镜像内容在构建后不会被改变</strong>。</p>
<p>然后我们来看下如何操作镜像。</p>
<h3>镜像操作</h3>
<p><img src="assets/CgqCHl9SDkWAaxh7AAFaMgWI7cI029.png" alt="Lark20200904-175130.png" /></p>
<p>图 1 镜像操作</p>
<p>从图中可知，镜像的操作可分为：</p>
<ul>
<li>拉取镜像，使用<code>docker pull</code>命令拉取远程仓库的镜像到本地 ；</li>
<li>重命名镜像，使用<code>docker tag</code>命令“重命名”镜像 ；</li>
<li>查看镜像，使用<code>docker image ls</code>或<code>docker images</code>命令查看本地已经存在的镜像 ；</li>
<li>删除镜像，使用<code>docker rmi</code>命令删除无用镜像 ；</li>
<li>构建镜像，构建镜像有两种方式。第一种方式是使用<code>docker build</code>命令基于 Dockerfile 构建镜像，也是我比较推荐的镜像构建方式；第二种方式是使用<code>docker commit</code>命令基于已经运行的容器提交为镜像。</li>
</ul>
<p>下面，我们逐一详细介绍。</p>
<h4>拉取镜像</h4>
<p>Docker 镜像的拉取使用<code>docker pull</code>命令， 命令格式一般为 docker pull [Registry]/[Repository]/[Image]:[Tag]。</p>
<ul>
<li>Registry 为注册服务器，Docker 默认会从 docker.io 拉取镜像，如果你有自己的镜像仓库，可以把 Registry 替换为自己的注册服务器。</li>
<li>Repository 为镜像仓库，通常把一组相关联的镜像归为一个镜像仓库，<code>library</code>为 Docker 默认的镜像仓库。</li>
<li>Image 为镜像名称。</li>
<li>Tag 为镜像的标签，如果你不指定拉取镜像的标签，默认为<code>latest</code>。</li>
</ul>
<p>例如，我们需要获取一个 busybox 镜像，可以执行以下命令：</p>
<blockquote>
<p>busybox 是一个集成了数百个 Linux 命令（例如 curl、grep、mount、telnet 等）的精简工具箱，只有几兆大小，被誉为 Linux 系统的瑞士军刀。我经常会使用 busybox 做调试来查找生产环境中遇到的问题。</p>
</blockquote>
<pre><code>$ docker pull busybox
Using default tag: latest
latest: Pulling from library/busybox
61c5ed1cbdf8: Pull complete
Digest: sha256:4f47c01fa91355af2865ac10fef5bf6ec9c7f42ad2321377c21e844427972977
Status: Downloaded newer image for busybox:latest
docker.io/library/busybox:latest
</code></pre>
<p>实际上执行<code>docker pull busybox</code>命令，都是先从本地搜索，如果本地搜索不到<code>busybox</code>镜像则从 Docker Hub 下载镜像。</p>
<p>拉取完镜像，如果你想查看镜像，应该怎么操作呢？</p>
<h4>查看镜像</h4>
<p>Docker 镜像查看使用<code>docker images</code>或者<code>docker image ls</code>命令。</p>
<p>下面我们使用<code>docker images</code>命令列出本地所有的镜像。</p>
<pre><code>$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
nginx               latest              4bb46517cac3        9 days ago          133MB
nginx               1.15                53f3fd8007f7        15 months ago       109MB
busybox             latest              018c9d7b792b        3 weeks ago         1.22MB
</code></pre>
<p>如果我们想要查询指定的镜像，可以使用<code>docker image ls</code>命令来查询。</p>
<pre><code>$ docker image ls busybox
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             latest              018c9d7b792b        3 weeks ago         1.22MB
</code></pre>
<p>当然你也可以使用<code>docker images</code>命令列出所有镜像，然后使用<code>grep</code>命令进行过滤。使用方法如下：</p>
<pre><code>$ docker images |grep busybox
busybox             latest              018c9d7b792b        3 weeks ago         1.22MB
</code></pre>
<h4>“重命名”镜像</h4>
<p>如果你想要自定义镜像名称或者推送镜像到其他镜像仓库，你可以使用<code>docker tag</code>命令将镜像重命名。<code>docker tag</code>的命令格式为 docker tag [SOURCE_IMAGE][:TAG] [TARGET_IMAGE][:TAG]。</p>
<p>下面我们通过实例演示一下：</p>
<pre><code>$ docker tag busybox:latest mybusybox:latest
</code></pre>
<p>执行完<code>docker tag</code>命令后，可以使用查询镜像命令查看一下镜像列表：</p>
<pre><code>docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             latest              018c9d7b792b        3 weeks ago         1.22MB
mybusybox           latest              018c9d7b792b        3 weeks ago         1.22MB
</code></pre>
<p>可以看到，镜像列表中多了一个<code>mybusybox</code>的镜像。但细心的同学可能已经发现，<code>busybox</code>和<code>mybusybox</code>这两个镜像的 IMAGE ID 是完全一样的。为什么呢？实际上它们指向了同一个镜像文件，只是别名不同而已。
如果我不需要<code>mybusybox</code>镜像了，想删除它，应该怎么操作呢？</p>
<h4>删除镜像</h4>
<p>你可以使用<code>docker rmi</code>或者<code>docker image rm</code>命令删除镜像。</p>
<p>举例：你可以使用以下命令删除<code>mybusybox</code>镜像。</p>
<pre><code>$ docker rmi mybusybox
Untagged: mybusybox:latest
</code></pre>
<p>此时，再次使用<code>docker images</code>命令查看一下我们机器上的镜像列表。</p>
<pre><code>$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             latest              018c9d7b792b        3 weeks ago         1.22MB
</code></pre>
<p>通过上面的输出，我们可以看到，<code>mybusybox</code>镜像已经被删除。
如果你想构建属于自己的镜像，应该怎么做呢？</p>
<h4>构建镜像</h4>
<p>构建镜像主要有两种方式：</p>
<ol>
<li>使用<code>docker commit</code>命令从运行中的容器提交为镜像；</li>
<li>使用<code>docker build</code>命令从 Dockerfile 构建镜像。</li>
</ol>
<p>首先介绍下如何从运行中的容器提交为镜像。我依旧使用 busybox 镜像举例，使用以下命令创建一个名为 busybox 的容器并进入 busybox 容器。</p>
<pre><code>$ docker run --rm --name=busybox -it busybox sh
/ #
</code></pre>
<p>执行完上面的命令后，当前窗口会启动一个 busybox 容器并且进入容器中。在容器中，执行以下命令创建一个文件并写入内容：</p>
<pre><code>/ # touch hello.txt &amp;&amp; echo &quot;I love Docker. &quot; &gt; hello.txt
/ #
</code></pre>
<p>此时在容器的根目录下，已经创建了一个 hello.txt 文件，并写入了 &quot;I love Docker. &quot;。下面，我们新打开另一个命令行窗口，运行以下命令提交镜像：</p>
<pre><code>$ docker commit busybox busybox:hello
sha256:cbc6406aaef080d1dd3087d4ea1e6c6c9915ee0ee0f5dd9e0a90b03e2215e81c
</code></pre>
<p>然后使用上面讲到的<code>docker image ls</code>命令查看镜像：</p>
<pre><code>$ docker image ls busybox
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             hello               cbc6406aaef0        2 minutes ago       1.22MB
busybox             latest              018c9d7b792b        4 weeks ago         1.22MB
</code></pre>
<p>此时我们可以看到主机上新生成了 busybox:hello 这个镜像。</p>
<p>第二种方式是最重要也是最常用的镜像构建方式：Dockerfile。Dockerfile 是一个包含了用户所有构建命令的文本。通过<code>docker build</code>命令可以从 Dockerfile 生成镜像。</p>
<p>使用 Dockerfile 构建镜像具有以下特性：</p>
<ul>
<li>Dockerfile 的每一行命令都会生成一个独立的镜像层，并且拥有唯一的 ID；</li>
<li>Dockerfile 的命令是完全透明的，通过查看 Dockerfile 的内容，就可以知道镜像是如何一步步构建的；</li>
<li>Dockerfile 是纯文本的，方便跟随代码一起存放在代码仓库并做版本管理。</li>
</ul>
<p>看到使用 Dockerfile 的方式构建镜像有这么多好的特性，你是不是已经迫不及待想知道如何使用了。别着急，我们先学习下 Dockerfile 常用的指令。</p>
<table>
<thead>
<tr>
<th>Dockerfile 指令</th>
<th>指令简介</th>
</tr>
</thead>
<tbody>
<tr>
<td>FROM</td>
<td>Dockerfile 除了注释第一行必须是 FROM ，FROM 后面跟镜像名称，代表我们要基于哪个基础镜像构建我们的容器。</td>
</tr>
<tr>
<td>RUN</td>
<td>RUN 后面跟一个具体的命令，类似于 Linux 命令行执行命令。</td>
</tr>
<tr>
<td>ADD</td>
<td>拷贝本机文件或者远程文件到镜像内</td>
</tr>
<tr>
<td>COPY</td>
<td>拷贝本机文件到镜像内</td>
</tr>
<tr>
<td>USER</td>
<td>指定容器启动的用户</td>
</tr>
<tr>
<td>ENTRYPOINT</td>
<td>容器的启动命令</td>
</tr>
<tr>
<td>CMD</td>
<td>CMD 为 ENTRYPOINT 指令提供默认参数，也可以单独使用 CMD 指定容器启动参数</td>
</tr>
<tr>
<td>ENV</td>
<td>指定容器运行时的环境变量，格式为 key=value</td>
</tr>
<tr>
<td>ARG</td>
<td>定义外部变量，构建镜像时可以使用 build-arg = 的格式传递参数用于构建</td>
</tr>
<tr>
<td>EXPOSE</td>
<td>指定容器监听的端口，格式为 [port]/tcp 或者 [port]/udp</td>
</tr>
<tr>
<td>WORKDIR</td>
<td>为 Dockerfile 中跟在其后的所有 RUN、CMD、ENTRYPOINT、COPY 和 ADD 命令设置工作目录。</td>
</tr>
</tbody>
</table>
<p>看了这么多指令，感觉有点懵？别担心，我通过一个实例让你来熟悉它们。这是一个 Dockerfile：</p>
<pre><code>FROM centos:7
COPY nginx.repo /etc/yum.repos.d/nginx.repo
RUN yum install -y nginx
EXPOSE 80
ENV HOST=mynginx
CMD [&quot;nginx&quot;,&quot;-g&quot;,&quot;daemon off;&quot;]
</code></pre>
<p>好，我来逐行分析一下上述的 Dockerfile。</p>
<ul>
<li>第一行表示我要基于 centos:7 这个镜像来构建自定义镜像。这里需要注意，每个 Dockerfile 的第一行除了注释都必须以 FROM 开头。</li>
<li>第二行表示拷贝本地文件 nginx.repo 文件到容器内的 /etc/yum.repos.d 目录下。这里拷贝 nginx.repo 文件是为了添加 nginx 的安装源。</li>
<li>第三行表示在容器内运行<code>yum install -y nginx</code>命令，安装 nginx 服务到容器内，执行完第三行命令，容器内的 nginx 已经安装完成。</li>
<li>第四行声明容器内业务（nginx）使用 80 端口对外提供服务。</li>
<li>第五行定义容器启动时的环境变量 HOST=mynginx，容器启动后可以获取到环境变量 HOST 的值为 mynginx。</li>
<li>第六行定义容器的启动命令，命令格式为 json 数组。这里设置了容器的启动命令为 nginx ，并且添加了 nginx 的启动参数 -g 'daemon off;' ，使得 nginx 以前台的方式启动。</li>
</ul>
<p>上面这个 Dockerfile 的例子基本涵盖了常用的镜像构建指令，代码我已经放在 <a href="https://github.com/wilhelmguo/docker-demo/tree/master/dockerfiles">GitHub</a>上，如果你感兴趣可以到 <a href="https://github.com/wilhelmguo/docker-demo/tree/master/dockerfiles">GitHub 下载源码</a>并尝试构建这个镜像。</p>
<p>学习了镜像的各种操作，下面我们深入了解一下镜像的实现原理。</p>
<h3>镜像的实现原理</h3>
<p>其实 Docker 镜像是由一系列镜像层（layer）组成的，每一层代表了镜像构建过程中的一次提交。下面以一个镜像构建的 Dockerfile 来说明镜像是如何分层的。</p>
<pre><code>FROM busybox
COPY test /tmp/test
RUN mkdir /tmp/testdir
</code></pre>
<p>上面的 Dockerfile 由三步组成：</p>
<p>第一行基于 busybox 创建一个镜像层；</p>
<p>第二行拷贝本机 test 文件到镜像内；</p>
<p>第三行在 /test 文件夹下创建一个目录 testdir。</p>
<p>为了验证镜像的存储结构，我们使用<code>docker build</code>命令在上面 Dockerfile 所在目录构建一个镜像：</p>
<pre><code>$ docker build -t mybusybox .
</code></pre>
<p>这里我的 Docker 使用的是 overlay2 文件驱动，进入到<code>/var/lib/docker/overlay2</code>目录下使用<code>tree .</code>命令查看产生的镜像文件：</p>
<pre><code>$ tree .
# 以下为 tree . 命令输出内容
|-- 3e89b959f921227acab94f5ab4524252ae0a829ff8a3687178e3aca56d605679
|   |-- diff  # 这一层为基础层，对应上述 Dockerfile 第一行，包含 busybox 镜像所有文件内容，例如 /etc,/bin,/var 等目录
... 此次省略部分原始镜像文件内容
|   `-- link 
|-- 6591d4e47eb2488e6297a0a07a2439f550cdb22845b6d2ddb1be2466ae7a9391
|   |-- diff   # 这一层对应上述 Dockerfile 第二行，拷贝 test 文件到 /tmp 文件夹下，因此 diff 文件夹下有了 /tmp/test 文件
|   |   `-- tmp
|   |       `-- test
|   |-- link
|   |-- lower
|   `-- work
|-- backingFsBlockDev
|-- bec6a018080f7b808565728dee8447b9e86b3093b16ad5e6a1ac3976528a8bb1
|   |-- diff  # 这一层对应上述 Dockerfile 第三行，在 /tmp 文件夹下创建 testdir 文件夹，因此 diff 文件夹下有了 /tmp/testdir 文件夹
|   |   `-- tmp
|   |       `-- testdir
|   |-- link
|   |-- lower
|   `-- work
...
</code></pre>
<p>通过上面的目录结构可以看到，Dockerfile 的每一行命令，都生成了一个镜像层，每一层的 diff 夹下只存放了增量数据，如图 2 所示。</p>
<p><img src="assets/CgqCHl9SDmGACBEjAABkgtnn_hE625.png" alt="Lark20200904-175137.png" /></p>
<p>图 2 镜像文件系统</p>
<p>分层的结构使得 Docker 镜像非常轻量，每一层根据镜像的内容都有一个唯一的 ID 值，当不同的镜像之间有相同的镜像层时，便可以实现不同的镜像之间共享镜像层的效果。</p>
<p>总结一下， Docker 镜像是静态的分层管理的文件组合，镜像底层的实现依赖于联合文件系统（UnionFS）。充分掌握镜像的原理，可以帮助我们在生产实践中构建出最优的镜像，同时也可以帮助我们更好地理解容器和镜像的关系。</p>
<h4>总结</h4>
<p>到此，相信你已经对 Docker 镜像这一核心概念有了较深的了解，并熟悉了 Docker 镜像的常用操作（拉取、查看、“重命名”、删除和构建自定义镜像）及底层实现原理。</p>
<p>本课时内容精华，我帮你总结如下：</p>
<blockquote>
<p>镜像操作命令：</p>
<ol>
<li>拉取镜像，使用 docker pull 命令拉取远程仓库的镜像到本地 ；</li>
<li>重命名镜像，使用 docker tag 命令“重命名”镜像 ；</li>
<li>查看镜像，使用 docker image ls 或 docker images 命令查看本地已经存在的镜像；</li>
<li>删除镜像，使用 docker rmi 命令删除无用镜像 ；</li>
<li>构建镜像，构建镜像有两种方式。第一种方式是使用 docker build 命令基于 Dockerfile 构建镜像，也是我比较推荐的镜像构建方式；第二种方式是使用 docker commit 命令基于已经运行的容器提交为镜像。</li>
</ol>
<p>镜像的实现原理：
镜像是由一系列的镜像层（layer ）组成，每一层代表了镜像构建过程中的一次提交，当我们需要修改镜像内的某个文件时，只需要在当前镜像层的基础上新建一个镜像层，并且只存放修改过的文件内容。分层结构使得镜像间共享镜像层变得非常简单和方便。</p>
</blockquote>
<p>最后试想下，如果有一天我们机器存储空间不足，那你知道使用什么命令可以清理本地无用的镜像和容器文件吗？思考后，可以把你的想法写在留言区。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="02&#32;&#32;核心概念：镜像、容器、仓库，彻底掌握&#32;Docker&#32;架构核心设计理念.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="04&#32;&#32;容器操作：得心应手掌握&#32;Docker&#32;容器基本操作.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359b37f85645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
