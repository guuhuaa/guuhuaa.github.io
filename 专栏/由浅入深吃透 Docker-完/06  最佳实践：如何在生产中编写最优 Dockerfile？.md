<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>06  最佳实践：如何在生产中编写最优 Dockerfile？.md</title>
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

                    <a class="current-tab" href="06&#32;&#32;最佳实践：如何在生产中编写最优&#32;Dockerfile？.md">06  最佳实践：如何在生产中编写最优 Dockerfile？.md</a>
                    

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
                        <div><h1>06  最佳实践：如何在生产中编写最优 Dockerfile？</h1>
<p>在介绍 Dockerfile 最佳实践前，这里再强调一下，<strong>生产实践中一定优先使用 Dockerfile 的方式构建镜像。</strong> 因为使用 Dockerfile 构建镜像可以带来很多好处：</p>
<ul>
<li>易于版本化管理，Dockerfile 本身是一个文本文件，方便存放在代码仓库做版本管理，可以很方便地找到各个版本之间的变更历史；</li>
<li>过程可追溯，Dockerfile 的每一行指令代表一个镜像层，根据 Dockerfile 的内容即可很明确地查看镜像的完整构建过程；</li>
<li>屏蔽构建环境异构，使用 Dockerfile 构建镜像无须考虑构建环境，基于相同 Dockerfile 无论在哪里运行，构建结果都一致。</li>
</ul>
<p>虽然有这么多好处，但是如果你 Dockerfile 使用不当也会引发很多问题。比如镜像构建时间过长，甚至镜像构建失败；镜像层数过多，导致镜像文件过大。所以，这一课时我就教你如何在生产环境中编写最优的 Dockerfile。</p>
<p>在介绍 Dockerfile 最佳实践前，我们再聊一下我们平时书写 Dockerfile 应该尽量遵循的原则。</p>
<h3>Dockerfile 书写原则</h3>
<p>遵循以下 Dockerfile 书写原则，不仅可以使得我们的 Dockerfile 简洁明了，让协作者清楚地了解镜像的完整构建流程，还可以帮助我们减少镜像的体积，加快镜像构建的速度和分发速度。</p>
<h4>（1）单一职责</h4>
<p>由于容器的本质是进程，一个容器代表一个进程，因此不同功能的应用应该尽量拆分为不同的容器，每个容器只负责单一业务进程。</p>
<h4>（2）提供注释信息</h4>
<p>Dockerfile 也是一种代码，我们应该保持良好的代码编写习惯，晦涩难懂的代码尽量添加注释，让协作者可以一目了然地知道每一行代码的作用，并且方便扩展和使用。</p>
<h4>（3）保持容器最小化</h4>
<p>应该避免安装无用的软件包，比如在一个 nginx 镜像中，我并不需要安装 vim 、gcc 等开发编译工具。这样不仅可以加快容器构建速度，而且可以避免镜像体积过大。</p>
<h4>（4）合理选择基础镜像</h4>
<p>容器的核心是应用，因此只要基础镜像能够满足应用的运行环境即可。例如一个<code>Java</code>类型的应用运行时只需要<code>JRE</code>，并不需要<code>JDK</code>，因此我们的基础镜像只需要安装<code>JRE</code>环境即可。</p>
<h4>（5）使用 .dockerignore 文件</h4>
<p>在使用<code>git</code>时，我们可以使用<code>.gitignore</code>文件忽略一些不需要做版本管理的文件。同理，使用<code>.dockerignore</code>文件允许我们在构建时，忽略一些不需要参与构建的文件，从而提升构建效率。<code>.dockerignore</code>的定义类似于<code>.gitignore</code>。</p>
<p><code>.dockerignore</code>的本质是文本文件，Docker 构建时可以使用换行符来解析文件定义，每一行可以忽略一些文件或者文件夹。具体使用方式如下：</p>
<table>
<thead>
<tr>
<th>规则</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td>#</td>
<td># 开头的表示注释，# 后面所有内容将会被忽略</td>
</tr>
<tr>
<td><em>/tmp</em></td>
<td>匹配当前目录下任何以 tmp 开头的文件或者文件夹</td>
</tr>
<tr>
<td>*.md</td>
<td>匹配以 .md 为后缀的任意文件</td>
</tr>
<tr>
<td>tem?</td>
<td>匹配以 tem 开头并且以任意字符结尾的文件，？代表任意一个字符</td>
</tr>
<tr>
<td>!README.md</td>
<td>! 表示排除忽略。 例如 .dockerignore 定义如下：  *.md !README.md  表示除了 README.md 文件外所有以 .md 结尾的文件。</td>
</tr>
</tbody>
</table>
<h4>（6）尽量使用构建缓存</h4>
<p>Docker 构建过程中，每一条 Dockerfile 指令都会提交为一个镜像层，下一条指令都是基于上一条指令构建的。如果构建时发现要构建的镜像层的父镜像层已经存在，并且下一条命令使用了相同的指令，即可命中构建缓存。</p>
<p>Docker 构建时判断是否需要使用缓存的规则如下：</p>
<ul>
<li>从当前构建层开始，比较所有的子镜像，检查所有的构建指令是否与当前完全一致，如果不一致，则不使用缓存；</li>
<li>一般情况下，只需要比较构建指令即可判断是否需要使用缓存，但是有些指令除外（例如<code>ADD</code>和<code>COPY</code>）；</li>
<li>对于<code>ADD</code>和<code>COPY</code>指令不仅要校验命令是否一致，还要为即将拷贝到容器的文件计算校验和（根据文件内容计算出的一个数值，如果两个文件计算的数值一致，表示两个文件内容一致 ），命令和校验和完全一致，才认为命中缓存。</li>
</ul>
<p>因此，基于 Docker 构建时的缓存特性，我们可以把不轻易改变的指令放到 Dockerfile 前面（例如安装软件包），而可能经常发生改变的指令放在 Dockerfile 末尾（例如编译应用程序）。</p>
<p>例如，我们想要定义一些环境变量并且安装一些软件包，可以按照如下顺序编写 Dockerfile：</p>
<pre><code>FROM centos:7
# 设置环境变量指令放前面
ENV PATH /usr/local/bin:$PATH
# 安装软件指令放前面
RUN yum install -y make
# 把业务软件的配置,版本等经常变动的步骤放最后
...
</code></pre>
<p>按照上面原则编写的 Dockerfile 在构建镜像时，前面步骤命中缓存的概率会增加，可以大大缩短镜像构建时间。</p>
<h4>（7）正确设置时区</h4>
<p>我们从 Docker Hub 拉取的官方操作系统镜像大多数都是 UTC 时间（世界标准时间）。如果你想要在容器中使用中国区标准时间（东八区），请根据使用的操作系统修改相应的时区信息，下面我介绍几种常用操作系统的修改方式：</p>
<ul>
<li><strong>Ubuntu 和Debian 系统</strong></li>
</ul>
<p>Ubuntu 和Debian 系统可以向 Dockerfile 中添加以下指令：</p>
<pre><code>RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo &quot;Asia/Shanghai&quot; &gt;&gt; /etc/timezone
</code></pre>
<ul>
<li><strong>CentOS系统</strong></li>
</ul>
<p>CentOS 系统则向 Dockerfile 中添加以下指令：</p>
<pre><code>RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
</code></pre>
<h4>（8）使用国内软件源加快镜像构建速度</h4>
<p>由于我们常用的官方操作系统镜像基本都是国外的，软件服务器大部分也在国外，所以我们构建镜像的时候想要安装一些软件包可能会非常慢。</p>
<p>这里我以 CentOS 7 为例，介绍一下如何使用 163 软件源（国内有很多大厂，例如阿里、腾讯、网易等公司都免费提供的软件加速源）加快镜像构建。</p>
<p>首先在容器构建目录创建文件 CentOS7-Base-163.repo，文件内容如下：</p>
<pre><code># CentOS-Base.repo
#
# The mirror system uses the connecting IP address of the client and the
# update status of each mirror to pick mirrors that are updated to and
# geographically close to the client.  You should use this for CentOS updates
# unless you are manually picking other mirrors.
#
# If the mirrorlist= does not work for you, as a fall back you can try the 
# remarked out baseurl= line instead.
#
#
[base]
name=CentOS-$releasever - Base - 163.com
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&amp;arch=$basearch&amp;repo=os
baseurl=http://mirrors.163.com/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
#released updates
[updates]
name=CentOS-$releasever - Updates - 163.com
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&amp;arch=$basearch&amp;repo=updates
baseurl=http://mirrors.163.com/centos/$releasever/updates/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
#additional packages that may be useful
[extras]
name=CentOS-$releasever - Extras - 163.com
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&amp;arch=$basearch&amp;repo=extras
baseurl=http://mirrors.163.com/centos/$releasever/extras/$basearch/
gpgcheck=1
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus - 163.com
baseurl=http://mirrors.163.com/centos/$releasever/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=http://mirrors.163.com/centos/RPM-GPG-KEY-CentOS-7
</code></pre>
<p>然后在 Dockerfile 中添加如下指令：</p>
<pre><code>COPY CentOS7-Base-163.repo /etc/yum.repos.d/CentOS7-Base.repo
</code></pre>
<p>执行完上述步骤后，再使用<code>yum install</code>命令安装软件时就会默认从 163 获取软件包，这样可以大大提升构建速度。</p>
<h4>（9）最小化镜像层数</h4>
<p>在构建镜像时尽可能地减少 Dockerfile 指令行数。例如我们要在 CentOS 系统中安装<code>make</code>和<code>net-tools</code>两个软件包，应该在 Dockerfile 中使用以下指令：</p>
<pre><code>RUN yum install -y make net-tools
</code></pre>
<p>而不应该写成这样：</p>
<pre><code>RUN yum install -y make
RUN yum install -y make
</code></pre>
<p>了解完 Dockerfile 的书写原则后，我们再来具体了解下这些原则落实到具体的 Dockerfile 指令应该如何书写。</p>
<h3>Dockerfile 指令书写建议</h3>
<p>下面是我们常用的一些指令，这些指令对于刚接触 Docker 的人来说会非常容易出错，下面我对这些指令的书写建议详细讲解一下。</p>
<h4>（1）RUN</h4>
<p><code>RUN</code>指令在构建时将会生成一个新的镜像层并且执行<code>RUN</code>指令后面的内容。</p>
<p>使用<code>RUN</code>指令时应该尽量遵循以下原则：</p>
<ul>
<li>当<code>RUN</code>指令后面跟的内容比较复杂时，建议使用反斜杠（\） 结尾并且换行；</li>
<li><code>RUN</code>指令后面的内容尽量按照字母顺序排序，提高可读性。</li>
</ul>
<p>例如，我想在官方的 CentOS 镜像下安装一些软件，一个建议的 Dockerfile 指令如下：</p>
<pre><code>FROM centos:7
RUN yum install -y automake \
                   curl \
                   python \
                   vim
</code></pre>
<h4>（2）CMD 和 ENTRYPOINT</h4>
<p><code>CMD</code>和<code>ENTRYPOINT</code>指令都是容器运行的命令入口，这两个指令使用中有很多相似的地方，但是也有一些区别。</p>
<p>这两个指令的相同之处，<code>CMD</code>和<code>ENTRYPOINT</code>的基本使用格式分为两种。</p>
<ul>
<li>第一种为<code>CMD</code>/<code>ENTRYPOINT</code>[&quot;command&quot; , &quot;param&quot;]。这种格式是使用 Linux 的<code>exec</code>实现的， 一般称为<code>exec</code>模式，这种书写格式为<code>CMD</code>/<code>ENTRYPOINT</code>后面跟 json 数组，也是Docker 推荐的使用格式。</li>
<li>另外一种格式为<code>CMD</code>/<code>ENTRYPOINT</code>command param ，这种格式是基于 shell 实现的， 通常称为<code>shell</code>模式。当使用<code>shell</code>模式时，Docker 会以 /bin/sh -c command 的方式执行命令。</li>
</ul>
<p>这两个指令的区别：</p>
<ul>
<li>Dockerfile 中如果使用了<code>ENTRYPOINT</code>指令，启动 Docker 容器时需要使用 --entrypoint 参数才能覆盖 Dockerfile 中的<code>ENTRYPOINT</code>指令 ，而使用<code>CMD</code>设置的命令则可以被<code>docker run</code>后面的参数直接覆盖。</li>
<li><code>ENTRYPOINT</code>指令可以结合<code>CMD</code>指令使用，也可以单独使用，而<code>CMD</code>指令只能单独使用。</li>
</ul>
<p>看到这里你也许会问，我什么时候应该使用<code>ENTRYPOINT</code>,什么时候使用<code>CMD</code>呢？</p>
<p>如果你希望你的镜像足够灵活，推荐使用<code>CMD</code>指令。如果你的镜像只执行单一的具体程序，并且不希望用户在执行<code>docker run</code>时覆盖默认程序，建议使用<code>ENTRYPOINT</code>。</p>
<p>最后再强调一下，无论使用<code>CMD</code>还是<code>ENTRYPOINT</code>，都尽量使用<code>exec</code>模式。</p>
<h4>（3）ADD 和 COPY</h4>
<p><code>ADD</code>和<code>COPY</code>指令功能类似，都是从外部往容器内添加文件。但是<code>COPY</code>指令只支持基本的文件和文件夹拷贝功能，<code>ADD</code>则支持更多文件来源类型，比如自动提取 tar 包，并且可以支持源文件为 URL 格式。</p>
<p>那么在日常应用中，我们应该使用哪个命令向容器里添加文件呢？你可能在想，既然<code>ADD</code>指令支持的功能更多，当然应该使用<code>ADD</code>指令了。然而事实恰恰相反，我更推荐你使用<code>COPY</code>指令，因为<code>COPY</code>指令更加透明，仅支持本地文件向容器拷贝，而且使用<code>COPY</code>指令可以更好地利用构建缓存，有效减小镜像体积。</p>
<p>当你想要使用<code>ADD</code>向容器中添加 URL 文件时，请尽量考虑使用其他方式替代。例如你想要在容器中安装 memtester（一种内存压测工具），你应该避免使用以下格式：</p>
<pre><code>ADD http://pyropus.ca/software/memtester/old-versions/memtester-4.3.0.tar.gz /tmp/
RUN tar -xvf /tmp/memtester-4.3.0.tar.gz -C /tmp
RUN make -C /tmp/memtester-4.3.0 &amp;&amp; make -C /tmp/memtester-4.3.0 install
</code></pre>
<p>下面是推荐写法：</p>
<pre><code>RUN wget -O /tmp/memtester-4.3.0.tar.gz http://pyropus.ca/software/memtester/old-versions/memtester-4.3.0.tar.gz \
&amp;&amp; tar -xvf /tmp/memtester-4.3.0.tar.gz -C /tmp \
&amp;&amp; make -C /tmp/memtester-4.3.0 &amp;&amp; make -C /tmp/memtester-4.3.0 install
</code></pre>
<h4>（4）WORKDIR</h4>
<p>为了使构建过程更加清晰明了，推荐使用 WORKDIR 来指定容器的工作路径，应该尽量避免使用 RUN cd /work/path &amp;&amp; do some work 这样的指令。</p>
<p>最后给出几个常用软件的官方 Dockerfile 示例链接，希望可以对你有所帮助。</p>
<ul>
<li><a href="https://github.com/docker-library/golang/blob/4d68c4dd8b51f83ce4fdce0f62484fdc1315bfa8/1.15/buster/Dockerfile">Go</a></li>
<li><a href="https://github.com/nginxinc/docker-nginx/blob/9774b522d4661effea57a1fbf64c883e699ac3ec/mainline/buster/Dockerfile">Nginx</a></li>
<li><a href="https://github.com/hylang/docker-hylang/blob/f9c873b7f71f466e5af5ea666ed0f8f42835c688/dockerfiles-generated/Dockerfile.python3.8-buster">Hy</a></li>
</ul>
<h3>结语</h3>
<p>好了，到此为止，相信你已经对 Dockerfile 的书写原则和一些重要指令有了较深的认识。</p>
<p>当你需要编写编译型语言（例如 Golang、Java）的 Dockerfile 时，如何分离编译环境和运行环境，使得镜像体积尽可能小呢？思考后，可以把你的想法写在留言区。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="05&#32;&#32;仓库访问：怎样搭建属于你的私有仓库？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="07&#32;&#32;Docker&#32;安全：基于内核的弱隔离系统如何保障安全性？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4359c6d9ba645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
