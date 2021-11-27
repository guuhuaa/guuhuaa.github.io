<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>08  容器监控：容器监控原理及 cAdvisor 的安装与使用.md</title>
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

                    <a class="current-tab" href="08&#32;&#32;容器监控：容器监控原理及&#32;cAdvisor&#32;的安装与使用.md">08  容器监控：容器监控原理及 cAdvisor 的安装与使用.md</a>
                    

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
                        <div><h1>08  容器监控：容器监控原理及 cAdvisor 的安装与使用</h1>
<p>生产环境中监控容器的运行状况十分重要，通过监控我们可以随时掌握容器的运行状态，做到线上隐患和问题早发现，早解决。所以今天我就和你分享关于容器监控的知识（原理及工具 cAdvisor）。</p>
<p>虽然传统的物理机和虚拟机监控已经有了比较成熟的监控方案，但是容器的监控面临着更大的挑战，因为容器的行为和本质与传统的虚拟机是不一样的，总的来说，容器具有以下特性：</p>
<ul>
<li>容器是短期存活的，并且可以动态调度；</li>
<li>容器的本质是进程，而不是一个完整操作系统；</li>
<li>由于容器非常轻量，容器的创建和销毁也会比传统虚拟机更加频繁。</li>
</ul>
<p>Docker 容器的监控方案有很多，除了 Docker 自带的<code>docker stats</code>命令，还有很多开源的解决方案，例如 sysdig、cAdvisor、Prometheus 等，都是非常优秀的监控工具。</p>
<p>下面我们首先来看下，不借助任何外部工具，如何用 Docker 自带的<code>docker stats</code>命令实现容器的监控。</p>
<h3>使用 docker stats 命令</h3>
<p>使用Docker自带的<code>docker stats</code>命令可以很方便地看到主机上所有容器的 CPU、内存、网络 IO、磁盘 IO、PID 等资源的使用情况。下面我们可以具体操作看看。</p>
<p>首先在主机上使用以下命令启动一个资源限制为 1 核 2G 的 nginx 容器：</p>
<pre><code>$ docker run --cpus=1 -m=2g --name=nginx  -d nginx
</code></pre>
<p>容器启动后，可以使用<code>docker stats</code>命令查看容器的资源使用状态:</p>
<pre><code>$ docker stats nginx
</code></pre>
<p>通过<code>docker stats</code>命令可以看到容器的运行状态如下：</p>
<pre><code>CONTAINER           CPU %               MEM USAGE / LIMIT   MEM %               NET I/O             BLOCK I/O           PIDS
f742a467b6d8        0.00%               1.387 MiB / 2 GiB   0.07%               656 B / 656 B       0 B / 9.22 kB       2
</code></pre>
<p>从容器的运行状态可以看出，<code>docker stats</code>命令确实可以获取并显示 Docker 容器运行状态。但是它的缺点也很明显，因为它只能获取本机数据，无法查看历史监控数据，没有可视化展示面板。</p>
<p>因此，生产环境中我们通常使用另一种容器监控解决方案 cAdvisor。</p>
<h3>cAdvisor</h3>
<p>cAdvisor 是谷歌开源的一款通用的容器监控解决方案。cAdvisor 不仅可以采集机器上所有运行的容器信息，还提供了基础的查询界面和 HTTP 接口，更方便与外部系统结合。所以，cAdvisor很快成了容器指标监控最常用组件，并且 Kubernetes 也集成了 cAdvisor 作为容器监控指标的默认工具。</p>
<h4>cAdvisor 的安装与使用</h4>
<p>下面我们以 cAdvisor 0.37.0 版本为例，演示一下 cAdvisor 的安装与使用。</p>
<p>cAdvisor 官方提供了 Docker 镜像，我们只需要拉取镜像并且启动镜像即可。</p>
<blockquote>
<p>由于 cAdvisor 镜像存放在谷歌的 gcr.io 镜像仓库中，国内无法访问到。这里我把打好的镜像放在了 Docker Hub。你可以使用 docker pull lagoudocker/cadvisor:v0.37.0 命令从 Docker Hub 拉取。</p>
</blockquote>
<p>首先使用以下命令启动 cAdvisor：</p>
<pre><code>$ docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  --privileged \
  --device=/dev/kmsg \
  lagoudocker/cadvisor:v0.37.0
</code></pre>
<p>此时，cAdvisor 已经成功启动，我们可以通过访问 <a href="http://localhost:8080/">http://localhost:8080</a> 访问到 cAdvisor 的 Web 界面。</p>
<p><img src="assets/Ciqc1F9rCXSAQEwLAADKlh0at8o307.png" alt="Drawing 0.png" /></p>
<p>图1 cAdvisor 首页</p>
<p>cAdvisor 不仅可以监控容器的资源使用情况，还可以监控主机的资源使用情况。下面我们就先看下它是如何查看主机资源使用情况的。</p>
<h4>使用 cAdvisor 查看主机监控</h4>
<p>访问 <a href="http://localhost:8080/containers/">http://localhost:8080/containers/</a> 地址，在首页可以看到主机的资源使用情况，包含 CPU、内存、文件系统、网络等资源，如下图所示。</p>
<p><img src="assets/CgqCHl9rCX2ANrtaAADIGkeKKPc100.png" alt="Drawing 1.png" /></p>
<p>图2 主机 CPU 使用情况</p>
<h4>使用 cAdvisor 查看容器监控</h4>
<p>如果你想要查看主机上运行的容器资源使用情况，可以访问 <a href="http://localhost:8080/docker/">http://localhost:8080/docker/</a>，这个页面会列出 Docker 的基本信息和运行的容器情况，如下图所示。</p>
<p><img src="assets/Ciqc1F9rCZyAN8hYAAGAOL1FGcg401.png" alt="Drawing 2.png" /></p>
<p>图3 Docker 容器</p>
<p>在上图中的Subcontainers 下会列出当前主机上运行的所有容器，点击其中一个容器即可查看该容器的详细运行状态，如下图所示。</p>
<p><img src="assets/CgqCHl9rCaWAVSLVAAGGy2lTMqY130.png" alt="Drawing 3.png" /></p>
<p>图4 容器监控状态</p>
<p>总体来说，使用 cAdvisor 监控容器具有以下特点：</p>
<ul>
<li>可以同时采集物理机和容器的状态；</li>
<li>可以展示监控历史数据。</li>
</ul>
<p>了解 Docker 的监控工具，你是否想问，这些监控数据是怎么来的呢？下面我就带你了解一下容器监控的原理。</p>
<h3>监控原理</h3>
<p>我们知道 Docker 是基于 Namespace、Cgroups 和联合文件系统实现的。其中 Cgroups 不仅可以用于容器资源的限制，还可以提供容器的资源使用率。无论何种监控方案的实现，底层数据都来源于 Cgroups。</p>
<p>Cgroups 的工作目录为<code>/sys/fs/cgroup</code>，<code>/sys/fs/cgroup</code>目录下包含了 Cgroups 的所有内容。Cgroups包含很多子系统，可以用来对不同的资源进行限制。例如对CPU、内存、PID、磁盘 IO等资源进行限制和监控。</p>
<p>为了更详细的了解 Cgroups 的子系统，我们通过 ls -l 命令查看<code>/sys/fs/cgroup</code>文件夹，可以看到很多目录：</p>
<pre><code>$ sudo ls -l /sys/fs/cgroup/
total 0
dr-xr-xr-x 5 root root  0 Jul  9 19:32 blkio
lrwxrwxrwx 1 root root 11 Jul  9 19:32 cpu -&gt; cpu,cpuacct
dr-xr-xr-x 5 root root  0 Jul  9 19:32 cpu,cpuacct
lrwxrwxrwx 1 root root 11 Jul  9 19:32 cpuacct -&gt; cpu,cpuacct
dr-xr-xr-x 3 root root  0 Jul  9 19:32 cpuset
dr-xr-xr-x 5 root root  0 Jul  9 19:32 devices
dr-xr-xr-x 3 root root  0 Jul  9 19:32 freezer
dr-xr-xr-x 3 root root  0 Jul  9 19:32 hugetlb
dr-xr-xr-x 5 root root  0 Jul  9 19:32 memory
lrwxrwxrwx 1 root root 16 Jul  9 19:32 net_cls -&gt; net_cls,net_prio
dr-xr-xr-x 3 root root  0 Jul  9 19:32 net_cls,net_prio
lrwxrwxrwx 1 root root 16 Jul  9 19:32 net_prio -&gt; net_cls,net_prio
dr-xr-xr-x 3 root root  0 Jul  9 19:32 perf_event
dr-xr-xr-x 5 root root  0 Jul  9 19:32 pids
dr-xr-xr-x 5 root root  0 Jul  9 19:32 systemd
</code></pre>
<p>这些目录代表了 Cgroups 的子系统，Docker 会在每一个 Cgroups 子系统下创建 docker 文件夹。这里如果你对 Cgroups 子系统不了解的话，不要着急，后续我会在第 10课时对 Cgroups 子系统做详细讲解，这里你只需要明白容器监控数据来源于 Cgroups 即可。</p>
<h4>监控系统是如何获取容器的内存限制的？</h4>
<p>下面我们以memory 子系统（memory 子系统是Cgroups 众多子系统的一个，主要用来限制内存使用，Cgroups 会在第十课时详细讲解）为例，讲解一下监控组件是如何获取到容器的资源限制和使用状态的（即容器的内存限制）。</p>
<p>我们首先在主机上使用以下命令启动一个资源限制为 1 核 2G 的 nginx 容器：</p>
<pre><code>$ docker run --name=nginx --cpus=1 -m=2g --name=nginx  -d nginx
## 这里输出的是容器 ID
51041a74070e9260e82876974762b8c61c5ed0a51832d74fba6711175f89ede1
</code></pre>
<blockquote>
<p>注意：如果你已经创建过名称为 nginx 的容器，请先使用 docker  rm -f nginx 命令删除已经存在的 nginx 容器。</p>
</blockquote>
<p>容器启动后，我们通过命令行的输出可以得到容器的 ID，同时 Docker 会在<code>/sys/fs/cgroup/memory/docker</code>目录下以容器 ID 为名称创建对应的文件夹。</p>
<p>下面我们查看一下<code>/sys/fs/cgroup/memory/docker</code>目录下的文件：</p>
<pre><code>$ sudo ls -l /sys/fs/cgroup/memory/docker
total 0
drwxr-xr-x 2 root root 0 Sep  2 15:12 51041a74070e9260e82876974762b8c61c5ed0a51832d74fba6711175f89ede1
-rw-r--r-- 1 root root 0 Sep  2 14:57 cgroup.clone_children
--w--w--w- 1 root root 0 Sep  2 14:57 cgroup.event_control
-rw-r--r-- 1 root root 0 Sep  2 14:57 cgroup.procs
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.failcnt
--w------- 1 root root 0 Sep  2 14:57 memory.force_empty
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.failcnt
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.max_usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.slabinfo
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.tcp.failcnt
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.tcp.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.tcp.max_usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.tcp.usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 14:57 memory.kmem.usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.max_usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.memsw.failcnt
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.memsw.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.memsw.max_usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 14:57 memory.memsw.usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.move_charge_at_immigrate
-r--r--r-- 1 root root 0 Sep  2 14:57 memory.numa_stat
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.oom_control
---------- 1 root root 0 Sep  2 14:57 memory.pressure_level
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.soft_limit_in_bytes
-r--r--r-- 1 root root 0 Sep  2 14:57 memory.stat
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.swappiness
-r--r--r-- 1 root root 0 Sep  2 14:57 memory.usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 14:57 memory.use_hierarchy
-rw-r--r-- 1 root root 0 Sep  2 14:57 notify_on_release
-rw-r--r-- 1 root root 0 Sep  2 14:57 tasks
</code></pre>
<p>可以看到 Docker 已经创建了以容器 ID 为名称的目录，我们再使用 ls 命令查看一下该目录的内容：</p>
<pre><code>$ sudo ls -l /sys/fs/cgroup/memory/docker/51041a74070e9260e82876974762b8c61c5ed0a51832d74fba6711175f89ede1
total 0
-rw-r--r-- 1 root root 0 Sep  2 15:21 cgroup.clone_children
--w--w--w- 1 root root 0 Sep  2 15:13 cgroup.event_control
-rw-r--r-- 1 root root 0 Sep  2 15:12 cgroup.procs
-rw-r--r-- 1 root root 0 Sep  2 15:12 memory.failcnt
--w------- 1 root root 0 Sep  2 15:21 memory.force_empty
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.failcnt
-rw-r--r-- 1 root root 0 Sep  2 15:12 memory.kmem.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.max_usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.slabinfo
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.tcp.failcnt
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.tcp.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.tcp.max_usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.tcp.usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 15:21 memory.kmem.usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:12 memory.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:12 memory.max_usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.memsw.failcnt
-rw-r--r-- 1 root root 0 Sep  2 15:12 memory.memsw.limit_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.memsw.max_usage_in_bytes
-r--r--r-- 1 root root 0 Sep  2 15:21 memory.memsw.usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.move_charge_at_immigrate
-r--r--r-- 1 root root 0 Sep  2 15:21 memory.numa_stat
-rw-r--r-- 1 root root 0 Sep  2 15:13 memory.oom_control
---------- 1 root root 0 Sep  2 15:21 memory.pressure_level
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.soft_limit_in_bytes
-r--r--r-- 1 root root 0 Sep  2 15:21 memory.stat
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.swappiness
-r--r--r-- 1 root root 0 Sep  2 15:12 memory.usage_in_bytes
-rw-r--r-- 1 root root 0 Sep  2 15:21 memory.use_hierarchy
-rw-r--r-- 1 root root 0 Sep  2 15:21 notify_on_release
-rw-r--r-- 1 root root 0 Sep  2 15:21 tasks
</code></pre>
<p>由上可以看到，容器 ID 的目录下有很多文件，其中 memory.limit_in_bytes 文件代表该容器内存限制大小，单位为 byte，我们使用 cat 命令（cat 命令可以查看文件内容）查看一下文件内容：</p>
<pre><code>$ sudo cat /sys/fs/cgroup/memory/docker/51041a74070e9260e82876974762b8c61c5ed0a51832d74fba6711175f89ede1/memory.limit_in_bytes
2147483648
</code></pre>
<p>这里可以看到memory.limit_in_bytes 的值为2147483648，转换单位后正好为 2G，符合我们启动容器时的内存限制 2G。</p>
<p>通过 memory 子系统的例子，我们可以知道<strong>监控组件通过读取 memory.limit_in_bytes 文件即可获取到容器内存的限制值</strong>。了解完容器的内存限制我们来了解一下容器的内存使用情况。</p>
<h4>监控系统是如何获取容器的内存使用状态的？</h4>
<p>内存使用情况存放在 memory.usage_in_bytes 文件里，同样我们也使用 cat 命令查看一下文件内容:</p>
<pre><code>$ sudo /sys/fs/cgroup/memory/docker/51041a74070e9260e82876974762b8c61c5ed0a51832d74fba6711175f89ede1/memory.usage_in_bytes
4259840
</code></pre>
<p>可以看到当前内存的使用大小为 4259840 byte，约为 4 M。了解了内存的监控，下面我们来了解下网络的监控数据来源。</p>
<p>网络的监控数据来源是从 /proc/{PID}/net/dev 目录下读取的，其中 PID 为容器在主机上的进程 ID。下面我们首先使用 docker inspect 命令查看一下上面启动的 nginx 容器的 PID，命令如下：</p>
<pre><code>$ docker inspect nginx |grep Pid
            &quot;Pid&quot;: 27348,
            &quot;PidMode&quot;: &quot;&quot;,
            &quot;PidsLimit&quot;: 0,
</code></pre>
<p>可以看到容器的 PID 为 27348，使用 cat 命令查看一下 /proc/27348/net/dev 的内容：</p>
<pre><code>$ sudo cat /proc/27348/net/dev
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
  eth0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
</code></pre>
<p>/proc/27348/net/dev 文件记录了该容器里每一个网卡的流量接收和发送情况，以及错误数、丢包数等信息。可见容器的网络监控数据都是定时从这里读取并展示的。</p>
<p>总结一下，<strong>容器的监控原理其实就是定时读取 Linux 主机上相关的文件并展示给用户。</strong></p>
<h3>结语</h3>
<p>到此，相信你已经可以使用 docker stats 和 cAdvisor 监控并查看容器的状态了；也可以自己启动一个 cAdvisor 容器来监控主机和主机上的容器，并对监控系统的原理有了较深的了解。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="07&#32;&#32;Docker&#32;安全：基于内核的弱隔离系统如何保障安全性？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="09&#32;&#32;资源隔离：为什么构建容器需要&#32;Namespace&#32;？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359d9390e645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
