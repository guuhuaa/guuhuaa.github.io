<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13  数据存储：剖析 Docker 卷与持久化数据存储的底层原理.md</title>
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

                    <a class="current-tab" href="13&#32;&#32;数据存储：剖析&#32;Docker&#32;卷与持久化数据存储的底层原理.md">13  数据存储：剖析 Docker 卷与持久化数据存储的底层原理.md</a>
                    

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
                        <div><h1>13  数据存储：剖析 Docker 卷与持久化数据存储的底层原理</h1>
<p>上一课时我介绍了 Docker 网络实现，为我们的容器插上了网线。这一课时我将介绍 Docker 的卷，为我们的容器插上磁盘，实现容器数据的持久化。</p>
<h3>为什么容器需要持久化存储</h3>
<p>容器按照业务类型，总体可以分为两类：</p>
<ul>
<li>无状态的（数据不需要被持久化）</li>
<li>有状态的（数据需要被持久化）</li>
</ul>
<p>显然，容器更擅长无状态应用。因为未持久化数据的容器根目录的生命周期与容器的生命周期一样，容器文件系统的本质是在镜像层上面创建的读写层，运行中的容器对任何文件的修改都存在于该读写层，当容器被删除时，容器中的读写层也会随之消失。</p>
<p>虽然容器希望所有的业务都尽量保持无状态，这样容器就可以开箱即用，并且可以任意调度，但实际业务总是有各种需要数据持久化的场景，比如 MySQL、Kafka 等有状态的业务。因此为了解决有状态业务的需求，Docker 提出了卷（Volume）的概念。</p>
<p>什么是卷？卷的本质是文件或者目录，它可以绕过默认的联合文件系统，直接以文件或目录的形式存在于宿主机上。卷的概念不仅解决了数据持久化的问题，还解决了容器间共享数据的问题。使用卷可以将容器内的目录或文件持久化，当容器重启后保证数据不丢失，例如我们可以使用卷将 MySQL 的目录持久化，实现容器重启数据库数据不丢失。</p>
<p>Docker 提供了卷（Volume）的功能，使用<code>docker volume</code>命令可以实现对卷的创建、查看和删除等操作。下面我们来详细了解一下这些命令。</p>
<h3>Docker 卷的操作</h3>
<h4>创建数据卷</h4>
<p>使用<code>docker volume create</code>命令可以创建一个数据卷。</p>
<p>我们使用以下命令创建一个名为 myvolume 的数据卷：</p>
<pre><code>$ docker volume create myvolume
</code></pre>
<p>在这里要说明下，默认情况下 ，Docker 创建的数据卷为 local 模式，仅能提供本主机的容器访问。如果想要实现远程访问，需要借助网络存储来实现。Docker 的 local 存储模式并未提供配额管理，因此在生产环境中需要手动维护磁盘存储空间。</p>
<p>除了使用<code>docker volume create</code>的方式创建卷，我们还可以在 Docker 启动时使用 -v 的方式指定容器内需要被持久化的路径，Docker 会自动为我们创建卷，并且绑定到容器中，使用命令如下：</p>
<pre><code>$ docker run -d --name=nginx-volume -v /usr/share/nginx/html nginx
</code></pre>
<p>使用以上命令，我们启动了一个 nginx 容器，<code>-v</code>参数使得 Docker 自动生成一个卷并且绑定到容器的 /usr/share/nginx/html 目录中。
我们可以使用<code>docker volume ls</code>命令来查看下主机上的卷：</p>
<pre><code>$ docker volume ls

DRIVER              VOLUME NAME

local               eaa8a223eb61a2091bf5cd5247c1b28ac287450a086d6eee9632d9d1b9f69171
</code></pre>
<p>可以看到，Docker 自动为我们创建了一个名称为随机 ID 的卷。</p>
<h4>查看数据卷</h4>
<p>已经创建的数据卷可以使用 docker volume ls 命令查看。</p>
<pre><code>$ docker volume ls

DRIVER              VOLUME NAME

local               myvolume
</code></pre>
<p>通过输出可以看到 myvolume 卷已经创建成功。
如果想要查看某个数据卷的详细信息，可以使用<code>docker volume inspect</code>命令。例如，我想查看 myvolume 的详细信息，命令如下：</p>
<pre><code>$ docker volume inspect myvolume

    {

        &quot;CreatedAt&quot;: &quot;2020-09-08T09:10:50Z&quot;,

        &quot;Driver&quot;: &quot;local&quot;,

        &quot;Labels&quot;: {},

        &quot;Mountpoint&quot;: &quot;/var/lib/docker/volumes/myvolume/_data&quot;,

        &quot;Name&quot;: &quot;myvolume&quot;,

        &quot;Options&quot;: {},

        &quot;Scope&quot;: &quot;local&quot;

    }

]
</code></pre>
<p>通过<code>docker volume inspect</code>命令可以看到卷的创建日期、命令、挂载路径信息。</p>
<h4>使用数据卷</h4>
<p>使用<code>docker volume</code>创建的卷在容器启动时，添加 --mount 参数指定卷的名称即可使用。</p>
<p>这里我们使用上一步创建的卷来启动一个 nginx 容器，并将 /usr/share/nginx/html 目录与卷关联，命令如下：</p>
<pre><code>$ docker run -d --name=nginx --mount source=myvolume,target=/usr/share/nginx/html nginx
</code></pre>
<p>使用 Docker 的卷可以实现指定目录的文件持久化，下面我们进入容器中并且修改 index.html 文件内容，命令如下：</p>
<pre><code>$ docker exec -it  nginx bash

## 使用以下内容直接替换 /usr/share/nginx/html/index.html 文件 

<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="97e5f8f8e3d7a0a6aef3a4f4a4a5f2a5a6a6">[email&#160;protected]</a>:/# cat &lt;&lt;EOF &gt;/usr/share/nginx/html/index.html

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

&lt;title&gt;Hello, Docker Volume!&lt;/title&gt;

&lt;style&gt;

    body {

        width: 35em;

        margin: 0 auto;

        font-family: Tahoma, Verdana, Arial, sans-serif;

    }

&lt;/style&gt;

&lt;/head&gt;

&lt;body&gt;

&lt;h1&gt;Hello, Docker Volume!&lt;/h1&gt;

&lt;/body&gt;

&lt;/html&gt;

EOF
</code></pre>
<p>此时我们使用<code>docker rm</code>命令将运行中的 nginx 容器彻底删除。</p>
<pre><code>$ docker rm -f nginx
</code></pre>
<p>旧的 nginx 容器删除后，我们再使用<code>docker run</code>命令启动一个新的容器，并且挂载 myvolume 卷，命令如下。</p>
<pre><code>$ docker run -d --name=nginx --mount source=myvolume,target=/usr/share/nginx/html nginx
</code></pre>
<p>新容器启动后，我们进入容器查看一下 index.html 文件内容：</p>
<pre><code>$ docker exec -it nginx bash

<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f88a97978cb8cf9e9e999bcecccd9ecccbc9">[email&#160;protected]</a>:/# cat /usr/share/nginx/html/index.html

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

&lt;title&gt;Hello, Docker Volume!&lt;/title&gt;

&lt;style&gt;

    body {

        width: 35em;

        margin: 0 auto;

        font-family: Tahoma, Verdana, Arial, sans-serif;

    }

&lt;/style&gt;

&lt;/head&gt;

&lt;body&gt;

&lt;h1&gt;Hello, Docker Volume!&lt;/h1&gt;

&lt;/body&gt;

&lt;/html&gt;
</code></pre>
<p>可以看到，此时 index.html 文件内容依旧为我们之前写入的内容。可见，使用 Docker 卷后我们的数据并没有随着容器的删除而消失。</p>
<h4>删除数据卷</h4>
<p>容器的删除并不会自动删除已经创建的数据卷，因此不再使用的数据卷需要我们手动删除，删除的命令为 docker volume rm 。例如，我们想要删除上面创建 myvolume 数据卷，可以使用以下命令：</p>
<pre><code>$ docker volume rm myvolume
</code></pre>
<p>这里需要注意，正在被使用中的数据卷无法删除，如果你想要删除正在使用中的数据卷，需要先删除所有关联的容器。</p>
<p>有时候，两个容器之间会有共享数据的需求，很典型的一个场景就是容器内产生的日志需要一个专门的日志采集程序去采集日志内容，例如我需要使用 Filebeat (一种日志采集工具)采集 nginx 容器内的日志，我就需要使用卷来共享一个日志目录，从而使得 Filebeat 和 nginx 容器都可以访问到这个目录，这时就需要用到容器之间共享数据卷的方式。</p>
<h4>容器与容器之间数据共享</h4>
<p>那如何实现容器与容器之间数据共享呢？下面我举例说明。</p>
<p>首先使用<code>docker volume create</code>命令创建一个共享日志的数据卷。</p>
<pre><code>$ docker volume create log-vol
</code></pre>
<p>启动一个生产日志的容器（下面用 producer 窗口来表示）：</p>
<pre><code>$ docker run --mount source=log-vol,target=/tmp/log --name=log-producer -it busybox
</code></pre>
<p>然后新打开一个命令行窗口，启动一个消费者容器（下面用 consumer 窗口来表示）：</p>
<pre><code>docker run -it --name consumer --volumes-from log-producer  busybox
</code></pre>
<p>使用<code>volumes-from</code>参数可以在启动新的容器时来挂载已经存在的容器的卷，<code>volumes-from</code>参数后面跟已经启动的容器名称。
下面我们切换到 producer 窗口，使用以下命令创建一个 mylog.log 文件并写入 &quot;Hello，My log.&quot; 的内容：</p>
<pre><code>/ # cat &lt;&lt;EOF &gt;/tmp/log/mylog.log

Hello, My log.

EOF
</code></pre>
<p>然后我们切换到 consumer 窗口，查看一下相关内容：</p>
<pre><code>/ # cat /tmp/log/mylog.log

Hello, My log.
</code></pre>
<p>可以看到我们从 producer 容器写入的文件内容会自动出现在 consumer 容器中，证明我们成功实现了两个容器间的数据共享。</p>
<p>总结一下，我们首先使用 docker volume create 命令创建了 log-vol 卷来作为共享目录，log-producer 容器向该卷写入数据，consumer 容器从该卷读取数据。这就像主机上的两个进程，一个向主机目录写数据，一个从主机目录读数据，利用主机的目录，实现了容器之间的数据共享。</p>
<h4>主机与容器之间数据共享</h4>
<p>Docker 卷的目录默认在 /var/lib/docker 下，当我们想把主机的其他目录映射到容器内时，就需要用到主机与容器之间数据共享的方式了，例如我想把 MySQL 容器中的 /var/lib/mysql 目录映射到主机的 /var/lib/mysql 目录中，我们就可以使用主机与容器之间数据共享的方式来实现。</p>
<p>要实现主机与容器之间数据共享，其实很简单，只需要我们在启动容器的时候添加<code>-v</code>参数即可, 使用格式为：<code>-v HOST_PATH:CONTIANAER_PATH</code>。</p>
<p>例如，我想挂载主机的 /data 目录到容器中的 /usr/local/data 中，可以使用以下命令来启动容器：</p>
<pre><code>$ docker run -v /data:/usr/local/data -it busybox
</code></pre>
<p>容器启动后，便可以在容器内的 /usr/local/data 访问到主机 /data 目录的内容了，并且容器重启后，/data 目录下的数据也不会丢失。</p>
<p>以上就是 Docker 卷的操作，关键命令我帮你总结如下：</p>
<p><img src="assets/Ciqc1F-BW1SAQEkaAACOwJuMTHI950.png" alt="Lark20201010-145710.png" /></p>
<p>那你了解完卷的相关操作后，你有没有想过 Docker 的卷是怎么实现的呢？接下来我们就看看卷的实现原理。</p>
<h3>Docker 卷的实现原理</h3>
<p>在了解 Docker 卷的原理之前，我们先来回顾一下镜像和容器的文件系统原理。</p>
<blockquote>
<p><strong>镜像和容器的文件系统原理：</strong> 镜像是由多层文件系统组成的，当我们想要启动一个容器时，Docker 会在镜像上层创建一个可读写层，容器中的文件都工作在这个读写层中，当容器删除时，与容器相关的工作文件将全部丢失。</p>
</blockquote>
<p>Docker 容器的文件系统不是一个真正的文件系统，而是通过联合文件系统实现的一个伪文件系统，而 Docker 卷则是直接利用主机的某个文件或者目录，它可以绕过联合文件系统，直接挂载主机上的文件或目录到容器中，这就是它的工作原理。</p>
<p>下面，我们通过一个实例来说明卷的工作原理。首先，我们创建一个名称为 volume-data 的卷：</p>
<pre><code>$ docker volume create volume-data
</code></pre>
<p>我们使用 ls 命令查看一下 /var/lib/docker/volumes 目录下的内容：</p>
<pre><code>$ sudo ls -l /var/lib/docker/volumes

drwxr-xr-x. 3 root root    19 Sep  8 10:59 volume-data
</code></pre>
<p>然后再看下 volume-data 目录下有什么内容：</p>
<pre><code>$ sudo ls -l /var/lib/docker/volumes/volume-data

total 0

drwxr-xr-x. 2 root root 6 Sep  8 10:59 _data
</code></pre>
<p>可以看到我们创建的卷出现在了 /var/lib/docker/volumes 目录下，并且 volume-data 目录下还创建了一个 _data 目录。</p>
<p>实际上，在我们创建 Docker 卷时，Docker 会把卷的数据全部放在 /var/lib/docker/volumes 目录下，并且在每个对应的卷的目录下创建一个 _data 目录，然后把 _data 目录绑定到容器中。因此我们在容器中挂载卷的目录下操作文件，实际上是在操作主机上的 _data 目录。为了证实我的说法，我们来实际演示下。</p>
<p>首先，我们启动一个容器，并且绑定 volume-data 卷到容器内的 /data 目录下：</p>
<pre><code>$  docker run -it --mount source=volume-data,target=/data busybox

/ #
</code></pre>
<p>我们进入到容器的 /data 目录，创建一个 data.log 文件:</p>
<pre><code>/ # cd data/

/data # touch data.log
</code></pre>
<p>然后我们新打开一个命令行窗口，查看一下主机上的文件内容：</p>
<pre><code>$  sudo ls -l /var/lib/docker/volumes/volume-data/_data

total 0

-rw-r--r--. 1 root root 0 Sep  8 11:15 data.log
</code></pre>
<p>可以看到主机上的 _data 目录下也出现了 data.log 文件。这说明，在容器内操作卷挂载的目录就是直接操作主机上的 _data 目录，符合我上面的说法。</p>
<p>综上，<strong>Docker 卷的实现原理是在主机的 /var/lib/docker/volumes 目录下，根据卷的名称创建相应的目录，然后在每个卷的目录下创建 _data 目录，在容器启动时如果使用 --mount 参数，Docker 会把主机上的目录直接映射到容器的指定目录下，实现数据持久化。</strong></p>
<h3>结语</h3>
<p>到此，相信你已经了解了 Docker 使用卷做持久化存储的必要性，也了解 Docker 卷的常用操作，并且对卷的实现原理也有了较清晰的认识。</p>
<p>那么，你知道 Docker 如何使用卷来挂载 NFS 类型的持久化存储到容器内吗？思考后，把你的想法写在留言区。</p>
<p>下一课时，我将讲解 Docker 文件存储驱动 AUFS 的系统原理及生产环境的最佳配置。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;&#32;网络模型：剖析&#32;Docker&#32;网络实现及&#32;Libnetwork&#32;底层原理.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;&#32;文件存储驱动：AUFS&#32;文件系统原理及生产环境的最佳配置.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359f77aeb645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
