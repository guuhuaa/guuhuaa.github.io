<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10  命令行监控 Linux 服务器的要点.md</title>
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

                    <a class="current-tab" href="10&#32;&#32;命令行监控&#32;Linux&#32;服务器的要点.md">10  命令行监控 Linux 服务器的要点.md</a>
                    

                </li>
                <li>

                    
                    <a href="11&#32;&#32;分布式服务链路监控以及报警方案.md">11  分布式服务链路监控以及报警方案.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;如何把可视化监控也做得酷炫？.md">12  如何把可视化监控也做得酷炫？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;Docker&#32;的制作、运行以及监控.md">13  Docker 的制作、运行以及监控.md</a>

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
                        <div><h1>10  命令行监控 Linux 服务器的要点</h1>
<p>前面两个模块带你学习了如何使用 JMeter 工具，如何做好一份性能测试方案，第三模块我将带你进行监控的学习。在你执行性能测试的过程中，监控服务端的资源消耗等也是必备内容，监控的结果是帮助你发现问题的眼睛。然而在实操过程中发现很多同学喜欢用JMeter 工具提供的插件进行监控，但是我并<strong>不推荐</strong>你使用这种方式，原因如下：</p>
<ul>
<li>指标相对简单且固定，结果数据粗糙且界面显示并不是很友好；</li>
<li>较大地增加了客户端压测机的资源开销，影响性能测试结果；</li>
<li>特定环境下，在服务器上安装插件是不被允许的，会很不方便。</li>
</ul>
<p>所以这一讲我想带你了解下监控的内容有哪些？既然不推荐使用 JMeter 自带的监控方式，那我是如何做监控的呢？</p>
<p>本讲作为监控模块的第一篇，我想先聊一聊如何能够把监控这件事情做好，正所谓“<strong>磨刀不误砍柴工</strong>”，监控绝不是简单地敲几个命令，做几个图表就可以的，你需要从多角度来理解这件事情。首先我认为把监控做好需要有以下三个关键词：<strong>层次清晰、全面覆盖、定向深入</strong>。我来解释下这三个关键词代表的含义。</p>
<h3>层次清晰</h3>
<p>从执行一次性能测试来看，你需要监控的内容有很多，重点是要能理清楚不同的监控类型，以及分别能够解决什么问题？我从下面几个层次做下介绍，从而让你对各层面的监控做一个初步了解，也为后面的章节做一些铺垫。</p>
<h4>1.硬件层</h4>
<p>硬件层是最容易想到的一个层面，一般包含了 CPU 的使用率、内存使用率、磁盘和网络读写速度等，通过这些指标能够反馈出系统运行的基本情况，以及不同的 TPS 量级会消耗多少硬件资源。</p>
<h4>2.系统层</h4>
<p>系统层监控包括连接请求数、拒绝数、丢包率、请求超时等，相对于基础的硬件监控而言，这些指标更能够反映出目前系统存在的瓶颈，从而为根因问题的定位提供有力的线索。</p>
<h4>3.链路层</h4>
<p>在我看来，链路层是直接面向架构和代码的，它的监控能够帮助你更加准确地看到代码执行了哪些函数，涉及哪些服务，并且能够较为清晰地看到函数之间的调用耗时，还可以帮助你定位代码存在的问题。</p>
<h4>4.业务层</h4>
<p>业务层监控本意是帮助你判断用户输入是否合规，代码逻辑是否健壮。对于性能测试而言，业务层的监控可以帮助你发现脚本参数问题以及高并发下业务逻辑运行是否正常等，比如随着测试的进行，可能会存在商品库存不足的情况。如果有业务层面的监控，当库存低于某阈值时，可以进行一定的提示以规避此类问题。</p>
<h3>全面覆盖</h3>
<p>如果你能够完整地画出应用的部署架构图（参考第 09 讲的部署架构图），并且能够按照我说的几个层次将其完整地部署落地，我想监控这件事情至少可以给你打到 85 分，剩下来的 15 分在哪里呢？我认为除了应用层的监控，你还需要考虑<strong>底层链路的监控</strong>，比如防火墙、F5 负载均衡等，这些往往是一下子考虑不到的事情。</p>
<p>在我的实际工作中，尤其是新项目监控部署经常存在“缺斤少两”的情况。虽然在测试之前做了系统监控，但出现问题后仔细分析时，经常发现某一些机器并没有被监控到，或者监控了 CPU 又发现磁盘没有被监控上。这些问题主要是考验你的组织能力，也反映了团队是否能在性能测试上更细致更深入，毕竟性能的分析是不能放过任何“蛛丝马迹”的。</p>
<h3>定向深入</h3>
<p>首先通过基本的监控可以获得一些异常点，比如 CPU 高了、磁盘在等待，这些说白了是表象问题。就比如说某位同学今天发烧了，通过发烧这个现象并不能直接下定论说他感冒了，医生也需要做进一步的化验分析才可以下结论。对于监控也是这样，是否有定位根因问题的手段，CPU 高了，需不需要进行线程分析，需要哪些权限和定位工具，这些在监控部署时都需要考虑到。</p>
<p>下面我从监控硬件资源开始，通过使用 Linux 命令行对服务器进行监控，为什么我要讲解 Linux 命令的监控呢？我认为它具有灵活迅速的特点，通过命令可以最快地输出对应结果。接下来我会分别从 CPU、内存、磁盘、网络维度既快又能直击要害地帮你分析硬件瓶颈。</p>
<h3>CPU</h3>
<p>top 是我们查看各个进程的资源占用状况最常用的命令，如下代码所示，这个命令简单却包含很大的信息量，接下来我选一些常用的内容给你重点解释。</p>
<pre><code>top - 18:17:47 up 158 days,  9:32,  2 users,

load average: 0.07, 0.15, 0.21

Tasks: 154 total,   1 running, 152 sleeping,   0 stopped,   1 zombie

%Cpu(s):  3.9 us,  1.3 sy,  0.0 ni, 94.6 id,  0.2 wa,  0.0 hi,  0.0 si,  0.0 st

KiB Mem :  8010676 total,   337308 free,  6036100 used,  1637268 buff/cache

KiB Swap:        0 total,        0 free,        0 used.  1223072 avail Mem

以下省略
</code></pre>
<h4>1. load average</h4>
<p>关于这一内容的代码如下所示：</p>
<pre><code>load average: 0.07, 0.15, 0.21
</code></pre>
<p>三个数字都是代表进程队列的长度，从左到右分别表示一分钟、 五分钟和十五分钟的数据，数字越小压力值就越低，数字越大则压力越高，然而这个数值多小算小呢？多大算大呢？</p>
<p>以<strong>单核处理器</strong>为例，打个比方就像收费站的一个 ETC 通道一样：</p>
<ul>
<li>0 表示没有任何车辆需要通过；</li>
<li>从 0 到 1 可以认为很流畅，车辆不需要任何等待就可以通过；</li>
<li>1 表示正好在这个通道可接受范围之内；</li>
<li>超过 1 就已经有车辆在后面排队了。</li>
</ul>
<p>所以理想情况下，希望平均负载值在 1 以下。如果是 1 就代表目前没有可用资源了。在实际情况中，很多运维同学会把理想负载设置在 0.7 以下，这也是业内的一个“<strong>经验值</strong>”。</p>
<p>刚刚说的是一个单核处理器的情况，多核 CPU 的话，负载数值 / CPU 核数在 0.00~1.00 之间表示正常，理想值也是在 0.7 以内。</p>
<h4>2. CPU 状态</h4>
<p>从 top 中你也可以看到每种类型进程消耗的 CPU 时间百分比，如下所示：</p>
<pre><code> %Cpu(s):  3.9 us,  1.3 sy,  0.0 ni, 94.6 id,  0.2 wa,  0.0 hi,  0.0 si,  0.0 st
</code></pre>
<p>首先来看代码中的一些重要信息。</p>
<ul>
<li>us 列显示了用户进程所花费 CPU 时间的百分比。这个数值越高，说明用户进程消耗的 CPU 时间越多，可以用来分析代码中的 CPU 消耗热点。</li>
<li>sy 列表示系统进程消耗的 CPU 时间百分比。</li>
<li>ni 列表示改变优先级的进程占用 CPU 的百分比。</li>
<li>id 列表示 CPU 处于空闲状态的时间百分比。</li>
<li>wa 列显示了 I/O 等待所占用的 CPU 时间的百分比，这里 wa 的参考值为 0.5，如果长期高于这个参考值，需要注意是否存在磁盘瓶颈。</li>
<li>hi 列表示硬件中断占用 CPU 时间百分比。</li>
<li>si 列表示软件中断占用 CPU 时间百分比。</li>
<li>st 列表示当系统运行在虚拟机中时，当前虚拟机在等待 CPU 为它服务的时间。</li>
</ul>
<p>在已经输入 top 的情况下再输入数字 1，可以查看 CPU 的核数和每个核的运行状态。</p>
<p>如下图是两核 CPU 的运行状态。</p>
<pre><code>%Cpu0  :  3.0 us,  1.7 sy,  0.0 ni, 95.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st

%Cpu1  :  2.4 us,  1.0 sy,  0.0 ni, 96.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
</code></pre>
<p>值得注意的是，很多同学看 CPU 的使用率时，只看 us 这个数值，通过上面的讲解，可以看出这是不准确的。除了用户进程，还有其他系统进程会占用 CPU，所以实际 CPU 的使用率可以用 100 减去空闲值（id）去计算。</p>
<h3>如何统计内存使用情况</h3>
<p>最常见的是通过 free 来查看 Linux 内存使用情况。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ec9e838398aca6a8">[email&#160;protected]</a> ~]# free -m

              total        used        free      shared  buff/cache   available

Mem:           7822        5917         302         373        1602        1195

Swap:             0           0           0
</code></pre>
<p>相信通过单词的意思我们也能大概看出来 total、used、free 表示什么，它们分别是<strong>总的</strong>物理内存大小、<strong>已经被使用的</strong>物理内存和<strong>空闲的</strong>物理内存值是多少。</p>
<p>曾经有同学问我，为什么 free 值很低却未必代表内存达到瓶颈呢？</p>
<p>这和 Linux 内核机制有关系，简单来说，内存空间会开辟 buffer 和 cache 缓冲区，对于物理内存来说，这都属于被使用过的内存。而应用需要内存时，如果没有可用的 free 内存，内核就会从缓冲区回收内存以满足要求，当 free 值很低的时候，如上代码中的 available 就能体现出缓冲区可用内存的大小，这个指标可以比较真实地反映出内存是否达到使用上限。</p>
<h3>磁盘查看</h3>
<p>这一部分我们来讲两个重要的命令。</p>
<h4>1.iostat</h4>
<pre><code> [<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2c5e4343586c6668">[email&#160;protected]</a> ~]# iostat -x

Linux 3.10.0-514.el7.x86_64 (JD)        01/18/2021      _x86_64_        (2 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle

           5.24    0.00    1.57    0.07    0.00   93.12

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util

vda               0.00     0.29    0.57    5.30    20.50   630.14   221.82     0.07   11.53   59.83    6.36   1.18   0.69
</code></pre>
<p>通过这个命令你能看到磁盘实时运行的情况，一般可以优先看 idle、util 和 svctm 这几列的数值：</p>
<ul>
<li>idle 代表磁盘空闲百分比；</li>
<li>util 接近 100%，表示磁盘产生的 I/O 请求太多，I/O 系统已经满负荷在工作，该磁盘可能存在瓶颈；</li>
<li>svctm 代表平均每次设备 I/O 操作的服务时间 (毫秒)。</li>
</ul>
<p>在我的经验中，会组合看这些指标，如果 idle 长期在 50% 以下，util 值在 50% 以上以及 svctm 高于 10ms，说明磁盘可能存在一定的问题。接着我会定位到具体是哪个进程造成的磁盘瓶颈，下面我就为你介绍一个关于定位的命令。</p>
<h4>2.iotop</h4>
<p>iotop 这个命令并不是 linux 原生的，需要安装，以 CentOS 7.0 为例：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b5c7dadac1f5fff1">[email&#160;protected]</a> ~]# yum -y install iotop
</code></pre>
<p>安装完成之后，直接输入 iotop，示意如下，你就能清楚地看到哪些进程在消耗磁盘资源。</p>
<pre><code>6448 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % ifrit-agent

14647 be/4 root        0.00 B/s    7.70 K/s  0.00 %  0.00 % java -Dserver.port=9080
</code></pre>
<h3>网络</h3>
<h4>netstat</h4>
<p>netstat 能提供 TCP 和 UDP 的连接状态等统计信息，可以简单判断网络是否存在堵塞。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="64160b0b10242e20">[email&#160;protected]</a> ~]# netstat

Active Internet connections (w/o servers)

Proto Recv-Q Send-Q Local Address           Foreign Address         State

tcp        0      1 JD:49190                169.254.169.250:http    FIN_WAIT1

tcp        0      0 JD:39444                169.254.169.254:http    TIME_WAIT

tcp        0      0 JD:us-srv               worker-18.:sentinel-ent ESTABLISHED
</code></pre>
<p>**Proto：**协议名（可以 TCP 协议或者 UDP 协议）。</p>
<p><strong>recv-Q</strong>：网络接收队列还有多少请求在排队。</p>
<p><strong>send-Q</strong>：网络发送队列有多少请求在排队。</p>
<p><strong>recv-Q</strong> 和 <strong>send-Q</strong> 如果长期不为 0，很可能存在网络拥堵，这个是判断网络瓶颈的重要依据。</p>
<p><strong>Foreign Address</strong>：与本机端口通信的外部 socket。</p>
<p><strong>State</strong>：TCP 的连接状态。</p>
<h3>总结</h3>
<p>通过本讲的学习，你已经知道了如何通过命令行监控 Linux 资源，包括 CPU、磁盘、内存、网络，也知道了判断硬件瓶颈的一些策略。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;&#32;如何制定一份有效的性能测试方案？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;&#32;分布式服务链路监控以及报警方案.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435b904be1645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
