<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07  进程、重定向和管道指令：xargs 指令的作用是？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么大厂面试必考操作系统？.md">00 开篇词  为什么大厂面试必考操作系统？.md</a>

                </li>
                <li>

                    
                    <a href="00&#32;课前必读&#32;&#32;构建知识体系，可以这样做！.md">00 课前必读  构建知识体系，可以这样做！.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;计算机是什么：“如何把程序写好”这个问题是可计算的吗？.md">01  计算机是什么：“如何把程序写好”这个问题是可计算的吗？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;程序的执行：相比&#32;32&#32;位，64&#32;位的优势是什么？（上）.md">02  程序的执行：相比 32 位，64 位的优势是什么？（上）.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;程序的执行：相比&#32;32&#32;位，64&#32;位的优势是什么？（下）.md">03  程序的执行：相比 32 位，64 位的优势是什么？（下）.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;构造复杂的程序：将一个递归函数转成非递归函数的通用方法.md">04  构造复杂的程序：将一个递归函数转成非递归函数的通用方法.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;存储器分级：L1&#32;Cache&#32;比内存和&#32;SSD&#32;快多少倍？.md">05  存储器分级：L1 Cache 比内存和 SSD 快多少倍？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;(1)&#32;加餐&#32;&#32;练习题详解（一）.md">05 (1) 加餐  练习题详解（一）.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;目录结构和文件管理指令：rm&#32;&#32;-rf&#32;指令的作用是？.md">06  目录结构和文件管理指令：rm  -rf 指令的作用是？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="07&#32;&#32;进程、重定向和管道指令：xargs&#32;指令的作用是？.md">07  进程、重定向和管道指令：xargs 指令的作用是？.md</a>
                    

                </li>
                <li>

                    
                    <a href="08&#32;&#32;用户和权限管理指令：&#32;请简述&#32;Linux&#32;权限划分的原则？.md">08  用户和权限管理指令： 请简述 Linux 权限划分的原则？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;Linux&#32;中的网络指令：如何查看一个域名有哪些&#32;NS&#32;记录？.md">09  Linux 中的网络指令：如何查看一个域名有哪些 NS 记录？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;软件的安装：&#32;编译安装和包管理器安装有什么优势和劣势？.md">10  软件的安装： 编译安装和包管理器安装有什么优势和劣势？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;高级技巧之日志分析：利用&#32;Linux&#32;指令分析&#32;Web&#32;日志.md">11  高级技巧之日志分析：利用 Linux 指令分析 Web 日志.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;高级技巧之集群部署：利用&#32;Linux&#32;指令同时在多台机器部署程序.md">12  高级技巧之集群部署：利用 Linux 指令同时在多台机器部署程序.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;(1)加餐&#32;&#32;练习题详解（二）.md">12 (1)加餐  练习题详解（二）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;操作系统内核：Linux&#32;内核和&#32;Windows&#32;内核有什么区别？.md">13  操作系统内核：Linux 内核和 Windows 内核有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;用户态和内核态：用户态线程和内核态线程有什么区别？.md">14  用户态和内核态：用户态线程和内核态线程有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;中断和中断向量：Javajs&#32;等语言为什么可以捕获到键盘输入？.md">15  中断和中断向量：Javajs 等语言为什么可以捕获到键盘输入？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;WinMacUnixLinux&#32;的区别和联系：为什么&#32;Debian&#32;漏洞排名第一还这么多人用？.md">16  WinMacUnixLinux 的区别和联系：为什么 Debian 漏洞排名第一还这么多人用？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;(1)加餐&#32;&#32;练习题详解（三）.md">16 (1)加餐  练习题详解（三）.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;进程和线程：进程的开销比线程大在了哪里？.md">17  进程和线程：进程的开销比线程大在了哪里？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;锁、信号量和分布式锁：如何控制同一时间只有&#32;2&#32;个线程运行？.md">18  锁、信号量和分布式锁：如何控制同一时间只有 2 个线程运行？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;乐观锁、区块链：除了上锁还有哪些并发控制方法？.md">19  乐观锁、区块链：除了上锁还有哪些并发控制方法？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;线程的调度：线程调度都有哪些方法？.md">20  线程的调度：线程调度都有哪些方法？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;哲学家就餐问题：什么情况下会触发饥饿和死锁？.md">21  哲学家就餐问题：什么情况下会触发饥饿和死锁？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;进程间通信：&#32;进程间通信都有哪些方法？.md">22  进程间通信： 进程间通信都有哪些方法？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;分析服务的特性：我的服务应该开多少个进程、多少个线程？.md">23  分析服务的特性：我的服务应该开多少个进程、多少个线程？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;(1)加餐&#32;&#32;练习题详解（四）.md">23 (1)加餐  练习题详解（四）.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;虚拟内存&#32;：一个程序最多能使用多少内存？.md">24  虚拟内存 ：一个程序最多能使用多少内存？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;内存管理单元：&#32;什么情况下使用大内存分页？.md">25  内存管理单元： 什么情况下使用大内存分页？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;缓存置换算法：&#32;LRU&#32;用什么数据结构实现更合理？.md">26  缓存置换算法： LRU 用什么数据结构实现更合理？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;内存回收上篇：如何解决内存的循环引用问题？.md">27  内存回收上篇：如何解决内存的循环引用问题？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;内存回收下篇：三色标记-清除算法是怎么回事？.md">28  内存回收下篇：三色标记-清除算法是怎么回事？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;(1)加餐&#32;&#32;练习题详解（五）.md">28 (1)加餐  练习题详解（五）.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;Linux&#32;下的各个目录有什么作用？.md">29  Linux 下的各个目录有什么作用？.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;文件系统的底层实现：FAT、NTFS&#32;和&#32;Ext3&#32;有什么区别？.md">30  文件系统的底层实现：FAT、NTFS 和 Ext3 有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E9%87%8D%E5%AD%A6%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F-%E5%AE%8C/31%20%20%E6%95%B0%E6%8D%AE%E5%BA%93%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E4%BE%8B%EF%BC%9AMySQL%20%E4%B8%AD%20B%20%E6%A0%91%E5%92%8C%20B+%20%E6%A0%91%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%EF%BC%9F.md">31  数据库文件系统实例：MySQL 中 B 树和 B+ 树有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;HDFS&#32;介绍：分布式文件系统是怎么回事？.md">32  HDFS 介绍：分布式文件系统是怎么回事？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;(1)加餐&#32;&#32;练习题详解（六）.md">32 (1)加餐  练习题详解（六）.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;互联网协议群（TCPIP）：多路复用是怎么回事？.md">33  互联网协议群（TCPIP）：多路复用是怎么回事？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;UDP&#32;协议：UDP&#32;和&#32;TCP&#32;相比快在哪里？.md">34  UDP 协议：UDP 和 TCP 相比快在哪里？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;Linux&#32;的&#32;IO&#32;模式：selectpollepoll&#32;有什么区别？.md">35  Linux 的 IO 模式：selectpollepoll 有什么区别？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;公私钥体系和网络安全：什么是中间人攻击？.md">36  公私钥体系和网络安全：什么是中间人攻击？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;(1)加餐&#32;&#32;练习题详解（七）.md">36 (1)加餐  练习题详解（七）.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;虚拟化技术介绍：VMware&#32;和&#32;Docker&#32;的区别？.md">37  虚拟化技术介绍：VMware 和 Docker 的区别？.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;容器编排技术：如何利用&#32;K8s&#32;和&#32;Docker&#32;Swarm&#32;管理微服务？.md">38  容器编排技术：如何利用 K8s 和 Docker Swarm 管理微服务？.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;Linux&#32;架构优秀在哪里.md">39  Linux 架构优秀在哪里.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;商业操作系统：电商操作系统是不是一个噱头？.md">40  商业操作系统：电商操作系统是不是一个噱头？.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;(1)加餐&#32;&#32;练习题详解（八）.md">40 (1)加餐  练习题详解（八）.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;结束语&#32;&#32;论程序员的发展——信仰、选择和博弈.md">41 结束语  论程序员的发展——信仰、选择和博弈.md</a>

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
                        <div><h1>07  进程、重定向和管道指令：xargs 指令的作用是？</h1>
<p>在面试中，我们经常会遇到面试官询问 Linux 指令，06 课时中讲到的<code>rm -rf /</code>属于比较简单的题目，相当于小学难度。<strong>这节课给你带来一道初中难度的题目：</strong><code>xargs</code><strong>指令的作用是什么</strong>？</p>
<p>通常这个指令是和管道一起使用，因此就引出了这节课的主题：管道。为了理解管道，和学习管道相关的内容，还有一些概念需要你理解，比如：进程、标准流和重定向。好的，接下来请和我一起，把这块知识一网打尽！</p>
<h3>进程</h3>
<p>为了弄清楚这节课程的内容，也就是管道，我们先来讨论一下进程。</p>
<p>我们知道，应用的可执行文件是放在文件系统里，把可执行文件启动，就会在操作系统里（具体来说是内存中）形成一个应用的副本，这个副本就是进程。</p>
<p><em><strong>插一个小知识，以后你再遇到面试题：什么是进程？</strong></em></p>
<p><em><strong>可以回答：进程是应用的执行副本；而不要回答进程是操作系统分配资源的最小单位。前者是定义，后者是作用</strong></em>*。*</p>
<p><strong>ps</strong></p>
<p>如果你要看当前的进程，可以用<code>ps</code>指令。p 代表 processes，也就是进程；s 代表 snapshot，也就是快照。所谓快照，就是像拍照一样。</p>
<p><img src="assets/CgqCHl9twJSAZMbHAADiXX3JRVw649.png" alt="Drawing 0.png" /></p>
<p>如上图所示，我启动了两个进程，<code>ps</code>和<code>bash</code>。ps 就是我刚刚启动的，被<code>ps</code>自己捕捉到了；<code>bash</code>是因为我开了这个控制台，执行的<code>shell</code>是<code>bash</code>。</p>
<p>当然操作系统也不可能只有这么几个进程，这是因为不带任何参数的<code>ps</code>指令显示的是同一个电传打字机（TTY上）的进程。TTY 这个概念是一个历史的概念，过去用来传递信息，现在已经被传真、邮件、微信等取代。</p>
<p>操作系统上的 TTY 是一个输入输出终端的概念，比如用户打开 bash，操作系统就为用户分配了一个输入输出终端。没有加任何参数的<code>ps</code>只显示在同一个 TTY 的进程。</p>
<p>如果想看到所有的进程，可以用<code>ps -e</code>，<code>-e</code>没有特殊含义，只是为了和<code>-A</code>区分开。我们通常不直接用<code>ps -e</code>而是用<code>ps -ef</code>，这是因为<code>-f</code>可以带上更多的描述字段，如下图所示：</p>
<p><img src="assets/Ciqc1F9twKuAcx9KAAMttqMWk0U603.png" alt="Drawing 1.png" /></p>
<ul>
<li>UID 指进程的所有者；</li>
<li>PID 是进程的唯一标识；</li>
<li>PPID 是进程的父进程 ID；</li>
<li>C 是 CPU 的利用率（就是 CPU 占用）；</li>
<li>STIME 是开始时间；</li>
<li>TTY 是进程所在的 TTY，如果没有 TTY 就是 ？号；</li>
<li>TIME；</li>
<li>CMD 是进程启动时的命令，如果不是一个 Shell 命令，而是用方括号括起来，那就是系统进程或者内核过程。</li>
</ul>
<p>另外一个用得比较多的是<code>ps aux</code>，它和<code>ps -ef</code>能力差不多，但是是 BSD 风格的。就是加州伯克利分校研发的 Unix 分支版本的衍生风格，这种风格其实不太好描述，我截了一张图，你可以体会一下：</p>
<p><img src="assets/CgqCHl9twMGAAl8XAAOd-4G_G6U649.png" alt="Drawing 2.png" /></p>
<p>在 BSD 风格中有些字段的叫法和含义变了，如果你感兴趣，可以作为课后延伸学习的内容。</p>
<h4>top</h4>
<p>另外还有一个和<code>ps</code>能力差不多，但是显示的不是快照而是实时更新数据的<code>top</code>指令。因为自带的<code>top</code>显示的内容有点少， 所以我喜欢用一个叫作<code>htop</code>的指令，具体的安装全方法我会在 10 | 软件的安装： 编译安装和包管理器安装有什么优势和劣势？中给你介绍。本课时，我们先看一下使用效果，如下图所示：</p>
<p><img src="assets/Ciqc1F9twNKAbWUxAAjBKXaXn90775.png" alt="Drawing 3.png" /></p>
<p>以上，我们一起把进程学了一个皮毛，更多关于进程的内容我们会在模块四：进程和线程中讨论。</p>
<h3>管道（Pipeline）</h3>
<p>现在你已经掌握了一点点进程的基础，下面我们来学习管道，管道（Pipeline）的作用是在命令和命令之间，传递数据。比如说一个命令的结果，就可以作为另一个命令的输入。我们了解了进程，所以这里说的命令就是进程。更准确地说，管道在进程间传递数据。</p>
<h4>输入输出流</h4>
<p>每个进程拥有自己的标准输入流、标准输出流、标准错误流。</p>
<p>这几个标准流说起来很复杂，但其实都是文件。</p>
<ul>
<li>标准输入流（用 0 表示）可以作为进程执行的上下文（进程执行可以从输入流中获取数据）。</li>
<li>标准输出流（用 1 表示）中写入的结果会被打印到屏幕上。</li>
<li>如果进程在执行过程中发生异常，那么异常信息会被记录到标准错误流（用 2 表示）中。</li>
</ul>
<p><strong>重定向</strong></p>
<p>我们执行一个指令，比如<code>ls -l</code>，结果会写入标准输出流，进而被打印。这时可以用重定向符将结果重定向到一个文件，比如说<code>ls -l &gt; out</code>，这样<code>out</code>文件就会有<code>ls -l</code>的结果；而屏幕上也不会再打印<code>ls -l</code>的结果。</p>
<p><img src="assets/Ciqc1F9twOiAWhAGAAU25o5Gb_s323.png" alt="Drawing 4.png" /></p>
<p>具体来说<code>&gt;</code>符号叫作覆盖重定向；<code>&gt;&gt;</code>叫作追加重定向。<code>&gt;</code>每次都会把目标文件覆盖，<code>&gt;&gt;</code>会在目标文件中追加。比如你每次启动一个程序日志都写入<code>/var/log/somelogfile</code>中，可以这样操作，如下所示：</p>
<pre><code>start.sh &gt;&gt; /var/log/somelogfile
</code></pre>
<p>经过这样的操作后，每次执行程序日志就不会被覆盖了。</p>
<p>另外还有一种情况，比如我们输入:</p>
<pre><code>ls1 &gt; out
</code></pre>
<p>结果并不会存入<code>out</code>文件，因为<code>ls1</code>指令是不存在的。结果会输出到标准错误流中，仍然在屏幕上。这里我们可以把标准错误流也重定向到标准输出流，然后再重定向到文件。</p>
<pre><code>ls1 &amp;&gt; out
</code></pre>
<p>这个写法等价于：</p>
<pre><code>ls1 &gt; out 2&gt;&amp;1
</code></pre>
<p><img src="assets/CgqCHl9twP2AefIFAAL1fMsTbHk961.png" alt="Drawing 5.png" /></p>
<p>相当于把<code>ls1</code>的标准输出流重定向到<code>out</code>，因为<code>ls1 &gt; out</code>出错了，所以标准错误流被定向到了标准输出流。<code>&amp;</code>代表一种引用关系，具体代表的是<code>ls1 &gt;out</code>的标准输出流。</p>
<h4>管道的作用和分类</h4>
<p>有了进程和重定向的知识，接下来我们梳理下管道的作用。管道（Pipeline）将一个进程的输出流定向到另一个进程的输入流，就像水管一样，作用就是把这两个文件接起来。如果一个进程输出了一个字符 X，那么另一个进程就会获得 X 这个输入。</p>
<p><strong>管道和重定向很像，但是管道是一个连接一个进行计算，重定向是将一个文件的内容定向到另一个文件，这二者经常会结合使用</strong>。</p>
<p>Linux 中的管道也是文件，有两种类型的管道：</p>
<ol>
<li>匿名管道（Unnamed Pipeline），这种管道也在文件系统中，但是它只是一个存储节点，不属于任何一个目录。说白了，就是没有路径。</li>
<li>命名管道（Named Pipeline），这种管道就是一个文件，有自己的路径。</li>
</ol>
<h4>FIFO</h4>
<p>管道具有 FIFO（First In First Out），FIFO 和排队场景一样，先排到的先获得。所以先流入管道文件的数据，也会先流出去传递给管道下游的进程。</p>
<h3>使用场景分析</h3>
<p>接下来我们以多个场景举例帮助你深入学习管道。</p>
<h4>排序</h4>
<p>比如我们用<code>ls</code>，希望按照文件名排序倒序，可以使用匿名管道，将<code>ls</code>的结果传递给<code>sort</code>指令去排序。你看，这样<code>ls</code>的开发者就不用关心排序问题了。</p>
<p><img src="assets/Ciqc1F9twQmAUpYzAADI43WGK9A660.png" alt="Drawing 6.png" /></p>
<h4>去重</h4>
<p>另一个比较常见的场景是去重，比如有一个字典文件，里面都是词语。如下所示：</p>
<pre><code>Apple

Banana

Apple

Banana

……
</code></pre>
<p>如果我们想要去重可以使用<code>uniq</code>指令，<code>uniq</code>指令能够找到文件中相邻的重复行，然后去重。但是我们上面的文件重复行是交替的，所以不可以直接用<code>uniq</code>，因此可以先<code>sort</code>这个文件，然后利用管道将<code>sort</code>的结果重定向到<code>uniq</code>指令。指令如下：</p>
<p><img src="assets/CgqCHl9twRGAXmhPAACPjv2JnVo451.png" alt="Drawing 7.png" /></p>
<h4>筛选</h4>
<p>有时候我们想根据正则模式筛选对应的内容。比如说我们想找到项目文件下所有文件名中含有<code>Spring</code>的文件。就可以利用<code>grep</code>指令，操作如下：</p>
<pre><code>find ./ | grep Spring
</code></pre>
<p><code>find ./</code>递归列出当前目录下所有目录中的文件。<code>grep</code>从<code>find</code>的输出流中找出含有<code>Spring</code>关键字的行。</p>
<p>如果我们希望包含<code>Spring</code>但不包含<code>MyBatis</code>就可以这样操作：</p>
<pre><code>find ./ | grep Spring | grep -v MyBatis
</code></pre>
<p><code>grep -v</code>是匹配不包含 MyBatis 的结果。</p>
<h4>数行数</h4>
<p>还有一个比较常见的场景是数行数。比如你写了一个 Java 文件想知道里面有多少行，就可以使用<code>wc -l</code>指令，如下所示：</p>
<p><img src="assets/Ciqc1F9twRqAH6ezAAD5iEQBhxE628.png" alt="Drawing 8.png" /></p>
<p>但是如果你想知道当前目录下有多少个文件，可以用<code>ls | wc -l</code>，如下所示：</p>
<p><img src="assets/Ciqc1F9twSCAN0h-AABgIcsEgKI655.png" alt="Drawing 9.png" /></p>
<p><strong>接下来请你思考一个问题：我们如何知道当前</strong><code>java</code><strong>的项目目录下有多少行代码</strong>？</p>
<p>提示一下。你可以使用下面这个指令：</p>
<pre><code>find -i &quot;.java&quot; ./ | wc -l
</code></pre>
<p>快去自己动手写一写吧，你在尝试的过程中如果遇到什么问题，也可以写在留言区，我会逐一为你解答。</p>
<h4>中间结果</h4>
<p>管道一个接着一个，是一个计算逻辑。有时候我们想要把中间的结果保存下来，这就需要用到<code>tee</code>指令。<code>tee</code>指令从标准输入流中读取数据到标准输出流。</p>
<p>这时候，你可能会问： 老师， 这不是什么都没做吗？</p>
<p>别急，<code>tee</code>还有一个能力，就是自己利用这个过程把输入流中读取到的数据存到文件中。比如下面这条指令：</p>
<pre><code>find ./ -i &quot;*.java&quot; | tee JavaList | grep Spring
</code></pre>
<p>这句指令的意思是从当前目录中找到所有含有 Spring 关键字的 Java 文件。tee 本身不影响指令的执行，但是 tee 会把 find 指令的结果保存到 JavaList 文件中。</p>
<p><code>tee</code>这个执行就像英文字母中的 T 一样，连通管道两端，下面又开了口。这个开口，在函数式编程里面叫作副作用。</p>
<h4>xargs</h4>
<p>上面我们学习的内容难度，已经由小学 1 年级攀升到了小学 6 年级，最后我们来看看初中难度的<code>xargs</code>指令。</p>
<p><code>xargs</code>指令从标准数据流中构造并执行一行行的指令。<code>xargs</code>从输入流获取字符串，然后利用空白、换行符等切割字符串，在这些字符串的基础上构造指令，最后一行行执行这些指令。</p>
<p>举个例子，如果我们重命名当前目录下的所有 .a 的文件，想在这些文件前面加一个前缀<code>prefix_</code>。比如说<code>x.a</code>文件需要重命名成<code>prefix_x.a</code>，我们就可以用<code>xargs</code>指令构造模块化的指令。</p>
<p>现在我们有<code>x.a``y.a``z.a</code>三个文件，如下图所示：</p>
<p><img src="assets/CgqCHl9twTWALpuzAABnixlvrS8980.png" alt="Drawing 10.png" /></p>
<p>然后使用下图中的指令构造我们需要的指令：</p>
<p><img src="assets/CgqCHl9twT-AOUALAAE5FDR8Tiw234.png" alt="Drawing 11.png" /></p>
<ul>
<li>我们用<code>ls</code>找到所有的文件；</li>
<li><code>-I</code>参数是查找替换符，这里我们用<code>GG</code>替代<code>ls</code>找到的结果；<code>-I GG</code>后面的字符串 GG 会被替换为<code>x.a``x.b</code>或<code>x.z</code>；</li>
<li><code>echo</code>是一个在命令行打印字符串的指令。使用<code>echo</code>主要是为了安全，帮助我们检查指令是否有错误。</li>
</ul>
<p>我们用<code>xargs</code>构造了 3 条指令。这里我再多讲一个词，叫作样板代码。如果你没有用<code>xargs</code>指令，而是用一条条<code>mv</code>指令去敲，这样就构成了样板代码。</p>
<p>最后去掉 echo，就是我们想要的结果，如下所示：</p>
<p><img src="assets/Ciqc1F9twUiAOcNlAAEsaaMV4DI747.png" alt="Drawing 12.png" /></p>
<h3>管道文件</h3>
<p>上面我们花了较长的一段时间讨论匿名管道，用<code>|</code>就可以创造和使用。匿名管道也是利用了文件系统的能力，是一种文件结构。当你学到模块六文件系统的内容，会知道匿名管道拥有一个自己的<code>inode</code>，但不属于任何一个文件夹。</p>
<p>还有一种管道叫作命名管道（Named Pipeline）。命名管道是要挂到文件夹中的，因此需要创建。用<code>mkfifo</code>指令可以创建一个命名管道，下面我们来创建一个叫作<code>pipe1</code>的命名管道，如下图所示：</p>
<p><img src="assets/CgqCHl9twU-ASY8bAAC7_lc6Pr8814.png" alt="Drawing 13.png" /></p>
<p>命名管道和匿名管道能力类似，可以连接一个输出流到另一个输入流，也是 First In First Out。</p>
<p>当执行<code>cat pipe1</code>的时候，你可以观察到，当前的终端处于等待状态。因为我们<code>cat pipe1</code>的时候<code>pipe1</code>中没有内容。</p>
<p>如果这个时候我们再找一个终端去写一点东西到<code>pipe</code>中，比如说:</p>
<pre><code>echo &quot;XXX&quot; &gt; pipe1
</code></pre>
<p>这个时候，<code>cat pipe1</code>就会返回，并打印出<code>xxx</code>，如下所示：</p>
<p><img src="assets/CgqCHl9twViAT-M2AADtPsSTV5c658.png" alt="Drawing 14.png" /></p>
<p>我们可以像上图那样演示这段程序，在<code>cat pipe1</code>后面增加了一个<code>&amp;</code>符号。这个<code>&amp;</code>符号代表指令在后台执行，不会阻塞用户继续输入。然后我们通过<code>echo</code>指令往<code>pipe1</code>中写入东西，接着就会看到<code>xxx</code>被打印出来。</p>
<h3>总结</h3>
<p>这节课我们为了学习管道，先简单接触了进程的概念，然后学习了重定向。之后我们学习了匿名管道的应用场景，匿名管道帮助我们把 Linux 指令串联起来形成很强的计算能力。特别是<code>xargs</code>指令支持模板化的生成指令，拓展了指令的能力。最后我们还学习了命名管道，命名管道让我们可以真实拿到一个管道文件，让多个程序之间可以方便地进行通信。</p>
<p><strong>那么通过这节课的学习，你现在可以来回答本节关联的面试题目：xargs 的作用了吗？</strong></p>
<p>老规矩，请你先在脑海里构思下给面试官的表述，并把你的思考写在留言区，然后再来看我接下来的分析。</p>
<p><strong>【解析】</strong> xargs 将标准输入流中的字符串分割成一条条子字符串，然后再按照我们自己想要的方式构建成一条条指令，大大拓展了 Linux 指令的能力。</p>
<p>比如我们可以用来按照某种特定的方式逐个处理一个目录下所有的文件；根据一个 IP 地址列表逐个 ping 这些 IP，收集到每个 IP 地址的延迟等。</p>
<h3>思考题</h3>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;&#32;目录结构和文件管理指令：rm&#32;&#32;-rf&#32;指令的作用是？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;&#32;用户和权限管理指令：&#32;请简述&#32;Linux&#32;权限划分的原则？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435cfc7f72645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E9%87%8D%E5%AD%A6%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
