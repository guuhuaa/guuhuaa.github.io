<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>09  Linux 中的网络指令：如何查看一个域名有哪些 NS 记录？.md</title>
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

                    <a class="current-tab" href="09&#32;&#32;Linux&#32;中的网络指令：如何查看一个域名有哪些&#32;NS&#32;记录？.md">09  Linux 中的网络指令：如何查看一个域名有哪些 NS 记录？.md</a>
                    

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
                        <div><h1>09  Linux 中的网络指令：如何查看一个域名有哪些 NS 记录？</h1>
<p><strong>我看到过一道关于 Linux 指令的面试题：如何查看一个域名有哪些 NS 记录</strong>？</p>
<p>这类题目是根据一个场景，考察一件具体的事情如何处理。虽然你可以通过查资料找到解决方案，但是，这类问题在面试中还是有必要穿插一下，用于确定求职者技能是否熟练、经验是否丰富。特别是计算机网络相关的指令，平时在远程操作、开发、联调、Debug 线上问题的时候，会经常用到。</p>
<p>Linux 中提供了不少网络相关的指令，因为网络指令比较分散，本课时会从下面几个维度给你介绍，帮助你梳理常用的网络指令：</p>
<ul>
<li>远程操作；</li>
<li>查看本地网络状态；</li>
<li>网络测试；</li>
<li>DNS 查询；</li>
<li>HTTP。</li>
</ul>
<p>这块知识从体系上属于 Linux 指令，同时也关联了很多计算机网络的知识，比如说 TCP/IP 协议、UDP 协议，我会在“<strong>模块七</strong>”为你简要介绍。</p>
<p>如果你对这部分指令背后的网络原理有什么困惑，可以在评论区提问。另外，你也可以关注我将在拉勾教育推出的《<strong>计算机网络</strong>》课程。下面我们开始学习今天的内容。</p>
<h3>远程操作指令</h3>
<p>远程操作指令用得最多的是<code>ssh</code>，<code>ssh</code>指令允许远程登录到目标计算机并进行远程操作和管理。还有一个比较常用的远程指令是<code>scp</code>，<code>scp</code>帮助我们远程传送文件。</p>
<h4>ssh（Secure Shell）</h4>
<p>有一种场景需要远程登录一个 Linux 系统，这时我们会用到<code>ssh</code>指令。比如你想远程登录一台机器，可以使用<code>ssh <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c6b3b5a3b486afb6">[email&#160;protected]</a></code>的方式，如下图所示：</p>
<p><img src="assets/CgqCHl92j8GAMNHAAAPCrIyhHHk744.png" alt="Drawing 0.png" /></p>
<p>上图中，我在使用<code>ssh</code>指令从机器<code>u1</code>登录我的另一台虚拟机<code>u2</code>。这里<code>u1</code>和<code>u2</code>对应着 IP 地址，是我在<code>/etc/hosts</code>中设置的，如下图所示：</p>
<p><img src="assets/CgqCHl92j8mAIMPdAACTOATTrQM694.png" alt="Drawing 1.png" /></p>
<p><code>/etc/hosts</code>这个文件可以设置 IP 地址对应的域名。我这里是一个小集群，总共有两台机器，因此我设置了方便记忆和操作的名字。</p>
<h4>scp</h4>
<p>另一种场景是我需要拷贝一个文件到远程，这时可以使用<code>scp</code>指令，如下图，我使用<code>scp</code>指令将本地计算机的一个文件拷贝到了 ubuntu 虚拟机用户的家目录中。</p>
<p>比如从<code>u1</code>拷贝家目录下的文件<code>a.txt</code>到<code>u2</code>。家目录有一个简写，就是用<code>~</code>。具体指令见下图：</p>
<p><img src="assets/Ciqc1F92j9OADjTcAAPER8w5DNg904.png" alt="Drawing 2.png" /></p>
<p>输入 scp 指令之后会弹出一个提示，要求输入密码，系统验证通过后文件会被成功拷贝。</p>
<h3>查看本地网络状态</h3>
<p>如果你想要了解本地的网络状态，比较常用的网络指令是<code>ifconfig</code>和<code>netstat</code>。</p>
<h4>ifconfig</h4>
<p>当你想知道本地<code>ip</code>以及本地有哪些网络接口时，就可以使用<code>ifconfig</code>指令。你可以把一个网络接口理解成一个网卡，有时候虚拟机会装虚拟网卡，虚拟网卡是用软件模拟的网卡。</p>
<p>比如：VMware 为每个虚拟机创造一个虚拟网卡，通过虚拟网卡接入虚拟网络。当然物理机也可以接入虚拟网络，它可以通过虚拟网络向虚拟机的虚拟网卡上发送信息。</p>
<p>下图是我的 ubuntu 虚拟机用 ifconfig 查看网络接口信息。</p>
<p><img src="assets/Ciqc1F92j9yAaioXAAbz00ZJYlw555.png" alt="Drawing 3.png" /></p>
<p>可以看到我的这台 ubuntu 虚拟机一共有 2 个网卡，ens33 和 lo。<code>lo</code>是本地回路（local lookback），发送给<code>lo</code>就相当于发送给本机。<code>ens33</code>是一块连接着真实网络的虚拟网卡。</p>
<h4>netstat</h4>
<p>另一个查看网络状态的场景是想看目前本机的网络使用情况，这个时候可以用<code>netstat</code>。</p>
<p><strong>默认行为</strong></p>
<p>不传任何参数的<code>netstat</code>帮助查询所有的本地 socket，下图是<code>netstat | less</code>的结果。</p>
<p><img src="assets/Ciqc1F92j-aAAZlfAAizLye7uc4727.png" alt="Drawing 4.png" /></p>
<p>如上图，我们看到的是 socket 文件。socket 是网络插槽被抽象成了文件，负责在客户端、服务器之间收发数据。当客户端和服务端发生连接时，客户端和服务端会同时各自生成一个 socket 文件，用于管理这个连接。这里，可以用<code>wc -l</code>数一下有多少个<code>socket</code>。</p>
<p><img src="assets/Ciqc1F92j-2AVEYjAAA8xcVMQzc068.png" alt="Drawing 5.png" /></p>
<p>你可以看到一共有 615 个 socket 文件，因为有很多 socket 在解决进程间的通信。就是将两个进程一个想象成客户端，一个想象成服务端。并不是真的有 600 多个连接着互联网的请求。</p>
<p><strong>查看 TCP 连接</strong></p>
<p>如果想看有哪些 TCP 连接，可以使用<code>netstat -t</code>。比如下面我通过<code>netstat -t</code>看<code>tcp</code>协议的网络情况：</p>
<p><img src="assets/CgqCHl92j_aAbxdlAAEAdzG3a2s636.png" alt="Drawing 6.png" /></p>
<p>这里没有找到连接中的<code>tcp</code>，因为我们这台虚拟机当时没有发生任何的网络连接。因此我们尝试从机器<code>u2</code>（另一台机器）ssh 登录进<code>u1</code>，再看一次：</p>
<p><img src="assets/CgqCHl92kAaAMuMDAAFWQdSNGfk978.png" alt="Drawing 7.png" /></p>
<p>如上图所示，可以看到有一个 TCP 连接了。</p>
<p><strong>查看端口占用</strong></p>
<p>还有一种非常常见的情形，我们想知道某个端口是哪个应用在占用。如下图所示：</p>
<p><img src="assets/Ciqc1F92kBKAHr2RAAEnmEOZ8RM010.png" alt="Drawing 8.png" /></p>
<p>这里我们看到 22 端口被 sshd，也就是远程登录模块被占用了。<code>-n</code>是将一些特殊的端口号用数字显示，<code>-t</code>是指看 TCP 协议，<code>-l</code>是只显示连接中的连接，<code>-p</code>是显示程序名称。</p>
<h3>网络测试</h3>
<p>当我们需要测试网络延迟、测试服务是否可用时，可能会用到<code>ping</code>和<code>telnet</code>指令。</p>
<h4>ping</h4>
<p>想知道本机到某个网站的网络延迟，就可以使用<code>ping</code>指令。如下图所示：</p>
<p><img src="assets/CgqCHl92kB-ARKR5AAP30Xk0nBg068.png" alt="Drawing 9.png" /></p>
<p><code>ping</code>一个网站需要使用 ICMP 协议。因此你可以在上图中看到 icmp 序号。 这里的时间<code>time</code>是往返一次的时间。<code>ttl</code>叫作 time to live，是封包的生存时间。就是说，一个封包从发出就开始倒计时，如果途中超过 128ms，这个包就会被丢弃。如果包被丢弃，就会被算进丢包率。</p>
<p>另外<code>ping</code>还可以帮助我们看到一个网址的 IP 地址。 通过网址获得 IP 地址的过程叫作 DNS Lookup（DNS 查询）。<code>ping</code>利用了 DNS 查询，但是没有显示全部的 DNS 查询结果。</p>
<h4>telnet</h4>
<p>有时候我们想知道本机到某个 IP + 端口的网络是否通畅，也就是想知道对方服务器是否在这个端口上提供了服务。这个时候可以用<code>telnet</code>指令。 如下图所示：</p>
<p><img src="assets/CgqCHl92kCmAcPQzAADcRdxOtdw609.png" alt="Drawing 10.png" /></p>
<p>telnet 执行后会进入一个交互式的界面，比如这个时候，我们输入下图中的文字就可以发送 HTTP 请求了。如果你对 HTTP 协议还不太了解，建议自学一下 HTTP 协议。如果希望和林老师一起学习，可以等待下我之后的《<strong>计算机网络</strong>》专栏。</p>
<p><img src="assets/Ciqc1F92kDKAcYUbAASLFyOyBg4948.png" alt="Drawing 11.png" /></p>
<p>如上图所示，第 5 行的<code>GET</code> 和第 6 行的<code>HOST</code>是我输入的。 拉勾网返回了一个 301 永久跳转。这是因为拉勾网尝试把<code>http</code>协议链接重定向到<code>https</code>。</p>
<h3>DNS 查询</h3>
<p>我们排查网络故障时想要进行一次 DNS Lookup，想知道一个网址 DNS 的解析过程。这个时候有多个指令可以用。</p>
<h4>host</h4>
<p>host 就是一个 DNS 查询工具。比如我们查询拉勾网的 DNS，如下图所示：</p>
<p><img src="assets/Ciqc1F92kD6AOJPQAAGW1va0D9c041.png" alt="Drawing 12.png" /></p>
<p>我们看到拉勾网 <a href="http://www.lagou.comw/">www.lagou.com</a> 是一个别名，它的原名是 lgmain 开头的一个域名，这说明拉勾网有可能在用 CDN 分发主页（关于 CDN，我们《计算机网络》专栏见）。</p>
<p>上图中，可以找到 3 个域名对应的 IP 地址。</p>
<p>如果想追查某种类型的记录，可以使用<code>host -t</code>。比如下图我们追查拉勾的 AAAA 记录，因为拉勾网还没有部署 IPv6，所以没有找到。</p>
<p><img src="assets/CgqCHl92kFWAHIqAAACvpo6qaOs100.png" alt="Drawing 13.png" /></p>
<h4>dig</h4>
<p><code>dig</code>指令也是一个做 DNS 查询的。不过<code>dig</code>指令显示的内容更详细。下图是<code>dig</code>拉勾网的结果。</p>
<p><img src="assets/CgqCHl92kGaADOhxAAR-BfryZ5g689.png" alt="Drawing 14.png" /></p>
<p>从结果可以看到<a href="http://www.lagou.c/">www.lagou.com</a> 有一个别名，用 CNAME 记录定义 lgmain 开头的一个域名，然后有 3 条 A 记录，通常这种情况是为了均衡负载或者分发内容。</p>
<h3>HTTP 相关</h3>
<p>最后我们来说说<code>http</code>协议相关的指令。</p>
<h4>curl</h4>
<p>如果要在命令行请求一个网页，或者请求一个接口，可以用<code>curl</code>指令。<code>curl</code>支持很多种协议，比如 LDAP、SMTP、FTP、HTTP 等。</p>
<p>我们可以直接使用 curl 请求一个网址，获取资源，比如我用 curl 直接获取了拉勾网的主页，如下图所示：</p>
<p><img src="assets/Ciqc1F92kG-AJPyrAANJZYQ4u5w784.png" alt="Drawing 15.png" /></p>
<p>如果只想看 HTTP 返回头，可以使用<code>curl -I</code>。</p>
<p>另外<code>curl</code>还可以执行 POST 请求，比如下面这个语句：</p>
<pre><code>curl -d '{&quot;x&quot; : 1}' -H &quot;Content-Type: application/json&quot; -X POST http://localhost:3000/api
</code></pre>
<p>curl在向<code>localhost:3000</code>发送 POST 请求。<code>-d</code>后面跟着要发送的数据， -<code>X</code>后面是用到的 HTTP 方法，<code>-H</code>是指定自定义的请求头。</p>
<h3>总结</h3>
<p>这节课我们学习了不少网络相关的 Linux 指令，这些指令是将来开发和调试的强大工具。这里再给你复习一下这些指令：</p>
<ul>
<li>远程登录的 ssh 指令；</li>
<li>远程拷贝文件的 scp 指令；</li>
<li>查看网络接口的 ifconfig 指令；</li>
<li>查看网络状态的 netstat 指令；</li>
<li>测试网络延迟的 ping 指令；</li>
<li>可以交互式调试和服务端的 telnet 指令；</li>
<li>两个 DNS 查询指令 host 和 dig；</li>
<li>可以发送各种请求包括 HTTPS 的 curl 指令。</li>
</ul>
<p><strong>那么通过这节课的学习，你现在可以来回答本节关联的面试题目：如何查看一个域名有哪些 NS 记录了吗？</strong></p>
<p>老规矩，请你先在脑海里构思下给面试官的表述，并把你的思考写在留言区，然后再来看我接下来的分析。</p>
<p><strong>【解析】</strong> host 指令提供了一个<code>-t</code>参数指定需要查找的记录类型。我们可以使用<code>host -t ns {网址}</code>。另外 dig 也提供了同样的能力。如果你感兴趣，还可以使用<code>man</code>对系统进行操作。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="08&#32;&#32;用户和权限管理指令：&#32;请简述&#32;Linux&#32;权限划分的原则？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="10&#32;&#32;软件的安装：&#32;编译安装和包管理器安装有什么优势和劣势？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435d096e27645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
