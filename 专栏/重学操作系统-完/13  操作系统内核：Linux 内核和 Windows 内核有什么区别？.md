<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13  操作系统内核：Linux 内核和 Windows 内核有什么区别？.md</title>
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

                    
                    <a href="07&#32;&#32;进程、重定向和管道指令：xargs&#32;指令的作用是？.md">07  进程、重定向和管道指令：xargs 指令的作用是？.md</a>

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

                    <a class="current-tab" href="13&#32;&#32;操作系统内核：Linux&#32;内核和&#32;Windows&#32;内核有什么区别？.md">13  操作系统内核：Linux 内核和 Windows 内核有什么区别？.md</a>
                    

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
                        <div><h1>13  操作系统内核：Linux 内核和 Windows 内核有什么区别？</h1>
<p>Windows 和 Linux 是当今两款最主流的服务器操作系统产品，都拥有广泛的用户和信徒。Windows 通过强大的商业运作，驱动了大量优秀人才加盟到它的开发团队中；Linux 通过社区产品的魅力吸引着世界上大量的顶级程序员为它贡献源代码、解答问题。两者在服务器市场上竞争激烈，不分伯仲，但也存在互相扶持的关系。</p>
<p>我觉得，两个操作系统各有千秋。每次学习两个操作系统的技术知识，都让我切实地感受到编程真的是一门艺术，而学习编程就像是在探索艺术。</p>
<p><strong>今天我们继续从一道面试题目“ Linux 内核和 Windows 内核有什么区别</strong>？”入手，去了解这两个操作系统内核的设计，帮助你学习操作系统中最核心的一个概念——内核，并希望这些知识可以伴随你日后的每个系统设计。</p>
<h3>什么是内核？</h3>
<p>说到操作系统，就必须说内核。内核是操作系统中应用连接硬件设备的桥梁。</p>
<h4>内核的能力</h4>
<p>对于一个现代的操作系统来说，它的内核至少应该提供以下 4 种基本能力：</p>
<ul>
<li>管理进程、线程（决定哪个进程、线程使用 CPU）；</li>
<li>管理内存（决定内存用来做什么）；</li>
<li>连接硬件设备（为进程、和设备间提供通信能力）；</li>
<li>提供系统调用（接收进程发送来的系统调用）。</li>
</ul>
<h4>操作系统分层</h4>
<p>从上面 4 种能力来看操作系统和内核之间的关系，通常可以把操作系统分成 3 层，最底层的硬件设备抽象、中间的内核和最上层的应用。</p>
<p><img src="assets/CgqCHl-P5meAd3VdAAB1f7DWz-I273.png" alt="Lark20201021-153830.png" /></p>
<h4>内核是如何工作的？</h4>
<p><strong>为了帮助你理解什么是内核，请你先思考一个问题：进程和内核的关系，是不是像浏览器请求服务端服务</strong>？你可以先自己思考，然后在留言区写下你此时此刻对这个问题的认知，等学完“模块三”再反过头来回顾这个知识，相信你定会产生新的理解。</p>
<p>接下来，我们先一起分析一下这个问题。</p>
<p>内核权限非常高，它可以管理进程、可以直接访问所有的内存，因此确实需要和进程之间有一定的隔离。这个隔离用类似请求/响应的模型，非常符合常理。</p>
<p><img src="assets/CgqCHl-P5naAc5fsAABuTlhIQkw555.png" alt="Lark20201021-153825.png" /></p>
<p>但不同的是在浏览器、服务端模型中，浏览器和服务端是用不同的机器在执行，因此不需要共享一个 CPU。但是在进程调用内核的过程中，这里是存在资源共享的。</p>
<ul>
<li>比如，一个机器有 4 个 CPU，不可能让内核用一个 CPU，其他进程用剩下的 CPU。这样太浪费资源了。</li>
<li>再比如，进程向内核请求 100M 的内存，内核把 100M 的数据传回去。 这个模型不可行，因为传输太慢了。</li>
</ul>
<p>所以，这里多数操作系统的设计都遵循一个原则：进程向内核发起一个请求，然后将 CPU 执行权限让出给内核。内核接手 CPU 执行权限，然后完成请求，再转让出 CPU 执行权限给调用进程。</p>
<p>关于这块知识，我们会在“ 14 |户态和内核态：用户态线程和内核态线程有什么区别？”中详细讨论。</p>
<h3>Linux 的设计</h3>
<p>Linux 操作系统第一版是1991 年林纳斯托·瓦兹（一个芬兰的小伙子，当时 22 岁）用 C 语音写的。 写完之后他在网络上发布了 Linux 内核的源代码。又经过了 3 年的努力，在 1994 年发布了完整的核心 Version 1.0。</p>
<p>说到 Linux 内核设计，这里有很多有意思的名词。大多数听起来复杂、专业，但是理解起来其实很简单。接下来我们一一讨论。</p>
<ul>
<li><strong>Multitask and SMP（Symmetric multiprocessing）</strong></li>
</ul>
<p><strong>MultiTask 指多任务</strong>，Linux 是一个多任务的操作系统。多任务就是多个任务可以同时执行，这里的“同时”并不是要求并发，而是在一段时间内可以执行多个任务。当然 Linux 支持并发。</p>
<p><strong>SMP 指对称多处理</strong>。其实是说 Linux 下每个处理器的地位是相等的，内存对多个处理器来说是共享的，每个处理器都可以访问完整的内存和硬件资源。 这个特点决定了在 Linux 上不会存在一个特定的处理器处理用户程序或者内核程序，它们可以被分配到任何一个处理器上执行。</p>
<ul>
<li><strong>ELF（Executable and Linkable Format）</strong></li>
</ul>
<p><img src="assets/Ciqc1F-P5pOAeET-AAEzXOQTzbA445.png" alt="Lark20201021-153821.png" /></p>
<p>这个名词翻译过来叫作可执行文件链接格式。这是一种从 Unix 继承而来的可执行文件的存储格式。我们可以看到 ELF 中把文件分成了一个个分段（Segment），每个段都有自己的作用。如果想要深入了解这块知识，会涉及部分编译原理的知识，如果你感兴趣可以去网上多查些资料或者去留言区我们一起讨论。</p>
<ul>
<li><strong>Monolithic Kernel</strong></li>
</ul>
<p>这个名词翻译过来就是宏内核，宏内核反义词就是 Microkernel ，微内核的意思。Linux 是宏内核架构，这说明 Linux 的内核是一个完整的可执行程序，且内核用最高权限来运行。宏内核的特点就是有很多程序会打包在内核中，比如，文件系统、驱动、内存管理等。当然这并不是说，每次安装驱动都需要重新编译内核，现在 Linux 也可以动态加载内核模块。所以哪些模块在内核层，哪些模块在用户层，这是一种系统层的拆分，并不是很强的物理隔离。</p>
<p>与宏内核对应，接下来说说<strong>微内核，内核只保留最基本的能力。比如进程调度、虚拟内存、中断。多数应用，甚至包括驱动程序、文件系统，是在用户空间管理的</strong>。</p>
<p><img src="assets/CgqCHl-QEKSAYD22AAFXRfj1rsA581.png" alt="Lark20201021-183457.png" /></p>
<p>学到这里，你可能会问：在内核层和在用户层有什么区别吗？</p>
<p>感觉分层其实差不多。 我这里说一个很大的区别，比如说驱动程序是需要频繁调用底层能力的，如果在内核中，性能肯定会好很多。对于微内核设计，驱动在内核外，驱动和硬件设备交互就需要频繁做内核态的切换。</p>
<p>当然微内核也有它的好处，比如说微内核体积更小、可移植性更强。不过我认为，随着计算能力、存储技术越来越发达，体积小、安装快已经不能算是一个很大的优势了。现在更重要的是如何有效利用硬件设备的性能。</p>
<p>之所以这么思考，也可能因为我是带着现代的目光回望当时人们对内核的评判，事实上，当时 Linux 团队也因此争论过很长一段时间。 但是我觉得历史往往是螺旋上升的，说不定将来性能发展到了一个新的阶段，像微内核的灵活性、可以提供强大的抽象能力这样的特点，又重新受到人们的重视。</p>
<p>还有一种就是混合类型内核。 混合类型的特点就是架构像微内核，内核中会有一个最小版本的内核，其他功能会在这个能力上搭建。但是实现的时候，是用宏内核的方式实现的，就是内核被做成了一个完整的程序，大部分功能都包含在内核中。就是在宏内核之内有抽象出了一个微内核。</p>
<p>上面我们大体介绍了内核几个重要的特性，有关进程、内存、虚拟化等特性，我们会在后面几个模块中逐步讨论。</p>
<h3>Window 设计</h3>
<p>接下来我们说说 Windows 的设计，Windows 和 Linux 的设计有很大程度的相似性。Windows也有内核，它的内核是 C/C++ 写的。准确地说，Windows 有两个内核版本。一个是早期的Windows 9x 内核，早期的 Win95, Win98 都是这个内核。我们今天用的 Windows 7, Windows 10 是另一个内核，叫作 Windows NT。NT 指的是 New Technology。接下来我们讨论的都是 NT 版本的内核。</p>
<p>下面我找到一张 Windows 内核架构的图片给你一个直观感受。</p>
<p><img src="assets/Ciqc1F-P5suAH9CJAAFl4zKFbJc816.png" alt="Drawing 3.png" /></p>
<p>Windows 同样支持 Multitask 和 SMP（对称多处理）。Windows 的内核设计属于混合类型。你可以看到内核中有一个 Microkernel 模块。而整个内核实现又像宏内核一样，含有的能力非常多，是一个完整的整体。</p>
<p>Windows 下也有自己的可执行文件格式，这个格式叫作 Portable Executable（PE），也就是可移植执行文件，扩展名通常是<code>.exe</code>、<code>.dll</code>、<code>.sys</code>等。</p>
<p>PE 文件的结构和 ELF 结构有很多相通的地方，我找到了一张图片帮助你更直观地理解。 因为这部分知识涉及编译原理，我这里就不详细介绍了，感兴趣同学可以在留言区和大家一起讨论，或者查阅更多资料。</p>
<p><img src="assets/CgqCHl-P5ySAAg5CAACF0kTmx_k209.png" alt="Lark20201021-153828.png" /></p>
<p>Windows 还有很多独特的能力，比如 Hyper-V 虚拟化技术，有关虚拟化技术我们将在“模块八：虚拟化和其他”中详细讲解。</p>
<h3>总结</h3>
<p>这一讲我们学习了内核的基础知识，包括内核的作用、整体架构以及 3 种内核类型（宏内核、微内核和混合类型内核）。内核很小（微内核）方便移植，因为体积小、安装快；内核大（宏内核），方便优化性能，毕竟内核更了解计算机中的资源。我们还学习了操作系统对执行文件的抽象，但是没有很深入讨论，内核部分有很多知识是需要在后面的几个模块中体现的，比如进程、文件、内存相关的能力等。</p>
<p><strong>那么通过这一讲的学习，你现在可以来回答本节关联的面试题目：Linux 内核和 Windows 内核有什么区别？</strong></p>
<p>老规矩，请你先在脑海里构思下给面试官的表述，并把你的思考写在留言区，然后再来看我接下来的分析。</p>
<p><strong>【解析】</strong> Windows 有两个内核，最新的是 NT 内核，目前主流的 Windows 产品都是 NT 内核。NT 内核和 Linux 内核非常相似，没有太大的结构化差异。</p>
<p>从整体设计上来看，Linux 是宏内核，NT 内核属于混合型内核。和微内核不同，宏内核和混合类型内核从实现上来看是一个完整的程序。只不过混合类型内核内部也抽象出了微内核的概念，从内核内部看混合型内核的架构更像微内核。</p>
<p>另外 NT 内核和 Linux 内核还存在着许多其他的差异，比如：</p>
<ul>
<li>Linux 内核是一个开源的内核；</li>
<li>它们支持的可执行文件格式不同；</li>
<li>它们用到的虚拟化技术不同。</li>
</ul>
<p>关于这块知识就不展开说了， 我们会在后续的“进程、内存、虚拟化”等模块中仔细讨论。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;(1)加餐&#32;&#32;练习题详解（二）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;&#32;用户态和内核态：用户态线程和内核态线程有什么区别？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435d296f9c645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
