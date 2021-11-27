<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>21  如何使 Docker 和 Kubernetes 结合发挥容器的最大价值？.md</title>
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

                    <a class="current-tab" href="21&#32;&#32;如何使&#32;Docker&#32;和&#32;Kubernetes&#32;结合发挥容器的最大价值？.md">21  如何使 Docker 和 Kubernetes 结合发挥容器的最大价值？.md</a>
                    

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
                        <div><h1>21  如何使 Docker 和 Kubernetes 结合发挥容器的最大价值？</h1>
<p>Docker 虽然在容器领域有着不可撼动的地位，然而在容器的编排领域，却有着另外一个事实标准，那就是 Kubernetes。本课时，我就带你一起来认识下 Kubernetes。</p>
<h3>Kubernetes 的前生今世</h3>
<p>说起 Kubernetes，这一切还得从云计算这个词说起，云计算这个概念是 2006 年由 Google 提起的，近些年被提及的频率也越来越高。云计算从起初的概念演变为现在的 AWS、阿里云等实实在在的云产品（主要是虚拟机和相关的网络、存储服务），可见已经变得非常成熟和稳定。</p>
<p>正当大家以为云计算领域已经变成了以虚拟机为代表的云平台时，Docker 在 2013 年横空出世，Docker 提出了镜像、仓库等核心概念，规范了服务的交付标准，使得复杂服务的落地变得更加简单，之后 Docker 又定义了 OCI 标准，可以说在容器领域 Docker 已经成了事实的标准。</p>
<p>然而 Docker 诞生只是帮助我们定义了开发和交付标准，如果想要在生产环境中大批量的使用容器，还离不开的容器的编排技术。于是，在 2014 年 6 月 7 日，Kubernetes（Kubernetes 简称为 K8S，8 代表 ubernete 8个字母） 的第一个 commit（提交）拉开了容器编排标准定义的序幕。</p>
<p>Kubernetes 是舵手的意思，我们把 Docker 比喻成一个个集装箱，而 Kubernetes 正是运输这些集装箱的舵手。早期的 Kubernetes 主要参考 Google 内部的 Borg 系统，Kubernetes 刚刚诞生时，提出了 Pod、Sidecar 等概念，这些都是 Google 内部多年实战和沉淀所积累的精华。经过将近一年的沉淀和积累，Kubernetes 于 2015 年 7 月 21 日对外发布了第一个正式版本 v1.0，正式走入了大众的视线。</p>
<p>很荣幸，我也是在 2015 年下半年正式开始了 Kubernetes 和 Docker 的研发之路。时至今日，Kubernetes 经过 6 年的沉淀，已经成为了事实的编排技术标准。</p>
<p>接下来，我们就看来看看，究竟是什么样的架构使得 Kubernetes 在容器编排领域成为了王者？</p>
<h3>Kubernetes 架构</h3>
<p>Kubernetes 采用声明式 API 来工作，所有组件的运行过程都是异步的，整个工作过程大致为用户声明想要的状态，然后 Kubernetes 各个组件相互配合并且努力达到用户想要的状态。</p>
<p>Kubernetes 采用典型的主从架构，分为 Master 和 Node 两个角色。</p>
<ul>
<li>Mater 是 Kubernetes 集群的控制节点，负责整个集群的管理和控制功能。</li>
<li>Node 为工作节点，负责业务容器的生命周期管理。</li>
</ul>
<p>整体架构如下图：</p>
<p><img src="assets/Ciqc1F-k_FqAdHbtAAFVTi8cyOE246.png" alt="image" /></p>
<p>图 1 Kubernetes 架构图（来源：Kubernetes 官网）</p>
<h4>Master 节点</h4>
<p>Master 节点负责对集群中所有容器的调度，各种资源对象的控制，以及响应集群的所有请求。Master 节点包含三个重要的组件： kube-apiserver、kube-scheduler、kube-controller-manager。下面我对这三个组件逐一介绍。</p>
<ul>
<li><strong>kube-apiserver</strong></li>
</ul>
<p>kube-apiserver 主要负责提供 Kubernetes 的 API 服务，所有的组件都需要与 kube-apiserver 交互获取或者更新资源信息，它是 Kubernetes Master 中最前端组件。</p>
<p>kube-apiserver 的所有数据都存储在 <a href="https://etcd.io/">etcd</a> 中，etcd 是一种采用 Go 语言编写的高可用 Key-Value 数据库，由 CoreOS 开发。etcd 虽然不是 Kubernetes 的组件，但是它在 Kubernetes 中却扮演着至关重要的角色，它是 Kubernetes 的数据大脑。可以说 etcd 的稳定性直接关系着 Kubernetes 集群的稳定性，因此生产环境中 etcd 一定要部署多个实例以确保集群的高可用。</p>
<ul>
<li><strong>kube-scheduler</strong></li>
</ul>
<p>kube-scheduler 用于监听未被调度的 Pod，然后根据一定调度策略将 Pod 调度到合适的 Node 节点上运行。</p>
<ul>
<li><strong>kube-controller-manager</strong></li>
</ul>
<p>kube-controller-manager 负责维护整个集群的状态和资源的管理。例如多个副本数量的保证，Pod 的滚动更新等。每种资源的控制器都是一个独立协程。kube-controller-manager 实际上是一系列资源控制器的总称。</p>
<blockquote>
<p>为了保证 Kubernetes 集群的高可用，Master 组件需要部署在多个节点上，由于 Kubernetes 所有数据都存在于 etcd 中，Etcd 是基于 Raft 协议实现，因此生产环境中 Master 通常建议至少三个节点（如果你想要更高的可用性，可以使用 5 个或者 7 个节点）。</p>
</blockquote>
<h4>Node 节点</h4>
<p>Node 节点是 Kubernetes 的工作节点，负责运行业务容器。Node 节点主要包含两个组件 ：kubelet 和 kube-proxy。</p>
<ul>
<li><strong>kubelet</strong></li>
</ul>
<p>Kubelet 是在每个工作节点运行的代理，它负责管理容器的生命周期。Kubelet 通过监听分配到自己运行的主机上的 Pod 对象，确保这些 Pod 处于运行状态，并且负责定期检查 Pod 的运行状态，将 Pod 的运行状态更新到 Pod 对象中。</p>
<ul>
<li><strong>kube-proxy</strong></li>
</ul>
<p>Kube-proxy 是在每个工作节点的网络插件，它实现了 Kubernetes 的 <a href="https://kubernetes.io/docs/concepts/services-networking/service/">Service</a> 的概念。Kube-proxy 通过维护集群上的网络规则，实现集群内部可以通过负载均衡的方式访问到后端的容器。</p>
<p>Kubernetes 的成功不仅得益于其优秀的架构设计，更加重要的是 Kubernetes 提出了很多核心的概念，这些核心概念构成了容器编排的主要模型。</p>
<h3>Kubernetes 核心概念</h3>
<p>Kubernetes 这些概念是 Google 多年的技术沉淀和积累，理解 Kubernetes 的核心概念有助于我们更好的理解 Kubernetes 的设计理念。</p>
<h4>（1）集群</h4>
<p>集群是一组被 Kubernetes 统一管理和调度的节点，被 Kubernetes 纳管的节点可以是物理机或者虚拟机。集群其中一部分节点作为 Master 节点，负责集群状态的管理和协调，另一部分作为 Node 节点，负责执行具体的任务，实现用户服务的启停等功能。</p>
<h4>（2）标签（Label）</h4>
<p>Label 是一组键值对，每一个资源对象都会拥有此字段。Kubernetes 中使用 Label 对资源进行标记，然后根据 Label 对资源进行分类和筛选。</p>
<h4>（3）命名空间（Namespace）</h4>
<p>Kubernetes 中通过命名空间来实现资源的虚拟化隔离，将一组相关联的资源放到同一个命名空间内，避免不同租户的资源发生命名冲突，从逻辑上实现了多租户的资源隔离。</p>
<h4>（4）容器组（Pod）</h4>
<p>Pod 是 Kubernetes 中的最小调度单位，它由一个或多个容器组成，一个 Pod 内的容器共享相同的网络命名空间和存储卷。Pod 是真正的业务进程的载体，在 Pod 运行前，Kubernetes 会先启动一个 Pause 容器开辟一个网络命名空间，完成网络和存储相关资源的初始化，然后再运行业务容器。</p>
<h4>（5）部署（Deployment）</h4>
<p>Deployment 是一组 Pod 的抽象，通过 Deployment 控制器保障用户指定数量的容器副本正常运行，并且实现了滚动更新等高级功能，当我们需要更新业务版本时，Deployment 会按照我们指定策略自动的杀死旧版本的 Pod 并且启动新版本的 Pod。</p>
<h4>（6）状态副本集（StatefulSet）</h4>
<p>StatefulSet 和 Deployment 类似，也是一组 Pod 的抽象，但是 StatefulSet 主要用于有状态应用的管理，StatefulSet 生成的 Pod 名称是固定且有序的，确保每个 Pod 独一无二的身份标识。</p>
<h4>（7）守护进程集（DaemonSet）</h4>
<p>DaemonSet 确保每个 Node 节点上运行一个 Pod，当我们集群有新加入的 Node 节点时，Kubernetes 会自动帮助我们在新的节点上运行一个 Pod。一般用于日志采集，节点监控等场景。</p>
<h4>（8）任务（Job）</h4>
<p>Job 可以帮助我们创建一个 Pod 并且保证 Pod 的正常退出，如果 Pod 运行过程中出现了错误，Job 控制器可以帮助我们创建新的 Pod，直到 Pod 执行成功或者达到指定重试次数。</p>
<h4>（9）服务（Service）</h4>
<p>Service 是一组 Pod 访问配置的抽象。由于 Pod 的地址是动态变化的，我们不能直接通过 Pod 的 IP 去访问某个服务，Service 通过在主机上配置一定的网络规则，帮助我们实现通过一个固定的地址访问一组 Pod。</p>
<h4>（10）配置集（ConfigMap）</h4>
<p>ConfigMap 用于存放我们业务的配置信息，使用 Key-Value 的方式存放于 Kubernetes 中，使用 ConfigMap 可以帮助我们将配置数据和应用程序代码分开。</p>
<h4>（11）加密字典（Secret）</h4>
<p>Secret 用于存放我们业务的敏感配置信息，类似于 ConfigMap，使用 Key-Value 的方式存在于 Kubernetes 中，主要用于存放密码和证书等敏感信息。</p>
<p>了解完 Kubernetes 的架构和核心概念，你是不是已经迫不及待地想要体验下了。下面就让我们动手安装一个 Kubernetes 集群，来体验下 Kubernetes 的强大之处吧。</p>
<h3>安装 Kubernetes</h3>
<p>Kubernetes 目前已经支持在多种环境下安装，我们可以在公有云，私有云，甚至裸金属中安装 Kubernetes。下面，我们通过 minikube 来演示一下如何快速安装和启动一个 Kubernetes 集群，minikube 是官方提供的一个快速搭建本地 Kubernetes 集群的工具，主要用于本地开发和调试。</p>
<p>下面，我以 Linux 平台为例，演示一下如何使用 minikube 安装一个 Kubernetes 集群。</p>
<blockquote>
<p>如果你想要在其他平台使用 minikube 安装 Kubernetes，请参考官网<a href="https://minikube.sigs.k8s.io/docs/start/">安装教程</a>。
在使用 minikube 安装 Kubernetes 之前，请确保我们的机器已经正确安装并且启动 Docker。</p>
</blockquote>
<p>第一步，安装 minikube 和 kubectl。首先执行以下命令安装 minikube。</p>
<pre><code>$ curl -LO https://github.com/kubernetes/minikube/releases/download/v1.13.1/minikube-linux-amd64

$ sudo install minikube-linux-amd64 /usr/local/bin/minikube
</code></pre>
<p>Kubectl 是 Kubernetes 官方的命令行工具，可以实现对 Kubernetes 集群的管理和控制。
我们使用以下命令来安装 kubectl：</p>
<pre><code>$ curl -LO https://dl.k8s.io/v1.19.2/kubernetes-client-linux-amd64.tar.gz

$ tar -xvf kubernetes-client-linux-amd64.tar.gz

kubernetes/

kubernetes/client/

kubernetes/client/bin/

kubernetes/client/bin/kubectl

$ sudo install kubernetes/client/bin/kubectl /usr/local/bin/kubectl
</code></pre>
<p>第二步，安装 Kubernetes 集群。
执行以下命令使用 minikube 安装 Kubernetes 集群：</p>
<pre><code>$ minikube start
</code></pre>
<p>执行完上述命令后，minikube 会自动帮助我们创建并启动一个 Kubernetes 集群。命令输出如下，当命令行输出 Done 时，代表集群已经部署完成。</p>
<p><img src="assets/CgqCHl-lL_WABqFRAAE7sPUop9w125.png" alt="111.png" /></p>
<p>第三步，检查集群状态。集群安装成功后，我们可以使用以下命令检查 Kubernetes 集群是否成功启动。</p>
<pre><code>$ kubectl cluster-info

Kubernetes master is running at https://172.17.0.3:8443

KubeDNS is running at https://172.17.0.3:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
</code></pre>
<p>执行<code>kubectl cluster-info</code>命令后，输出 &quot;Kubernetes master is running&quot; 表示我们的集群已经成功运行。</p>
<blockquote>
<p>172.17.0.3 为演示环境机器的 IP 地址，这个 IP 会根据你的实际 IP 地址而变化。</p>
</blockquote>
<h3>创建第一个应用</h3>
<p>集群搭建好后，下面我们来试着使用 Kubernetes 来创建我们的第一个应用。</p>
<p>这里我们使用 Deployment 来定义应用的部署信息，使用 Service 暴露我们的应用到集群外部，从而使得我们的应用可以从外部访问到。</p>
<p>第一步，创建 deployment.yaml 文件，并且定义启动的副本数（replicas）为 3。</p>
<pre><code>apiVersion: apps/v1

kind: Deployment

metadata:

  name: hello-world

spec:

  replicas: 3

  selector:

    matchLabels:

      app: hello-world

  template:

    metadata:

      labels:

        app: hello-world

    spec:

      containers:

      - name: hello-world

        image: wilhelmguo/nginx-hello:v1

        ports:

        - containerPort: 80
</code></pre>
<p>第二步，发布部署文件到 Kubernetes 集群中。</p>
<pre><code>$ kubectl create -f deployment.yaml
</code></pre>
<p>部署发布完成后，我们可以使用 kubectl 来查看一下 Pod 是否被成功启动。</p>
<pre><code>$ kubectl get pod -o wide

NAME                           READY   STATUS    RESTARTS   AGE     IP           NODE       NOMINATED NODE   READINESS GATES

hello-world-57968f9979-xbmzt   1/1     Running   0          3m19s   172.18.0.7   minikube   &lt;none&gt;           &lt;none&gt;

hello-world-57968f9979-xq5w4   1/1     Running   0          3m18s   172.18.0.5   minikube   &lt;none&gt;           &lt;none&gt;

hello-world-57968f9979-zwvgg   1/1     Running   0          4m14s   172.18.0.6   minikube   &lt;none&gt;           &lt;none&gt;
</code></pre>
<p>这里可以看到 Kubernetes 帮助我们创建了 3 个 Pod 实例。</p>
<p>第三步，创建 service.yaml 文件，帮助我们将服务暴露出去，内容如下：</p>
<pre><code>apiVersion: v1

kind: Service

metadata:

  name: hello-world

spec:

  type: NodePort

  ports:

  - port: 80

    targetPort: 80

  selector:

    app: hello-world
</code></pre>
<p>服务创建完成后，Kubernetes 会随机帮助我们分配一个外部访问端口，可以通过以下命令查看服务信息：</p>
<pre><code>$ kubectl  get service -o wide

NAME          TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE   SELECTOR

hello-world   NodePort    10.101.83.18   &lt;none&gt;        80:32391/TCP   12s   app=hello-world

kubernetes    ClusterIP   10.96.0.1      &lt;none&gt;        443/TCP        40m   &lt;none&gt;
</code></pre>
<p>由于我们的集群使用 minikube 安装，要想集群中的服务可以通过外部访问，还需要执行以下命令：</p>
<pre><code>$ minikube service hello-world
</code></pre>
<p>输出如下：</p>
<p><img src="assets/Ciqc1F-k_seAeN4RAACePALnr0Q662.png" alt="Lark20201106-154358.png" /></p>
<p>可以看到 minikube 将我们的服务暴露在了 32391 端口上，我们通过 http://{YOUR-IP}:32391 可以访问到我们启动的服务，如下图所示。</p>
<p><img src="assets/Ciqc1F-k_J-AWWQyAABkHB5NA0A837.png" alt="image" /></p>
<p>图 2 服务请求结果</p>
<p>总结下，我们首先使用 Deployment 创建了三个 nginx-hello 的实例，然后使用 Service 的方式随机负载到后端的三个实例，并将服务通过 NodePort 的方式暴露在主机上，使得我们可以直接使用主机的端口访问到容器中的服务。</p>
<h3>结语</h3>
<p>Kubernetes 从诞生到现在已经经历了 6 个年头，起初由于它的超前理念被世人误认为设计过度复杂，使得 Kubernetes 的入门门槛非常高。然而 6 年后的今天， Kubernetes 已经拥有了非常完善的社区和工具集，它可以帮助我们一键搭建 Kubernetes 集群，并且围绕 Kubernetes 构建的各种应用也是越来越丰富。</p>
<p>Kubernetes 的目标一直很明确，那就是对标 Borg，可以支撑数亿容器的运行。目前来看，要达到这个目标，Kubernetes 还有很长的路要走，但是当我们谈及云原生，谈及容器云时都必然会提到 Kubernetes，显然它已经成为容器编排的标准和标杆，目前大多数公有云也有支持 Kubernetes。容器的未来一定是美好的，而使用 Kubernetes 来调度容器则更是未来云计算的一个重要风向标。</p>
<p>那么，你的朋友中有没有人从事过 Kubernetes 或 Docker 相关的项目研发，现在这些项目发展得怎么样了呢？欢迎留言和我一起讨论容器圈创业那点事。</p>
<p>下一课时，我将为你带来 Docker 的综合实战案例，Docker 下如何实现镜像多阶级构建？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="20&#32;&#32;如何在生产环境中使用&#32;Docker&#32;Swarm&#32;调度容器？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="22&#32;&#32;多阶级构建：Docker&#32;下如何实现镜像多阶级构建？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a327901645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
