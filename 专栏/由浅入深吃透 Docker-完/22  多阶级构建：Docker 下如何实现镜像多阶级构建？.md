<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>22  多阶级构建：Docker 下如何实现镜像多阶级构建？.md</title>
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

                    
                    <a href="19&#32;&#32;如何使用&#32;Docker&#32;Compose&#32;解决开发环境的依赖？.md">19  如何使用 Docker Compose 解决开发环境的依赖？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;如何在生产环境中使用&#32;Docker&#32;Swarm&#32;调度容器？.md">20  如何在生产环境中使用 Docker Swarm 调度容器？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;如何使&#32;Docker&#32;和&#32;Kubernetes&#32;结合发挥容器的最大价值？.md">21  如何使 Docker 和 Kubernetes 结合发挥容器的最大价值？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="22&#32;&#32;多阶级构建：Docker&#32;下如何实现镜像多阶级构建？.md">22  多阶级构建：Docker 下如何实现镜像多阶级构建？.md</a>
                    

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
                        <div><h1>22  多阶级构建：Docker 下如何实现镜像多阶级构建？</h1>
<p>通过前面课程的学习，我们知道 Docker 镜像是分层的，并且每一层镜像都会额外占用存储空间，一个 Docker 镜像层数越多，这个镜像占用的存储空间则会越多。镜像构建最重要的一个原则就是要保持镜像体积尽可能小，要实现这个目标通常可以从两个方面入手：</p>
<ul>
<li>基础镜像体积应该尽量小；</li>
<li>尽量减少 Dockerfile 的行数，因为 Dockerfile 的每一条指令都会生成一个镜像层。</li>
</ul>
<p>在 Docker 的早期版本中，对于编译型语言（例如 C、Java、Go）的镜像构建，我们只能将应用的编译和运行环境的准备，全部都放到一个 Dockerfile 中，这就导致我们构建出来的镜像体积很大，从而增加了镜像的存储和分发成本，这显然与我们的镜像构建原则不符。</p>
<p>为了减小镜像体积，我们需要借助一个额外的脚本，将镜像的编译过程和运行过程分开。</p>
<ul>
<li>编译阶段：负责将我们的代码编译成可执行对象。</li>
<li>运行时构建阶段：准备应用程序运行的依赖环境，然后将编译后的可执行对象拷贝到镜像中。</li>
</ul>
<p>我以 Go 语言开发的一个 HTTP 服务为例，代码如下：</p>
<pre><code>package main

import (

   &quot;fmt&quot;

   &quot;net/http&quot;

)

func hello(w http.ResponseWriter, req *http.Request) {

   fmt.Fprintf(w, &quot;hello world!\n&quot;)

}

func main() {

   http.HandleFunc(&quot;/&quot;, hello)

   http.ListenAndServe(&quot;:8080&quot;, nil)

}
</code></pre>
<p>我将这个 Go 服务构建成镜像分为两个阶段：代码的编译阶段和镜像构建阶段。</p>
<p>我们构建镜像时，镜像中需要包含 Go 语言编译环境，应用的编译阶段我们可以使用 Dockerfile.build 文件来构建镜像。Dockerfile.build 的内容如下：</p>
<pre><code>FROM golang:1.13

WORKDIR /go/src/github.com/wilhelmguo/multi-stage-demo/

COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux go build -o http-server .
</code></pre>
<p>Dockerfile.build 可以帮助我们把代码编译成可以执行的二进制文件，我们使用以下 Dockerfile 构建一个运行环境：</p>
<pre><code>FROM alpine:latest  

WORKDIR /root/

COPY http-server .

CMD [&quot;./http-server&quot;] 
</code></pre>
<p>然后，我们将应用的编译和运行环境的准备步骤，都放到一个 build.sh 脚本文件中，内容如下：</p>
<pre><code>#!/bin/sh

echo Building http-server:build

docker build -t http-server:build . -f Dockerfile.build

docker create --name builder http-server:build  

docker cp builder:/go/src/github.com/wilhelmguo/multi-stage-demo/http-server ./http-server  

docker rm -f builder

echo Building http-server:latest

docker build -t http-server:latest .

rm ./http-server
</code></pre>
<p>下面，我带你来逐步分析下这个脚本。</p>
<p>第一步，声明 shell 文件，然后输出开始构建信息。</p>
<pre><code>#!/bin/sh

echo Building http-server:build
</code></pre>
<p>第二步，使用 Dockerfile.build 文件来构建一个临时镜像 http-server:build。</p>
<pre><code>docker build -t http-server:build . -f Dockerfile.build
</code></pre>
<p>第三步，使用 http-server:build 镜像创建一个名称为 builder 的容器，该容器包含编译后的 http-server 二进制文件。</p>
<pre><code>docker create --name builder http-server:build  
</code></pre>
<p>第四步，使用<code>docker cp</code>命令从 builder 容器中拷贝 http-server 文件到当前构建目录下，并且删除名称为 builder 的临时容器。</p>
<pre><code>docker cp builder:/go/src/github.com/wilhelmguo/multi-stage-demo/http-server ./http-server  

docker rm -f builder
</code></pre>
<p>第五步，输出开始构建镜像信息。</p>
<pre><code>echo Building http-server:latest
</code></pre>
<p>第六步，构建运行时镜像，然后删除临时文件 http-server。</p>
<pre><code>docker build -t http-server:latest .

rm ./http-server
</code></pre>
<p>我这里总结一下，我们是使用 Dockerfile.build 文件来编译应用程序，使用 Dockerfile 文件来构建应用的运行环境。然后我们通过创建一个临时容器，把编译后的 http-server 文件拷贝到当前构建目录中，然后再把这个文件拷贝到运行环境的镜像中，最后指定容器的启动命令为 http-server。</p>
<p>使用这种方式虽然可以实现分离镜像的编译和运行环境，但是我们需要额外引入一个 build.sh 脚本文件，而且构建过程中，还需要创建临时容器 builder 拷贝编译后的 http-server 文件，这使得整个构建过程比较复杂，并且整个构建过程也不够透明。</p>
<p>为了解决这种问题， Docker 在 17.05 推出了多阶段构建（multistage-build）的解决方案。</p>
<h3>使用多阶段构建</h3>
<p>Docker 允许我们在 Dockerfile 中使用多个 FROM 语句，而每个 FROM 语句都可以使用不同基础镜像。最终生成的镜像，是以最后一条 FROM 为准，所以我们可以在一个 Dockerfile 中声明多个 FROM，然后选择性地将一个阶段生成的文件拷贝到另外一个阶段中，从而实现最终的镜像只保留我们需要的环境和文件。多阶段构建的主要使用场景是<strong>分离编译环境和运行环境。</strong></p>
<p>接下来，我们使用多阶段构建的特性，将上述未使用多阶段构建的过程精简成如下 Dockerfile：</p>
<pre><code>FROM golang:1.13

WORKDIR /go/src/github.com/wilhelmguo/multi-stage-demo/

COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux go build -o http-server .

FROM alpine:latest  

WORKDIR /root/

COPY --from=0 /go/src/github.com/wilhelmguo/multi-stage-demo/http-server .

CMD [&quot;./http-server&quot;] 
</code></pre>
<p>然后，我们将这个 Dockerfile 拆解成两步进行分析。</p>
<p>第一步，编译代码。</p>
<pre><code>FROM golang:1.13

WORKDIR /go/src/github.com/wilhelmguo/multi-stage-demo/

COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux go build -o http-server .
</code></pre>
<p>将代码拷贝到 golang:1.13 镜像（已经安装好了 go）中，并且使用<code>go build</code>命令编译代码生成 http-server 文件。</p>
<p>第二步，构建运行时镜像。</p>
<pre><code>FROM alpine:latest  

WORKDIR /root/

COPY --from=0 /go/src/github.com/wilhelmguo/multi-stage-demo/http-server .

CMD [&quot;./http-server&quot;]
</code></pre>
<p>使用第二个 FROM 命令表示镜像构建的第二阶段，使用 COPY 指令拷贝编译后的文件到 alpine 镜像中，--from=0 表示从第一阶段构建结果中拷贝文件到当前构建阶段。</p>
<p>最后，我们只需要使用以下命令，即可实现整个镜像的构建：</p>
<pre><code>docker build -t http-server:latest .
</code></pre>
<p>构建出来的镜像与未使用多阶段构建之前构建的镜像大小一致，为了验证这一结论，我们分别使用这两种方式来构建镜像，最后对比一下镜像构建的结果。</p>
<h3>镜像构建对比</h3>
<p>使用多阶段构建前后的代码我都已经放在了<a href="https://github.com/wilhelmguo/multi-stage-demo">Github</a>，你只需要克隆代码到本地即可。</p>
<pre><code>$ mkdir /go/src/github.com/wilhelmguo

$ cd /go/src/github.com/wilhelmguo

$ git clone https://github.com/wilhelmguo/multi-stage-demo.git
</code></pre>
<p>代码克隆完成后，我们首先切换到without-multi-stage分支：</p>
<pre><code>$ cd without-multi-stage

$ git checkout without-multi-stage
</code></pre>
<p>这个分支是未使用多阶段构建技术构建镜像的代码，我们可以通过执行 build.sh 文件构建镜像：</p>
<pre><code>$  chmod +x build.sh &amp;&amp; ./build.sh

Building http-server:build

Sending build context to Docker daemon  96.26kB

Step 1/4 : FROM golang:1.13

1.13: Pulling from library/golang

d6ff36c9ec48: Pull complete 

c958d65b3090: Pull complete 

edaf0a6b092f: Pull complete 

80931cf68816: Pull complete 

813643441356: Pull complete 

799f41bb59c9: Pull complete 

16b5038bccc8: Pull complete 

Digest: sha256:8ebb6d5a48deef738381b56b1d4cd33d99a5d608e0d03c5fe8dfa3f68d41a1f8

Status: Downloaded newer image for golang:1.13

 ---&gt; d6f3656320fe

Step 2/4 : WORKDIR /go/src/github.com/wilhelmguo/multi-stage-demo/

 ---&gt; Running in fa3da5ffb0c0

Removing intermediate container fa3da5ffb0c0

 ---&gt; 97245cbb773f

Step 3/4 : COPY main.go .

 ---&gt; a021d2f2a5bb

Step 4/4 : RUN CGO_ENABLED=0 GOOS=linux go build -o http-server .

 ---&gt; Running in b5c36bb67b9c

Removing intermediate container b5c36bb67b9c

 ---&gt; 76c0c88a5cf7

Successfully built 76c0c88a5cf7

Successfully tagged http-server:build

4b0387b270bc4a4da570e1667fe6f9baac765f6b80c68f32007494c6255d9e5b

builder

Building http-server:latest

Sending build context to Docker daemon  7.496MB

Step 1/4 : FROM alpine:latest

latest: Pulling from library/alpine

df20fa9351a1: Already exists 

Digest: sha256:185518070891758909c9f839cf4ca393ee977ac378609f700f60a771a2dfe321

Status: Downloaded newer image for alpine:latest

 ---&gt; a24bb4013296

Step 2/4 : WORKDIR /root/

 ---&gt; Running in 0b25ffe603b8

Removing intermediate container 0b25ffe603b8

 ---&gt; 80da40d3a0b4

Step 3/4 : COPY http-server .

 ---&gt; 3f2300210b7b

Step 4/4 : CMD [&quot;./http-server&quot;]

 ---&gt; Running in 045cea651dde

Removing intermediate container 045cea651dde

 ---&gt; 5c73883177e7

Successfully built 5c73883177e7

Successfully tagged http-server:latest
</code></pre>
<p>经过一段时间的等待，我们的镜像就构建完成了。
镜像构建完成后，我们使用<code>docker image ls</code>命令查看一下刚才构建的镜像大小：</p>
<pre><code>$ docker image ls http-server

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE

http-server         latest              5c73883177e7        3 minutes ago       13MB

http-server         build               76c0c88a5cf7        3 minutes ago       819MB
</code></pre>
<p>可以看到，http-server:latest 镜像只有 13M，而我们的编译镜像 http-server:build 则为 819M，虽然我们编写了很复杂的脚本 build.sh，但是这个脚本确实帮助我们将镜像体积减小了很多。</p>
<p>下面，我们将代码切换到多阶段构建分支：</p>
<pre><code>$ git checkout with-multi-stage

Switched to branch 'with-multi-stage'
</code></pre>
<p>为了避免镜像名称重复，我们将多阶段构建的镜像命名为 http-server-with-multi-stage:latest ，并且禁用缓存，避免缓存干扰构建结果，构建命令如下：</p>
<pre><code>$ docker build --no-cache -t http-server-with-multi-stage:latest .

Sending build context to Docker daemon  96.77kB

Step 1/8 : FROM golang:1.13

 ---&gt; d6f3656320fe

Step 2/8 : WORKDIR /go/src/github.com/wilhelmguo/multi-stage-demo/

 ---&gt; Running in 640da7a92a62

Removing intermediate container 640da7a92a62

 ---&gt; 9c27b4606da0

Step 3/8 : COPY main.go .

 ---&gt; bd9ce4af24cb

Step 4/8 : RUN CGO_ENABLED=0 GOOS=linux go build -o http-server .

 ---&gt; Running in 6b441b4cc6b7

Removing intermediate container 6b441b4cc6b7

 ---&gt; 759acbf6c9a6

Step 5/8 : FROM alpine:latest

 ---&gt; a24bb4013296

Step 6/8 : WORKDIR /root/

 ---&gt; Running in c2aa2168acd8

Removing intermediate container c2aa2168acd8

 ---&gt; f026884acda6

Step 7/8 : COPY --from=0 /go/src/github.com/wilhelmguo/multi-stage-demo/http-server .

 ---&gt; 667503e6bc14

Step 8/8 : CMD [&quot;./http-server&quot;]

 ---&gt; Running in 15c4cc359144

Removing intermediate container 15c4cc359144

 ---&gt; b73cc4d99088

Successfully built b73cc4d99088

Successfully tagged http-server-with-multi-stage:latest
</code></pre>
<p>镜像构建完成后，我们同样使用<code>docker image ls</code>命令查看一下镜像构建结果：</p>
<pre><code>$ docker image ls http-server-with-multi-stage:latest

REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE

http-server-with-multi-stage   latest              b73cc4d99088        2 minutes ago       13MB
</code></pre>
<p>可以看到，使用多阶段构建的镜像大小与上一步构建的镜像大小一致，都为 13M。但是使用多阶段构建后，却大大减少了我们的构建步骤，使得构建过程更加清晰可读。</p>
<h3>多阶段构建的其他使用方式</h3>
<p>多阶段构建除了我们上面讲解的使用方式，还有更多其他的使用方式，这些使用方式，可以使得多阶段构建实现更多的功能。</p>
<h4>为构建阶段命名</h4>
<p>默认情况下，每一个构建阶段都没有被命名，你可以通过 FROM 指令出现的顺序来引用这些构建阶段，构建阶段的序号是从 0 开始的。然而，为了提高 Dockerfile 的可读性，我们需要为某些构建阶段起一个名称，这样即便后面我们对 Dockerfile 中的内容进程重新排序或者添加了新的构建阶段，其他构建过程中的 COPY 指令也不需要修改。</p>
<p>上面的 Dockerfile 我们可以优化成如下内容：</p>
<pre><code>FROM golang:1.13 AS builder

WORKDIR /go/src/github.com/wilhelmguo/multi-stage-demo/

COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux go build -o http-server .

FROM alpine:latest  

WORKDIR /root/

COPY --from=builder /go/src/github.com/wilhelmguo/multi-stage-demo/http-server .

CMD [&quot;./http-server&quot;]
</code></pre>
<p>我们在第一个构建阶段，使用 AS 指令将这个阶段命名为 builder。然后在第二个构建阶段使用 --from=builder 指令，即可从第一个构建阶段中拷贝文件，使得 Dockerfile 更加清晰可读。</p>
<h4>停止在特定的构建阶段</h4>
<p>有时候，我们的构建阶段非常复杂，我们想在代码编译阶段进行调试，但是多阶段构建默认构建 Dockerfile 的所有阶段，为了减少每次调试的构建时间，我们可以使用 target 参数来指定构建停止的阶段。</p>
<p>例如，我只想在编译阶段调试 Dockerfile 文件，可以使用如下命令：</p>
<pre><code>$ docker build --target builder -t http-server:latest .
</code></pre>
<p>在执行<code>docker build</code>命令时添加 target 参数，可以将构建阶段停止在指定阶段，从而方便我们调试代码编译过程。</p>
<h4>使用现有镜像作为构建阶段</h4>
<p>使用多阶段构建时，不仅可以从 Dockerfile 中已经定义的阶段中拷贝文件，还可以使用<code>COPY --from</code>指令从一个指定的镜像中拷贝文件，指定的镜像可以是本地已经存在的镜像，也可以是远程镜像仓库上的镜像。</p>
<p>例如，当我们想要拷贝 nginx 官方镜像的配置文件到我们自己的镜像中时，可以在 Dockerfile 中使用以下指令：</p>
<pre><code>COPY --from=nginx:latest /etc/nginx/nginx.conf /etc/local/nginx.conf
</code></pre>
<p>从现有镜像中拷贝文件还有一些其他的使用场景。例如，有些工具没有我们使用的操作系统的安装源，或者安装源太老，需要我们自己下载源码并编译这些工具，但是这些工具可能依赖的编译环境非常复杂，而网上又有别人已经编译好的镜像。这时我们就可以使用<code>COPY --from</code>指令从编译好的镜像中将工具拷贝到我们自己的镜像中，很方便地使用这些工具了。</p>
<h3>结语</h3>
<p>多阶段构建可以让我们通过一个 Dockerfile 很方便地构建出体积更小的镜像，并且我们只需要编写 Dockerfile 文件即可，无须借助外部脚本文件。这使得镜像构建过程更加简单透明，但要提醒一点：使用多阶段构建的唯一限制条件是我们使用的 Docker 版本必须高于 17.05 。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="21&#32;&#32;如何使&#32;Docker&#32;和&#32;Kubernetes&#32;结合发挥容器的最大价值？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="23&#32;&#32;DevOps：容器化后如何通过&#32;DevOps&#32;提高协作效能？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a3849e3645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
