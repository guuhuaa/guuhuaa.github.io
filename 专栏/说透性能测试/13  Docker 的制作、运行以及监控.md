<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13  Docker 的制作、运行以及监控.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么每个测试人都要学好性能测试？.md">00 开篇词  为什么每个测试人都要学好性能测试？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;JMeter&#32;的核心概念.md">01  JMeter 的核心概念.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;JMeter&#32;参数化策略.md">02  JMeter 参数化策略.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;构建并执行&#32;JMeter&#32;脚本的正确姿势.md">03  构建并执行 JMeter 脚本的正确姿势.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;JMeter&#32;二次开发其实并不难.md">04  JMeter 二次开发其实并不难.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;如何基于&#32;JMeter&#32;API&#32;开发性能测试平台？.md">05  如何基于 JMeter API 开发性能测试平台？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Nginx&#32;在系统架构中的作用.md">06  Nginx 在系统架构中的作用.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;你真的知道如何制定性能测试的目标吗？.md">07  你真的知道如何制定性能测试的目标吗？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;性能测试场景的分类和意义.md">08  性能测试场景的分类和意义.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;如何制定一份有效的性能测试方案？.md">09  如何制定一份有效的性能测试方案？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;命令行监控&#32;Linux&#32;服务器的要点.md">10  命令行监控 Linux 服务器的要点.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;分布式服务链路监控以及报警方案.md">11  分布式服务链路监控以及报警方案.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何把可视化监控也做得酷炫？.md">12  如何把可视化监控也做得酷炫？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="13&#32;&#32;Docker&#32;的制作、运行以及监控.md">13  Docker 的制作、运行以及监控.md</a>
                    

                </li>
                <li>

                    
                    <a href="14&#32;&#32;如何从&#32;CPU&#32;飙升定位到热点方法？.md">14  如何从 CPU 飙升定位到热点方法？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;如何基于&#32;JVM&#32;分析内存使用对象？.md">15  如何基于 JVM 分析内存使用对象？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;如何通过&#32;Arthas&#32;定位代码链路问题？.md">16  如何通过 Arthas 定位代码链路问题？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;如何应对&#32;Redis&#32;缓存穿透、击穿和雪崩？.md">17  如何应对 Redis 缓存穿透、击穿和雪崩？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何才能优化&#32;MySQL&#32;性能？.md">18  如何才能优化 MySQL 性能？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何根治慢&#32;SQL？.md">19  如何根治慢 SQL？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;结束语&#32;&#32;线上全链路性能测试实践总结.md">20 结束语  线上全链路性能测试实践总结.md</a>

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
                        <div><h1>13  Docker 的制作、运行以及监控</h1>
<p>模块三主要讲解了不同层级的监控以及监控的方式，作为模块三的最后一讲，我将带你来学习 Docker 的制作、运行以及监控。对于很多测试来说，经常听到 Docker 容器，但自己好像又不是很熟悉，只是用相关命令去查询日志等，而对于为什么要使用 Docker 还不是特别清楚。其实 Docker 并不难学，有时候你只是差一个学习的切入点，这一讲我会从测试的使用层面带你学习下 Docker 的要点知识，希望作为一名测试的你，对 Docker 也不会再陌生。</p>
<h3>为什么要使用 Docker？</h3>
<p>你可以回忆下 Docker 的图标（如图 1 所示），是不是像一条船上装了很多集装箱，其实这和Docker 的设计思想有关系，集装箱能解决什么问题呢？就是货物的隔离，如果我们把食物和化学品分别放在两个集装箱中用一艘轮船运走则无妨，但是你不可以把它们放在同一个集装箱中，其实对于 Docker 设计也是如此。</p>
<p><strong>操作系统就相当于这艘轮船</strong>，上面可以有很多集装箱，即 Docker，你可以把 Docker 看作是独立的子环境，有独立的系统和应用，比如经常因为一些历史原因开发的多个模块依赖于不同的 JDK 版本，将这两个模块部署在一台 Linux 服务器上可能很容易出问题，但是如果以 Docker 的方式便很容易解决版本冲突的问题。</p>
<p><img src="assets/Cgp9HWAs40-AKWVUAAI_WngHwng787.png" alt="Drawing 0.png" /></p>
<p>图 1：Docker 图标</p>
<h3>Docker 的用法（基于 CentOS 7.0）</h3>
<p>如何学习 Docker 呢？<strong>从应用技术维度来看它是一个容器</strong>，<strong>从学习角度来看它就是一种工具。</strong></p>
<p>对于工具的学习我认为从实际的例子切入是最有代入感的，接下来我就在 CentOS 环境下安装一个基于 Ubuntu 的 Docker 环境，带你从使用层面了解下 Docker，知道 Docker 最基本的安装方式，如下所示：</p>
<pre><code>yum install -y docker  //安装Docker

service docker status //查看Docker运行状态
</code></pre>
<p>接下来运行一个 Docker 容器，我目前用的是 CentOS 系统，可现在还需要一个 Ubuntu 环境，我就需要通过如下命令基于 Ubuntu 镜像启动一个容器：</p>
<pre><code>docker run -i -t ubuntu /bin/bash
</code></pre>
<p>通过这个命令，就直接创建了基于 Ubuntu 的 Docker 环境，并直接进入了交互 shell，这样你就<strong>可以认为是在 Ubuntu 系统下工作了</strong>，通过如下命令可以查看版本号：</p>
<pre><code><a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9be9f4f4efdbfaf8a8a3acaffaa2ada3a2ab">[email&#160;protected]</a>:/# cat /etc/issue

Ubuntu 20.04.1 LTS
</code></pre>
<p>同样的道理，如果你的 Java 服务有的依赖 JDK1.7，有的依赖 JDK1.8，则可以通过 Docker 来做不一样的服务。</p>
<p>上面就是一个简单的实例，在 CentOS 系统里创建一个基于 Docker 的 Ubuntu 系统以实现你特定的需求。</p>
<p>我们再来看看 Docker 常用的命令有哪些，这些可能是你和 Docker 打交道的过程中最常见的命令。</p>
<p>对于 Docker 的命令，都是在 Linux 终端直接输出就可以，比如查看 Docker 镜像，就是直接输出 docker images，展示信息如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3d4f5252497d7779">[email&#160;protected]</a> ~]# docker images

REPOSITORY                     TAG          IMAGE ID    CREATED             SIZE

docker.io/ubuntu              latest        f643c72bc252

3 weeks ago        72.9 MB

docker.io/gitlab/gitlab-ce    latest        6e2336419031

8 months ago       1.92 GB
</code></pre>
<ul>
<li><strong>REPOSITORY</strong> 是指仓库名字；</li>
<li><strong>TAG</strong> 一般指版本号；</li>
<li><strong>IMAGE ID</strong> 是指镜像 ID；</li>
<li><strong>CREATED</strong> 指镜像创建时间；</li>
<li><strong>SIZE</strong> 指镜像大小；</li>
</ul>
<p>如果我们要查看正在运行的 Docker 进程，可以使用命令 docker ps，如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="81f3eeeef5c1cbc5">[email&#160;protected]</a> ~]# docker ps

CONTAINER ID        IMAGE                             COMMAND                          CREATED             STATUS                          PORTS                     NAMES

3e6ab93074c7      rancher/scheduler:v0.8.6     &quot;/.r/r /rancher-en...&quot;   25 hours ago        Up About an hour                                                   r-scheduler-scheduler-1-056ab74a   2a6a718fa85d        gitlab/gitlab-ce:latest           &quot;/assets/wrapper&quot;        8 months ago        Restarting (127) 11 hours ago                                      gitlab
</code></pre>
<p>其中第一列是容器的 <strong>ID 号</strong>，它是一个<strong>重要的标识</strong>，通过 ID 号我们可以查看指定容器的日志以及启停容器等。读到这里你会发现，你已经知道了两个 ID：</p>
<ul>
<li>一个是 <strong>IMAGE ID</strong>；</li>
<li>另外一个是 <strong>CONTAINER ID</strong>。</li>
</ul>
<p>当你要删除镜像时，就需要使用到 IMAGE ID 了，也就是使用命令 docker rmi image id。那 IMAGE 和 CONTAINER 是什么关系呢？按照我的理解打个比方：</p>
<ul>
<li><strong>IMAGE 相当于类</strong>；</li>
<li><strong>CONTAINER 相当于实例化后的对象</strong>，是在使用层面表现出来的形态。</li>
</ul>
<p>不过你要注意的是 docker ps 只会展示运行的容器：</p>
<ul>
<li>如果你想<strong>展示所有的容器</strong>，需要使用 docker ps -a，这个命令会展示运行的容器和已经停止的容器；</li>
<li>如果你机器上运行的容器很多，想看<strong>最近创建的 10 个容器</strong>，可以使用 docker ps -n 10。</li>
<li>如果你要<strong>停止运行某个容器</strong>，可以使用 docker stop container id 来终止，并且可以结合上文说的 docker ps -a 来看终止状态的容器；</li>
<li>如果要使用 docker rmi<strong>删除容器镜像</strong>，你也需要先关闭对应运行的容器才能执行删除。</li>
</ul>
<p>值得注意的是一些初学者会误用 systemctl stop docker 这个命令，它是<strong>停止整个 Docker 服务</strong>，相当于你机器上的 <strong>Docker 全部关闭</strong>，这是初学者一定要注意到的。</p>
<p>作为测试或者开发，<strong>通过日志去排查问题</strong>是必不可少的，如下所示就是查看指定 Docker 容器日志的方法：</p>
<pre><code>docker logs -f 3e6asb93074c7  #最后一列为容器id号
</code></pre>
<p>你可以将 Docker 看作是一个子系统，自然可以进入这个系统进行一定的操作。在我的使用过程中，经常会使用如下命令进入 Docker 容器找应用的 dump 信息：</p>
<pre><code>docker exec -it 3e6ab93074c7 /bin/bash
</code></pre>
<p>以上是测试同学在使用层面最常见的命令，如果你对 Docker 还不是很了解，可以将这些作为切入点，先掌握使用，在此基础上再去了解 Docker 的架构设计以及一些进阶思想。</p>
<h3>Dockerfile、Docker 镜像、Docker 容器的区别是什么？</h3>
<p>上文带你熟悉了 Docker 的用法，相当于小试牛刀，可能你总听公司的人说 Dockerfile、Docker 容器、Docker 镜像，但又分不清楚，下面我就来解释下它们之间的具体区别是什么：</p>
<ul>
<li>Dockerfile 是一个<strong>用来构建镜像的文本文件</strong>，文本内容包含了一条条构建镜像所需的指令和说明，相当于你做镜像的材料清单和执行步骤；</li>
<li>Docker 镜像是根据这些原材料做出来的<strong>成品</strong>；</li>
<li>而 Docker 容器，你可以认为是<strong>基于镜像运行的软件</strong>。</li>
</ul>
<p>我以包饺子为例：</p>
<ul>
<li>Dockerfile 相当于猪肉、葱姜蒜、饺子皮这些原料的描述以及包饺子的步骤；</li>
<li>Docker 镜像是你包完的生水饺；</li>
<li>而 Docker 容器则是已经煮熟可以食用的水饺了。</li>
</ul>
<p>通过下面这个示意图可以看出从 Dockfile 到 Docker 容器的过程：</p>
<p><img src="assets/CioPOWAs5b6AZbO1AAAk45YQf-w768.png" alt="Drawing 1.png" /></p>
<p>图 2：Dockfile 到 Docker 容器的过程</p>
<h3>应用实例：如何制作基于 JMeter 的 Docker 镜像？</h3>
<p>首先来说为什么会有这样的需求，对于<strong>用户体量比较大</strong>的公司，他们需要的系统处理能力自然也越高。在压测过程中，并不是单台压力机就可以解决问题，我们可能会在压测过程中动态调度JMeter 节点，其中一个比较方便的方式就是使用 Docker 的方式动态进行。</p>
<p>接下来我主要讲解如何制作基于 JMeter 的 Docker 镜像，这也是基于 Docker 扩容的关键部分。</p>
<p>首先我新建了一个文件夹 jmeter_docker，里面存放制作 JMeter 的 Docker 的原材料，如下所示：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="88fae7e7fcc8c2cc">[email&#160;protected]</a> jmeter_docker]# ls

apache-jmeter-5.2.1.tgz  Dockerfile  jdk-8u101-linux-x64.tar.gz
</code></pre>
<p>接着我打开 Dockerfile，看看我的“原料表”里面有哪些内容，从下面的文件描述中可以看出我需要的“原料”和执行步骤：</p>
<pre><code>FROM java:8

# 基础java版本

MAINTAINER cctester

# 作者

ENV http_proxy &quot;&quot;

ENV https_proxy &quot;&quot;

RUN mkdir /test &amp;&amp; \

    chmod -R 777 /test

# 创建/test目录，用于存放jmx脚本、jtl结果文件、html测试报告文件

ENV JMETER_VERSION=5.2.1

ENV JMETER_HOME=/usr/local/apache-jmeter-${JMETER_VERSION}

ENV JMETER_PATH=${JMETER_HOME}/bin:${PATH}

ENV PATH=${JMETER_HOME}/bin:${PATH}

# 设置JMeter环境变量

ADD apache-jmeter-${JMETER_VERSION}.tgz /usr/local

# 添加JMeter

RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &amp;&amp; \

    echo &quot;Asia/Shanghai&quot; &gt; /etc/timezone
</code></pre>
<p>在制作 JMeter 镜像时，请不要忽略后面的一个点（.），具体如下所示：</p>
<pre><code> [<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="42302d2d36020806">[email&#160;protected]</a> jmeter_docker]# docker build -t jmeter .

.....省略

  Successfully built 267c5b4303a6

# 你还可以通过docker images查看完成的镜像

[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3644595942767c72">[email&#160;protected]</a> jmeter_docker]# docker images

REPOSITORY    TAG      IMAGE ID        CREATED        SIZE

jmeter      latest    267c5b4303a6   6 minutes ago   762 MB
</code></pre>
<p>为了方便替换压测脚本或者参数化文件，我在 jmeter_docker 文件下创建一个 test 文件夹来存放这些文件。</p>
<pre><code>mkdir test

# 在当前路径创建test目录,用户存放jmeter文件

docker run -d -it --name jmeter5.2.1 -v $PWD/test:/test jmeter

31f465a1ae646c65e855084d46313754e74a2f377776d9692c0119d32949a130  //启动成功，生成运行id
</code></pre>
<p>然后进入容器，看下 JMeter 是否可用：</p>
<pre><code><a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="55273a3a2115666433616360346434306361">[email&#160;protected]</a>:/test# jmeter -v

Dec 19, 2020 6:11:34 PM java.util.prefs.FileSystemPreferences$1 run

INFO: Created user preferences directory.
</code></pre>
<p>到这里我们就可以运行 JMeter 进行测试了，上传一个 cctester.jmx 脚本到 test 文件夹，使用方式以及结果反馈如下所示：</p>
<pre><code><a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4c3e2323380c7f7d2a787a792d7d2d297a78">[email&#160;protected]</a>:/test# jmeter -n -t /test/cctester.jmx 

Creating summariser &lt;summary&gt;

Created the tree successfully using /test/cctester.jmx

Starting standalone test @ Sat Dec 19 18:22:11 CST 2020 (1608373331470)

Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445

summary +   3344 in 00:00:18 =  185.0/s Avg:    52 Min:    14 Max:  1312 Err:     0 (0.00%) Active: 10 St
</code></pre>
<p>到此就完成了一个基于 Docker 的 JMeter，上面演示了从制作到运行的全过程，同样对于其他Docker 的制作流程也是类似的，你可以基于一种先练习。</p>
<h3>Docker 如何监控</h3>
<p>通过前面章节的学习，我想对于监控你已经并不陌生，并且可以提炼出一套搭建监控体系的方法，对于 Docker 监控本质上也是换汤不换药，我主要进行思路上的一些讲解。</p>
<p><strong>Docker 本身也是可以通过命令行来监控的</strong>，看下 docker stats 的输出，如下所示：</p>
<pre><code>CONTAINER           CPU %               MEM USAGE / LIMIT  MEM %               NET I/O             BLOCK I/O     PIDS

b667f6b988b4        0.07%               381.3 MiB / 7.64 GiB   4.87%               119 MB / 105 MB     275 MB / 0 B        61

f650d561b729        0.04%               233.1 MiB / 7.64 GiB   2.98%               94.9 MB / 118 MB    139 MB / 397 MB     49

c7575bf9a7d7        0.00%               4.711 MiB / 7.64 GiB   0.06%               0 B / 0 B           954 kB / 0 B        6

2a72f849baaa        0.10%               4.008 MiB / 7.64 GiB   0.05%               18.8 MB / 14.5 MB   68.5 MB / 3.04 MB   6

760e653d4324        0.00%               4.887 MiB / 7.64 GiB   0.06%               0 B / 0 B           92.5 MB / 4.1 kB    27
</code></pre>
<p>你可以看到不同的实例都有对应包括 CPU、内存、磁盘、网络的监控，这样的数据比较详细直观。所以这一讲我给你留一个作业，自行搭建 Docker 的可视化监控，可以结合之前讲过的 Grafana、Promethues 等，欢迎在评论区留下你搭建过程中的心得体会以及问题。</p>
<h3>总结</h3>
<p>本讲作为第三模块的收尾，带你学习了 Docker 的基础知识，包括镜像制作、运行，以及监控的常见方式。通过对第三模块的系统学习，你也应该掌握常见的监控方法以及监控部署开展的思路。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;&#32;如何把可视化监控也做得酷炫？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;&#32;如何从&#32;CPU&#32;飙升定位到热点方法？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435ba33cf8645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E8%AF%B4%E9%80%8F%E6%80%A7%E8%83%BD%E6%B5%8B%E8%AF%95/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
