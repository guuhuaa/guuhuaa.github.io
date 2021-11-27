<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>20  如何在生产环境中使用 Docker Swarm 调度容器？.md</title>
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

                    <a class="current-tab" href="20&#32;&#32;如何在生产环境中使用&#32;Docker&#32;Swarm&#32;调度容器？.md">20  如何在生产环境中使用 Docker Swarm 调度容器？.md</a>
                    

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
                        <div><h1>20  如何在生产环境中使用 Docker Swarm 调度容器？</h1>
<p>上一课时，我介绍了 Docker 的单节点引擎工具 Docker Compose，它能够在单一节点上管理和编排多个容器，当我们的服务和容器数量较小时可以使用 Docker Compose 来管理容器。</p>
<p>然而随着我们的业务规模越来越大，我们的容器规模也逐渐增大时，数量庞大的容器管理将给我们带来许多挑战。Docker 官方为了解决多容器管理的问题推出了 Docker Swarm ，我们可以用它来管理规模更大的容器集群。</p>
<h3>Swarm 的前生今世</h3>
<p>2014 年 Docker 在容器界越来越火，这时容器的编排工具 Mesos 和 Kubernetes 也开始崭露头角。此时，Docker 公司也开始筹划容器的编排和集群管理工具，推出了自己的通信协议项目 Beam。后来，通过改进 Beam，Beam 成为一个允许使用 Docker API 来控制的一种分布式系统，之后项目被重命名为 libswarm。然而在 2014 年 11 月，Docker 公司又对 libswarm 进行了重新设计，支持了远程调用 API，并且被重新命名为 Swarm。到此我们称之为 Swarm V1。</p>
<p>在 2016 年，为了解决中央服务可扩展性的问题，Docker 团队重新设计了 Swarm，并称之为 Swarm V2。此时的 Docker Swarm 已经可以支持超过 1000 多个节点的集群规模，并且 Docker 团队在发布 Docker 1.12 版本时，将 Docker Swarm 默认集成到了 Docker 引擎中。</p>
<p>由于 Swarm 是 Docker 官方推出的容器集群管理工具，因此 Swarm 最大的优势之一就是原生支持 Docker API，给用户带来了极大的便利，原来的 Docker 用户可以很方便地将服务迁移到 Swarm 中来。</p>
<p>与此同时，Swarm 还内置了对 Docker 网络插件的支持，因此用户可以很方便地部署需要跨主机通信的容器集群。其实 Swarm 的优点远远不止这些，还有很多，例如以下优点。</p>
<ul>
<li><strong>分布式：</strong> Swarm 使用<a href="https://raft.github.io/">Raft</a>（一种分布式一致性协议）协议来做集群间数据一致性保障，使用多个容器节点组成管理集群，从而避免单点故障。</li>
<li><strong>安全：</strong> Swarm 使用 TLS 双向认证来确保节点之间通信的安全，它可以利用双向 TLS 进行节点之间的身份认证，角色授权和加密传输，并且可以自动执行证书的颁发和更换。</li>
<li><strong>简单：</strong> Swarm 的操作非常简单，并且除 Docker 外基本无其他外部依赖，而且从 Docker 1.12 版本后， Swarm 直接被内置到了 Docker 中，可以说真正做到了开箱即用。</li>
</ul>
<p>Swarm 的这些优点得益于它优美的架构设计，下面我们来了解一下 Swarm 的架构。</p>
<h3>Swarm 的架构</h3>
<p>Swarm 的架构整体分为<strong>管理节点</strong>（Manager Nodes）和<strong>工作节点</strong>（Worker Nodes），整体架构如下图：</p>
<p><img src="assets/CgqCHl-iZxSAbYhzAABiA3_fQM8971.png" alt="image.png" /></p>
<p>图 1 Swarm 架构图</p>
<p><strong>管理节点：</strong> 管理节点负责接受用户的请求，用户的请求中包含用户定义的容器运行状态描述，然后 Swarm 负责调度和管理容器，并且努力达到用户所期望的状态。</p>
<p><strong>工作节点：</strong> 工作节点运行执行器（Executor）负责执行具体的容器管理任务（Task），例如容器的启动、停止、删除等操作。</p>
<blockquote>
<p>管理节点和工作节点的角色并不是一成不变的，你可以手动将工作节点转换为管理节点，也可以将管理节点转换为工作节点。</p>
</blockquote>
<h3>Swarm 核心概念</h3>
<p>在真正使用 Swarm 之前，我们需要了解几个 Swarm 的核心概念，这些核心概念可以帮助我们更好地学习和理解 Swarm 的设计理念。</p>
<h4>Swarm 集群</h4>
<p>Swarm 集群是一组被 Swarm 统一管理和调度的节点，被 Swarm纳管的节点可以是物理机或者虚拟机。其中一部分节点作为管理节点，负责集群状态的管理和协调，另一部分作为工作节点，负责执行具体的任务来管理容器，实现用户服务的启停等功能。</p>
<h4>节点</h4>
<p>Swarm 集群中的每一台物理机或者虚拟机称为节点。节点按照工作职责分为<strong>管理节点</strong>和<strong>工作节点</strong>，管理节点由于需要使用 Raft 协议来协商节点状态，生产环境中通常建议将管理节点的数量设置为奇数个，一般为 3 个、5 个或 7 个。</p>
<h4>服务</h4>
<p>服务是为了支持容器编排所提出的概念，它是一系列复杂容器环境互相协作的统称。一个服务的声明通常包含容器的启动方式、启动的副本数、环境变量、存储、配置、网络等一系列配置，用户通过声明一个服务，将它交给 Swarm，Swarm 负责将用户声明的服务实现。</p>
<p>服务分为全局服务（global services）和副本服务（replicated services）。</p>
<ul>
<li>全局服务：每个工作节点上都会运行一个任务，类似于 Kubernetes 中的 <a href="https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/">Daemonset</a>。</li>
<li>副本服务：按照指定的副本数在整个集群中调度运行。</li>
</ul>
<h4>任务</h4>
<p>任务是集群中的最小调度单位，它包含一个真正运行中的 Docker 容器。当管理节点根据服务中声明的副本数将任务调度到节点时，任务则开始在该节点启动和运行，当节点出现异常时，任务会运行失败。此时调度器会把失败的任务重新调度到其他正常的节点上正常运行，以确保运行中的容器副本数满足用户所期望的副本数。</p>
<h4>服务外部访问</h4>
<p>由于容器的 IP 只能在集群内部访问到，而且容器又是用后马上销毁，这样容器的 IP 也会动态变化，因此容器集群内部的服务想要被集群外部的用户访问到，服务必须要映射到主机上的固定端口。Swarm 使用入口负载均衡（ingress load balancing）的模式将服务暴露在主机上，该模式下，每一个服务会被分配一个公开端口（PublishedPort），你可以指定使用某个未被占用的公开端口，也可以让 Swarm 自动分配一个。</p>
<p>Swarm 集群的公开端口可以从集群内的任意节点上访问到，当请求达到集群中的一个节点时，如果该节点没有要请求的服务，则会将请求转发到实际运行该服务的节点上，从而响应用户的请求。公有云的云负载均衡器（cloud load balancers）可以利用这一特性将流量导入到集群中的一个或多个节点，从而实现利用公有云的云负载均衡器将流量导入到集群中的服务。</p>
<h3>搭建 Swarm 集群</h3>
<p>要想使用 Swarm 集群有如下一些要求：</p>
<ul>
<li>Docker 版本大于 1.12，推荐使用最新稳定版 Docker；</li>
<li>主机需要开放一些端口（TCP：2377 UDP:4789 TCP 和 UDP:7946）。</li>
</ul>
<p>下面我通过四台机器来搭建一个 Swarm 集群，演示的节点规划如下：</p>
<p><img src="assets/Ciqc1F-iZ0KAdrQoAABINXCXUv0846.png" alt="Lark20201104-162431.png" /></p>
<blockquote>
<p>生产环境中推荐使用至少三个 manager 作为管理节点。</p>
</blockquote>
<ul>
<li>第一步：初始化集群</li>
</ul>
<p>Docker 1.12 版本后， Swarm 已经默认集成到了 Docker 中，因此我们可以直接使用 Docker 命令来初始化 Swarm，集群初始化的命令格式如下：</p>
<pre><code>docker swarm init --advertise-addr &lt;YOUR-IP&gt;
</code></pre>
<blockquote>
<p>advertise-addr 一般用于主机有多块网卡的情况，如果你的主机只有一块网卡，可以忽略此参数。</p>
</blockquote>
<p>在管理节点上，通过以下命令初始化集群：</p>
<pre><code>$ docker swarm init

Swarm initialized: current node (1ehtnlcf3emncktgjzpoux5ga) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1kal5b1iozbfmnnhx3kjfd3y6yqcjjjpcftrlg69pm2g8hw5vx-8j4l0t2is9ok9jwwc3tovtxbp 192.168.31.100:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
</code></pre>
<p>集群初始化后， Swarm 会提示我们当前节点已经作为一个管理节点了，并且提示了如何把一台主机加入集群成为工作节点。</p>
<ul>
<li>第二步：加入工作节点</li>
</ul>
<p>按照第一步集群初始化后输出的提示，只需要复制其中的命令即可，然后在剩余的三台工作节点上分别执行如下命令：</p>
<pre><code>$ docker swarm join --token SWMTKN-1-1kal5b1iozbfmnnhx3kjfd3y6yqcjjjpcftrlg69pm2g8hw5vx-8j4l0t2is9ok9jwwc3tovtxbp 192.168.31.100:2377

This node joined a swarm as a worker.
</code></pre>
<p>默认加入的节点为工作节点，如果是生产环境，我们可以使用<code>docker swarm join-token manager</code>命令来查看如何加入管理节点：</p>
<pre><code>$ docker swarm join-to ken manager

To add a manager to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-1kal5b1iozbfmnnhx3kjfd3y6yqcjjjpcftrlg69pm2g8hw5vx-8fq89jxo2axwggryvom5a337t 192.168.31.100:2377
</code></pre>
<p>复制 Swarm 输出的结果即可加入管理节点到集群中。</p>
<blockquote>
<p>注意：管理节点的数量必须为奇数，生产环境推荐使用3个、5个或7个管理节点来管理 Swarm 集群。</p>
</blockquote>
<ul>
<li>第三步：节点查看</li>
</ul>
<p>节点添加完成后，我们使用以下命令可以查看当前节点的状态：</p>
<pre><code>$ ]# docker node ls

ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION

1ehtnlcf3emncktgjzpoux5ga *   swarm-manager       Ready               Active              Leader              19.03.12

pn7gdm847sfzydqhcv3vma97y *   swarm-node1         Ready               Active                                        19.03.12

4dtc9pw5quyjs5yf25ccgr8uh *   swarm-node2         Ready               Active                                        19.03.12

est7ww3gngna4u7td22g9m2k5 *   swarm-node3         Ready               Active                                        19.03.12
</code></pre>
<p>到此，一个包含 1 个管理节点，3 个工作节点的 Swarm 集群已经搭建完成。</p>
<h3>使用 Swarm</h3>
<p>集群搭建完成后，我们就可以在 Swarm 集群中创建服务了，Swarm 集群中常用的服务部署方式有以下两种。</p>
<h4>（1）通过 docker service 命令创建服务</h4>
<p>使用<code>docker service create</code>命令可以创建服务，创建服务的命令如下：</p>
<pre><code>$ docker service create --replicas 1 --name hello-world nginx

24f9ng83m9sq4ml3e92k4g5by

overall progress: 1 out of 1 tasks

1/1: running   [==================================================&gt;]

verify: Service converged
</code></pre>
<p>此时我们已经创建好了一个服务，使用<code>docker service ls</code>命令可以查看已经启动的服务：</p>
<pre><code>$ docker service ls

ID                  NAME                  MODE                REPLICAS            IMAGE               PORTS

24f9ng83m9sq        hello-world           replicated          1/1                 nginx:latest
</code></pre>
<p>当我们不再需要这个服务了，可以使用<code>docker service rm</code>命令来删除服务：</p>
<pre><code>$ docker service rm hello-world

hello-world
</code></pre>
<p>此时 hello-world 这个服务已经成功地从集群中删除。
想要了解更多的<code>docker service</code>命令的相关操作，可以参考<a href="https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service/">这里</a>。</p>
<p>生产环境中，我们推荐使用 docker-compose 模板文件来部署服务，这样服务的管理会更加方便并且可追踪，而且可以同时创建和管理多个服务，更加适合生产环境中依赖关系较复杂的部署模式。</p>
<h4>（2）通过 docker stack 命令创建服务</h4>
<p>我们在 19 课时中创建了 docker-compose 的模板文件，成功的使用该模板文件创建并启动了 MySQL 服务和 WordPress 两个服务。这里我们将 19 讲中的 docker-compose 模板文件略微改造一下：</p>
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

     deploy:

       mode: replicated

       replicas: 2

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
<p>我在服务模板文件中添加了 deploy 指令，并且指定使用副本服务（replicated）的方式启动两个 WordPress 实例。</p>
<p>准备好启动 WordPress 服务的配置后，我们在 /tmp 目下新建 docker-compose.yml 文件，并且写入以上的内容，然后我们使用以下命令启动服务：</p>
<pre><code>$ docker stack deploy -c docker-compose.yml wordpress

Ignoring unsupported options: restart

Creating network wordpress_default

Creating service wordpress_mysql

Creating service wordpress_wordpress
</code></pre>
<p>执行完以上命令后，我们成功启动了两个服务：</p>
<ol>
<li>MySQL 服务，默认启动了一个副本。</li>
<li>WordPress 服务，根据我们 docker-compose 模板的定义启动了两个副本。</li>
</ol>
<p>下面我们用<code>docker service ls</code>命令查看一下当前启动的服务。</p>
<pre><code>$ docker service ls

ID                  NAME                  MODE                REPLICAS            IMAGE               PORTS

v8i0pzb4e3tc        wordpress_mysql       replicated          1/1                 mysql:5.7

96m8xfyeqzr5        wordpress_wordpress   replicated          2/2                 wordpress:php7.4    *:8080-&gt;80/tcp
</code></pre>
<p>可以看到，Swarm 已经为我们成功启动了一个 MySQL 服务，并且启动了两个 WordPress 实例。WordPress 实例通过 8080 端口暴露在了主机上，我们通过访问集群中的任意节点的 IP 加 8080 端口即可访问到 WordPress 服务。例如，我们访问<a href="http://192.168.31.101:8080/">http://192.168.31.101:8080</a>即可成功访问到我们搭建的 WordPress 服务。</p>
<h3>结语</h3>
<p>Docker Swarm 是一个用来定义复杂应用的集群编排工具，可以帮我们把多台主机组成一个 Swarm 集群，并且帮助我们管理和调度复杂的容器服务。由于 Swarm 已经被内置于 Docker 中，因此 Swarm 的安装和使用也变得非常简单，只要你有 Docker 的使用经验，就可以很快地将你的应用迁移到 Swarm 集群中。</p>
<p>那么，学完本课时内容，你可以试着构建一个高可用（管理节点扩展为 3 个或 5 个）的 Swarm 集群吗？</p>
<p>下一课时，我将为你讲解目前使用最多的容器编排系统Kubernetes，再会。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="19&#32;&#32;如何使用&#32;Docker&#32;Compose&#32;解决开发环境的依赖？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="21&#32;&#32;如何使&#32;Docker&#32;和&#32;Kubernetes&#32;结合发挥容器的最大价值？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a2d18b5645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
