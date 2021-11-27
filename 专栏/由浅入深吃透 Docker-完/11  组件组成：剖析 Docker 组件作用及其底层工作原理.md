<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11  组件组成：剖析 Docker 组件作用及其底层工作原理.md</title>
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

                    <a class="current-tab" href="11&#32;&#32;组件组成：剖析&#32;Docker&#32;组件作用及其底层工作原理.md">11  组件组成：剖析 Docker 组件作用及其底层工作原理.md</a>
                    

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
                        <div><h1>11  组件组成：剖析 Docker 组件作用及其底层工作原理</h1>
<p>首先我们来回顾一下 Docker 的组件构成。</p>
<h3>Docker 的组件构成</h3>
<p>Docker 整体架构采用 C/S（客户端 / 服务器）模式，主要由客户端和服务端两大部分组成。客户端负责发送操作指令，服务端负责接收和处理指令。客户端和服务端通信有多种方式，即可以在同一台机器上通过<code>UNIX</code>套接字通信，也可以通过网络连接远程通信。</p>
<p><img src="assets/CgqCHl9rFtSAPGOeAADIK4E6wrc522.png" alt="image.png" /></p>
<p>图1 Docker 整体架构图</p>
<p>从整体架构可知，Docker 组件大体分为 Docker 相关组件，containerd 相关组件和容器运行时相关组件。下面我们深入剖析下各个组件。</p>
<h3>Docker 组件剖析</h3>
<p>Docker 到底有哪些组件呢？我们可以在 Docker 安装路径下执行 ls 命令，这样可以看到以下与 Docker 有关的组件。</p>
<pre><code>-rwxr-xr-x 1 root root 27941976 Dec 12  2019 containerd

-rwxr-xr-x 1 root root  4964704 Dec 12  2019 containerd-shim

-rwxr-xr-x 1 root root 15678392 Dec 12  2019 ctr

-rwxr-xr-x 1 root root 50683148 Dec 12  2019 docker

-rwxr-xr-x 1 root root   764144 Dec 12  2019 docker-init

-rwxr-xr-x 1 root root  2837280 Dec 12  2019 docker-proxy

-rwxr-xr-x 1 root root 54320560 Dec 12  2019 dockerd

-rwxr-xr-x 1 root root  7522464 Dec 12  2019 runc
</code></pre>
<p>这些组件根据工作职责可以分为以下三大类。</p>
<ol>
<li>Docker 相关的组件：docker、dockerd、docker-init 和 docker-proxy</li>
<li>containerd 相关的组件：containerd、containerd-shim 和 ctr</li>
<li>容器运行时相关的组件：runc</li>
</ol>
<p>下面我们就逐一了解。</p>
<h4>Docker 相关的组件</h4>
<p><strong>（1）docker</strong></p>
<p>docker 是 Docker 客户端的一个完整实现，它是一个二进制文件，对用户可见的操作形式为 docker 命令，通过 docker 命令可以完成所有的 Docker 客户端与服务端的通信（还可以通过 REST API、SDK 等多种形式与 Docker 服务端通信）。</p>
<p>Docker 客户端与服务端的交互过程是：docker 组件向服务端发送请求后，服务端根据请求执行具体的动作并将结果返回给 docker，docker 解析服务端的返回结果，并将结果通过命令行标准输出展示给用户。这样一次完整的客户端服务端请求就完成了。</p>
<p><strong>（2）dockerd</strong></p>
<p>dockerd 是 Docker 服务端的后台常驻进程，用来接收客户端发送的请求，执行具体的处理任务，处理完成后将结果返回给客户端。</p>
<p>Docker 客户端可以通过多种方式向 dockerd 发送请求，我们常用的 Docker 客户端与 dockerd 的交互方式有三种。</p>
<ul>
<li>通过 UNIX 套接字与服务端通信：配置格式为unix://socket_path，默认 dockerd 生成的 socket 文件路径为 /var/run/docker.sock，该文件只有 root 用户或者 docker 用户组的用户才可以访问，这就是为什么 Docker 刚安装完成后只有 root 用户才能使用 docker 命令的原因。</li>
<li>通过 TCP 与服务端通信：配置格式为tcp://host:port，通过这种方式可以实现客户端远程连接服务端，但是在方便的同时也带有安全隐患，因此在生产环境中如果你要使用 TCP 的方式与 Docker 服务端通信，推荐使用 TLS 认证，可以通过设置 Docker 的 TLS 相关参数，来保证数据传输的安全。</li>
<li>通过文件描述符的方式与服务端通信：配置格式为：fd://这种格式一般用于 systemd 管理的系统中。</li>
</ul>
<p>Docker 客户端和服务端的通信形式必须保持一致，否则将无法通信，只有当 dockerd 监听了 UNIX 套接字客户端才可以使用 UNIX 套接字的方式与服务端通信，UNIX 套接字也是 Docker 默认的通信方式，如果你想要通过远程的方式访问 dockerd，可以在 dockerd 启动的时候添加 -H 参数指定监听的 HOST 和 PORT。</p>
<p><strong>（3）docker-init</strong></p>
<p>如果你熟悉 Linux 系统，你应该知道在 Linux 系统中，1 号进程是 init 进程，是所有进程的父进程。主机上的进程出现问题时，init 进程可以帮我们回收这些问题进程。同样的，在容器内部，当我们自己的业务进程没有回收子进程的能力时，在执行 docker run 启动容器时可以添加 --init 参数，此时 Docker 会使用 docker-init 作为1号进程，帮你管理容器内子进程，例如回收僵尸进程等。</p>
<p>下面我们通过启动一个 busybox 容器来演示下：</p>
<pre><code>$ docker run -it busybox sh

/ # ps aux

PID   USER     TIME  COMMAND

    1 root      0:00 sh

    6 root      0:00 ps aux

/ #
</code></pre>
<p>可以看到容器启动时如果没有添加 --init 参数，1 号进程就是 sh 进程。</p>
<p>我们使用 Crtl + D 退出当前容器，重新启动一个新的容器并添加 --init 参数，然后看下进程：</p>
<pre><code>$ docker run -it --init busybox sh

/ # ps aux

PID   USER     TIME  COMMAND

    1 root      0:00 /sbin/docker-init -- sh

    6 root      0:00 sh

    7 root      0:00 ps aux
</code></pre>
<p>可以看到此时容器内的 1 号进程已经变为 /sbin/docker-init，而不再是 sh 了。</p>
<p><strong>（4）docker-proxy</strong></p>
<p>docker-proxy 主要是用来做端口映射的。当我们使用 docker run 命令启动容器时，如果使用了 -p 参数，docker-proxy 组件就会把容器内相应的端口映射到主机上来，底层是依赖于 iptables 实现的。</p>
<p>下面我们通过一个实例演示下。</p>
<p>使用以下命令启动一个 nginx 容器并把容器的 80 端口映射到主机的 8080 端口。</p>
<pre><code>$ docker run --name=nginx -d -p 8080:80 nginx
</code></pre>
<p>然后通过以下命令查看一下启动的容器 IP：</p>
<pre><code>$ docker inspect --format '{{ .NetworkSettings.IPAddress }}' nginx

172.17.0.2
</code></pre>
<p>可以看到，我们启动的 nginx 容器 IP 为 172.17.0.2。</p>
<p>此时，我们使用 ps 命令查看一下主机上是否有 docker-proxy 进程：</p>
<pre><code>$ sudo ps aux |grep docker-proxy

root      9100  0.0  0.0 290772  9160 ?        Sl   07:48   0:00 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 8080 -container-ip 172.17.0.2 -container-port 80

root      9192  0.0  0.0 112784   992 pts/0    S+   07:51   0:00 grep --color=auto docker-proxy
</code></pre>
<p>可以看到当我们启动一个容器时需要端口映射时， Docker 为我们创建了一个 docker-proxy 进程，并且通过参数把我们的容器 IP 和端口传递给 docker-proxy 进程，然后 docker-proxy 通过 iptables 实现了 nat 转发。</p>
<p>我们通过以下命令查看一下主机上 iptables nat 表的规则：</p>
<pre><code>$  sudo iptables -L -nv -t nat

Chain PREROUTING (policy ACCEPT 35 packets, 2214 bytes)

 pkts bytes target     prot opt in     out     source               destination

  398 21882 DOCKER     all  --  *      *       0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT 35 packets, 2214 bytes)

 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 1 packets, 76 bytes)

 pkts bytes target     prot opt in     out     source               destination

    0     0 DOCKER     all  --  *      *       0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT 1 packets, 76 bytes)

 pkts bytes target     prot opt in     out     source               destination

    0     0 MASQUERADE  all  --  *      !docker0  172.17.0.0/16        0.0.0.0/0

    0     0 MASQUERADE  tcp  --  *      *       172.17.0.2           172.17.0.2           tcp dpt:80

Chain DOCKER (2 references)

 pkts bytes target     prot opt in     out     source               destination

    0     0 RETURN     all  --  docker0 *       0.0.0.0/0            0.0.0.0/0

    0     0 DNAT       tcp  --  !docker0 *       0.0.0.0/0            0.0.0.0/0            tcp dpt:8080 to:172.17.0.2:80
</code></pre>
<p>通过最后一行规则我们可以得知，当我们访问主机的 8080 端口时，iptables 会把流量转发到 172.17.0.2 的 80 端口，从而实现了我们从主机上可以直接访问到容器内的业务。</p>
<p>我们通过 curl 命令访问一下 nginx 容器：</p>
<pre><code>$ curl http://localhost:8080

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

&lt;title&gt;Welcome to nginx!&lt;/title&gt;

&lt;style&gt;

    body {

        width: 35em;

        margin: 0 auto;

        font-family: Tahoma, Verdana, Arial, sans-serif;

    }

&lt;/style&gt;

&lt;/head&gt;

&lt;body&gt;

&lt;h1&gt;Welcome to nginx!&lt;/h1&gt;

&lt;p&gt;If you see this page, the nginx web server is successfully installed and

working. Further configuration is required.&lt;/p&gt;

&lt;p&gt;For online documentation and support please refer to

&lt;a href=&quot;http://nginx.org/&quot;&gt;nginx.org&lt;/a&gt;.&lt;br/&gt;

Commercial support is available at

&lt;a href=&quot;http://nginx.com/&quot;&gt;nginx.com&lt;/a&gt;.&lt;/p&gt;

&lt;p&gt;&lt;em&gt;Thank you for using nginx.&lt;/em&gt;&lt;/p&gt;

&lt;/body&gt;

&lt;/html&gt;
</code></pre>
<p>通过上面的输出可以得知我们已经成功访问到了 nginx 容器。</p>
<p>总体来说，docker 是官方实现的标准客户端，dockerd 是 Docker 服务端的入口，负责接收客户端发送的指令并返回相应结果，而 docker-init 在业务主进程没有进程回收功能时则十分有用，docker-proxy 组件则是实现 Docker 网络访问的重要组件。</p>
<p>了解完 docker 相关的组件，下面我来介绍下 containerd 相关的组件。</p>
<h4>containerd 相关的组件</h4>
<p><strong>（1）containerd</strong></p>
<p><a href="https://github.com/containerd/containerd">containerd</a> 组件是从 Docker 1.11 版本正式从 dockerd 中剥离出来的，它的诞生完全遵循 OCI 标准，是容器标准化后的产物。containerd 完全遵循了 OCI 标准，并且是完全社区化运营的，因此被容器界广泛采用。</p>
<p>containerd 不仅负责容器生命周期的管理，同时还负责一些其他的功能：</p>
<ul>
<li>镜像的管理，例如容器运行前从镜像仓库拉取镜像到本地；</li>
<li>接收 dockerd 的请求，通过适当的参数调用 runc 启动容器；</li>
<li>管理存储相关资源；</li>
<li>管理网络相关资源。</li>
</ul>
<p>containerd 包含一个后台常驻进程，默认的 socket 路径为 /run/containerd/containerd.sock，dockerd 通过 UNIX 套接字向 containerd 发送请求，containerd 接收到请求后负责执行相关的动作并把执行结果返回给 dockerd。</p>
<p>如果你不想使用 dockerd，也可以直接使用 containerd 来管理容器，由于 containerd 更加简单和轻量，生产环境中越来越多的人开始直接使用 containerd 来管理容器。</p>
<p><strong>（2）containerd-shim</strong></p>
<p>containerd-shim 的意思是垫片，类似于拧螺丝时夹在螺丝和螺母之间的垫片。containerd-shim 的主要作用是将 containerd 和真正的容器进程解耦，使用 containerd-shim 作为容器进程的父进程，从而实现重启 containerd 不影响已经启动的容器进程。</p>
<p><strong>（3）ctr</strong></p>
<p>ctr 实际上是 containerd-ctr，它是 containerd 的客户端，主要用来开发和调试，在没有 dockerd 的环境中，ctr 可以充当 docker 客户端的部分角色，直接向 containerd 守护进程发送操作容器的请求。</p>
<p>了解完 containerd 相关的组件，我们来了解一下容器的真正运行时 runc。</p>
<h4>容器运行时组件runc</h4>
<p>runc 是一个标准的 OCI 容器运行时的实现，它是一个命令行工具，可以直接用来创建和运行容器。</p>
<p>下面我们通过一个实例来演示一下 runc 的神奇之处。</p>
<p>第一步，准备容器运行时文件：进入 /home/centos 目录下，创建 runc 文件夹，并导入 busybox 镜像文件。</p>
<pre><code> $ cd /home/centos

 ## 创建 runc 运行根目录

 $ mkdir runc

 ## 导入 rootfs 镜像文件

 $ mkdir rootfs &amp;&amp; docker export $(docker create busybox) | tar -C rootfs -xvf -
</code></pre>
<p>第二步，生成 runc config 文件。我们可以使用 runc spec 命令根据文件系统生成对应的 config.json 文件。命令如下：</p>
<pre><code>$ runc spec
</code></pre>
<p>此时会在当前目录下生成 config.json 文件，我们可以使用 cat 命令查看一下 config.json 的内容：</p>
<pre><code>$ cat config.json

{

	&quot;ociVersion&quot;: &quot;1.0.1-dev&quot;,

	&quot;process&quot;: {

		&quot;terminal&quot;: true,

		&quot;user&quot;: {

			&quot;uid&quot;: 0,

			&quot;gid&quot;: 0

		},

		&quot;args&quot;: [

			&quot;sh&quot;

		],

		&quot;env&quot;: [

			&quot;PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin&quot;,

			&quot;TERM=xterm&quot;

		],

		&quot;cwd&quot;: &quot;/&quot;,

		&quot;capabilities&quot;: {

			&quot;bounding&quot;: [

				&quot;CAP_AUDIT_WRITE&quot;,

				&quot;CAP_KILL&quot;,

				&quot;CAP_NET_BIND_SERVICE&quot;

			],

			&quot;effective&quot;: [

				&quot;CAP_AUDIT_WRITE&quot;,

				&quot;CAP_KILL&quot;,

				&quot;CAP_NET_BIND_SERVICE&quot;

			],

			&quot;inheritable&quot;: [

				&quot;CAP_AUDIT_WRITE&quot;,

				&quot;CAP_KILL&quot;,

				&quot;CAP_NET_BIND_SERVICE&quot;

			],

			&quot;permitted&quot;: [

				&quot;CAP_AUDIT_WRITE&quot;,

				&quot;CAP_KILL&quot;,

				&quot;CAP_NET_BIND_SERVICE&quot;

			],

			&quot;ambient&quot;: [

				&quot;CAP_AUDIT_WRITE&quot;,

				&quot;CAP_KILL&quot;,

				&quot;CAP_NET_BIND_SERVICE&quot;

			]

		},

		&quot;rlimits&quot;: [

			{

				&quot;type&quot;: &quot;RLIMIT_NOFILE&quot;,

				&quot;hard&quot;: 1024,

				&quot;soft&quot;: 1024

			}

		],

		&quot;noNewPrivileges&quot;: true

	},

	&quot;root&quot;: {

		&quot;path&quot;: &quot;rootfs&quot;,

		&quot;readonly&quot;: true

	},

	&quot;hostname&quot;: &quot;runc&quot;,

	&quot;mounts&quot;: [

		{

			&quot;destination&quot;: &quot;/proc&quot;,

			&quot;type&quot;: &quot;proc&quot;,

			&quot;source&quot;: &quot;proc&quot;

		},

		{

			&quot;destination&quot;: &quot;/dev&quot;,

			&quot;type&quot;: &quot;tmpfs&quot;,

			&quot;source&quot;: &quot;tmpfs&quot;,

			&quot;options&quot;: [

				&quot;nosuid&quot;,

				&quot;strictatime&quot;,

				&quot;mode=755&quot;,

				&quot;size=65536k&quot;

			]

		},

		{

			&quot;destination&quot;: &quot;/dev/pts&quot;,

			&quot;type&quot;: &quot;devpts&quot;,

			&quot;source&quot;: &quot;devpts&quot;,

			&quot;options&quot;: [

				&quot;nosuid&quot;,

				&quot;noexec&quot;,

				&quot;newinstance&quot;,

				&quot;ptmxmode=0666&quot;,

				&quot;mode=0620&quot;,

				&quot;gid=5&quot;

			]

		},

		{

			&quot;destination&quot;: &quot;/dev/shm&quot;,

			&quot;type&quot;: &quot;tmpfs&quot;,

			&quot;source&quot;: &quot;shm&quot;,

			&quot;options&quot;: [

				&quot;nosuid&quot;,

				&quot;noexec&quot;,

				&quot;nodev&quot;,

				&quot;mode=1777&quot;,

				&quot;size=65536k&quot;

			]

		},

		{

			&quot;destination&quot;: &quot;/dev/mqueue&quot;,

			&quot;type&quot;: &quot;mqueue&quot;,

			&quot;source&quot;: &quot;mqueue&quot;,

			&quot;options&quot;: [

				&quot;nosuid&quot;,

				&quot;noexec&quot;,

				&quot;nodev&quot;

			]

		},

		{

			&quot;destination&quot;: &quot;/sys&quot;,

			&quot;type&quot;: &quot;sysfs&quot;,

			&quot;source&quot;: &quot;sysfs&quot;,

			&quot;options&quot;: [

				&quot;nosuid&quot;,

				&quot;noexec&quot;,

				&quot;nodev&quot;,

				&quot;ro&quot;

			]

		},

		{

			&quot;destination&quot;: &quot;/sys/fs/cgroup&quot;,

			&quot;type&quot;: &quot;cgroup&quot;,

			&quot;source&quot;: &quot;cgroup&quot;,

			&quot;options&quot;: [

				&quot;nosuid&quot;,

				&quot;noexec&quot;,

				&quot;nodev&quot;,

				&quot;relatime&quot;,

				&quot;ro&quot;

			]

		}

	],

	&quot;linux&quot;: {

		&quot;resources&quot;: {

			&quot;devices&quot;: [

				{

					&quot;allow&quot;: false,

					&quot;access&quot;: &quot;rwm&quot;

				}

			]

		},

		&quot;namespaces&quot;: [

			{

				&quot;type&quot;: &quot;pid&quot;

			},

			{

				&quot;type&quot;: &quot;network&quot;

			},

			{

				&quot;type&quot;: &quot;ipc&quot;

			},

			{

				&quot;type&quot;: &quot;uts&quot;

			},

			{

				&quot;type&quot;: &quot;mount&quot;

			}

		],

		&quot;maskedPaths&quot;: [

			&quot;/proc/acpi&quot;,

			&quot;/proc/asound&quot;,

			&quot;/proc/kcore&quot;,

			&quot;/proc/keys&quot;,

			&quot;/proc/latency_stats&quot;,

			&quot;/proc/timer_list&quot;,

			&quot;/proc/timer_stats&quot;,

			&quot;/proc/sched_debug&quot;,

			&quot;/sys/firmware&quot;,

			&quot;/proc/scsi&quot;

		],

		&quot;readonlyPaths&quot;: [

			&quot;/proc/bus&quot;,

			&quot;/proc/fs&quot;,

			&quot;/proc/irq&quot;,

			&quot;/proc/sys&quot;,

			&quot;/proc/sysrq-trigger&quot;

		]

	}

}
</code></pre>
<p>config.json 文件定义了 runc 启动容器时的一些配置，如根目录的路径，文件挂载路径等配置。
第三步，使用 runc 启动容器。我们可以使用 runc run 命令直接启动 busybox 容器。</p>
<pre><code>$ runc run busybox

/ #
</code></pre>
<p>此时，我们已经创建并启动了一个 busybox 容器。</p>
<p>我们新打开一个命令行窗口，可以使用 run list 命令看到刚才启动的容器。</p>
<pre><code>$ cd /home/centos/runc/

$ runc list

D          PID         STATUS      BUNDLE              CREATED                          OWNER

busybox     9778        running     /home/centos/runc   2020-09-06T09:25:32.441957273Z   root
</code></pre>
<p>通过上面的输出，我们可以看到，当前已经有一个 busybox 容器处于运行状态。</p>
<p>总体来说，Docker 的组件虽然很多，但每个组件都有自己清晰的工作职责，Docker 相关的组件负责发送和接受 Docker 请求，contianerd 相关的组件负责管理容器的生命周期，而 runc 负责真正意义上创建和启动容器。这些组件相互配合，才使得 Docker 顺利完成了容器的管理工作。</p>
<h3>总结</h3>
<p>到此，相信你已经完全掌握了 Docker 的组件构成，各个组件的作用和工作原理。本节课时的重点我帮你总结如下。</p>
<p><img src="assets/Ciqc1F9y4vGAVzmAAADk1nlHpUA424.png" alt="7.png" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;&#32;资源限制：如何通过&#32;Cgroups&#32;机制实现资源限制？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;&#32;网络模型：剖析&#32;Docker&#32;网络实现及&#32;Libnetwork&#32;底层原理.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359ea1bba645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
