<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17  原理实践：自己动手使用 Golang 开发 Docker（上）.md</title>
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

                    <a class="current-tab" href="17&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（上）.md">17  原理实践：自己动手使用 Golang 开发 Docker（上）.md</a>
                    

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
                        <div><h1>17  原理实践：自己动手使用 Golang 开发 Docker（上）</h1>
<p>第一模块，我们从 Docker 基础概念讲到 Docker 的基本操作。第二模块，我们详细剖析了 Docker 的三大关键技术（ Namespace、cgroups 和联合文件系统）的实现原理，并且讲解了 Docker 的网络模型等关键性技术。相信此时的你已经对 Docker 有了一个新的认识。</p>
<p>接下来的两课时，我就趁热打铁，带你动手使用 Golang 编写一个 Docker。学习这两节的内容需要你能够熟练使用 Golang 语言，如果你没有 Golang 编程基础，建议先学习一下 Golang 的基本语法。那么 Golang 究竟是什么呢? Golang 应该如何安装使用？下面我带你一一学习。</p>
<h3>Golang 是什么?</h3>
<p>Golang 又称为 Go，是 Google 开源的一种静态编译型语言，Golang 自带内存管理机制，相比于 C 和 C++ 语言，我们不需要关心内存的分配和回收。</p>
<p>Golang 是新一代的互联网编程语言，在 Golang 诞生前，C 或 C++ 作为服务端高性能编程语言，使用 C 或 C++ 开发的业务具有非常高的执行效率，但是编译和开发效率却不尽人意，Java、.NET 等语言的诞生大大提高了软件开发速度，但是运行效率和资源占用却不如 C 和 C++。</p>
<p>这时 Golang 横空出世，由于 Golang 较高的开发效率和执行效率，很快便从众多编程语言中脱颖而出，成为众多互联网公司的新宠儿。滴滴、知乎、阿里等众多大型互联网公司都在大量使用 Golang。 同时，Docker 和 Kubernetes 等众多明星项目也都是使用 Golang 开发的。因此，熟练掌握 Golang 将会为你加分很多。</p>
<p>这么好的编程语言，你是不是已经迫不及待地想要安装体验一下了？别着急，下面我带你来安装一个 Golang 环境。</p>
<h3>Golang 安装</h3>
<p>安装信息如下：</p>
<ul>
<li>CentOS 7系统</li>
<li>Golang 版本 1.15.2</li>
</ul>
<p>首先我们到<a href="https://golang.org/">Golang 官网</a>（由于国内无法访问 Golang 官网，推荐到<a href="https://studygolang.com/dl">Golang 中文网</a>下载安装包）下载一个对应操作系统的安装包。</p>
<pre><code>$ cd /tmp &amp;&amp; wget https://studygolang.com/dl/golang/go1.15.2.linux-amd64.tar.gz
</code></pre>
<p>解压缩安装包：</p>
<pre><code>$ sudo tar -C /usr/local -xzf go1.15.2.linux-amd64.tar.gz
</code></pre>
<p>在 $HOME/.bashrc 文件末尾添加以下内容，将 Golang 可执行文件目录添加到系统 PATH 中：</p>
<pre><code>export PATH=$PATH:/usr/local/go/bin
</code></pre>
<p>将 go 的安装路径添加到系统 PATH 中后，就可以在命令行直接使用 go 命令了。配置好 go 命令后，我们还需要配置 GOPATH 才能正确存放和编译我们的 go 代码。</p>
<h4>配置 GOPATH</h4>
<p>GOPATH 是 Golang 的源码和相关编译文件的存放路径，GOPATH 路径下有三个文件夹 src、pkg 和 bin，它们的用途分别是：</p>
<table>
<thead>
<tr>
<th><strong>目录</strong></th>
<th><strong>用途</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>src</td>
<td>源代码存放路径或者引用的外部库</td>
</tr>
<tr>
<td>pkg</td>
<td>编译时生成的对象文件</td>
</tr>
<tr>
<td>bin</td>
<td>编译后的可执行二进制</td>
</tr>
</tbody>
</table>
<p>这里我们开始配置 GOPATH 路径为 /go。首先准备相关的目录：</p>
<pre><code>$ sudo mkdir /go

$ sudo mkdir /go/src

$ sudo mkdir /go/pkg

$ sudo mkdir /go/bin
</code></pre>
<p>然后将 GOPATH 添加到 $HOME/.bashrc 文件末尾，并且把 GOPATH 下的 bin 目录也添加到系统的 PATH 中，这样方便程序编译后直接使用。添加的内容如下：</p>
<pre><code>export GOPATH=/go

export PATH=$PATH:$GOPATH/bin

# 设置 Golang 的代理，方便我们顺利下载依赖包

export GOPROXY=&quot;https://goproxy.io,direct&quot;
</code></pre>
<p>接下来，使用 source $HOME/.bashrc 命令生效一下我们的配置，然后我们再使用 go env 命令查看一下我们的配置结果：</p>
<pre><code>$ go env

GO111MODULE=&quot;&quot;

GOARCH=&quot;amd64&quot;

GOBIN=&quot;&quot;

GOCACHE=&quot;/root/.cache/go-build&quot;

GOENV=&quot;/root/.config/go/env&quot;

GOEXE=&quot;&quot;

GOFLAGS=&quot;&quot;

GOHOSTARCH=&quot;amd64&quot;

GOHOSTOS=&quot;linux&quot;

GOINSECURE=&quot;&quot;

GOMODCACHE=&quot;/go/pkg/mod&quot;

GONOPROXY=&quot;&quot;

GONOSUMDB=&quot;&quot;

GOOS=&quot;linux&quot;

GOPATH=&quot;/go&quot;

GOPRIVATE=&quot;&quot;

GOPROXY=&quot;https://goproxy.io,direct&quot;

GOROOT=&quot;/usr/local/go&quot;

GOSUMDB=&quot;sum.golang.org&quot;

GOTMPDIR=&quot;&quot;

GOTOOLDIR=&quot;/usr/local/go/pkg/tool/linux_amd64&quot;

GCCGO=&quot;gccgo&quot;

AR=&quot;ar&quot;

CC=&quot;gcc&quot;

CXX=&quot;g++&quot;

CGO_ENABLED=&quot;1&quot;

GOMOD=&quot;&quot;

CGO_CFLAGS=&quot;-g -O2&quot;

CGO_CPPFLAGS=&quot;&quot;

CGO_CXXFLAGS=&quot;-g -O2&quot;

CGO_FFLAGS=&quot;-g -O2&quot;

CGO_LDFLAGS=&quot;-g -O2&quot;

PKG_CONFIG=&quot;pkg-config&quot;

GOGCCFLAGS=&quot;-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build352828668=/tmp/go-build -gno-record-gcc-switches&quot;
</code></pre>
<p>从 GOPATH 和 GOPROXY 两个变量的结果，可以看到 GOPATH 和 GOPROXY 均已经生效。到此，我们的 Golang 已经安装完毕。下面，我们就开始真正的 Docker 编写之旅吧。</p>
<h3>编写 Docker</h3>
<p>在开始编写 Docker 之前，我先介绍几个基础知识，如果你对这些基础知识已经很熟悉了，可以直接跳过这块的基础知识。</p>
<h4>Linux Proc 文件系统</h4>
<p>Linux 系统中，/proc 目录是一种“文件系统”，这里我用了引号，其实 /proc 目录并不是一个真正的文件系统。<strong>/proc 目录存放于内存中，是一个虚拟的文件系统，该目录存放了当前内核运行状态的一系列特殊的文件，你可以通过这些文件查看当前的进程信息。</strong></p>
<p>下面，我们通过 ls 命令查看一下 /proc 目录下的内容：</p>
<pre><code>$ sudo ls -l /proc

total 0

dr-xr-xr-x  9 root    root                  0 Sep 19 21:34 1

dr-xr-xr-x  9 root    root                  0 Sep 19 21:34 30097

...省略部分输出

dr-xr-xr-x  9 root    root                  0 Sep 19 21:34 8

dr-xr-xr-x  9 root    root                  0 Sep 19 21:34 9

dr-xr-xr-x  9 root    root                  0 Sep 19 21:34 97

dr-xr-xr-x  2 root    root                  0 Sep 19 22:27 acpi

-r--r--r--  1 root    root                  0 Sep 19 22:27 buddyinfo

dr-xr-xr-x  4 root    root                  0 Sep 19 22:27 bus

-r--r--r--  1 root    root                  0 Sep 19 22:27 cgroups

-r--r--r--  1 root    root                  0 Sep 19 22:27 cmdline

-r--r--r--  1 root    root                  0 Sep 19 22:27 consoles

-r--r--r--  1 root    root                  0 Sep 19 22:27 cpuinfo

-r--r--r--  1 root    root                  0 Sep 19 22:27 crypto

-r--r--r--  1 root    root                  0 Sep 19 22:27 devices

-r--r--r--  1 root    root                  0 Sep 19 21:34 diskstats

-r--r--r--  1 root    root                  0 Sep 19 22:27 dma

dr-xr-xr-x  2 root    root                  0 Sep 19 22:27 driver

-r--r--r--  1 root    root                  0 Sep 19 22:27 execdomains

-r--r--r--  1 root    root                  0 Sep 19 22:27 fb

-r--r--r--  1 root    root                  0 Sep 19 22:27 filesystems

dr-xr-xr-x  5 root    root                  0 Sep 19 22:27 fs

-r--r--r--  1 root    root                  0 Sep 19 22:27 interrupts

-r--r--r--  1 root    root                  0 Sep 19 22:27 iomem

-r--r--r--  1 root    root                  0 Sep 19 22:27 ioports

dr-xr-xr-x 27 root    root                  0 Sep 19 22:27 irq

-r--r--r--  1 root    root                  0 Sep 19 22:27 kallsyms

-r--------  1 root    root    140737486266368 Sep 19 22:27 kcore

-r--r--r--  1 root    root                  0 Sep 19 22:27 key-users

-r--r--r--  1 root    root                  0 Sep 19 22:27 keys

-r--------  1 root    root                  0 Sep 19 22:27 kmsg

-r--------  1 root    root                  0 Sep 19 22:27 kpagecount

-r--------  1 root    root                  0 Sep 19 22:27 kpageflags

-r--r--r--  1 root    root                  0 Sep 19 22:27 loadavg

-r--r--r--  1 root    root                  0 Sep 19 22:27 locks

-r--r--r--  1 root    root                  0 Sep 19 22:27 mdstat

-r--r--r--  1 root    root                  0 Sep 19 22:27 meminfo

-r--r--r--  1 root    root                  0 Sep 19 22:27 misc

-r--r--r--  1 root    root                  0 Sep 19 22:27 modules

lrwxrwxrwx  1 root    root                 11 Sep 19 22:27 mounts -&gt; self/mounts

-rw-r--r--  1 root    root                  0 Sep 19 22:27 mtrr

lrwxrwxrwx  1 root    root                  8 Sep 19 22:27 net -&gt; self/net

-r--r--r--  1 root    root                  0 Sep 19 22:27 pagetypeinfo

-r--r--r--  1 root    root                  0 Sep 19 22:27 partitions

-r--r--r--  1 root    root                  0 Sep 19 22:27 sched_debug

-r--r--r--  1 root    root                  0 Sep 19 22:27 schedstat

dr-xr-xr-x  2 root    root                  0 Sep 19 22:27 scsi

lrwxrwxrwx  1 root    root                  0 Sep 19 21:34 self -&gt; 30097

-r--------  1 root    root                  0 Sep 19 22:27 slabinfo

-r--r--r--  1 root    root                  0 Sep 19 22:27 softirqs

-r--r--r--  1 root    root                  0 Sep 19 21:34 stat

-r--r--r--  1 root    root                  0 Sep 19 21:34 swaps

dr-xr-xr-x  1 root    root                  0 Sep 19 21:34 sys

--w-------  1 root    root                  0 Sep 19 22:27 sysrq-trigger

dr-xr-xr-x  2 root    root                  0 Sep 19 22:27 sysvipc

-r--r--r--  1 root    root                  0 Sep 19 22:27 timer_list

-rw-r--r--  1 root    root                  0 Sep 19 22:27 timer_stats

dr-xr-xr-x  4 root    root                  0 Sep 19 22:27 tty

-r--r--r--  1 root    root                  0 Sep 19 22:27 uptime

-r--r--r--  1 root    root                  0 Sep 19 22:27 version

-r--------  1 root    root                  0 Sep 19 22:27 vmallocinfo

-r--r--r--  1 root    root                  0 Sep 19 22:27 vmstat

-r--r--r--  1 root    root                  0 Sep 19 22:27 zoneinfo
</code></pre>
<p>可以看到，这个目录下有很多数字，这些数字目录实际上是以进程 ID 命名的。除了这些以进程 ID 命名的目录，还有一些特殊的目录，这里我讲解一下与我们编写 Docker 有关的文件和目录。</p>
<ul>
<li><strong>self 目录</strong>：它是连接到当前正在运行的进程目录，比如我当前的进程 ID 为 30097，则 self 目录实际连接到 /proc/30097 这个目录。</li>
<li><strong>/proc/{PID}/exe 文件</strong>：exe 连接到进程执行的命令文件，例如 30097 这个进程的运行命令为 docker，则执行 /proc/30097/exe ps 等同于执行 docker ps。</li>
</ul>
<p>好了，了解完这些基础知识后，我们就开始行动吧！因为我们的精简版 Docker 是使用 Golang 编写，这里就给我们编写的 Docker 命名为 gocker 吧。</p>
<h4>实现 gocker 的 run 命令</h4>
<p>通过前面的章节，我们学习了要运行一个容器，必须先有镜像。这里我们首先准备一个 busybox 镜像，以便我们运行 gocker 容器。</p>
<pre><code>$ mkdir /tmp/busybox &amp;&amp; cd /tmp/busybox

$ docker export $(docker create busybox) -o busybox.tar

$ tar -xf busybox.tar
</code></pre>
<p>以上是我们在 /tmp/busybox 目录，使用 docker export 命令导出的一个 busybox 镜像文件，然后对镜像文件包进行解压，解压后 /tmp/busybox 目录内容如下：</p>
<pre><code>$ ls -l /tmp/busybox/

total 1472

drwxr-xr-x 2 root      root        12288 Sep  9 02:09 bin

-rw------- 1 root      root      1455104 Sep 19 22:47 busybox.tar

drwxr-xr-x 4 root      root         4096 Sep 19 16:41 dev

drwxr-xr-x 3 root      root         4096 Sep 19 16:41 etc

drwxr-xr-x 2 nfsnobody nfsnobody    4096 Sep  9 02:09 home

drwxr-xr-x 2 root      root         4096 Sep 19 16:41 proc

drwx------ 2 root      root         4096 Sep 19 21:07 root

drwxr-xr-x 2 root      root         4096 Sep 19 16:41 sys

drwxrwxrwt 2 root      root         4096 Sep  9 02:09 tmp

drwxr-xr-x 3 root      root         4096 Sep  9 02:09 usr

drwxr-xr-x 4 root      root         4096 Sep  9 02:09 var
</code></pre>
<p>准备好镜像文件后，把我为你准备好的 gocker 代码下载下来吧，这里我使用手动下载源码的方式克隆代码：</p>
<pre><code>$ mkdir -p /go/src/github.com/wilhelmguo

$ cd /go/src/github.com/wilhelmguo &amp;&amp; git clone https://github.com/wilhelmguo/gocker.git

$ cd gocker

$ git checkout lesson-17
</code></pre>
<blockquote>
<p>我的 GOPATH 在 /go 目录下，如果你的 GOPATH 跟我不一致，请根据 GOPATH 存放和编译源码。本课时的源码存放在<a href="https://github.com/wilhelmguo/gocker/tree/lesson-17">这里</a>，你也可以在线阅读。</p>
</blockquote>
<p>代码下载完后，我们进入 gocker 的目录，查看下源码文件：</p>
<pre><code>$ tree .

.

|-- go.mod

|-- go.sum

|-- main.go

|-- README.md

|-- runc

|   `-- run.go

`-- vendor

... 省略 vendor 目录结构

15 directories, 59 files
</code></pre>
<blockquote>
<p>本项目使用 go mod 管理包依赖，go mod 是在 golang 1.11 版本加入的新的特性，是用来管理包的依赖的，也是目前官方的包依赖管理工具。如果你想学习更多个 go mod 使用方法，可以参考<a href="https://golang.org/ref/mod">官网</a>。</p>
</blockquote>
<p>可以看到该源码下有两个主要文件：一个是 main.go 文件，这是 gocker 的主入口函数；另外一个是 run.go ，这个文件是 gocker run 命令的具体实现。</p>
<p>下面我们使用 go install 命令来编译一下我们的 gocker 项目：</p>
<pre><code>$ go install
</code></pre>
<p>执行完 go install 后， Golang 会自动帮助我们编译当前项目下的代码，编译后的二进制文件存放在 $GOPATH/bin 目录下。由于我们之前在 $HOME/.bashrc 文件下把 $GOPATH/bin 放入了系统 PATH 中，所以此时你可以直接使用 gocker 命令了。
接下来我们使用 gocker 来启动一个容器：</p>
<pre><code># gocker run -it -rootfs=/tmp/busybox /bin/sh

2020/09/19 23:46:27 Current path is  /tmp/busybox

2020/09/19 23:46:27 CmdArray is  [/bin/sh]

/ #
</code></pre>
<blockquote>
<p>如果出现 pivotRoot error pivot_root invalid argument 的报错，可以先执行 unshare -m 命令，然后使用 rm -rf /tmp/busybox/.pivot_root 命令删除临时文件，再次重试即可。</p>
</blockquote>
<p>这里我们使用 it 参数指定以命令行交互的模式启动容器，rootfs 指定准备好的镜像目录。执行完上面的命令后 busybox 容器就成功启动了。
这时候，我们使用 ps 命令查看一下当前进程信息：</p>
<pre><code>/ # /bin/ps -ef

PID   USER     TIME  COMMAND

    1 root      0:00 /bin/sh

    5 root      0:00 /bin/ps -ef
</code></pre>
<p>此时，容器内的进程已经与主机完全隔离。
我们再查看一下当前目录下的内容：</p>
<pre><code>/ # pwd

/ # /bin/ls -l

total 1468

drwxr-xr-x    2 root     root         12288 Sep  8 18:09 bin

-rw-------    1 root     root       1455104 Sep 19 14:47 busybox.tar

drwxr-xr-x    4 root     root          4096 Sep 19 08:41 dev

drwxr-xr-x    3 root     root          4096 Sep 19 08:41 etc

drwxr-xr-x    2 nobody   nobody        4096 Sep  8 18:09 home

dr-xr-xr-x  122 root     root             0 Sep 19 15:46 proc

drwx------    2 root     root          4096 Sep 19 13:07 root

drwxr-xr-x    2 root     root          4096 Sep 19 08:41 sys

drwxrwxrwt    2 root     root          4096 Sep  8 18:09 tmp

drwxr-xr-x    3 root     root          4096 Sep  8 18:09 usr

drwxr-xr-x    4 root     root          4096 Sep  8 18:09 var
</code></pre>
<p>可以看到当前目录已经为根目录，并且根目录下的文件就是我们上面准备的 busybox 镜像文件。
到此，一个完全由我们自己编写的 gocker 已经可以启动容器了。</p>
<h3>结语</h3>
<p>本课时我们讲解了 Golang 是什么, 并且配置好了 Golang 环境，编译了 gocker，也了解了 Linux /proc 文件系统的一些重要功能，最后使用 gocker 成功启动了一个 busybox 容器。</p>
<p>那么你知道，为什么 Docker 会选择使用 Golang 来开发吗？思考后，把你的想法写在留言区。</p>
<p>下一课时我将为你全面剖析 gocker 的源码以及它的实现原理，让你能够自己动手把它写出来，到时见。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;&#32;文件存储驱动：OverlayFS&#32;文件系统原理及生产环境的最佳配置.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a1a097f645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
