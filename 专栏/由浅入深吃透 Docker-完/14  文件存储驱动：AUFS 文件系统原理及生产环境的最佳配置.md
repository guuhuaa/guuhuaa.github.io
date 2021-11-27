<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14  文件存储驱动：AUFS 文件系统原理及生产环境的最佳配置.md</title>
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

                    <a class="current-tab" href="14&#32;&#32;文件存储驱动：AUFS&#32;文件系统原理及生产环境的最佳配置.md">14  文件存储驱动：AUFS 文件系统原理及生产环境的最佳配置.md</a>
                    

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
                        <div><h1>14  文件存储驱动：AUFS 文件系统原理及生产环境的最佳配置</h1>
<p>我们知道，Docker 主要是基于 Namespace、cgroups 和联合文件系统这三大核心技术实现的。前面的课时我详细讲解了 Namespace 和 cgroups 的相关原理，那么你知道联合文件系统是什么吗？它的原理又是什么呢？</p>
<p>首先我们来了解一下什么是联合文件系统。</p>
<h3>什么是联合文件系统</h3>
<p>联合文件系统（Union File System，Unionfs）是一种分层的轻量级文件系统，它可以把多个目录内容联合挂载到同一目录下，从而形成一个单一的文件系统，这种特性可以让使用者像是使用一个目录一样使用联合文件系统。</p>
<p>那联合文件系统对于 Docker 是一个怎样的存在呢？它可以说是 Docker 镜像和容器的基础，因为它可以使 Docker 可以把镜像做成分层的结构，从而使得镜像的每一层可以被共享。例如两个业务镜像都是基于 CentOS 7 镜像构建的，那么这两个业务镜像在物理机上只需要存储一次 CentOS 7 这个基础镜像即可，从而节省大量存储空间。</p>
<p>说到这儿，你有没有发现，联合文件系统只是一个概念，真正实现联合文件系统才是关键，那如何实现呢？其实实现方案有很多，Docker 中最常用的联合文件系统有三种：AUFS、Devicemapper 和 OverlayFS。</p>
<p>今天我主要讲解 Docker 中最常用的联合文件系统里的 AUFS，为什么呢？因为 AUFS 是 Docker 最早使用的文件系统驱动，多用于 Ubuntu 和 Debian 系统中。在 Docker 早期，OverlayFS 和 Devicemapper 相对不够成熟，AUFS 是最早也是最稳定的文件系统驱动。 Devicemapper 和 OverlayFS 联合文件系统，我将在第 15 和 16 课时为你详细剖析 。</p>
<p>接下来，我们就看看如何配置 Docker 的 AUFS 模式。</p>
<h3>如何配置 Docker 的 AUFS 模式</h3>
<p>AUFS 目前并未被合并到 Linux 内核主线，因此只有 Ubuntu 和 Debian 等少数操作系统支持 AUFS。你可以使用以下命令查看你的系统是否支持 AUFS：</p>
<pre><code>$ grep aufs /proc/filesystems

nodev   aufs
</code></pre>
<p>执行以上命令后，如果输出结果包含<code>aufs</code>，则代表当前操作系统支持 AUFS。AUFS 推荐在 Ubuntu 或 Debian 操作系统下使用，如果你想要在 CentOS 等操作系统下使用 AUFS，需要单独安装 AUFS 模块（生产环境不推荐在 CentOS 下使用 AUFS，如果你想在 CentOS 下安装 AUFS 用于研究和测试，可以参考这个<a href="https://github.com/bnied/kernel-ml-aufs">链接</a>），安装完成后使用上述命令输出结果中有<code>aufs</code>即可。
当确认完操作系统支持 AUFS 后，你就可以配置 Docker 的启动参数了。</p>
<p>先在 /etc/docker 下新建 daemon.json 文件，并写入以下内容：</p>
<pre><code>{

  &quot;storage-driver&quot;: &quot;aufs&quot;

}
</code></pre>
<p>然后使用以下命令重启 Docker：</p>
<pre><code>$ sudo systemctl restart docker
</code></pre>
<p>Docker 重启以后使用<code>docker info</code>命令即可查看配置是否生效：</p>
<pre><code>$ sudo docker info

Client:

 Debug Mode: false

Server:

 Containers: 0

  Running: 0

  Paused: 0

  Stopped: 0

 Images: 1

 Server Version: 19.03.12

 Storage Driver: aufs

  Root Dir: /var/lib/docker/aufs

  Backing Filesystem: extfs

  Dirs: 1

  Dirperm1 Supported: true
</code></pre>
<p>可以看到 Storage Driver 已经变为 aufs，证明配置已经生效，配置生效后就可以使用 AUFS 为 Docker 提供联合文件系统了。</p>
<p>配置好 Docker 的 AUFS 联合文件系统后，你一定很好奇 AUFS 到底是如何工作的呢？下面我带你详细学习一下 AUFS 的工作原理。</p>
<h3>AUFS 工作原理</h3>
<h4>AUFS 是如何存储文件的？</h4>
<p>AUFS 是联合文件系统，意味着它在主机上使用多层目录存储，<strong>每一个目录在 AUFS 中都叫作分支，而在 Docker 中则称之为层（layer），但最终呈现给用户的则是一个普通单层的文件系统，我们把多层以单一层的方式呈现出来的过程叫作联合挂载。</strong></p>
<p><img src="assets/CgqCHl-GwcCAOu4aAABzKSlpRlI180.png" alt="Lark20201014-171313.png" /></p>
<p>图 1 AUFS 工作原理示意图</p>
<p>如图 1 所示，每一个镜像层和容器层都是 /var/lib/docker 下的一个子目录，镜像层和容器层都在 aufs/diff 目录下，每一层的目录名称是镜像或容器的 ID 值，联合挂载点在 aufs/mnt 目录下，mnt 目录是真正的容器工作目录。</p>
<p>下面我们针对 aufs 文件夹下的各目录结构，在创建容器前后的变化做详细讲述。</p>
<p>当一个镜像未生成容器时，AUFS 的存储结构如下。</p>
<ul>
<li>diff 文件夹：存储镜像内容，每一层都存储在以镜像层 ID 命名的子文件夹中。</li>
<li>layers 文件夹：存储镜像层关系的元数据，在 diif 文件夹下的每个镜像层在这里都会有一个文件，文件的内容为该层镜像的父级镜像的 ID。</li>
<li>mnt 文件夹：联合挂载点目录，未生成容器时，该目录为空。</li>
</ul>
<p>当一个镜像已经生成容器时，AUFS 存储结构会发生如下变化。</p>
<ul>
<li>diff 文件夹：当容器运行时，会在 diff 目录下生成容器层。</li>
<li>layers 文件夹：增加容器层相关的元数据。</li>
<li>mnt 文件夹：容器的联合挂载点，这和容器中看到的文件内容一致。</li>
</ul>
<p>以上便是 AUFS 的工作原理，那你知道容器的在工作过程中是如何使用 AUFS 的吗？</p>
<h4>AUFS 是如何工作的？</h4>
<p>AUFS 的工作过程中对文件的操作分为读取文件和修改文件。下面我们分别来看下 AUFS 对于不同的文件操作是如何工作的。</p>
<h5>1. 读取文件</h5>
<p>当我们在容器中读取文件时，可能会有以下场景。</p>
<ul>
<li>文件在容器层中存在时：当文件存在于容器层时，直接从容器层读取。</li>
<li>当文件在容器层中不存在时：当容器运行时需要读取某个文件，如果容器层中不存在时，则从镜像层查找该文件，然后读取文件内容。</li>
<li>文件既存在于镜像层，又存在于容器层：当我们读取的文件既存在于镜像层，又存在于容器层时，将会从容器层读取该文件。</li>
</ul>
<h5>2. 修改文件或目录</h5>
<p>AUFS 对文件的修改采用的是写时复制的工作机制，这种工作机制可以最大程度节省存储空间。</p>
<p>具体的文件操作机制如下。</p>
<ul>
<li>第一次修改文件：当我们第一次在容器中修改某个文件时，AUFS 会触发写时复制操作，AUFS 首先从镜像层复制文件到容器层，然后再执行对应的修改操作。</li>
</ul>
<blockquote>
<p>AUFS 写时复制的操作将会复制整个文件，如果文件过大，将会大大降低文件系统的性能，因此当我们有大量文件需要被修改时，AUFS 可能会出现明显的延迟。好在，写时复制操作只在第一次修改文件时触发，对日常使用没有太大影响。</p>
</blockquote>
<ul>
<li>删除文件或目录：当文件或目录被删除时，AUFS 并不会真正从镜像中删除它，因为镜像层是只读的，AUFS 会创建一个特殊的文件或文件夹，这种特殊的文件或文件夹会阻止容器的访问。</li>
</ul>
<p>下面我们通过一个实例来演示一下 AUFS 。</p>
<h3>AUFS 演示</h3>
<h4>准备演示目录和文件</h4>
<p>首先我们在 /tmp 目录下创建 aufs 目录：</p>
<pre><code>$ cd /tmp

/tmp$ mkdir aufs
</code></pre>
<p>准备挂载点目录：</p>
<pre><code>/tmp$ cd aufs

/tmp/aufs$ mkdir mnt
</code></pre>
<p>接下来准备容器层内容：</p>
<pre><code>## 创建镜像层目录

/tmp/aufs$ mkdir container1

## 在镜像层目录下准备一个文件

/tmp/aufs$ echo Hello, Container layer! &gt; container1/container1.txt
</code></pre>
<p>最后准备镜像层内容：</p>
<pre><code>## 创建两个镜像层目录

/tmp/aufs$ mkdir image1 &amp;&amp; mkdir image2

## 分别写入数据

/tmp/aufs$ echo Hello, Image layer1! &gt; image1/image1.txt

/tmp/aufs$ echo Hello, Image layer2! &gt; image2/image2.txt
</code></pre>
<p>准备好的目录和文件结构如下：</p>
<pre><code>/tmp/aufs$ tree .

.

|-- container1

|   `-- container1.txt

|-- image1

|   `-- image1.txt

|-- image2

|   `-- image2.txt

`-- mnt

4 directories, 3 files
</code></pre>
<h4>创建 AUFS 联合文件系统</h4>
<p>使用 mount 命令可以创建 AUFS 类型的文件系统，命令如下：</p>
<pre><code>/tmp/aufs$ sudo mount -t aufs -o dirs=./container1:./image2:./image1  none ./mnt
</code></pre>
<p>mount 命令创建 AUFS 类型文件系统时，这里要注意，<strong>dirs 参数第一个冒号默认为读写权限，后面的目录均为只读权限，与 Docker 容器使用 AUFS 的模式一致。</strong></p>
<p>执行完上述命令后，mnt 变成了 AUFS 的联合挂载目录，我们可以使用 mount 命令查看一下已经创建的 AUFS 文件系统：</p>
<pre><code>/tmp/aufs$ mount -t aufs

none on /tmp/aufs/mnt type aufs (rw,relatime,si=4174b83d649ffb7c)
</code></pre>
<p>我们每创建一个 AUFS 文件系统，AUFS 都会为我们生成一个 ID，这个 ID 在 /sys/fs/aufs/ 会创建对应的目录，在这个 ID 的目录下可以查看文件挂载的权限。</p>
<pre><code>tmp/aufs$ cat /sys/fs/aufs/si_4174b83d649ffb7c/*

/tmp/aufs/container1=rw

/tmp/aufs/image2=ro

/tmp/aufs/image1=ro

64

65

66
</code></pre>
<p>可以看到 container1 目录的权限为 rw（代表可读写），image1 和 image2 的权限为 ro（代表只读）。</p>
<p>为了验证 mnt 目录下可以看到 container1、image1 和 image2 目录下的所有内容，我们使用 ls 命令查看一下 mnt 目录：</p>
<pre><code>/tmp/aufs$ ls -l mnt/

total 12

-rw-rw-r-- 1 ubuntu ubuntu 24 Sep  9 16:55 container1.txt

-rw-rw-r-- 1 ubuntu ubuntu 21 Sep  9 16:59 image1.txt

-rw-rw-r-- 1 ubuntu ubuntu 21 Sep  9 16:59 image2.txt
</code></pre>
<p>可以看到 mnt 目录下已经出现了我们准备的所有镜像层和容器层的文件。下面让我们来验证一下 AUFS 的写时复制。</p>
<h4>验证 AUFS 的写时复制</h4>
<p>AUFS 的写时复制是指在容器中，只有需要修改某个文件时，才会把文件从镜像层复制到容器层，下面我们通过修改联合挂载目录 mnt 下的内容来验证下这个过程。</p>
<p>我们使用以下命令修改 mnt 目录下的 image1.txt 文件：</p>
<pre><code>/tmp/aufs$ echo Hello, Image layer1 changed! &gt; mnt/image1.txt
</code></pre>
<p>然后我们查看下 image1/image1.txt 文件内容：</p>
<pre><code>/tmp/aufs$ cat image1/image1.txt

Hello, Image layer1!
</code></pre>
<p>发现“镜像层”的 image1.txt 文件并未被修改。
然后我们查看一下&quot;容器层&quot;对应的 image1.txt 文件内容：</p>
<pre><code>/tmp/aufs$ ls -l container1/

total 8

-rw-rw-r-- 1 ubuntu ubuntu 24 Sep  9 16:55 container1.txt

-rw-rw-r-- 1 ubuntu ubuntu 29 Sep  9 17:21 image1.txt

## 查看文件内容

/tmp/aufs$ cat container1/image1.txt

Hello, Image layer1 changed!
</code></pre>
<p>发现 AUFS 在“容器层”自动创建了 image1.txt 文件，并且内容为我们刚才写入的内容。</p>
<p>至此，我们完成了 AUFS 写时复制的验证。我们在第一次修改镜像内某个文件时，AUFS 会复制这个文件到容器层，然后在容器层对该文件进行修改操作，这就是 AUFS 最典型的特性写时复制。</p>
<h3>结语</h3>
<p>到此，相信你知道了联合文件系统是一种分层的轻量级文件系统，它可以把多个目录内容联合挂载到同一目录下，从而形成一个单一的文件系统。同时也学会了如何配置 Docker 使用 AUFS ，并且明白了 AUFS 的工作原理。</p>
<p>那么你知道 AUFS 为什么一直没能成功进入 Linux 内核主线吗？ 思考后，可以把你的想法写在留言区。</p>
<p>下一课时，我将讲解 Docker 的另一个文件存储驱动：Devicemapper 文件系统原理及生产环境的最佳配置。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="13&#32;&#32;数据存储：剖析&#32;Docker&#32;卷与持久化数据存储的底层原理.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;&#32;文件存储驱动：Devicemapper&#32;文件系统原理及生产环境的最佳配置.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359ff9b87645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
