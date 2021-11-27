<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  文件存储驱动：OverlayFS 文件系统原理及生产环境的最佳配置.md</title>
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

                    <a class="current-tab" href="16&#32;&#32;文件存储驱动：OverlayFS&#32;文件系统原理及生产环境的最佳配置.md">16  文件存储驱动：OverlayFS 文件系统原理及生产环境的最佳配置.md</a>
                    

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
                        <div><h1>16  文件存储驱动：OverlayFS 文件系统原理及生产环境的最佳配置</h1>
<p>前面课时我分别介绍了 Docker 常见的联合文件系统解决方案： AUFS 和 Devicemapper。今天我给你介绍一个性能更好的联合文件系统解决方案—— OverlayFS。</p>
<p>OverlayFS 的发展分为两个阶段。2014 年，OverlayFS 第一个版本被合并到 Linux 内核 3.18 版本中，此时的 OverlayFS 在 Docker 中被称为<code>overlay</code>文件驱动。由于第一版的<code>overlay</code>文件系统存在很多弊端（例如运行一段时间后Docker 会报 &quot;too many links problem&quot; 的错误）， Linux 内核在 4.0 版本对<code>overlay</code>做了很多必要的改进，此时的 OverlayFS 被称之为<code>overlay2</code>。</p>
<p>因此，在 Docker 中 OverlayFS 文件驱动被分为了两种，一种是早期的<code>overlay</code>，不推荐在生产环境中使用，另一种是更新和更稳定的<code>overlay2</code>，推荐在生产环境中使用。下面的内容我们主要围绕<code>overlay2</code>展开。</p>
<h3>使用 overlay2 的先决条件</h3>
<p><code>overlay2</code>虽然很好，但是它的使用是有一定条件限制的。</p>
<ul>
<li>要想使用<code>overlay2</code>，Docker 版本必须高于 17.06.02。</li>
<li>如果你的操作系统是 RHEL 或 CentOS，Linux 内核版本必须使用 3.10.0-514 或者更高版本，其他 Linux 发行版的内核版本必须高于 4.0（例如 Ubuntu 或 Debian），你可以使用<code>uname -a</code>查看当前系统的内核版本。</li>
<li><code>overlay2</code>最好搭配 xfs 文件系统使用，并且使用 xfs 作为底层文件系统时，d_type必须开启，可以使用以下命令验证 d_type 是否开启：</li>
</ul>
<pre><code>$ xfs_info /var/lib/docker | grep ftype

naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
</code></pre>
<p>当输出结果中有 ftype=1 时，表示 d_type 已经开启。如果你的输出结果为 ftype=0，则需要重新格式化磁盘目录，命令如下：</p>
<pre><code>$ sudo mkfs.xfs -f -n ftype=1 /path/to/disk
</code></pre>
<p>另外，在生产环境中，推荐挂载 /var/lib/docker 目录到单独的磁盘或者磁盘分区，这样可以避免该目录写满影响主机的文件写入，并且把挂载信息写入到 /etc/fstab，防止机器重启后挂载信息丢失。</p>
<p>挂载配置中推荐开启 pquota，这样可以防止某个容器写文件溢出导致整个容器目录空间被占满。写入到 /etc/fstab 中的内容如下：</p>
<pre><code>$UUID /var/lib/docker xfs defaults,pquota 0 0
</code></pre>
<p>其中 UUID 为 /var/lib/docker 所在磁盘或者分区的 UUID 或者磁盘路径。
如果你的操作系统无法满足上面的任何一个条件，那我推荐你使用 AUFS 或者 Devicemapper 作为你的 Docker 文件系统驱动。</p>
<blockquote>
<p>通常情况下， overlay2 会比 AUFS 和 Devicemapper 性能更好，而且更加稳定，因为 overlay2 在 inode 优化上更加高效。因此在生产环境中推荐使用 overlay2 作为 Docker 的文件驱动。</p>
</blockquote>
<p>下面我通过实例来教你如何初始化 /var/lib/docker 目录，为后面配置 Docker 的<code>overlay2</code>文件驱动做准备。</p>
<h4>准备 /var/lib/docker 目录</h4>
<p>1.使用 lsblk（Linux 查看磁盘和块设备信息命令）命令查看本机磁盘信息：</p>
<pre><code>$ lsblk

NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT

vda    253:0    0  500G  0 disk

`-vda1 253:1    0  500G  0 part /

vdb    253:16   0  500G  0 disk

`-vdb1 253:17   0    8G  0 part
</code></pre>
<p>可以看到，我的机器有两块磁盘，一块是 vda，一块是 vdb。其中 vda 已经被用来挂载系统根目录，这里我想把 /var/lib/docker 挂载到 vdb1 分区上。</p>
<p>2.使用 mkfs 命令格式化磁盘 vdb1：</p>
<pre><code>$ sudo mkfs.xfs -f -n ftype=1 /dev/vdb1
</code></pre>
<p>3.将挂载信息写入到 /etc/fstab，保证机器重启挂载目录不丢失：</p>
<pre><code>$ sudo echo &quot;/dev/vdb1 /var/lib/docker xfs defaults,pquota 0 0&quot; &gt;&gt; /etc/fstab
</code></pre>
<p>4.使用 mount 命令使得挂载目录生效：</p>
<pre><code>$ sudo mount -a
</code></pre>
<p>5.查看挂载信息：</p>
<pre><code>$ lsblk

NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT

vda    253:0    0  500G  0 disk

`-vda1 253:1    0  500G  0 part /

vdb    253:16   0  500G  0 disk

`-vdb1 253:17   0    8G  0 part /var/lib/docker
</code></pre>
<p>可以看到此时 /var/lib/docker 目录已经被挂载到了 vdb1 这个磁盘分区上。我们使用 xfs_info 命令验证下 d_type 是否已经成功开启：</p>
<pre><code>$ xfs_info /var/lib/docker | grep ftype

naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
</code></pre>
<p>可以看到输出结果为 ftype=1，证明 d_type 已经被成功开启。</p>
<p>准备好 /var/lib/docker 目录后，我们就可以配置 Docker 的文件驱动为 overlay2，并且启动 Docker 了。</p>
<h3>如何在 Docker 中配置 overlay2？</h3>
<p>当你的系统满足上面的条件后，就可以配置你的 Docker 存储驱动为 overlay2 了，具体配置步骤如下。</p>
<p>1.停止已经运行的 Docker：</p>
<pre><code>$ sudo systemctl stop docker
</code></pre>
<p>2.备份 /var/lib/docker 目录：</p>
<pre><code>$ sudo cp -au /var/lib/docker /var/lib/docker.back
</code></pre>
<p>3.在 /etc/docker 目录下创建 daemon.json 文件，如果该文件已经存在，则修改配置为以下内容：</p>
<pre><code>{

  &quot;storage-driver&quot;: &quot;overlay2&quot;,

  &quot;storage-opts&quot;: [

    &quot;overlay2.size=20G&quot;,

    &quot;overlay2.override_kernel_check=true&quot;

  ]

}
</code></pre>
<p>其中 storage-driver 参数指定使用 overlay2 文件驱动，overlay2.size 参数表示限制每个容器根目录大小为 20G。限制每个容器的磁盘空间大小是通过 xfs 的 pquota 特性实现，overlay2.size 可以根据不同的生产环境来设置这个值的大小。我推荐你在生产环境中开启此参数，防止某个容器写入文件过大，导致整个 Docker 目录空间溢出。</p>
<p>4.启动 Docker：</p>
<pre><code>$ sudo systemctl start docker
</code></pre>
<p>5.检查配置是否生效：</p>
<pre><code>$ docker info

Client:

 Debug Mode: false

Server:

 Containers: 1

  Running: 0

  Paused: 0

  Stopped: 1

 Images: 1

 Server Version: 19.03.12

 Storage Driver: overlay2

  Backing Filesystem: xfs

  Supports d_type: true

  Native Overlay Diff: true

 Logging Driver: json-file

 Cgroup Driver: cgroupfs

 ... 省略部分无用输出
</code></pre>
<p>可以看到 Storage Driver 已经变为 overlay2，并且 d_type 也是 true。至此，你的 Docker 已经配置完成。下面我们看下 overlay2 是如何工作的。</p>
<h3>overlay2 工作原理</h3>
<h4>overlay2 是如何存储文件的？</h4>
<p>overlay2 和 AUFS 类似，它将所有目录称之为层（layer），overlay2 的目录是镜像和容器分层的基础，而把这些层统一展现到同一的目录下的过程称为联合挂载（union mount）。overlay2 把目录的下一层叫作<code>lowerdir</code>，上一层叫作<code>upperdir</code>，联合挂载后的结果叫作<code>merged</code>。</p>
<blockquote>
<p>overlay2 文件系统最多支持 128 个层数叠加，也就是说你的 Dockerfile 最多只能写 128 行，不过这在日常使用中足够了。</p>
</blockquote>
<p>下面我们通过拉取一个 Ubuntu 操作系统的镜像来看下 overlay2 是如何存放镜像文件的。</p>
<p>首先，我们通过以下命令拉取 Ubuntu 镜像：</p>
<pre><code>$ docker pull ubuntu:16.04

16.04: Pulling from library/ubuntu

8e097b52bfb8: Pull complete

a613a9b4553c: Pull complete

acc000f01536: Pull complete

73eef93b7466: Pull complete

Digest: sha256:3dd44f7ca10f07f86add9d0dc611998a1641f501833692a2651c96defe8db940

Status: Downloaded newer image for ubuntu:16.04

docker.io/library/ubuntu:16.04
</code></pre>
<p>可以看到镜像一共被分为四层拉取，拉取完镜像后我们查看一下 overlay2 的目录：</p>
<pre><code>$ sudo ls -l /var/lib/docker/overlay2/

total 0

drwx------. 3 root root      47 Sep 13 08:16 01946de89606800dac8530e3480b32be9d7c66b493a1cdf558df52d7a1476d4a

drwx------. 4 root root      55 Sep 13 08:16 0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb

drwx------. 4 root root      72 Sep 13 08:16 94222a2fa3b2405cb00459285dd0d0ba7e6936d9b693ed18fbb0d08b93dc272f

drwx------. 4 root root      72 Sep 13 08:16 9d392cf38f245d37699bdd7672daaaa76a7d702083694fa8be380087bda5e396

brw-------. 1 root root 253, 17 Sep 13 08:14 backingFsBlockDev

drwx------. 2 root root     142 Sep 13 08:16 l
</code></pre>
<p>可以看到 overlay2 目录下出现了四个镜像层目录和一个<code>l</code>目录，我们首先来查看一下<code>l</code>目录的内容：</p>
<pre><code>$ sudo ls -l /var/lib/docker/overlay2/l

total 0

lrwxrwxrwx. 1 root root 72 Sep 13 08:16 FWGSYEA56RNMS53EUCKEQIKVLQ -&gt; ../9d392cf38f245d37699bdd7672daaaa76a7d702083694fa8be380087bda5e396/diff

lrwxrwxrwx. 1 root root 72 Sep 13 08:16 RNN2FM3YISKADNAZFRONVNWTIS -&gt; ../0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb/diff

lrwxrwxrwx. 1 root root 72 Sep 13 08:16 SHAQ5GYA3UZLJJVEGXEZM34KEE -&gt; ../01946de89606800dac8530e3480b32be9d7c66b493a1cdf558df52d7a1476d4a/diff

lrwxrwxrwx. 1 root root 72 Sep 13 08:16 VQSNH735KNX4YK2TCMBAJRFTGT -&gt; ../94222a2fa3b2405cb00459285dd0d0ba7e6936d9b693ed18fbb0d08b93dc272f/diff
</code></pre>
<p>可以看到<code>l</code>目录是一堆软连接，把一些较短的随机串软连到镜像层的 diff 文件夹下，这样做是为了避免达到<code>mount</code>命令参数的长度限制。
下面我们查看任意一个镜像层下的文件内容：</p>
<pre><code>$ sudo ls -l /var/lib/docker/overlay2/0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb/

total 8

drwxr-xr-x. 3 root root 17 Sep 13 08:16 diff

-rw-r--r--. 1 root root 26 Sep 13 08:16 link

-rw-r--r--. 1 root root 86 Sep 13 08:16 lower

drwx------. 2 root root  6 Sep 13 08:16 work
</code></pre>
<p><strong>镜像层的 link 文件内容为该镜像层的短 ID，diff 文件夹为该镜像层的改动内容，lower 文件为该层的所有父层镜像的短 ID。</strong>
我们可以通过<code>docker image inspect</code>命令来查看某个镜像的层级关系，例如我想查看刚刚下载的 Ubuntu 镜像之间的层级关系，可以使用以下命令：</p>
<pre><code>$ docker image inspect ubuntu:16.04

...省略部分输出

&quot;GraphDriver&quot;: {

            &quot;Data&quot;: {

                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/9d392cf38f245d37699bdd7672daaaa76a7d702083694fa8be380087bda5e396/diff:/var/lib/docker/overlay2/94222a2fa3b2405cb00459285dd0d0ba7e6936d9b693ed18fbb0d08b93dc272f/diff:/var/lib/docker/overlay2/01946de89606800dac8530e3480b32be9d7c66b493a1cdf558df52d7a1476d4a/diff&quot;,

                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb/merged&quot;,

                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb/diff&quot;,

                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb/work&quot;

            },

            &quot;Name&quot;: &quot;overlay2&quot;

        },

...省略部分输出
</code></pre>
<p>其中 MergedDir 代表当前镜像层在 overlay2 存储下的目录，LowerDir 代表当前镜像的父层关系，使用冒号分隔，冒号最后代表该镜像的最底层。</p>
<p>下面我们将镜像运行起来成为容器：</p>
<pre><code>$ docker run --name=ubuntu -d ubuntu:16.04 sleep 3600
</code></pre>
<p>我们使用<code>docker inspect</code>命令来查看一下容器的工作目录：</p>
<pre><code>$ docker inspect ubuntu

...省略部分输出

 &quot;GraphDriver&quot;: {

            &quot;Data&quot;: {

                &quot;LowerDir&quot;: &quot;/var/lib/docker/overlay2/4753c2aa5bdb20c97cddd6978ee3b1d07ef149e3cc2bbdbd4d11da60685fe9b2-init/diff:/var/lib/docker/overlay2/0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb/diff:/var/lib/docker/overlay2/9d392cf38f245d37699bdd7672daaaa76a7d702083694fa8be380087bda5e396/diff:/var/lib/docker/overlay2/94222a2fa3b2405cb00459285dd0d0ba7e6936d9b693ed18fbb0d08b93dc272f/diff:/var/lib/docker/overlay2/01946de89606800dac8530e3480b32be9d7c66b493a1cdf558df52d7a1476d4a/diff&quot;,

                &quot;MergedDir&quot;: &quot;/var/lib/docker/overlay2/4753c2aa5bdb20c97cddd6978ee3b1d07ef149e3cc2bbdbd4d11da60685fe9b2/merged&quot;,

                &quot;UpperDir&quot;: &quot;/var/lib/docker/overlay2/4753c2aa5bdb20c97cddd6978ee3b1d07ef149e3cc2bbdbd4d11da60685fe9b2/diff&quot;,

                &quot;WorkDir&quot;: &quot;/var/lib/docker/overlay2/4753c2aa5bdb20c97cddd6978ee3b1d07ef149e3cc2bbdbd4d11da60685fe9b2/work&quot;

            },

            &quot;Name&quot;: &quot;overlay2&quot;

        },

...省略部分输出
</code></pre>
<p><strong>MergedDir 后面的内容即为容器层的工作目录，LowerDir 为容器所依赖的镜像层目录。</strong> 然后我们查看下 overlay2 目录下的内容：</p>
<pre><code>$ sudo ls -l /var/lib/docker/overlay2/

total 0

drwx------. 3 root root      47 Sep 13 08:16 01946de89606800dac8530e3480b32be9d7c66b493a1cdf558df52d7a1476d4a

drwx------. 4 root root      72 Sep 13 08:47 0849daa41598a333101f6a411755907d182a7fcef780c7f048f15d335b774deb

drwx------. 5 root root      69 Sep 13 08:47 4753c2aa5bdb20c97cddd6978ee3b1d07ef149e3cc2bbdbd4d11da60685fe9b2

drwx------. 4 root root      72 Sep 13 08:47 4753c2aa5bdb20c97cddd6978ee3b1d07ef149e3cc2bbdbd4d11da60685fe9b2-init

drwx------. 4 root root      72 Sep 13 08:16 94222a2fa3b2405cb00459285dd0d0ba7e6936d9b693ed18fbb0d08b93dc272f

drwx------. 4 root root      72 Sep 13 08:16 9d392cf38f245d37699bdd7672daaaa76a7d702083694fa8be380087bda5e396

brw-------. 1 root root 253, 17 Sep 13 08:14 backingFsBlockDev

drwx------. 2 root root     210 Sep 13 08:47 l
</code></pre>
<p>可以看到 overlay2 目录下增加了容器层相关的目录，我们再来查看一下容器层下的内容：</p>
<pre><code>$ sudo ls -l /var/lib/docker/overlay2/4753c2aa5bdb20c97cddd6978ee3b1d07ef149e3cc2bbdbd4d11da60685fe9b2

total 8

drwxr-xr-x. 2 root root   6 Sep 13 08:47 diff

-rw-r--r--. 1 root root  26 Sep 13 08:47 link

-rw-r--r--. 1 root root 144 Sep 13 08:47 lower

drwxr-xr-x. 1 root root   6 Sep 13 08:47 merged

drwx------. 3 root root  18 Sep 13 08:47 work
</code></pre>
<p>link 和 lower 文件与镜像层的功能一致，****link 文件内容为该容器层的短 ID，lower 文件为该层的所有父层镜像的短 ID 。<strong>diff 目录为容器的读写层，容器内修改的文件都会在 diff 中出现，merged 目录为分层文件联合挂载后的结果，也是容器内的工作目录。</strong></p>
<p>总体来说，overlay2 是这样储存文件的：<code>overlay2</code>将镜像层和容器层都放在单独的目录，并且有唯一 ID，每一层仅存储发生变化的文件，最终使用联合挂载技术将容器层和镜像层的所有文件统一挂载到容器中，使得容器中看到完整的系统文件。</p>
<h4>overlay2 如何读取、修改文件？</h4>
<p>overlay2 的工作过程中对文件的操作分为读取文件和修改文件。</p>
<p><strong>读取文件</strong></p>
<p>容器内进程读取文件分为以下三种情况。</p>
<ul>
<li>文件在容器层中存在：当文件存在于容器层并且不存在于镜像层时，直接从容器层读取文件；</li>
<li>当文件在容器层中不存在：当容器中的进程需要读取某个文件时，如果容器层中不存在该文件，则从镜像层查找该文件，然后读取文件内容；</li>
<li>文件既存在于镜像层，又存在于容器层：当我们读取的文件既存在于镜像层，又存在于容器层时，将会从容器层读取该文件。</li>
</ul>
<p><strong>修改文件或目录</strong></p>
<p>overlay2 对文件的修改采用的是写时复制的工作机制，这种工作机制可以最大程度节省存储空间。具体的文件操作机制如下。</p>
<ul>
<li>第一次修改文件：当我们第一次在容器中修改某个文件时，overlay2 会触发写时复制操作，overlay2 首先从镜像层复制文件到容器层，然后在容器层执行对应的文件修改操作。</li>
</ul>
<blockquote>
<p>overlay2 写时复制的操作将会复制整个文件，如果文件过大，将会大大降低文件系统的性能，因此当我们有大量文件需要被修改时，overlay2 可能会出现明显的延迟。好在，写时复制操作只在第一次修改文件时触发，对日常使用没有太大影响。</p>
</blockquote>
<ul>
<li>删除文件或目录：当文件或目录被删除时，overlay2 并不会真正从镜像中删除它，因为镜像层是只读的，overlay2 会创建一个特殊的文件或目录，这种特殊的文件或目录会阻止容器的访问。</li>
</ul>
<h3>结语</h3>
<p>overlay2 目前已经是 Docker 官方推荐的文件系统了，也是目前安装 Docker 时默认的文件系统，因为 overlay2 在生产环境中不仅有着较高的性能，它的稳定性也极其突出。但是 overlay2 的使用还是有一些限制条件的，例如要求 Docker 版本必须高于 17.06.02，内核版本必须高于 4.0 等。因此，在生产环境中，如果你的环境满足使用 overlay2 的条件，请尽量使用 overlay2 作为 Docker 的联合文件系统。</p>
<p>那么你知道除了我介绍的这三种联合文件系统外，Docker 还可以使用哪些联合文件系统吗？ 思考后，可以把你的想法写在留言区。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;文件存储驱动：Devicemapper&#32;文件系统原理及生产环境的最佳配置.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;原理实践：自己动手使用&#32;Golang&#32;开发&#32;Docker（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435a0f9b2e645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
