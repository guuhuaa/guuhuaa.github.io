<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05  存储器分级：L1 Cache 比内存和 SSD 快多少倍？.md</title>
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

                    <a class="current-tab" href="05&#32;&#32;存储器分级：L1&#32;Cache&#32;比内存和&#32;SSD&#32;快多少倍？.md">05  存储器分级：L1 Cache 比内存和 SSD 快多少倍？.md</a>
                    

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
                        <div><h1>05  存储器分级：L1 Cache 比内存和 SSD 快多少倍？</h1>
<p><strong>近两年我在面试求职者的时候，喜欢问这样一道面试题：SSD、内存和 L1 Cache 相比速度差多少倍</strong>？</p>
<p>其实比起复杂的技术问题，我更喜欢在面试中提问这种像生活常识一样的简单问题。因为我觉得，复杂的问题是由简单的问题组成的，如果你把简单的问题学扎实了，那么复杂问题也是可以自己推导的。</p>
<p>如果你不知道 L1 Cache，可能会错误地判断内存执行速度。我们写程序，会用寄存器、内存以及硬盘，所以按照墨菲定律，如果这里有一个认知是错误的，那么最终的结果就会产生问题。</p>
<p>下面，回到我们今天的问题，这个问题关联的知识点是存储器分级策略。接下来，请你带着问题开始学习今天的内容。</p>
<h3>为什么会有存储器分级策略？</h3>
<p>要想弄清楚存储器分级策略。</p>
<p>首先，你要弄清楚，“我们希望存储器是什么样子的”，也就是“我们的需求是什么”？</p>
<p>然后，你要弄清楚，我们的需求有哪些“实现约束”。</p>
<p>从需求上讲，我们希望存储器速度快、体积小、空间大、能耗低、散热好、断电数据不丢失。但在现实中，我们往往无法把所有需求都实现。</p>
<p>下面我们举几个例子，带你深入体会一下，比如：</p>
<ul>
<li>如果一个存储器的体积小，那它存储空间就会受到制约。</li>
<li>如果一个存储器电子元件密度很大，那散热就会有问题。因为电子元件都会产生热能，所以电子元件非常集中的 CPU，就需要单独的风扇或者水冷帮助电子元件降温。</li>
<li>如果一个存储器离 CPU 较远，那么在传输过程中必然会有延迟，因此传输速度也会下降。</li>
</ul>
<p>这里你可能会有疑问，因为在大多数人的认知里，光速是很快的，而信号又是以光速传输的。既然光速这么快，那信号的延迟应该很小才对。但事实并不是这样，比如时钟信号是 1GHz 的 CPU，1G 代表 10 个亿，因此时钟信号的一个周期是 1/10 亿秒。而光的速度是 3×10 的 8 次方米每秒，就是 3 亿米每秒。所以在一个周期内，光只能前进 30 厘米。</p>
<p>你看！虽然在宏观世界里光速非常快，但是到计算机世界里，光速并没有像我们认知中的那么快。所以即使元件离 CPU 的距离稍微远了一点，运行速度也会下降得非常明显。</p>
<p>你可能还会问，那干吗不把内存放到 CPU 里？</p>
<p>如果你这么做的话，除了整个电路散热和体积会出现问题，服务器也没有办法做定制内存了。也就是说 CPU 在出厂时就决定了它的内存大小，如果你想换更大的内存，就要换 CPU，而组装定制化是你非常重要的诉求，这肯定是不能接受的。</p>
<p>此外，在相同价格下，一个存储器的速度越快，那么它的能耗通常越高。能耗越高，发热量越大。</p>
<p>因此，我们上面提到的需求是不可能被全部满足的，除非将来哪天存储技术有颠覆性的突破。</p>
<h3>存储器分级策略</h3>
<p>既然我们不能用一块存储器来解决所有的需求，那就必须把需求分级。</p>
<p>一种可行的方案，就是根据数据的使用频率使用不同的存储器：高频使用的数据，读写越快越好，因此用最贵的材料，放到离 CPU 最近的位置；使用频率越低的数据，我们放到离 CPU 越远的位置，用越便宜的材料。</p>
<p><img src="assets/Ciqc1F9kgVGAD_IMAACXR1QKcDo779.png" alt="Lark20200918-174334.png" /></p>
<p>具体来说，通常我们把存储器分成这么几个级别：</p>
<ol>
<li>寄存器；</li>
<li>L1-Cache；</li>
<li>L2-Cache；</li>
<li>L3-Cahce；</li>
<li>内存；</li>
<li>硬盘/SSD。</li>
</ol>
<h4>寄存器（Register）</h4>
<p>寄存器紧挨着 CPU 的控制单元和逻辑计算单元，它所使用的材料速度也是最快的。就像我们前面讲到的，存储器的速度越快、能耗越高、产热越大，而且花费也是最贵的，因此数量不能很多。</p>
<p>寄存器的数量通常在几十到几百之间，每个寄存器可以用来存储一定字节（byte）的数据。比如：</p>
<ul>
<li>32 位 CPU 中大多数寄存器可以存储 4 个字节；</li>
<li>64 位 CPU 中大多数寄存器可以存储 8 个字节。</li>
</ul>
<p>寄存机的访问速度非常快，一般要求在半个 CPU 时钟周期内完成读写。比如一条要在 4 个周期内完成的指令，除了读写寄存器，还需要解码指令、控制指令执行和计算。如果寄存器的速度太慢，那 4 个周期就可能无法完成这条指令了。</p>
<h4>L1-Cache</h4>
<p>L1- 缓存在 CPU 中，相比寄存器，虽然它的位置距离 CPU 核心更远，但造价更低。通常 L1-Cache 大小在几十 Kb 到几百 Kb 不等，读写速度在 2~4 个 CPU 时钟周期。</p>
<h4>L2-Cache</h4>
<p>L2- 缓存也在 CPU 中，位置比 L1- 缓存距离 CPU 核心更远。它的大小比 L1-Cache 更大，具体大小要看 CPU 型号，有 2M 的，也有更小或者更大的，速度在 10~20 个 CPU 周期。</p>
<h4>L3-Cache</h4>
<p>L3- 缓存同样在 CPU 中，位置比 L2- 缓存距离 CPU 核心更远。大小通常比 L2-Cache 更大，读写速度在 20~60 个 CPU 周期。L3 缓存大小也是看型号的，比如 i9 CPU 有 512KB L1 Cache；有 2MB L2 Cache； 有16MB L3 Cache。</p>
<h4>内存</h4>
<p>内存的主要材料是半导体硅，是插在主板上工作的。因为它的位置距离 CPU 有一段距离，所以需要用总线和 CPU 连接。因为内存有了独立的空间，所以体积更大，造价也比上面提到的存储器低得多。现在有的个人电脑上的内存是 16G，但有些服务器的内存可以到几个 T。内存速度大概在 200~300 个 CPU 周期之间。</p>
<h3>SSD 和硬盘</h3>
<p>SSD 也叫固态硬盘，结构和内存类似，但是它的优点在于断电后数据还在。内存、寄存器、缓存断电后数据就消失了。内存的读写速度比 SSD 大概快 10~1000 倍。以前还有一种物理读写的磁盘，我们也叫作硬盘，它的速度比内存慢 100W 倍左右。因为它的速度太慢，现在已经逐渐被 SSD 替代。</p>
<p><img src="assets/Ciqc1F9kgMWAAU1JAABxd6qpCo0763.png" alt="Lark20200918-173926.png" /></p>
<p>当 CPU 需要内存中某个数据的时候，如果寄存器中有这个数据，我们可以直接使用；如果寄存器中没有这个数据，我们就要先查询 L1 缓存；L1 中没有，再查询 L2 缓存；L2 中没有再查询 L3 缓存；L3 中没有，再去内存中拿。</p>
<h3>缓存条目结构</h3>
<p>上面我们介绍了存储器分级结构大概有哪些存储以及它们的特点，接下来还有一些缓存算法和数据结构的设计困难要和你讨论。比如 CPU 想访问一个内存地址，那么如何检查这个数据是否在 L1- 缓存中？换句话说，缓存中的数据结构和算法是怎样的？</p>
<p>无论是缓存，还是内存，它们都是一个线性存储器，也就是数据一个挨着一个的存储。如果我们把内存想象成一个只有 1 列的表格，那么缓存就是一个多列的表格，这个表格中的每一行叫作一个缓存条目。</p>
<h4>方案 1</h4>
<p>缓存本质上是一个 Key-Value 的存储，它的 Key 是内存地址，值是缓存时刻内存地址中的值。我们先思考一种简单的方案，一个缓存条目设计 2 列：</p>
<ol>
<li>内存的地址；</li>
<li>缓存的值。</li>
</ol>
<p>CPU 读取到一个内存地址，我们就增加一个条目。当我们要查询一个内存地址的数据在不在 L1- 缓存中的时候，可以遍历每个条目，看条目中的内存地址是否和查询的内存地址相同。如果相同，我们就取出条目中缓存的值。</p>
<p>这个方法需要遍历缓存中的每个条目，因此计算速度会非常慢，在最坏情况下，算法需要检查所有的条目，所以这不是一个可行的方案。</p>
<h4>方案 2</h4>
<p>其实很多优秀的方案，往往是从最笨的方案改造而来的。现在我们已经拥有了一个方案，但是这个方案无法快速确定一个内存地址缓存在哪一行。因此我们想要找到一个更好的方法，让我们看到一个内存地址，就能够快速知道它在哪一行。</p>
<p>这里，我们可以用一个数学的方法。比如有 1000 个内存地址，但只有 10 个缓存条目。内存地址的编号是 0、1、2、3，...，999，缓存条目的编号是 0~9。我们思考一个内存编号，比如 701，然后用数学方法把它映射到一个缓存条目，比如 701 整除 10，得到缓存条目 1。</p>
<p>用这种方法，我们每次拿到一个内存地址，都可以快速确定它的缓存条目；然后再比较缓存条目中的第一列内存地址和查询的内存地址是否相同，就可以确定内存地址有没有被缓存。</p>
<p>延伸一下，这里用到了一种类似哈希表的方法：<code>地址 % 10</code>，其实就构成了一个简单的哈希函数。</p>
<h3>指令的预读</h3>
<p>接下来我们讨论下指令预读的问题。</p>
<p>之前我们学过，CPU 顺序执行内存中的指令，CPU 执行指令的速度是非常快的，一般是 2~6 个 CPU 时钟周期；这节课，我们学习了存储器分级策略，发现内存的读写速度其实是非常慢的，大概有 200~300 个时钟周期。</p>
<p>不知道你发现没有？这也产生了一个非常麻烦的问题：CPU 其实是不能从内存中一条条读取指令再执行的，如果是这样做，那每执行一条指令就需要 200~300 个时钟周期了。</p>
<p>那么，这个问题如何处理呢？</p>
<p>这里我再多说一句，你在做业务开发 RPC 调用的时候，其实也会经常碰到这种情况，远程调用拖慢了整体执行效率，下面我们一起讨论这类问题的解决方案。</p>
<p>一个解决办法就是 CPU 把内存中的指令预读几十条或者上百条到读写速度较快的 L1- 缓存中，因为 L1- 缓存的读写速度只有 2~4 个时钟周期，是可以跟上 CPU 的执行速度的。</p>
<p>这里又产生了另一个问题：如果数据和指令都存储在 L1- 缓存中，如果数据缓存覆盖了指令缓存，就会产生非常严重的后果。因此，L1- 缓存通常会分成两个区域，一个是指令区，一个是数据区。</p>
<p>与此同时，又出现了一个问题，L1- 缓存分成了指令区和数据区，那么 L2/L3 需不需要这样分呢？其实，是不需要的。因为 L2 和 L3，不需要协助处理指令预读的问题。</p>
<h3>缓存的命中率</h3>
<p>接下来，还有一个重要的问题需要解决。就是 L1/L2/L3 加起来，缓存的命中率有多少？</p>
<p>所谓命中就是指在缓存中找到需要的数据。和命中相反的是穿透，也叫 miss，就是一次读取操作没有从缓存中找到对应的数据。</p>
<p>据统计，L1 缓存的命中率在 80% 左右，L1/L2/L3 加起来的命中率在 95% 左右。因此，CPU 缓存的设计还是相当合理的。只有 5% 的内存读取会穿透到内存，95% 都能读取到缓存。 这也是为什么程序语言逐渐取消了让程序员操作寄存器的语法，因为缓存保证了很高的命中率，多余的优化意义不大，而且很容易出错。</p>
<h3>缓存置换问题</h3>
<p>最后的一个问题，比如现在 L1- 缓存条目已经存满了，接下来 CPU 又读了内存，需要把一个新的条目存到 L1- 缓存中，既然有一个新的条目要进来，那就有一个旧的条目要出去。所以，这个时候我们就需要用一个算法去计算哪个条目应该被置换出去。这个问题叫作缓存置换问题。有关缓存置换问题，我会在 “21 | 进程的调度：进程调度都有哪些方法？”中和你讨论。</p>
<h3>总结</h3>
<p>这节课我们讲到了存储器分级策略，讨论了 L1/L2/L3 缓存的工作原理。本课时学习的内容，是所有缓存知识的源头。所有缓存系统的设计，都是存储资源的分级。我们在设计缓存的时候，除了要关心整体架构外，还需要注意细节，比如：</p>
<ul>
<li>条目怎么设计？</li>
<li>算法怎么设计？</li>
<li>命中率怎么统计？</li>
<li>缓存怎么置换等？</li>
</ul>
<p>现在我们来说一下课前提出的问题：<strong>SSD、内存和 L1 Cache 相比速度差多少倍</strong>？</p>
<p>还是老规矩，请你先自己思考这个问题的答案，写在留言区，然后再来看我接下来的分析。</p>
<p><strong>【解析】</strong> 因为内存比 SSD 快 10~1000 倍，L1 Cache 比内存快 100 倍左右。因此 L1 Cache 比 SSD 快了 1000~100000 倍。所以你有没有发现 SSD 的潜力很大，好的 SSD 已经接近内存了，只不过造价还略高。</p>
<p>这个问题告诉我们，不同的存储器之间性能差距很大，构造存储器分级很有意义，分级的目的是要构造缓存体系。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;&#32;构造复杂的程序：将一个递归函数转成非递归函数的通用方法.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;(1)&#32;加餐&#32;&#32;练习题详解（一）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435ceae974645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
