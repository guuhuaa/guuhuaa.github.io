<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>12  网络模型：剖析 Docker 网络实现及 Libnetwork 底层原理.md</title>
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

                    <a class="current-tab" href="12&#32;&#32;网络模型：剖析&#32;Docker&#32;网络实现及&#32;Libnetwork&#32;底层原理.md">12  网络模型：剖析 Docker 网络实现及 Libnetwork 底层原理.md</a>
                    

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
                        <div><h1>12  网络模型：剖析 Docker 网络实现及 Libnetwork 底层原理</h1>
<p>前几课时，我介绍了 Linux 的 Namespace 和 Cgroups 技术，利用这两项技术可以实现各种资源的隔离和主机资源的限制，让我们的容器可以像一台虚拟机一样。但这时我们的容器就像一台未联网的电脑，不能被外部访问到，也不能主动与外部通信，这样的容器只能做一些离线的处理任务，无法通过外部访问。所以今天这一讲，我将介绍 Docker 网络相关的知识，使 Docker 容器接通网络。</p>
<h3>容器网络发展史</h3>
<p>提起 Docker 网络，我们不得不从容器战争说起。Docker 从 2013 年诞生，到后来逐渐成为了容器的代名词，然而 Docker 的野心也不止于此，它还想在更多的领域独占鳌头，比如制定容器的网络和存储标准。</p>
<p>于是 Docker 从 1.7 版本开始，便把网络和存储从 Docker 中正式以插件的形式剥离开来，并且分别为其定义了标准，Docker 定义的网络模型标准称之为 CNM (Container Network Model) 。</p>
<blockquote>
<p>Docker 推出 CNM 的同时，CoreOS 推出了 CNI（Container Network Model）。起初，以 Kubernetes 为代表的容器编排阵营考虑过使用 CNM 作为容器的网络标准，但是后来由于很多技术和非技术原因（如果你对详细原因感兴趣，可以参考这篇博客），Kubernetes 决定支持 CoreOS 推出的容器网络标准 CNI。</p>
</blockquote>
<p>从此，容器的网络标准便分为两大阵营，一个是以 Docker 公司为代表的 CNM，另一个便是以 Google、Kubernetes、CoreOS 为代表的 CNI 网络标准。</p>
<h3>CNM</h3>
<p>CNM (Container Network Model) 是 Docker 发布的容器网络标准，意在规范和指定容器网络发展标准，CNM 抽象了容器的网络接口 ，使得只要满足 CNM 接口的网络方案都可以接入到 Docker 容器网络，更好地满足了用户网络模型多样化的需求。</p>
<p>CNM 只是定义了网络标准，对于底层的具体实现并不太关心，这样便解耦了容器和网络，使得容器的网络模型更加灵活。</p>
<p>CNM 定义的网络标准包含三个重要元素。</p>
<ul>
<li><strong>沙箱（Sandbox）</strong>：沙箱代表了一系列网络堆栈的配置，其中包含路由信息、网络接口等网络资源的管理，沙箱的实现通常是 Linux 的 Net Namespace，但也可以通过其他技术来实现，比如 <a href="https://zh.wikipedia.org/wiki/FreeBSD_jail">FreeBSD jail</a> 等。</li>
<li><strong>接入点（Endpoint）</strong>：接入点将沙箱连接到网络中，代表容器的网络接口，接入点的实现通常是 Linux 的 veth 设备对。</li>
<li><strong>网络（Network</strong>）：网络是一组可以互相通信的接入点，它将多接入点组成一个子网，并且多个接入点之间可以相互通信。</li>
</ul>
<p>CNM 的三个要素基本抽象了所有网络模型，使得网络模型的开发更加规范。</p>
<p>为了更好地构建容器网络标准，Docker 团队把网络功能从 Docker 中剥离出来，成为独立的项目 libnetwork，它通过插件的形式为 Docker 提供网络功能。Libnetwork 是开源的，使用 Golang 编写，它完全遵循 CNM 网络规范，是 CNM 的官方实现。Libnetwork 的工作流程也是完全围绕 CNM 的三个要素进行的，下面我们来详细了解一下 Libnetwork 是如何围绕 CNM 的三要素工作的。</p>
<h3>Libnetwork 的工作流程</h3>
<p>Libnetwork 是 Docker 启动容器时，用来为 Docker 容器提供网络接入功能的插件，它可以让 Docker 容器顺利接入网络，实现主机和容器网络的互通。下面，我们来详细了解一下 Libnetwork 是如何为 Docker 容器提供网络的。</p>
<p>第一步：Docker 通过调用 libnetwork.New 函数来创建 NetworkController 实例。NetworkController 是一个接口类型，提供了各种接口，代码如下：</p>
<pre><code>type NetworkController interface {

   // 创建一个新的网络。 options 参数用于指定特性类型的网络选项。

   NewNetwork(networkType, name string, id string, options ...NetworkOption) (Network, error)

   // ... 此次省略部分接口

}
</code></pre>
<p>第二步：通过调用 NewNetwork 函数创建指定名称和类型的 Network，其中 Network 也是接口类型，代码如下:</p>
<pre><code>type Network interface {

   // 为该网络创建一个具有唯一指定名称的接入点（Endpoint）

   CreateEndpoint(name string, options ...EndpointOption) (Endpoint, error)

   // 删除网络

   Delete() error

// ... 此次省略部分接口

}
</code></pre>
<p>第三步：通过调用 CreateEndpoint 来创建接入点（Endpoint）。在 CreateEndpoint 函数中为容器分配了 IP 和网卡接口。其中 Endpoint 也是接口类型，代码如下：</p>
<pre><code>// Endpoint 表示网络和沙箱之间的逻辑连接。

type Endpoint interface {

   // 将沙箱连接到接入点，并将为接入点分配的网络资源填充到沙箱中。

   // the network resources allocated for the endpoint.

   Join(sandbox Sandbox, options ...EndpointOption) error

   // 删除接入点

   Delete(force bool) error

   // ... 此次省略部分接口

}
</code></pre>
<p>第四步：调用 NewSandbox 来创建容器沙箱，主要是初始化 Namespace 相关的资源。</p>
<p>第五步：调用 Endpoint 的 Join 函数将沙箱和网络接入点关联起来，此时容器就加入了 Docker 网络并具备了网络访问能力。</p>
<p>Libnetwork 基于以上工作流程可以构建出多种网络模式，以满足我们的在不同场景下的需求，下面我们来详细了解一下 Libnetwork 提供的常见的四种网络模式。</p>
<h3>Libnetwork 常见网络模式</h3>
<p>Libnetwork 比较典型的网络模式主要有四种，这四种网络模式基本满足了我们单机容器的所有场景。</p>
<ol>
<li>null 空网络模式：可以帮助我们构建一个没有网络接入的容器环境，以保障数据安全。</li>
<li>bridge 桥接模式：可以打通容器与容器间网络通信的需求。</li>
<li>host 主机网络模式：可以让容器内的进程共享主机网络，从而监听或修改主机网络。</li>
<li>container 网络模式：可以将两个容器放在同一个网络命名空间内，让两个业务通过 localhost 即可实现访问。</li>
</ol>
<p>下面我们对 libnetwork 的四种网络模式逐一讲解：</p>
<h4>（1）null 空网络模式</h4>
<p>有时候，我们需要处理一些保密数据，出于安全考虑，我们需要一个隔离的网络环境执行一些纯计算任务。这时候 null 网络模式就派上用场了，这时候我们的容器就像一个没有联网的电脑，处于一个相对较安全的环境，确保我们的数据不被他人从网络窃取。</p>
<p>使用 Docker 创建 null 空网络模式的容器时，容器拥有自己独立的 Net Namespace，但是此时的容器并没有任何网络配置。在这种模式下，Docker 除了为容器创建了 Net Namespace 外，没有创建任何网卡接口、IP 地址、路由等网络配置。我们可以一起来验证下。</p>
<p>我们使用 <code>docker run</code> 命令启动时，添加 --net=none 参数启动一个空网络模式的容器，命令如下：</p>
<pre><code>$ docker run --net=none -it busybox

/ #
</code></pre>
<p>容器启动后，我们使用 <code>ifconfig</code> 命令查看一下容器内网络配置信息：</p>
<pre><code>/ # ifconfig

lo        Link encap:Local Loopback

          inet addr:127.0.0.1  Mask:255.0.0.0

          UP LOOPBACK RUNNING  MTU:65536  Metric:1

          RX packets:0 errors:0 dropped:0 overruns:0 frame:0

          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0

          collisions:0 txqueuelen:1000

          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
</code></pre>
<p>可以看到容器内除了 Net Namespace 自带的 lo 网卡并没有创建任何虚拟网卡，然后我们再使用 <code>route -n</code> 命令查看一下容器内的路由信息:</p>
<pre><code>/ # route -n

Kernel IP routing table

Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
</code></pre>
<p>可以看到，容器内也并没有配置任何路由信息。</p>
<h4>（2）bridge 桥接模式</h4>
<p>Docker 的 bridge 网络是启动容器时默认的网络模式，使用 bridge 网络可以实现容器与容器的互通，可以从一个容器直接通过容器 IP 访问到另外一个容器。同时使用 bridge 网络可以实现主机与容器的互通，我们在容器内启动的业务，可以从主机直接请求。</p>
<p>在介绍 Docker 的 bridge 桥接模式前，我们需要先了解一下 Linux 的 veth 和 bridge 相关的技术，因为 Docker 的 bridge 模式正是由这两种技术实现的。</p>
<ul>
<li>Linux veth</li>
</ul>
<p>veth 是 Linux 中的虚拟设备接口，veth 都是成对出现的，它在容器中，通常充当一个桥梁。veth 可以用来连接虚拟网络设备，例如 veth 可以用来连通两个 Net Namespace，从而使得两个 Net Namespace 之间可以互相访问。</p>
<ul>
<li>Linux bridge</li>
</ul>
<p>Linux bridge 是一个虚拟设备，是用来连接网络的设备，相当于物理网络环境中的交换机。Linux bridge 可以用来转发两个 Net Namespace 内的流量。</p>
<ul>
<li>veth 与 bridge 的关系</li>
</ul>
<p><img src="assets/Ciqc1F9y8IKAa-1NAABjDM-2kBk665.png" alt="Lark20200929-162853.png" /></p>
<p>通过图 1 ，我们可以看到，bridge 就像一台交换机，而 veth 就像一根网线，通过交换机和网线可以把两个不同 Net Namespace 的容器连通，使得它们可以互相通信。</p>
<p>Docker 的 bridge 模式也是这种原理。Docker 启动时，libnetwork 会在主机上创建 docker0 网桥，docker0 网桥就相当于图 1 中的交换机，而 Docker 创建出的 brige 模式的容器则都会连接 docker0 上，从而实现网络互通。</p>
<p><strong>bridge 桥接模式是 Docker 的默认网络模式，当我们创建容器时不指定任何网络模式，Docker 启动容器默认的网络模式为 bridge。</strong></p>
<h4>（3）host 主机网络模式</h4>
<p>容器内的网络并不是希望永远跟主机是隔离的，有些基础业务需要创建或更新主机的网络配置，我们的程序必须以主机网络模式运行才能够修改主机网络，这时候就需要用到 Docker 的 host 主机网络模式。</p>
<p>使用 host 主机网络模式时：</p>
<ul>
<li>libnetwork 不会为容器创建新的网络配置和 Net Namespace。</li>
<li>Docker 容器中的进程直接共享主机的网络配置，可以直接使用主机的网络信息，此时，在容器内监听的端口，也将直接占用到主机的端口。</li>
<li>除了网络共享主机的网络外，其他的包括进程、文件系统、主机名等都是与主机隔离的。</li>
</ul>
<p>host 主机网络模式通常适用于想要使用主机网络，但又不想把运行环境直接安装到主机上的场景中。例如我想在主机上运行一个 busybox 服务，但又不想直接把 busybox 安装到主机上污染主机环境，此时我可以使用以下命令启动一个主机网络模式的 busybox 镜像：</p>
<pre><code>$ docker run -it --net=host busybox

/ #
</code></pre>
<p>然后我们使用<code>ip a</code> 命令查看一下容器内的网络环境：</p>
<pre><code>/ # ip a

1: lo: &lt;LOOPBACK,UP,LOWER\_UP&gt; mtu 65536 qdisc noqueue qlen 1000

link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

inet 127.0.0.1/8 scope host lo

valid\_lft forever preferred\_lft forever

inet6 ::1/128 scope host

valid\_lft forever preferred\_lft forever

2: eth0: &lt;BROADCAST,MULTICAST,UP,LOWER\_UP&gt; mtu 1500 qdisc pfifo\_fast qlen 1000

link/ether 02:11:b0:14:01:0c brd ff:ff:ff:ff:ff:ff

inet 172.20.1.11/24 brd 172.20.1.255 scope global dynamic eth0

valid\_lft 85785286sec preferred\_lft 85785286sec

inet6 fe80::11:b0ff:fe14:10c/64 scope link

valid\_lft forever preferred\_lft forever

3: docker0: \&lt;NO-CARRIER,BROADCAST,MULTICAST,UP&gt; mtu 1500 qdisc noqueue

link/ether 02:42:82:8d:a0:df brd ff:ff:ff:ff:ff:ff

inet 172.17.0.1/16 scope global docker0

valid\_lft forever preferred\_lft forever

inet6 fe80::42:82ff:fe8d:a0df/64 scope link

valid\_lft forever preferred\_lft forever
</code></pre>
<p>可以看到容器内的网络环境与主机完全一致。</p>
<h4>（4）container 网络模式</h4>
<p>container 网络模式允许一个容器共享另一个容器的网络命名空间。当两个容器需要共享网络，但其他资源仍然需要隔离时就可以使用 container 网络模式，例如我们开发了一个 http 服务，但又想使用 nginx 的一些特性，让 nginx 代理外部的请求然后转发给自己的业务，这时我们使用 container 网络模式将自己开发的服务和 nginx 服务部署到同一个网络命名空间中。</p>
<p>下面我举例说明。首先我们使用以下命令启动一个 busybox1 容器：</p>
<pre><code>$ docker run -d --name=busybox1 busybox sleep 3600
</code></pre>
<p>然后我们使用 <code>docker exec</code> 命令进入到 centos 容器中查看一下网络配置：</p>
<pre><code>$ docker exec -it busybox1 sh

/ # ifconfig

eth0 Link encap:Ethernet HWaddr 02:42:AC:11:00:02

inet addr:172.17.0.2 Bcast:172.17.255.255 Mask:255.255.0.0

UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1

RX packets:11 errors:0 dropped:0 overruns:0 frame:0

TX packets:0 errors:0 dropped:0 overruns:0 carrier:0

collisions:0 txqueuelen:0

RX bytes:906 (906.0 B) TX bytes:0 (0.0 B)

lo Link encap:Local Loopback

inet addr:127.0.0.1 Mask:255.0.0.0

UP LOOPBACK RUNNING MTU:65536 Metric:1

RX packets:0 errors:0 dropped:0 overruns:0 frame:0

TX packets:0 errors:0 dropped:0 overruns:0 carrier:0

collisions:0 txqueuelen:1000

RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
</code></pre>
<p>可以看到 busybox1 的 IP 地址为 172.17.0.2。</p>
<p>然后我们新打开一个命令行窗口，再启动一个 busybox2 容器，通过 container 网络模式连接到 busybox1 的网络，命令如下：</p>
<pre><code>$ docker run -it --net=container:busybox1 --name=busybox2 busybox sh

/ #
</code></pre>
<p>在 busybox2 容器内同样使用 ifconfig 命令查看一下容器内的网络配置：</p>
<pre><code>/ # ifconfig

eth0 Link encap:Ethernet HWaddr 02:42:AC:11:00:02

inet addr:172.17.0.2 Bcast:172.17.255.255 Mask:255.255.0.0

UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1

RX packets:14 errors:0 dropped:0 overruns:0 frame:0

TX packets:0 errors:0 dropped:0 overruns:0 carrier:0

collisions:0 txqueuelen:0

RX bytes:1116 (1.0 KiB) TX bytes:0 (0.0 B)

lo Link encap:Local Loopback

inet addr:127.0.0.1 Mask:255.0.0.0

UP LOOPBACK RUNNING MTU:65536 Metric:1

RX packets:0 errors:0 dropped:0 overruns:0 frame:0

TX packets:0 errors:0 dropped:0 overruns:0 carrier:0

collisions:0 txqueuelen:1000

RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
</code></pre>
<p>可以看到 busybox2 容器的网络 IP 也为 172.17.0.2，与 busybox1 的网络一致。</p>
<p>以上就是 Libnetwork 常见的四种网络模式，它们的作用及业务场景帮你总结如下：</p>
<p><img src="assets/Ciqc1F9y8HGAaH1iAAClKDUq5FY736.png" alt="Lark20200929-162901.png" /></p>
<h3>结语</h3>
<p>我上面有说到 Libnetwork 的工作流程是完全围绕 CNM 的三个要素进行的，CNM 制定标准之初不仅仅是为了单台主机上的容器互通，更多的是为了定义跨主机之间的容器通信标准。但是后来由于 Kubernetes 逐渐成为了容器编排的标准，而 Kubernetes 最终选择了 CNI 作为容器网络的定义标准（具体原因可以参考<a href="https://kubernetes.io/blog/2016/01/why-kubernetes-doesnt-use-libnetwork/">这里</a>），很遗憾 CNM 最终没有成为跨主机容器通信的标准，但是CNM 却为推动容器网络标准做出了重大贡献，且 Libnetwork 也是 Docker 的默认网络实现，提供了单独使用 Docker 容器时的多种网络接入功能。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="11&#32;&#32;组件组成：剖析&#32;Docker&#32;组件作用及其底层工作原理.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="13&#32;&#32;数据存储：剖析&#32;Docker&#32;卷与持久化数据存储的底层原理.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359ef2a51645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
