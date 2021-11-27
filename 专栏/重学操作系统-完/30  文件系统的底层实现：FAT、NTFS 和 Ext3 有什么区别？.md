<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>30  文件系统的底层实现：FAT、NTFS 和 Ext3 有什么区别？.md</title>
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

                    <a class="current-tab" href="30&#32;&#32;文件系统的底层实现：FAT、NTFS&#32;和&#32;Ext3&#32;有什么区别？.md">30  文件系统的底层实现：FAT、NTFS 和 Ext3 有什么区别？.md</a>
                    

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
                        <div><h1>30  文件系统的底层实现：FAT、NTFS 和 Ext3 有什么区别？</h1>
<p><strong>这一讲给你带来的面试题是： FAT、NTFS 和 Ext3 文件系统有什么区别</strong>？</p>
<p>10 年前 FAT 文件系统还是常见的格式，而现在 Windows 上主要是 NTFS，Linux 上主要是 Ext3、Ext4 文件系统。关于这块知识，一般资料只会从支持的磁盘大小、数据保护、文件名等各种维度帮你比较，但是最本质的内容却被一笔带过。<strong>它们最大的区别是文件系统的实现不同，具体怎么不同</strong>？<strong>文件系统又有哪些实现</strong>？这一讲，我将带你一起来探索和学习这部分知识。</p>
<h3>硬盘分块</h3>
<p>在了解文件系统实现之前，我们先来了解下操作系统如何使用硬盘。</p>
<p><strong>使用硬盘和使用内存有一个很大的区别，内存可以支持到字节级别的随机存取，而这种情况在硬盘中通常是不支持的</strong>。过去的机械硬盘内部是一个柱状结构，有扇区、柱面等。读取硬盘数据要转动物理的磁头，每转动一次磁头时间开销都很大，因此一次只读取一两个字节的数据，非常不划算。</p>
<p>随着 SSD 的出现，机械硬盘开始逐渐消失（还没有完全结束），现在的固态硬盘内部是类似内存的随机存取结构。但是硬盘的读写速度还是远远不及内存。而连续读多个字节的速度，还远不如一次读一个硬盘块的速度。</p>
<p>因此，<strong>为了提高性能，通常会将物理存储（硬盘）划分成一个个小块</strong>，比如每个 4KB。这样做也可以让硬盘的使用看起来非常整齐，方便分配和回收空间。况且，数据从磁盘到内存，需要通过电子设备，比如 DMA、总线等，如果一个字节一个字节读取，速度较慢的硬盘就太耗费时间了。过去的机械硬盘的速度可以比内存慢百万倍，现在的固态硬盘，也会慢几十到几百倍。即便是最新的 NvMe 接口的硬盘，和内存相比速度仍然有很大的差距。因此，一次读/写一个块（Block）才是可行的方案。</p>
<p><img src="assets/Cip5yF_ls_aAEer_AADHBXF7EHw534.png" alt="Lark20201225-174103.png" /></p>
<p>如上图所示，操作系统会将磁盘分成很多相等大小的块。这样做还有一个好处就是如果你知道块的序号，就可以准确地计算出块的物理位置。</p>
<h3>文件的描述</h3>
<p>我们将硬盘分块后，如何利用上面的硬盘存储文件，就是文件系统（File System）要负责的事情了。当然目录也是一种文件，因此我们先讨论文件如何读写。不同的文件系统利用方式不同，今天会重点讨论 3 种文件系统：</p>
<ul>
<li>早期的 FAT 格式</li>
<li>基于 inode 的传统文件系统</li>
<li>日志文件系统（如 NTFS, EXT2、3、4）</li>
</ul>
<h4>FAT 表</h4>
<p>早期人们找到了一种方案就是文件分配表（File Allocate Table，FAT）。如下图所示：</p>
<p><img src="assets/CgpVE1_ltAKAZe8tAACczq1tAiY181.png" alt="Lark20201225-174106.png" /></p>
<p><strong>一个文件，最基本的就是要描述文件在硬盘中到底对应了哪些块。FAT 表通过一种类似链表的结构描述了文件对应的块</strong>。上图中：文件 1 从位置 5 开始，这就代表文件 1 在硬盘上的第 1 个块的序号是 5 的块 。然后位置 5 的值是 2，代表文件 1 的下一个块的是序号 2 的块。顺着这条链路，我们可以找到 5 → 2 → 9 → 14 → 15 → -1。-1 代表结束，所以文件 1 的块是：5,2,9,14,15。同理，文件 2 的块是 3,8,12。</p>
<p><strong>FAT 通过一个链表结构解决了文件和物理块映射的问题，算法简单实用，因此得到过广泛的应用，到今天的 Windows/Linux/MacOS 都还支持 FAT 格式的文件系统</strong>。FAT 的缺点就是非常占用内存，比如 1T 的硬盘，如果块的大小是 1K，那么就需要 1G 个 FAT 条目。通常一个 FAT 条目还会存一些其他信息，需要 2~3 个字节，这就又要占用 2-3G 的内存空间才能用 FAT 管理 1T 的硬盘空间。显然这样做是非常浪费的，问题就出在了 FAT 表需要全部维护在内存当中。</p>
<h4>索引节点（inode）</h4>
<p>为了改进 FAT 的容量限制问题，可以考虑为每个文件增加一个索引节点（inode）。这样，随着虚拟内存的使用，当文件导入内存的时候，先导入索引节点（inode），然后索引节点中有文件的全部信息，包括文件的属性和文件物理块的位置。</p>
<p><img src="assets/CgpVE1_ltBCAP9AZAAC1vcuIPkE631.png" alt="Lark20201225-174108.png" /></p>
<p>如上图，索引节点除了属性和块的位置，还包括了一个指针块的地址。这是为了应对文件非常大的情况。一个大文件，一个索引节点存不下，需要通过指针链接到其他的块去描述文件。</p>
<p>这种文件索引节点（inode）的方式，完美地解决了 FAT 的缺陷，一直被沿用至今。FAT 要把所有的块信息都存在内存中，索引节点只需要把用到的文件形成数据结构，而且可以使用虚拟内存分配空间，随着页表置换，这就解决了 FAT 的容量限制问题。</p>
<h3>目录的实现</h3>
<p>有了文件的描述，接下来我们来思考如何实现目录（Directory）。目录是特殊的文件，所以每个目录都有自己的 inode。目录是文件的集合，所以目录的内容中必须有所有其下文件的 inode 指针。</p>
<p><img src="assets/Cip5yF_ltBqAG_agAAB0qsKok0o713.png" alt="Lark20201225-174111.png" /></p>
<p>文件名也最好不要放到 inode 中，而是放到文件夹中。这样就可以灵活设置文件的别名，及实现一个文件同时在多个目录下。</p>
<p><img src="assets/Cip5yF_ltCKAQ8wsAACxv79iv44798.png" alt="Lark20201225-174114.png" /></p>
<p>如上图，/foo 和 /bar 两个目录中的 b.txt 和 c.txt 其实是一个文件，但是拥有不同的名称。这种形式我们称作“硬链接”，就是多个文件共享 inode。</p>
<p><img src="assets/Cip5yF_ltCmANmxDAAEX0KEBlYU772.png" alt="Drawing 5.png" /></p>
<p>硬链接有一个非常显著的特点，硬链接的双方是平等的。上面的程序我们用<code>ln</code>指令为文件 a 创造了一个硬链接<code>b</code>。如果我们创造完删除了 a，那么 b 也是可以正常工作的。如果要删除掉这个文件的 inode，必须 a,b 同时删除。这里你可以看出 a,b 是平等的。</p>
<p>和硬链接相对的是软链接，软链接的原理如下图：</p>
<p><img src="assets/CgpVE1_ltDGAXzaKAADF0IcW0HA765.png" alt="Lark20201225-174117.png" /></p>
<p>图中<code>c.txt</code>是<code>b.txt</code>的一个软链接，软链接拥有自己的<code>inode</code>，但是文件内容就是一个快捷方式。因此，如果我们删除了<code>b.txt</code>，那么<code>b.txt</code>对应的 inode 也就被删除了。但是<code>c.txt</code>依然存在，只不过指向了一个空地址（访问不到）。如果删除了<code>c.txt</code>，那么不会对<code>b.txt</code>造成任何影响。</p>
<p>在 Linux 中可以通过<code>ln -s</code>创造软链接。</p>
<pre><code>ln -s a b # 将b设置为a的软链接(b是a的快捷方式)
</code></pre>
<p>以上，我们对文件系统的实现有了一个初步的了解。从<strong>整体设计上，本质还是将空间切块，然后划分成目录和文件管理这些分块</strong>。读、写文件需要通过 inode 操作磁盘。操作系统提供的是最底层读写分块的操作，抽象成文件就交给文件系统。比如想写入第 10001 个字节，那么会分成这样几个步骤：</p>
<ol>
<li>修改内存中的数据</li>
<li>计算要写入第几个块</li>
<li>查询 inode 找到真实块的序号</li>
<li>将这个块的数据完整的写入一次磁盘</li>
</ol>
<p><strong>你可以思考一个问题，如果频繁读写磁盘，上面这个模型会有什么问题</strong>？可以把你的思考和想法写在留言区，我们在本讲后面会详细讨论。</p>
<h3>解决性能和故障：日志文件系统</h3>
<p><strong>在传统的文件系统实现中，inode 解决了 FAT 容量限制问题，但是随着 CPU、内存、传输线路的速度越来越快，对磁盘读写性能的要求也越来越高</strong>。传统的设计，每次写入操作都需要进行一次持久化，所谓“持久化”就是将数据写入到磁盘，这种设计会成为整个应用的瓶颈。因为磁盘速度较慢，内存和 CPU 缓存的速度非常快，如果 CPU 进行高速计算并且频繁写入磁盘，那么就会有大量线程阻塞在等待磁盘 I/O 上。磁盘的瓶颈通常在写入上，因为通常读取数据的时候，会从缓存中读取，不存在太大的瓶颈。</p>
<p>加速写入的一种方式，就是利用缓冲区。</p>
<p><img src="assets/CgpVE1_ltEeASFyHAAD52tSCqME475.png" alt="Lark20201225-174119.png" /></p>
<p>上图中所有写操作先存入缓冲区，然后每过一定的秒数，才进行一次持久化。 这种设计，是一个很好的思路，但最大的问题在于容错。 比如上图的步骤 1 或者步骤 2 只执行了一半，如何恢复？如果步骤 2 只写入了一半，那么数据就写坏了。如果步骤 1 只写入了一半，那么数据就丢失了。无论出现哪种问题，都不太好处理。更何况写操作和写操作之间还有一致性问题，比如说一次删除 inode 的操作后又发生了写入……</p>
<p>解决上述问题的一个非常好的方案就是利用日志。假设 A 是文件中某个位置的数据，比起传统的方案我们反复擦写 A，日志会帮助我们把 A 的所有变更记录下来，比如：</p>
<pre><code>A=1

A=2

A=3
</code></pre>
<p>上面 A 写入了 3 次，因此有 3 条日志。日志文件系统文件中存储的就是像上面那样的日志，而不是文件真实的内容。当用户读取文件的时候，文件内容会在内存中还原，所以内存中 A 的值是 3，但实际磁盘上有 3 条记录。</p>
<p>从性能上分析，如果日志造成了 3 倍的数据冗余，那么读取的速度并不会真的慢三倍。因为我们多数时候是从内存和 CPU 缓存中读取数据。而写入的时候，因为采用日志的形式，可以考虑下图这种方式，在内存缓冲区中积累一批日志才写入一次磁盘。</p>
<p><img src="assets/Cip5yF_ltD-ANGHYAAD43z0foHQ229.png" alt="Lark20201225-174123.png" /></p>
<p>上图这种设计可以让写入变得非常快速，多数时间都是写内存，最后写一次磁盘。<strong>而上图这样的设计成不成立，核心在能不能解决容灾问题</strong>。</p>
<p>你可以思考一下这个问题——<strong>丢失一批日志和丢失一批数据的差别大不大</strong>。其实它们之间最大的差别在于，如果丢失一批日志，只不过丢失了近期的变更；但如果丢失一批数据，那么就可能造成永久伤害。</p>
<p>举个例子，比如说你把最近一天的订单数据弄乱了，你可以通过第三方支付平台的交易流水、系统的支付记录等帮助用户恢复数据，还可以通过订单关联的用户信息查询具体是哪些用户的订单出了问题。但是如果你随机删了一部分订单， 那问题就麻烦了。你要去第三发支付平台调出所有流水，用大数据引擎进行分析和计算。</p>
<p>为了进一步避免损失，一种可行的方案就是创建还原点（Checkpoint），比如说系统把最近 30s 的日志都写入一个区域中。下一个 30s 的日志，写入下一个区域中。每个区域，我们称作一个还原点。创建还原点的时候，我们将还原点涂成红色，写入完成将还原点涂成绿色。</p>
<p><img src="assets/CgpVE1_ltFyACwCsAADstiN6HAk886.png" alt="Lark20201225-174058.png" /></p>
<p>如上图，当日志文件系统写入磁盘的时候，每隔一段时间就会把这段时间内的所有日志写入一个或几个连续的磁盘块，我们称为还原点（Checkpoint）。操作系统读入文件的时候，依次读入还原点的数据，如果是绿色，那么就应用这些日志，如果是红色，就丢弃。所以上图中还原点 3 的数据是不完整的，这个时候会丢失不到 30s 的数据。如果将还原点的间隔变小，就可以控制风险的粒度。另外，我们还可以对还原点 3 的数据进行深度恢复，这里可以有人工分析，也可以通过一些更加复杂的算法去恢复。</p>
<h3>总结</h3>
<p>这一讲我们学习了 3 种文件系统的实现，我们再来一起总结回顾一下。</p>
<ul>
<li>FAT 的设计简单高效，如果你要自己管理一定的空间，可以优先考虑这种设计。</li>
<li>inode 的设计在内存中创造了一棵树状结构，对文件、目录进行管理，并且索引到磁盘中的数据。这是一种经典的数据结构，这种思路会被数据库设计、网络资源管理、缓存设计反复利用。</li>
<li>日志文件系统——日志结构简单、容易存储、按时间容易分块，这样的设计非常适合缓冲、批量写入和故障恢复。</li>
</ul>
<p>现在我们很多分布式系统的设计也是基于日志，比如 MySQL 同步数据用 binlog，Redis 的 AOF，著名的分布式一致性算法 Paxos ，因此 Zookeeper 内部也在通过实现日志的一致性来实现分布式一致性。</p>
<p><strong>那么通过这节课的学习，你现在可以尝试来回答本节关联的面试题目：FAT、NTFS 和 Ext3 有什么区别</strong>？</p>
<p>【<strong>解析</strong>】FAT 通过内存中一个类似链表的结构，实现对文件的管理。<strong>NTFS 和 Ext3 是日志文件系统，它们和 FAT 最大的区别在于写入到磁盘中的是日志，而不是数据</strong>。日志文件系统会先把日志写入到内存中一个高速缓冲区，定期写入到磁盘。日志写入是追加式的，不用考虑数据的覆盖。一段时间内的日志内容，会形成还原点。这种设计大大提高了性能，当然也会有一定的数据冗余。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="29&#32;&#32;Linux&#32;下的各个目录有什么作用？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E9%87%8D%E5%AD%A6%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F-%E5%AE%8C/31%20%20%E6%95%B0%E6%8D%AE%E5%BA%93%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E5%AE%9E%E4%BE%8B%EF%BC%9AMySQL%20%E4%B8%AD%20B%20%E6%A0%91%E5%92%8C%20B+%20%E6%A0%91%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%EF%BC%9F.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435da09a4d645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
