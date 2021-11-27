<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>35  Linux 的 IO 模式：selectpollepoll 有什么区别？.md</title>
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

                    <a class="current-tab" href="35&#32;&#32;Linux&#32;的&#32;IO&#32;模式：selectpollepoll&#32;有什么区别？.md">35  Linux 的 IO 模式：selectpollepoll 有什么区别？.md</a>
                    

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
                        <div><h1>35  Linux 的 IO 模式：selectpollepoll 有什么区别？</h1>
<p>我们总是想方设法地提升系统的性能。操作系统层面不能给予处理业务逻辑太多帮助，但对于 I/O 性能，操作系统可以通过底层的优化，帮助应用做到极致。</p>
<p>这一讲我将和你一起讨论 I/O 模型。为了引发你更多的思考，我将同步/异步、阻塞/非阻塞等概念滞后讲解。<strong>我们先回到一个最基本的问题：如果有一台服务器，需要响应大量的请求，操作系统如何去架构以适应这样高并发的诉求</strong>。</p>
<p>说到架构，就离不开操作系统提供给应用程序的系统调用。我们今天要介绍的 select/poll/epoll 刚好是操作系统提供给应用的三类处理 I/O 的系统调用。这三类系统调用有非常强的代表性，这一讲我会围绕它们，以及处理并发和 I/O 多路复用，为你讲解操作系统的 I/O 模型。</p>
<h3>从网卡到操作系统</h3>
<p>为了弄清楚高并发网络场景是如何处理的，我们先来看一个最基本的内容：<strong>当数据到达网卡之后，操作系统会做哪些事情</strong>？</p>
<p>网络数据到达网卡之后，首先需要把数据拷贝到内存。拷贝到内存的工作往往不需要消耗 CPU 资源，而是通过 DMA 模块直接进行内存映射。之所以这样做，是因为网卡没有大量的内存空间，只能做简单的缓冲，所以必须赶紧将它们保存下来。</p>
<p>Linux 中用一个双向链表作为缓冲区，你可以观察下图中的 Buffer，看上去像一个有很多个凹槽的线性结构，每个凹槽（节点）可以存储一个封包，这个封包可以从网络层看（IP 封包），也可以从传输层看（TCP 封包）。操作系统不断地从 Buffer 中取出数据，数据通过一个协议栈，你可以把它理解成很多个协议的集合。协议栈中数据封包找到对应的协议程序处理完之后，就会形成 Socket 文件。</p>
<p><img src="assets/Cip5yGABb8uAECMGAAERrnFoSrI090.png" alt="1111.png" />!</p>
<p>如果高并发的请求量级实在太大，有可能把 Buffer 占满，此时，操作系统就会拒绝服务。网络上有一种著名的攻击叫作<strong>拒绝服务攻击</strong>，就是利用的这个原理。<strong>操作系统拒绝服务，实际上是一种保护策略。通过拒绝服务，避免系统内部应用因为并发量太大而雪崩</strong>。</p>
<p>如上图所示，传入网卡的数据被我称为 Frames。一个 Frame 是数据链路层的传输单位（或封包）。现代的网卡通常使用 DMA 技术，将 Frame 写入缓冲区（Buffer），然后在触发 CPU 中断交给操作系统处理。操作系统从缓冲区中不断取出 Frame，通过协进栈（具体的协议）进行还原。</p>
<p>在 UNIX 系的操作系统中，一个 Socket 文件内部类似一个双向的管道。因此，非常适用于进程间通信。在网络当中，本质上并没有发生变化。网络中的 Socket 一端连接 Buffer， 一端连接应用——也就是进程。网卡的数据会进入 Buffer，Buffer 经过协议栈的处理形成 Socket 结构。通过这样的设计，进程读取 Socket 文件，可以从 Buffer 中对应节点读走数据。</p>
<p>对于 TCP 协议，Socket 文件可以用源端口、目标端口、源 IP、目标 IP 进行区别。不同的 Socket 文件，对应着 Buffer 中的不同节点。进程们读取数据的时候从 Buffer 中读取，写入数据的时候向 Buffer 中写入。通过这样一种结构，无论是读和写，进程都可以快速定位到自己对应的节点。</p>
<p>以上就是我们对操作系统和网络接口交互的一个基本讨论。接下来，我们讨论一下作为一个编程模型的 Socket。</p>
<h3>Socket 编程模型</h3>
<p>通过前面讲述，我们知道 Socket 在操作系统中，有一个非常具体的从 Buffer 到文件的实现。但是对于进程而言，Socket 更多是一种编程的模型。接下来我们讨论作为编程模型的 Socket。</p>
<p><img src="assets/Ciqc1GABP3OAHezqAABndlGAu9c457.png" alt="Lark20210115-150702.png" /></p>
<p>如上图所示，Socket 连接了应用和协议，如果应用层的程序想要传输数据，就创建一个 Socket。应用向 Socket 中写入数据，相当于将数据发送给了另一个应用。应用从 Socket 中读取数据，相当于接收另一个应用发送的数据。而具体的操作就是由 Socket 进行封装。具体来说，<strong>对于 UNIX 系的操作系统，是利用 Socket 文件系统，Socket 是一种特殊的文件——每个都是一个双向的管道。一端是应用，一端是缓冲</strong>区。</p>
<p>那么作为一个服务端的应用，如何知道有哪些 Socket 呢？也就是，哪些客户端连接过来了呢？这是就需要一种特殊类型的 Socket，也就是服务端 Socket 文件。</p>
<p><img src="assets/Ciqc1GABP3qADKbBAAB564sk120429.png" alt="Lark20210115-150706.png" /></p>
<p>如上图所示，当有客户端连接服务端时，服务端 Socket 文件中会写入这个客户端 Socket 的文件描述符。进程可以通过 accept() 方法，从服务端 Socket 文件中读出客户端的 Socket 文件描述符，从而拿到客户端的 Socket 文件。</p>
<p>程序员实现一个网络服务器的时候，会先手动去创建一个服务端 Socket 文件。服务端的 Socket 文件依然会存在操作系统内核之中，并且会绑定到某个 IP 地址和端口上。以后凡是发送到这台机器、目标 IP 地址和端口号的连接请求，在形成了客户端 Socket 文件之后，文件的文件描述符都会被写入到服务端的 Socket 文件中。应用只要调用 accept 方法，就可以拿到这些客户端的 Socket 文件描述符，这样服务端的应用就可以方便地知道有哪些客户端连接了进来。</p>
<p>而每个客户端对这个应用而言，都是一个文件描述符。如果需要读取某个客户端的数据，就读取这个客户端对应的 Socket 文件。如果要向某个特定的客户端发送数据，就写入这个客户端的 Socket 文件。</p>
<p>以上就是 Socket 的编程模型。</p>
<h3>I/O 多路复用</h3>
<p>在上面的讨论当中，进程拿到了它关注的所有 Socket，也称作关注的集合（Intersting Set）。如下图所示，这种过程相当于进程从所有的 Socket 中，筛选出了自己关注的一个子集，但是这时还有一个问题没有解决：<strong>进程如何监听关注集合的状态变化，比如说在有数据进来，如何通知到这个进程</strong>？</p>
<p><img src="assets/Ciqc1GABP4OAdKBcAACAbVkbI0g191.png" alt="Lark20210115-150708.png" /></p>
<p>其实更准确地说，一个线程需要处理所有关注的 Socket 产生的变化，或者说消息。实际上一个线程要处理很多个文件的 I/O。<strong>所有关注的 Socket 状态发生了变化，都由一个线程去处理，构成了 I/O 的多路复用问题</strong>。如下图所示：</p>
<p><img src="assets/Ciqc1GABP4uAW8-dAAB_SubmZ4Q301.png" alt="Lark20210115-150711.png" /></p>
<p>处理 I/O 多路复用的问题，需要操作系统提供内核级别的支持。Linux 下有三种提供 I/O 多路复用的 API，分别是：</p>
<ul>
<li>select</li>
<li>poll</li>
<li>epoll</li>
</ul>
<p>如下图所示，内核了解网络的状态。因此不难知道具体发生了什么消息，比如内核知道某个 Socket 文件状态发生了变化。但是内核如何知道该把哪个消息给哪个进程呢？</p>
<p><img src="assets/Ciqc1GABP5KAVSWVAAFSurtl2bU931.png" alt="Lark20210115-150654.png" /></p>
<p><strong>一个 Socket 文件，可以由多个进程使用；而一个进程，也可以使用多个 Socket 文件</strong>。进程和 Socket 之间是多对多的关系。<strong>另一方面，一个 Socket 也会有不同的事件类型</strong>。因此操作系统很难判断，将哪样的事件给哪个进程。</p>
<p>这样<strong>在进程内部就需要一个数据结构来描述自己会关注哪些 Socket 文件的哪些事件（读、写、异常等</strong>）。通常有两种考虑方向，<strong>一种是利用线性结构</strong>，比如说数组、链表等，这类结构的查询需要遍历。每次内核产生一种消息，就遍历这个线性结构。看看这个消息是不是进程关注的？<strong>另一种是索引结构</strong>，内核发生了消息可以通过索引结构马上知道这个消息进程关不关注。</p>
<h4>select()</h4>
<p>select 和 poll 都采用线性结构，select 允许用户传入 3 个集合。如下面这段程序所示：</p>
<pre><code>fd_set read_fd_set, write_fd_set, error_fd_set;

while(true) {

  select(..., &amp;read_fd_set, &amp;write_fd_set, &amp;error_fd_set); 

}
</code></pre>
<p><strong>每次 select 操作会阻塞当前线程，在阻塞期间所有操作系统产生的每个消息，都会通过遍历的手段查看是否在 3 个集合当中</strong>。上面程序<code>read_fd_set</code>中放入的是当数据可以读取时进程关心的 Socket；<code>write_fd_set</code>是当数据可以写入时进程关心的 Socket；<code>error_fd_set</code>是当发生异常时进程关心的 Socket。</p>
<p>**用户程序可以根据不同集合中是否有某个 Socket 判断发生的消息类型，**程序如下所示：</p>
<pre><code>fd_set read_fd_set, write_fd_set, error_fd_set;

while(true) {

  select(..., &amp;read_fd_set, &amp;write_fd_set, &amp;error_fd_set); 

  for (i = 0; i &lt; FD_SETSIZE; ++i)

        if (FD_ISSET (i, &amp;read_fd_set)){

          // Socket可以读取

        } else if(FD_ISSET(i, &amp;write_fd_set)) {

          // Socket可以写入

        } else if(FD_ISSET(i, &amp;error_fd_set)) {

          // Socket发生错误

        } 

}
</code></pre>
<p>上面程序中的 FD_SETSIZE 是一个系统的默认设置，通常是 1024。可以看出，select 模式能够一次处理的文件描述符是有上限的，也就是 FD_SETSIZE。当并发请求过多的时候， select 就无能为力了。但是对单台机器而言，1024 个并发已经是一个非常大的流量了。</p>
<p>接下来我给出一个完整的、用 select 实现的服务端程序供你参考，如下所示：</p>
<pre><code>#include &lt;stdio.h&gt;

#include &lt;errno.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;unistd.h&gt;

#include &lt;sys/types.h&gt;

#include &lt;sys/Socket.h&gt;

#include &lt;netinet/in.h&gt;

#include &lt;netdb.h&gt;

#define PORT    5555

#define MAXMSG  512

int

read_from_client (int filedes)

{

  char buffer[MAXMSG];

  int nbytes;

  nbytes = read (filedes, buffer, MAXMSG);

  if (nbytes &lt; 0)

    {

      /* Read error. */

      perror (&quot;read&quot;);

      exit (EXIT_FAILURE);

    }

  else if (nbytes == 0)

    /* End-of-file. */

    return -1;

  else

    {

      /* Data read. */

      fprintf (stderr, &quot;Server: got message: `%s'\n&quot;, buffer);

      return 0;

    }

}

int

main (void)

{

  extern int make_Socket (uint16_t port);

  int sock;

  fd_set active_fd_set, read_fd_set;

  int i;

  struct sockaddr_in clientname;

  size_t size;

  /* Create the Socket and set it up to accept connections. */

  sock = make_Socket (PORT);

  if (listen (sock, 1) &lt; 0)

    {

      perror (&quot;listen&quot;);

      exit (EXIT_FAILURE);

    }

  /* Initialize the set of active Sockets. */

  FD_ZERO (&amp;active_fd_set);

  FD_SET (sock, &amp;active_fd_set);

  while (1)

    {

      /* Block until input arrives on one or more active Sockets. */

      read_fd_set = active_fd_set;

      if (select (FD_SETSIZE, &amp;read_fd_set, NULL, NULL, NULL) &lt; 0)

        {

          perror (&quot;select&quot;);

          exit (EXIT_FAILURE);

        }

      /* Service all the Sockets with input pending. */

      for (i = 0; i &lt; FD_SETSIZE; ++i)

        if (FD_ISSET (i, &amp;read_fd_set))

          {

            if (i == sock)

              {

                /* Connection request on original Socket. */

                int new;

                size = sizeof (clientname);

                new = accept (sock,

                              (struct sockaddr *) &amp;clientname,

                              &amp;size);

                if (new &lt; 0)

                  {

                    perror (&quot;accept&quot;);

                    exit (EXIT_FAILURE);

                  }

                fprintf (stderr,

                         &quot;Server: connect from host %s, port %hd.\n&quot;,

                         inet_ntoa (clientname.sin_addr),

                         ntohs (clientname.sin_port));

                FD_SET (new, &amp;active_fd_set);

              }

            else

              {

                /* Data arriving on an already-connected Socket. */

                if (read_from_client (i) &lt; 0)

                  {

                    close (i);

                    FD_CLR (i, &amp;active_fd_set);

                  }

              }

          }

    }

}
</code></pre>
<h4>poll()</h4>
<p>从写程序的角度来看，select 并不是一个很好的编程模型。一个好的编程模型应该直达本质，当网络请求发生状态变化的时候，核心是会发生事件。<strong>一个好的编程模型应该是直接抽象成消息：用户不需要用 select 来设置自己的集合，而是可以通过系统的 API 直接拿到对应的消息，从而处理对应的文件描述符</strong>。</p>
<p>比如下面这段伪代码就是一个更好的编程模型，具体的分析如下：</p>
<ul>
<li>poll 是一个阻塞调用，它将某段时间内操作系统内发生的且进程关注的消息告知用户程序；</li>
<li>用户程序通过直接调用 poll 函数拿到消息；</li>
<li>poll 函数的第一个参数告知内核 poll 关注哪些 Socket 及消息类型；</li>
<li>poll 调用后，经过一段时间的等待（阻塞），就拿到了是一个消息的数组；</li>
<li>通过遍历这个数组中的消息，能够知道关联的文件描述符和消息的类型；</li>
<li>通过消息类型判断接下来该进行读取还是写入操作；</li>
<li>通过文件描述符，可以进行实际地读、写、错误处理。</li>
</ul>
<pre><code>while(true) {

  events = poll(fds, ...)

  for(evt in events) {

    fd = evt.fd;

    type = evt.revents;

    if(type &amp; POLLIN ) {

       // 有数据需要读，读取fd中的数据

    } else if(type &amp; POLLOUT) {

       // 可以写入数据

    } 

    else ...

  }

}
</code></pre>
<p>poll 虽然优化了编程模型，但是从性能角度分析，它和 select 差距不大。因为内核在产生一个消息之后，依然需要遍历 poll 关注的所有文件描述符来确定这条消息是否跟用户程序相关。</p>
<h4>epoll</h4>
<p>为了解决上述问题，<strong>epoll 通过更好的方案实现了从操作系统订阅消息。epoll 将进程关注的文件描述符存入一棵二叉搜索树，通常是红黑树的实现</strong>。在这棵红黑树当中，Key 是 Socket 的编号，值是这个 Socket 关注的消息。因此，当内核发生了一个事件：比如 Socket 编号 1000 可以读取。这个时候，可以马上从红黑树中找到进程是否关注这个事件。</p>
<p><strong>另外当有关注的事件发生时，epoll 会先放到一个队列当中。当用户调用</strong><code>epoll_wait</code>时候，就会从队列中返回一个消息。epoll 函数本身是一个构造函数，只用来创建红黑树和队列结构。<code>epoll_wait</code>调用后，如果队列中没有消息，也可以马上返回。因此<code>epoll</code>是一个非阻塞模型。</p>
<p><strong>总结一下，select/poll 是阻塞模型，epoll 是非阻塞模型</strong>。<strong>当然，并不是说非阻塞模型性能就更好。在多数情况下，epoll 性能更好是因为内部有红黑树的实现</strong>。</p>
<p>最后我再贴一段用 epoll 实现的 Socket 服务给你做参考，这段程序的作者将这段代码放到了 Public Domain，你以后看到公有领域的代码可以放心地使用。</p>
<p>下面这段程序跟之前 select 的原理一致，对于每一个新的客户端连接，都使用 accept 拿到这个连接的文件描述符，并且创建一个客户端的 Socket。然后通过<code>epoll_ctl</code>将客户端的文件描述符和关注的消息类型放入 epoll 的红黑树。操作系统每次监测到一个新的消息产生，就会通过红黑树对比这个消息是不是进程关注的（当然这段代码你看不到，因为它在内核程序中）。</p>
<p><strong>非阻塞模型的核心价值，并不是性能更好。当真的高并发来临的时候，所有的 CPU 资源，所有的网络资源可能都会被用完。这个时候无论是阻塞还是非阻塞，结果都不会相差太大</strong>。（前提是程序没有写错）。</p>
<p><code>epoll</code>有 2 个最大的优势：</p>
<ol>
<li>内部使用红黑树减少了内核的比较操作；</li>
<li>对于程序员而言，非阻塞的模型更容易处理各种各样的情况。程序员习惯了写出每一条语句就可以马上得到结果，这样不容易出 Bug。</li>
</ol>
<pre><code>// Asynchronous Socket server - accepting multiple clients concurrently,

	// multiplexing the connections with epoll.

	//

	// Eli Bendersky [http://eli.thegreenplace.net]

	// This code is in the public domain.

	#include &lt;assert.h&gt;

	#include &lt;errno.h&gt;

	#include &lt;stdbool.h&gt;

	#include &lt;stdint.h&gt;

	#include &lt;stdio.h&gt;

	#include &lt;stdlib.h&gt;

	#include &lt;string.h&gt;

	#include &lt;sys/epoll.h&gt;

	#include &lt;sys/Socket.h&gt;

	#include &lt;sys/types.h&gt;

	#include &lt;unistd.h&gt;

	

	#include &quot;utils.h&quot;

	

	#define MAXFDS 16 * 1024

	

	typedef enum { INITIAL_ACK, WAIT_FOR_MSG, IN_MSG } ProcessingState;

	

	#define SENDBUF_SIZE 1024

	

	typedef struct {

	  ProcessingState state;

	  uint8_t sendbuf[SENDBUF_SIZE];

	  int sendbuf_end;

	  int sendptr;

	} peer_state_t;

	

	// Each peer is globally identified by the file descriptor (fd) it's connected

	// on. As long as the peer is connected, the fd is unique to it. When a peer

	// disconnects, a new peer may connect and get the same fd. on_peer_connected

	// should initialize the state properly to remove any trace of the old peer on

	// the same fd.

	peer_state_t global_state[MAXFDS];

	

	// Callbacks (on_XXX functions) return this status to the main loop; the status

	// instructs the loop about the next steps for the fd for which the callback was

	// invoked.

	// want_read=true means we want to keep monitoring this fd for reading.

	// want_write=true means we want to keep monitoring this fd for writing.

	// When both are false it means the fd is no longer needed and can be closed.

	typedef struct {

	  bool want_read;

	  bool want_write;

	} fd_status_t;

	

	// These constants make creating fd_status_t values less verbose.

	const fd_status_t fd_status_R = {.want_read = true, .want_write = false};

	const fd_status_t fd_status_W = {.want_read = false, .want_write = true};

	const fd_status_t fd_status_RW = {.want_read = true, .want_write = true};

	const fd_status_t fd_status_NORW = {.want_read = false, .want_write = false};

	

	fd_status_t on_peer_connected(int sockfd, const struct sockaddr_in* peer_addr,

	                              socklen_t peer_addr_len) {

	  assert(sockfd &lt; MAXFDS);

	  report_peer_connected(peer_addr, peer_addr_len);

	

	  // Initialize state to send back a '*' to the peer immediately.

	  peer_state_t* peerstate = &amp;global_state[sockfd];

	  peerstate-&gt;state = INITIAL_ACK;

	  peerstate-&gt;sendbuf[0] = '*';

	  peerstate-&gt;sendptr = 0;

	  peerstate-&gt;sendbuf_end = 1;

	

	  // Signal that this Socket is ready for writing now.

	  return fd_status_W;

	}

	

	fd_status_t on_peer_ready_recv(int sockfd) {

	  assert(sockfd &lt; MAXFDS);

	  peer_state_t* peerstate = &amp;global_state[sockfd];

	

	  if (peerstate-&gt;state == INITIAL_ACK ||

	      peerstate-&gt;sendptr &lt; peerstate-&gt;sendbuf_end) {

	    // Until the initial ACK has been sent to the peer, there's nothing we

	    // want to receive. Also, wait until all data staged for sending is sent to

	    // receive more data.

	    return fd_status_W;

	  }

	

	  uint8_t buf[1024];

	  int nbytes = recv(sockfd, buf, sizeof buf, 0);

	  if (nbytes == 0) {

	    // The peer disconnected.

	    return fd_status_NORW;

	  } else if (nbytes &lt; 0) {

	    if (errno == EAGAIN || errno == EWOULDBLOCK) {

	      // The Socket is not *really* ready for recv; wait until it is.

	      return fd_status_R;

	    } else {

	      perror_die(&quot;recv&quot;);

	    }

	  }

	  bool ready_to_send = false;

	  for (int i = 0; i &lt; nbytes; ++i) {

	    switch (peerstate-&gt;state) {

	    case INITIAL_ACK:

	      assert(0 &amp;&amp; &quot;can't reach here&quot;);

	      break;

	    case WAIT_FOR_MSG:

	      if (buf[i] == '^') {

	        peerstate-&gt;state = IN_MSG;

	      }

	      break;

	    case IN_MSG:

	      if (buf[i] == '$') {

	        peerstate-&gt;state = WAIT_FOR_MSG;

	      } else {

	        assert(peerstate-&gt;sendbuf_end &lt; SENDBUF_SIZE);

	        peerstate-&gt;sendbuf[peerstate-&gt;sendbuf_end++] = buf[i] + 1;

	        ready_to_send = true;

	      }

	      break;

	    }

	  }

	  // Report reading readiness iff there's nothing to send to the peer as a

	  // result of the latest recv.

	  return (fd_status_t){.want_read = !ready_to_send,

	                       .want_write = ready_to_send};

	}

	

	fd_status_t on_peer_ready_send(int sockfd) {

	  assert(sockfd &lt; MAXFDS);

	  peer_state_t* peerstate = &amp;global_state[sockfd];

	

	  if (peerstate-&gt;sendptr &gt;= peerstate-&gt;sendbuf_end) {

	    // Nothing to send.

	    return fd_status_RW;

	  }

	  int sendlen = peerstate-&gt;sendbuf_end - peerstate-&gt;sendptr;

	  int nsent = send(sockfd, &amp;peerstate-&gt;sendbuf[peerstate-&gt;sendptr], sendlen, 0);

	  if (nsent == -1) {

	    if (errno == EAGAIN || errno == EWOULDBLOCK) {

	      return fd_status_W;

	    } else {

	      perror_die(&quot;send&quot;);

	    }

	  }

	  if (nsent &lt; sendlen) {

	    peerstate-&gt;sendptr += nsent;

	    return fd_status_W;

	  } else {

	    // Everything was sent successfully; reset the send queue.

	    peerstate-&gt;sendptr = 0;

	    peerstate-&gt;sendbuf_end = 0;

	

	    // Special-case state transition in if we were in INITIAL_ACK until now.

	    if (peerstate-&gt;state == INITIAL_ACK) {

	      peerstate-&gt;state = WAIT_FOR_MSG;

	    }

	

	    return fd_status_R;

	  }

	}

	

	int main(int argc, const char** argv) {

	  setvbuf(stdout, NULL, _IONBF, 0);

	

	  int portnum = 9090;

	  if (argc &gt;= 2) {

	    portnum = atoi(argv[1]);

	  }

	  printf(&quot;Serving on port %d\n&quot;, portnum);

	

	  int listener_sockfd = listen_inet_Socket(portnum);

	  make_Socket_non_blocking(listener_sockfd);

	

	  int epollfd = epoll_create1(0);

	  if (epollfd &lt; 0) {

	    perror_die(&quot;epoll_create1&quot;);

	  }

	

	  struct epoll_event accept_event;

	  accept_event.data.fd = listener_sockfd;

	  accept_event.events = EPOLLIN;

	  if (epoll_ctl(epollfd, EPOLL_CTL_ADD, listener_sockfd, &amp;accept_event) &lt; 0) {

	    perror_die(&quot;epoll_ctl EPOLL_CTL_ADD&quot;);

	  }

	

	  struct epoll_event* events = calloc(MAXFDS, sizeof(struct epoll_event));

	  if (events == NULL) {

	    die(&quot;Unable to allocate memory for epoll_events&quot;);

	  }

	

	  while (1) {

	    int nready = epoll_wait(epollfd, events, MAXFDS, -1);

	    for (int i = 0; i &lt; nready; i++) {

	      if (events[i].events &amp; EPOLLERR) {

	        perror_die(&quot;epoll_wait returned EPOLLERR&quot;);

	      }

	

	      if (events[i].data.fd == listener_sockfd) {

	        // The listening Socket is ready; this means a new peer is connecting.

	

	        struct sockaddr_in peer_addr;

	        socklen_t peer_addr_len = sizeof(peer_addr);

	        int newsockfd = accept(listener_sockfd, (struct sockaddr*)&amp;peer_addr,

	                               &amp;peer_addr_len);

	        if (newsockfd &lt; 0) {

	          if (errno == EAGAIN || errno == EWOULDBLOCK) {

	            // This can happen due to the nonblocking Socket mode; in this

	            // case don't do anything, but print a notice (since these events

	            // are extremely rare and interesting to observe...)

	            printf(&quot;accept returned EAGAIN or EWOULDBLOCK\n&quot;);

	          } else {

	            perror_die(&quot;accept&quot;);

	          }

	        } else {

	          make_Socket_non_blocking(newsockfd);

	          if (newsockfd &gt;= MAXFDS) {

	            die(&quot;Socket fd (%d) &gt;= MAXFDS (%d)&quot;, newsockfd, MAXFDS);

	          }

	

	          fd_status_t status =

	              on_peer_connected(newsockfd, &amp;peer_addr, peer_addr_len);

	          struct epoll_event event = {0};

	          event.data.fd = newsockfd;

	          if (status.want_read) {

	            event.events |= EPOLLIN;

	          }

	          if (status.want_write) {

	            event.events |= EPOLLOUT;

	          }

	

	          if (epoll_ctl(epollfd, EPOLL_CTL_ADD, newsockfd, &amp;event) &lt; 0) {

	            perror_die(&quot;epoll_ctl EPOLL_CTL_ADD&quot;);

	          }

	        }

	      } else {

	        // A peer Socket is ready.

	        if (events[i].events &amp; EPOLLIN) {

	          // Ready for reading.

	          int fd = events[i].data.fd;

	          fd_status_t status = on_peer_ready_recv(fd);

	          struct epoll_event event = {0};

	          event.data.fd = fd;

	          if (status.want_read) {

	            event.events |= EPOLLIN;

	          }

	          if (status.want_write) {

	            event.events |= EPOLLOUT;

	          }

	          if (event.events == 0) {

	            printf(&quot;Socket %d closing\n&quot;, fd);

	            if (epoll_ctl(epollfd, EPOLL_CTL_DEL, fd, NULL) &lt; 0) {

	              perror_die(&quot;epoll_ctl EPOLL_CTL_DEL&quot;);

	            }

	            close(fd);

	          } else if (epoll_ctl(epollfd, EPOLL_CTL_MOD, fd, &amp;event) &lt; 0) {

	            perror_die(&quot;epoll_ctl EPOLL_CTL_MOD&quot;);

	          }

	        } else if (events[i].events &amp; EPOLLOUT) {

	          // Ready for writing.

	          int fd = events[i].data.fd;

	          fd_status_t status = on_peer_ready_send(fd);

	          struct epoll_event event = {0};

	          event.data.fd = fd;

	

	          if (status.want_read) {

	            event.events |= EPOLLIN;

	          }

	          if (status.want_write) {

	            event.events |= EPOLLOUT;

	          }

	          if (event.events == 0) {

	            printf(&quot;Socket %d closing\n&quot;, fd);

	            if (epoll_ctl(epollfd, EPOLL_CTL_DEL, fd, NULL) &lt; 0) {

	              perror_die(&quot;epoll_ctl EPOLL_CTL_DEL&quot;);

	            }

	            close(fd);

	          } else if (epoll_ctl(epollfd, EPOLL_CTL_MOD, fd, &amp;event) &lt; 0) {

	            perror_die(&quot;epoll_ctl EPOLL_CTL_MOD&quot;);

	          }

	        }

	      }

	    }

	  }

	

	  return 0;

	}
</code></pre>
<h3>重新思考：I/O 模型</h3>
<p>在上面的模型当中，select/poll 是阻塞（Blocking）模型，epoll 是非阻塞（Non-Blocking）模型。<strong>阻塞和非阻塞强调的是线程的状态</strong>，所以阻塞就是触发了线程的阻塞状态，线程阻塞了就停止执行，并且切换到其他线程去执行，直到触发中断再回来。</p>
<p>还有一组概念是同步（Synchrounous）和异步（Asynchrounous），select/poll/epoll 三者都是同步调用。</p>
<p>**同步强调的是顺序，**所谓同步调用，就是可以确定程序执行的顺序的调用。比如说执行一个调用，知道调用返回之前下一行代码不会执行。这种顺序是确定的情况，就是同步。</p>
<p>而异步调用则恰恰相反，<strong>异步调用不明确执行顺序</strong>。比如说一个回调函数，不知道何时会回来。异步调用会加大程序员的负担，因为我们习惯顺序地思考程序。因此，我们还会发明像协程的 yield 、迭代器等将异步程序转为同步程序。</p>
<p>由此可见，<strong>非阻塞不一定是异步，阻塞也未必就是同步</strong>。比如一个带有回调函数的方法，阻塞了线程 100 毫秒，又提供了回调函数，那这个方法是异步阻塞。例如下面的伪代码：</p>
<pre><code>asleep(100ms, () -&gt; {

  // 100ms 或更多后到这里

  // ...do some thing

})

// 100 ms 后到这里
</code></pre>
<h3>总结</h3>
<p>总结下，操作系统给大家提供各种各样的 API，是希望满足各种各样程序架构的诉求。但总体诉求其实是一致的：希望程序员写的单机代码，能够在多线程甚至分布式的环境下执行。这样你就不需要再去学习复杂的并发控制算法。从这个角度去看，非阻塞加上同步的编程模型确实省去了我们编程过程当中的很多思考。</p>
<p>但可惜的是，至少在今天这个时代，<strong>多线程、并发编程依然是程序员们的必修课</strong>。因此你在思考 I/O 模型的时候，还是需要结合自己的业务特性及系统自身的架构特点，进行选择。<strong>I/O 模型并不是选择效率，而是选择编程的手段</strong>。试想一个所有资源都跑满了的服务器，并不会因为是异步或者非阻塞模型就获得更高的吞吐量。</p>
<p><strong>那么通过以上的学习，你现在可以尝试来回答本讲关联的面试题目：select/poll/epoll 有什么区别</strong>？</p>
<p>【<strong>解析</strong>】这三者都是处理 I/O 多路复用的编程手段。select/poll 模型是一种阻塞模型，epoll 是非阻塞模型。select/poll 内部使用线性结构存储进程关注的 Socket 集合，因此每次内核要判断某个消息是否发送给 select/poll 需要遍历进程关注的 Socket 集合。</p>
<p>而 epoll 不同，epoll 内部使用二叉搜索树（红黑树），用 Socket 编号作为索引，用关注的事件类型作为值，这样内核可以在非常快的速度下就判断某个消息是否需要发送给使用 epoll 的线程。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="34&#32;&#32;UDP&#32;协议：UDP&#32;和&#32;TCP&#32;相比快在哪里？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="36&#32;&#32;公私钥体系和网络安全：什么是中间人攻击？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435dc27b78645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
