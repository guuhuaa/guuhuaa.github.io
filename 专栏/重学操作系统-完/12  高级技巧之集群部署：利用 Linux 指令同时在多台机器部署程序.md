<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>12  高级技巧之集群部署：利用 Linux 指令同时在多台机器部署程序.md</title>
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

                    <a class="current-tab" href="12&#32;&#32;高级技巧之集群部署：利用&#32;Linux&#32;指令同时在多台机器部署程序.md">12  高级技巧之集群部署：利用 Linux 指令同时在多台机器部署程序.md</a>
                    

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
                        <div><h1>12  高级技巧之集群部署：利用 Linux 指令同时在多台机器部署程序</h1>
<p>Linux 指令是由很多顶级程序员共同设计的，使用 Linux 指令解决问题的过程，就好像在体验一款优秀的产品。每次通过查资料使用 Linux 指令解决问题后，都会让我感到收获满满。在这个过程中，我不仅学会了一条指令，还从中体会到了软件设计的魅力：彼此独立，又互成一体。这就像每个 Linux 指令一样，专注、高效。回想起来，在我第一次看到管道、第一次使用 awk、第一次使用 sort，都曾有过这种感受。</p>
<p>通过前面的学习，相信你已经掌握了一些基础指令的使用方法，今天我们继续挑战一个更复杂的问题——<strong>用 Linux 指令管理一个集群</strong>。这属于 Linux 指令的高级技巧，所谓高级技巧并不是我们要学习更多的指令，而是要把之前所学的指令进行排列组合。当你从最初只能写几条指令、执行然后看结果，成长到具备书写一个拥有几十行、甚至上百行的 bash 脚本的能力时，就意味着你具备了解决复杂问题的能力。而最终的目标，是提升你对指令的熟练程度，锻炼工程能力。</p>
<p>本课时，我将带你朝着这个目标努力，通过把简单的指令组合起来，分层组织成最终的多个脚本文件，解决一个复杂的工程问题：在成百上千的集群中安装一个 Java 环境。接下来，请你带着这个目标，开启今天的学习。</p>
<h3>第一步：搭建学习用的集群</h3>
<p>第一步我们先搭建一个学习用的集群。这里简化一下模型。我在自己的电脑上装一个<code>ubuntu</code>桌面版的虚拟机，然后再装两个<code>ubuntu</code>服务器版的虚拟机。</p>
<p>相对于桌面版，服务器版对资源的消耗会少很多。我将教学材料中桌面版的<code>ubuntu</code>命名为<code>u1</code>，两个用来被管理的服务器版<code>ubuntu</code>叫作<code>v1</code>和<code>v2</code>。</p>
<p>用桌面版的原因是：我喜欢<code>ubuntu</code>漂亮的开源字体，这样会让我在给你准备素材的时候拥有一个好心情。如果你对此感兴趣，可以搜索<code>ubuntu mono</code>，尝试把这个字体安装到自己的文本编辑器中。不过我还是觉得在<code>ubuntu</code>中敲代码更有感觉。</p>
<p>注意，我在这里只用了 3 台服务器，但是接下来我们要写的脚本是可以在很多台服务器之间复用的。</p>
<h3>第二步：循环遍历 IP 列表</h3>
<p>你可以想象一个局域网中有很多服务器需要管理，它们彼此之间网络互通，我们通过一台主服务器对它们进行操作，即通过<code>u1</code>操作<code>v1</code>和<code>v2</code>。</p>
<p>在主服务器上我们维护一个<code>ip</code>地址的列表，保存成一个文件，如下图所示：</p>
<p><img src="assets/CgqCHl-GsciASqucAACaCl1bXF4240.png" alt="Drawing 0.png" /></p>
<p>目前<code>iplist</code>中只有两项，但是如果我们有足够的机器，可以在里面放成百上千项。接下来，请你思考<code>shell</code>如何遍历这些<code>ip</code>？</p>
<p>你可以先尝试实现一个最简单的程序，从文件<code>iplist</code>中读出这些<code>ip</code>并尝试用<code>for</code>循环遍历这些<code>ip</code>，具体程序如下：</p>
<pre><code>#!/usr/bin/bash

readarray -t ips &lt; iplist

for ip in ${ips[@]}

do

    echo $ip

done
</code></pre>
<p>首行的<code>#!</code>叫作 Shebang。Linux 的程序加载器会分析 Shebang 的内容，决定执行脚本的程序。这里我们希望用<code>bash</code>来执行这段程序，因为我们用到的 readarray 指令是<code>bash 4.0</code>后才增加的能力。</p>
<p><code>readarray</code>指令将 iplist 文件中的每一行读取到变量<code>ips</code>中。<code>ips</code>是一个数组，可以用<code>echo ${ips[@]}</code>打印其中全部的内容：<code>@</code>代表取数组中的全部内容；<code>$</code>符号是一个求值符号。不带<code>$</code>的话，<code>ips[@]</code>会被认为是一个字符串，而不是表达式。</p>
<p><code>for</code>循环遍历数组中的每个<code>ip</code>地址，<code>echo</code>把地址打印到屏幕上。</p>
<p>如果用<code>shell</code>执行上面的程序会报错，因为<code>readarray</code>是<code>bash 4.0</code>后支持的能力，因此我们用<code>chomd</code>为<code>foreach.sh</code>增加执行权限，然后直接利用<code>shebang</code>的能力用<code>bash</code>执行，如下图所示：</p>
<p><img src="assets/Ciqc1F-GsdSAZPtIAAF5yL5VkdQ049.png" alt="Drawing 1.png" /></p>
<h3>第三步：创建集群管理账户</h3>
<p>为了方便集群管理，通常使用统一的用户名管理集群。这个账号在所有的集群中都需要保持命名一致。比如这个集群账号的名字就叫作<code>lagou</code>。</p>
<p>接下来我们探索一下如何创建这个账户<code>lagou</code>，如下图所示：</p>
<p><img src="assets/CgqCHl-GsdqAc2khAALNpLTWENc494.png" alt="Drawing 2.png" /></p>
<p>上面我们创建了<code>lagou</code>账号，然后把<code>lagou</code>加入<code>sudo</code>分组。这样<code>lagou</code>就有了<code>sudo</code>成为<code>root</code>的能力，如下图所示：</p>
<p><img src="assets/Ciqc1F-GseCAYss5AAB9-SYXFJU693.png" alt="Drawing 3.png" /></p>
<p>接下来，我们设置<code>lagou</code>用户的初始化<code>shell</code>是<code>bash</code>，如下图所示：</p>
<p><img src="assets/CgqCHl-GsiyAGKitAACU_gkGZRI467.png" alt="Drawing 4.png" /></p>
<p>这个时候如果使用命令<code>su lagou</code>，可以切换到<code>lagou</code>账号，但是你会发现命令行没有了颜色。因此我们可以将原来用户下面的<code>.bashrc</code>文件拷贝到<code>/home/lagou</code>目录下，如下图所示：</p>
<p><img src="assets/Ciqc1F-GsjeAL_RwAAEyx32py80146.png" alt="Drawing 5.png" /></p>
<p>这样，我们就把一些自己平时用的设置拷贝了过去，包括终端颜色的设置。<code>.bashrc</code>是启动<code>bash</code>的时候会默认执行的一个脚本文件。</p>
<p>接下来，我们编辑一下<code>/etc/sudoers</code>文件，增加一行<code>lagou ALL=(ALL)  NOPASSWD:ALL</code>表示<code>lagou</code>账号 sudo 时可以免去密码输入环节，如下图所示：</p>
<p><img src="assets/CgqCHl-Gsj6AQBXeAAEW0V065r0519.png" alt="Drawing 6.png" /></p>
<p>我们可以把上面的完整过程整理成指令文件，<code>create_lagou.sh</code>：</p>
<pre><code>sudo useradd -m -d /home/lagou lagou

sudo passwd lagou

sudo usermod -G sudo lagou

sudo usermod --shell /bin/bash lagou

sudo cp ~/.bashrc /home/lagou/

sudo chown lagou.lagou /home/lagou/.bashrc

sduo sh -c 'echo &quot;lagou ALL=(ALL)  NOPASSWD:ALL&quot;&gt;&gt;/etc/sudoers'
</code></pre>
<p>你可以删除用户<code>lagou</code>，并清理<code>/etc/sudoers</code>文件最后一行。用指令<code>userdel lagou</code>删除账户，然后执行<code>create_lagou.sh</code>重新创建回<code>lagou</code>账户。如果发现结果一致，就代表<code>create_lagou.sh</code>功能没有问题。</p>
<p>最后我们想在<code>v1``v2</code>上都执行<code>create_logou.sh</code>这个脚本。但是你不要忘记，我们的目标是让程序在成百上千台机器上传播，因此还需要一个脚本将<code>create_lagou.sh</code>拷贝到需要执行的机器上去。</p>
<p>这里，可以对<code>foreach.sh</code>稍做修改，然后分发<code>create_lagou.sh</code>文件。</p>
<p><em>foreach.sh</em></p>
<pre><code>#!/usr/bin/bash

readarray -t ips &lt; iplist

for ip in ${ips[@]}

do

    scp ~/remote/create_lagou.sh <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b1c3d0dcc3deddddf1">[email&#160;protected]</a>$ip:~/create_lagou.sh

done
</code></pre>
<p>这里，我们在循环中用<code>scp</code>进行文件拷贝，然后分别去每台机器上执行<code>create_lagou.sh</code>。</p>
<p>如果你的机器非常多，上述过程会变得非常烦琐。你可以先带着这个问题学习下面的<code>Step 4</code>，然后再返回来重新思考这个问题，当然你也可以远程执行脚本。另外，还有一个叫作<code>sshpass</code>的工具，可以帮你把密码传递给要远程执行的指令，如果你对这块内容感兴趣，可以自己研究下这个工具。</p>
<h3>第四步： 打通集群权限</h3>
<p>接下来我们需要打通从主服务器到<code>v1</code>和<code>v2</code>的权限。当然也可以每次都用<code>ssh</code>输入用户名密码的方式登录，但这并不是长久之计。 如果我们有成百上千台服务器，输入用户名密码就成为一件繁重的工作。</p>
<p>这时候，你可以考虑利用主服务器的公钥在各个服务器间登录，避免输入密码。接下来我们聊聊具体的操作步骤：</p>
<p>首先，需要在<code>u1</code>上用<code>ssh-keygen</code>生成一个公私钥对，然后把公钥写入需要管理的每一台机器的<code>authorized_keys</code>文件中。如下图所示：我们使用<code>ssh-keygen</code>在主服务器<code>u1</code>中生成公私钥对。</p>
<p><img src="assets/CgqCHl-GslSAAUT5AATF-5rjGWU079.png" alt="Drawing 7.png" /></p>
<p>然后使用<code>mkdir -p</code>创建<code>~/.ssh</code>目录，<code>-p</code>的优势是当目录不存在时，才需要创建，且不会报错。<code>~</code>代表当前家目录。 如果文件和目录名前面带有一个<code>.</code>，就代表该文件或目录是一个需要隐藏的文件。平时用<code>ls</code>的时候，并不会查看到该文件，通常这种文件拥有特别的含义，比如<code>~/.ssh</code>目录下是对<code>ssh</code>的配置。</p>
<p>我们用<code>cd</code>切换到<code>.ssh</code>目录，然后执行<code>ssh-keygen</code>。这样会在<code>~/.ssh</code>目录中生成两个文件，<code>id_rsa.pub</code>公钥文件和<code>is_rsa</code>私钥文件。 如下图所示：</p>
<p><img src="assets/CgqCHl-GsluAWyS-AAayQyKs6NY181.png" alt="Drawing 8.png" /></p>
<p>可以看到<code>id_rsa.pub</code>文件中是加密的字符串，我们可以把这些字符串拷贝到其他机器对应用户的<code>~/.ssh/authorized_keys</code>文件中，当<code>ssh</code>登录其他机器的时候，就不用重新输入密码了。 这个传播公钥的能力，可以用一个<code>shell</code>脚本执行，这里我用<code>transfer_key.sh</code>实现。</p>
<p>我们修改一下<code>foreach.sh</code>，并写一个<code>transfer_key.sh</code>配合<code>foreach.sh</code>的工作。<code>transfer_key.sh</code>内容如下：</p>
<p><em>foreach.sh</em></p>
<pre><code>#!/usr/bin/bash

readarray -t ips &lt; iplist

for ip in ${ips[@]}

do

    sh ./transfer_key.sh $ip

done
</code></pre>
<p><em>tranfer_key.sh</em></p>
<pre><code>ip=$1

pubkey=$(cat ~/.ssh/id_rsa.pub)

echo &quot;execute on .. $ip&quot;

ssh <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1975787e766c59">[email&#160;protected]</a>$ip &quot; 

mkdir -p ~/.ssh

echo $pubkey  &gt;&gt; ~/.ssh/authorized_keys

chmod 700 ~/.ssh

chmod 600 ~/.ssh/authorized_keys

&quot;
</code></pre>
<p>在<code>foreach.sh</code>中我们执行 transfer_key.sh，并且将 IP 地址通过参数传递过去。在 transfer_key.sh 中，用<code>$1</code>读出 IP 地址参数， 再将公钥写入变量<code>pubkey</code>，然后登录到对应的服务器，执行多行指令。用<code>mkdir</code>指令检查<code>.ssh</code>目录，如不存在就创建这个目录。最后我们将公钥追加写入目标机器的<code>~/.ssh/authorized_keys</code>中。</p>
<p><code>chmod 700</code>和<code>chmod 600</code>是因为某些特定的<code>linux</code>版本需要<code>.ssh</code>的目录为可读写执行，<code>authorized_keys</code>文件的权限为只可读写。而为了保证安全性，组用户、所有用户都不可以访问这个文件。</p>
<p>此前，我们执行<code>foreach.sh</code>需要输入两次密码。完成上述操作后，我们再登录这两台服务器就不需要输入密码了。</p>
<p><img src="assets/CgqCHl-GsnuAC-lYAAb76OR4cFs817.png" alt="Drawing 9.png" /></p>
<p>接下来，我们尝试一下免密登录，如下图所示：</p>
<p><img src="assets/Ciqc1F-GsoGANiKlAAIjYZ8fscs878.png" alt="Drawing 10.png" /></p>
<p>可以发现，我们登录任何一台机器，都不再需要输入用户名和密码了。</p>
<h3>第五步：单机安装 Java 环境</h3>
<p>在远程部署 Java 环境之前，我们先单机完成以下 Java 环境的安装，用来收集需要执行的脚本。</p>
<p>在<code>ubuntu</code>上安装<code>java</code>环境可以直接用<code>apt</code>。</p>
<p>我们通过下面几个步骤脚本配置 Java 环境：</p>
<pre><code>sudo apt install openjdk-11-jdk
</code></pre>
<p>经过一番等待我们已经安装好了<code>java</code>，然后执行下面的脚本确认<code>java</code>安装。</p>
<pre><code>which java

java --version
</code></pre>
<p><img src="assets/Ciqc1F-GspCAJ0r9AAJx-kzES1k505.png" alt="Drawing 11.png" /></p>
<p>根据最小权限原则，执行 Java 程序我们考虑再创建一个用户<code>ujava</code>。</p>
<pre><code>sudo useradd -m -d /opt/ujava ujava

sudo usermod --shell /bin/bash lagou
</code></pre>
<p>这个用户可以不设置密码，因为我们不会真的登录到这个用户下去做任何事情。接下来我们为用户配置 Java 环境变量，如下图所示：</p>
<p><img src="assets/Ciqc1F-GsqWAa2e2AAJosZCNXpU388.png" alt="Drawing 12.png" /></p>
<p>通过两次 ls 追查，可以发现<code>java</code>可执行文件软连接到<code>/etc/alternatives/java</code>然后再次软连接到<code>/usr/lib/jvm/java-11-openjdk-amd64</code>下。</p>
<p>这样我们就可以通过下面的语句设置 JAVA_HOME 环境变量了。</p>
<pre><code>export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/
</code></pre>
<p>Linux 的环境变量就好比全局可见的数据，这里我们使用 export 设置<code>JAVA_HOME</code>环境变量的指向。如果你想看所有的环境变量的指向，可以使用<code>env</code>指令。</p>
<p><img src="assets/CgqCHl-GsrGAMIfNAAW55Kdz1xc547.png" alt="Drawing 13.png" /></p>
<p>其中有一个环境变量比较重要，就是<code>PATH</code>。</p>
<p><img src="assets/Ciqc1F-GsriACI2JAAEtgeamQNI945.png" alt="Drawing 14.png" /></p>
<p>如上图，我们可以使用<code>shell</code>查看<code>PATH</code>的值，<code>PATH</code>中用<code>:</code>分割，每一个目录都是<code>linux</code>查找执行文件的目录。当用户在命令行输入一个命令，Linux 就会在<code>PATH</code>中寻找对应的执行文件。</p>
<p>当然我们不希望<code>JAVA_HOME</code>配置后重启一次电脑就消失，因此可以把这个环境变量加入<code>ujava</code>用户的<code>profile</code>中。这样只要发生用户登录，就有这个环境变量。</p>
<pre><code>sudo sh -c 'echo &quot;export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/&quot; &gt;&gt; /opt/ujava/.bash_profile'
</code></pre>
<p>将<code>JAVA_HOME</code>加入<code>bash_profile</code>，这样后续远程执行<code>java</code>指令时就可以使用<code>JAVA_HOME</code>环境变量了。</p>
<p>最后，我们将上面所有的指令整理起来，形成一个<code>install_java.sh</code>。</p>
<pre><code>sudo apt -y install openjdk-11-jdk

sudo useradd -m -d /opt/ujava ujava

sudo usermod --shell /bin/bash ujava

sudo sh -c 'echo &quot;export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/&quot; &gt;&gt; /opt/ujava/.bash_profile'
</code></pre>
<p><code>apt</code>后面增了一个<code>-y</code>是为了让执行过程不弹出确认提示。</p>
<h3>第六步：远程安装 Java 环境</h3>
<p>终于到了远程安装 Java 环境这一步，我们又需要用到<code>foreach.sh</code>。为了避免每次修改，你可以考虑允许<code>foreach.sh</code>带一个文件参数，指定需要远程执行的脚本。</p>
<p><em><strong>foreach.sh</strong></em></p>
<pre><code>#!/usr/bin/bash

readarray -t ips &lt; iplist

script=$1

for ip in ${ips[@]}

do

    ssh $ip 'bash -s' &lt; $script

done
</code></pre>
<p>改写后的<code>foreach</code>会读取第一个执行参数作为远程执行的脚本文件。 而<code>bash -s</code>会提示使用标准输入流作为命令的输入；<code>&lt; $script</code>负责将脚本文件内容重定向到远程<code>bash</code>的标准输入流。</p>
<p>然后我们执行<code>foreach.sh install_java.sh</code>，机器等待 1 分钟左右，在执行结束后，可以用下面这个脚本检测两个机器中的安装情况。</p>
<p><em><strong>check.sh</strong></em></p>
<pre><code>sudo -u ujava -i /bin/bash -c 'echo $JAVA_HOME'

sudo -u ujava -i java --version
</code></pre>
<p><code>check.sh</code>中我们切换到<code>ujava</code>用户去检查<code>JAVA_HOME</code>环境变量和 Java 版本。执行的结果如下图所示：</p>
<p><img src="assets/CgqCHl-GstWAFW9yAAQXx_nh6dw719.png" alt="Drawing 15.png" /></p>
<h3>总结</h3>
<p>这节课我们所讲的场景是自动化运维的一些皮毛。通过这样的场景练习，我们复习了很多之前学过的 Linux 指令。在尝试用脚本文件构建一个又一个小工具的过程中，可以发现复用很重要。</p>
<p>在工作中，优秀的工程师，总是善于积累和复用，而<code>shell</code>脚本就是积累和复用的利器。如果你第一次安装<code>java</code>环境，可以把今天的安装脚本保存在自己的笔记本中，下次再安装就能自动化完成了。除了积累和总结，另一个非常重要的就是你要尝试自己去查资料，包括使用<code>man</code>工具熟悉各种指令的使用方法，用搜索引擎查阅资料等。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="11&#32;&#32;高级技巧之日志分析：利用&#32;Linux&#32;指令分析&#32;Web&#32;日志.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;(1)加餐&#32;&#32;练习题详解（二）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435d1dac3a645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
