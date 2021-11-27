<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>38  容器编排技术：如何利用 K8s 和 Docker Swarm 管理微服务？.md</title>
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

                    <a class="current-tab" href="38&#32;&#32;容器编排技术：如何利用&#32;K8s&#32;和&#32;Docker&#32;Swarm&#32;管理微服务？.md">38  容器编排技术：如何利用 K8s 和 Docker Swarm 管理微服务？.md</a>
                    

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
                        <div><h1>38  容器编排技术：如何利用 K8s 和 Docker Swarm 管理微服务？</h1>
<p>作为操作系统的最后一个部分，我选择了三个主题：虚拟化、Linux 的架构哲学和商业操作系统的设计。我还是以探索式教学为主，帮助你建立和掌握虚拟化、程序架构、业务架构三个方向的基本概念。</p>
<p>操作系统的设计者和芯片的制造商们，早就感受到了虚拟化、容器化带来的变化，早早地支持了虚拟化，比如 Linux 的命名空间、Intel 的 VT-X 技术。这一讲作为虚拟化的一个延伸，我们一起讨论一下<strong>如何管理海量的容器，如何去构造一个高可用且具有扩展能力强的集群</strong>。</p>
<p>话不多说，让我们开始学习 Kubernetes 和 Docker Swarm 吧！</p>
<h3>微服务</h3>
<p>现在的面试官都喜欢问<strong>微服务相关的内容。微服务（Micro Service），指的是服务从逻辑上不可再分，是宏服务（Mono Service）的反义词。</strong></p>
<p>比如初学者可能认为交易相关的服务都应该属于交易服务，但事实上，交易相关的服务可能会有交易相关的配置服务、交易数据的管理服务、交易履约的服务、订单算价的服务、流程编排服务、前端服务……</p>
<p>所以到底什么是不可再分呢？</p>
<p>其实没有不可再分，永远都可以继续拆分下去。只不过从逻辑上讲，系统的拆分，应该结合公司部门组织架构的调整，反映公司的战斗结构编排。但总的来说，互联网上的服务越来越复杂，几个简单的接口就可能形成一个服务，这些服务都要上线。如果用实体机来承载这些服务，开销太大。如果用虚拟机来承载这些服务倒是不错的选择，但是创建服务的速度太慢，不适合今天这个时代的研发者们。</p>
<p>试想你的系统因为服务太多，该如何管理？尤其是在大型的公司，员工通过自发组织架构评审就可以上线微服务——天长日久，微服务越来越多，可能会有几万个甚至几十万个。那么这么多的微服务，如何分布到数万台物理机上工作呢？</p>
<p>如下图所示，为了保证微服务之间是隔离的，且可以快速上线。每个微服务我们都使用一个单独的容器，而一组容器，又包含在一个虚拟机当中，具体的关系如下图所示：</p>
<p><img src="assets/Ciqc1GAT7LeAJznRAAKOxTSise8097.png" alt="Lark20210129-190005.png" /></p>
<p>上图中的微服务 C 因为只有一个实例存在单点风险，可能会引发单点故障。因此需要为微服务 C 增加副本，通常情况下，我们必须保证每个微服务至少有一个副本，这样才能保证可用性。</p>
<p>上述架构的核心就是要解决两个问题：</p>
<ol>
<li>减少 downtime（就是减少服务不可用的时间）；</li>
<li>支持扩容（随时都可以针对某个微服务增加容器）。</li>
</ol>
<p>因此，我们需要容器编排技术。容器编排技术指自动化地对容器进行部署、管理、扩容、迁移、保证安全，以及针对网络负载进行优化等一系列技术的综合体。Kubernetes 和 Docker Swarm 都是出色的容器编排方案。</p>
<h3>Kubernetes</h3>
<p>Kubernetes（K8s）是一个 Google 开源的容器编排方案。</p>
<h4>节点（Master&amp;Worker）</h4>
<p><strong>K8s 通过集群管理容器</strong>。用户可以通过命令行、配置文件管理这个集群——从而编排容器；用户可以增加节点进行扩容，每个节点是一台物理机或者虚拟机。如下图所示，Kubernetes 提供了两种分布式的节点。Master 节点是集群的管理者，Worker 是工作节点，容器就在 Worker 上工作，一个 Worker 的内部可以有很多个容器。</p>
<p><img src="assets/CgqCHmAT7M-Af_RTAAKzmD-Lpm0018.png" alt="Lark20210129-190008.png" /></p>
<p>在我们为一个微服务扩容的时候，首选并不是去增加 Worker 节点。可以增加这个微服务的容器数量，也可以提升每个容器占用的 CPU、内存存储资源。只有当整个集群的资源不够用的时候，才会考虑增加机器、添加节点。</p>
<p>Master 节点至少需要 2 个，但并不是越多越好。Master 节点主要是管理集群的状态数据，不需要很大的内存和存储空间。Worker 节点根据集群的整体负载决定，一些大型网站还有弹性扩容的手段，也可以通过 K8s 实现。</p>
<h4>单点架构</h4>
<p>接下来我们讨论一下 Worker 节点的架构。所有的 Worker 节点上必须安装 kubelet，它是节点的管理程序，负责在节点上管理容器。</p>
<p>Pod 是 K8s 对容器的一个轻量级的封装，每个 Pod 有自己独立的、随机分配的 IP 地址。Pod 内部是容器，可以 1 个或多个容器。目前，Pod 内部的容器主要是 Docker，但是今后可能还会有其他的容器被大家使用，主要原因是 K8s 和 Docker 的生态也存在着竞争关系。总的来说，如下图所示，kubelet 管理 Pod，Pod 管理容器。当用户创建一个容器的时候，实际上在创建 Pod。</p>
<p><img src="assets/Ciqc1GAT7NyAI0-5AAEh6UfvPpY109.png" alt="Lark20210129-190011.png" /></p>
<p>虽然 K8s 允许同样的应用程序（比如微服务），在一个节点上创建多个 Pod。但是为了保证可用性，通常我们会考虑将微服务分散到不同的节点中去。如下图所示，如果其中一个节点宕机了，微服务 A，微服务 B 还能正常工作。当然，有一些微服务。因为程序架构或者编程语言的原因，只能使用单进程。这个时候，我们也可能会在单一的节点上部署多个相同的服务，去利用更多的 CPU 资源。</p>
<p><img src="assets/CgqCHmAT7OaAeadYAAJEm88_Xg8398.png" alt="Lark20210129-190014.png" /></p>
<h4>负载均衡</h4>
<p>Pod 的 IP 地址是动态的，如果要将 Pod 作为内部或者外部的服务，那么就需要一个能拥有静态 IP 地址的节点，这种节点我们称为服务（Service），服务不是一个虚拟机节点，而是一个虚拟的概念——或者理解成一段程序、一个组件。请求先到达服务，然后再到达 Pod，服务在这之间还提供负载均衡。当有新的 Pod 加入或者旧的 Pod 被删除，服务可以捕捉到这些状态，这样就大大降低了分布式应用架构的复杂度。</p>
<p><img src="assets/CgqCHmAT7PeAZRvoAACjdnGXVe0743.png" alt="Lark20210129-190001.png" /></p>
<p>如上图所示，当我们要提供服务给外部使用时，对安全的考虑、对性能的考量是超过内部服务的。 K8s 解决方案：在服务的上方再提供薄薄的一层控制程序，为外部提供服务——这就是 Ingress。</p>
<p>以上，就是 K8s 的整体架构。 在使用的过程当中，相信你会感受到这个工具的魅力。比如说组件非常齐全，有数据加密、网络安全、单机调试、API 服务器等。如果你想了解更多的内容，可以查看<a href="https://kubernetes.io/docs/concepts/overview/">这些资料</a>。</p>
<h3>Docker Swarm</h3>
<p>Docker Swarm 是 Docker 团队基于 Docker 生态打造的容器编排引擎。下图是 Docker Swarm 整体架构图。</p>
<p><img src="assets/CgqCHmAT7QaAcwO7AAJWW_dhVAU264.png" alt="Drawing 5.png" /></p>
<p>和 K8s 非常相似，节点被分成了 Manager 和 Worker。Manager 之间的状态数据通过 Raft 算法保证数据的一致性，Worker 内部是 Docker 容器。</p>
<p>和 K8s 的 Pod 类似，Docker Swarm 对容器进行了一层轻量级的封装——任务（Task），然后多个Task 通过服务进行负载均衡。</p>
<p><img src="assets/Ciqc1GAT7RCAYw67AAGVRE-fcmY185.png" alt="Drawing 6.png" /></p>
<h3>容器编排设计思考</h3>
<p>这样的设计，用户只需要指定哪些容器开多少个副本，容器编排引擎自动就会在工作节点之中复制这些容器。而服务是容器的分组，多个容器共享一个服务。容器自动被创建，用户在维护的时候不需要维护到容器创建级别，只需要指定容器数目，并指定这类型的容器对应着哪个服务。至于之后，哪一个容器中的程序执行出错，编排引擎就会杀死这个出错的容器，并且重启一个新的容器。</p>
<p>在这样的设计当中，容器最好是<strong>无状态</strong>的，所以容器中最好不要用来运行 MySQL 这样的数据库。对于 MySQL 数据库，并不是多个实例都可以通过负载均衡来使用。有的实例只可以读，有的实例只可以写，中间还有 Binlog 同步。因此，虽然 K8s 提供了状态管理组件，但是使用起来可能不如虚拟机划算。</p>
<p>也是因为这种原因，我们现在倾向于进行无状态服务的开发。所有的状态都是存储在远程，应用本身并没有状态。当然，<strong>在开发测试环境，用容器来管理数据库是一个非常好的方案</strong>。这样可以帮助我们快速搭建、切换开发测试环境，并且可以做到一人一环境，互不影响，也可以做到开发环境、测试环境和线上环境统一。</p>
<h3>总结</h3>
<p>本讲我们讨论了两套容器编排引擎的 Kubernetes 和 Docker。如果继续深入学习，你会发现 K8s 功能更复杂，对细节的处理更灵活。而 Docker Swarm 虽然不强大，但是在部署一些小中型应用时，非常简单。因为 Docker 是大家都用熟练的东西，用类似使用 Docker 的方式部署，学习成本更低。</p>
<p>至于到底选择哪个？你可以根据自己的业务场景综合考虑。</p>
<p>另外，一些大厂通常还会有自己的一套容器编排引擎。这些架构未必用了开源领域的产品，也许会让程序员感受到非常痛苦。因为即便是一家强大的商业公司，在研发产品的时候还是很难做到像社区产品这样认真和专注。所以我希望，当你以后成为一名优秀的架构师，如果不想让公司的技术栈被社区淘汰，就要不断地进行技术升级。</p>
<p><strong>那么通过这一讲的学习，你现在可以尝试来回答本讲关联的面试题目：如何利用 K8s 和 Docker Swarm 管理微服务</strong>？</p>
<p>【<strong>解析</strong>】这两个容器编排引擎都可以用来管理微服务。K8s 和 Docker Swarm 在使用微服务的时候有许多共性的步骤。</p>
<ol>
<li><strong>制作容器镜像</strong>：我们就是要先制作容器，如果使用 Docker 作为容器，那就要写 DockerFile，然后生成容器镜像。</li>
<li><strong>上传镜像</strong>：制作好容器之后，我们往往会将容器上传到容器的托管平台。很多公司内部有自己的容器托管平台，这样下载容器的速度会非常快。</li>
<li><strong>搭建集群</strong>：再接下来，我们要搭建一个 K8s 或者 Docker Swarm 的集群，将节点添加进去。</li>
<li><strong>添加微服务 Pod/Task</strong>：然后我们要在集群中添加 Pod 的或者 Task，可以通过命令行工具，也可以通过书写配置文件。</li>
<li><strong>设置服务</strong>：为 Pod/Task 设置服务，之后都通过服务来访问容器内的应用。</li>
</ol>
<p>以上 5 个步骤是无论用哪个容器编排引擎都需要做的。具体使用过程当中，还有很多差异。比如，有的时候使用图形界面就可以完成上面的管理；不同的引擎配置文件，参数格式都会有差异。但是从整体架构到使用方式，它们都有着很大的相似性。因此你在学习容器编排引擎时，不应该着眼于学习某一个引擎，而是将它们看作一类知识，对比着学习。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="37&#32;&#32;虚拟化技术介绍：VMware&#32;和&#32;Docker&#32;的区别？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="39&#32;&#32;Linux&#32;架构优秀在哪里.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435dd85a4d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
