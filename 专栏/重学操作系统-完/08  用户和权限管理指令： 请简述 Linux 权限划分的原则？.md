<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>08  用户和权限管理指令： 请简述 Linux 权限划分的原则？.md</title>
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

                    <a class="current-tab" href="08&#32;&#32;用户和权限管理指令：&#32;请简述&#32;Linux&#32;权限划分的原则？.md">08  用户和权限管理指令： 请简述 Linux 权限划分的原则？.md</a>
                    

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
                        <div><h1>08  用户和权限管理指令： 请简述 Linux 权限划分的原则？</h1>
<p><strong>我看到过这样一道面试题：请简述 Linux 权限划分的原则</strong>？</p>
<p>这种类型的面试题也是我比较喜欢的一种题目，因为它考察的不仅是一个具体的指令，还考察了候选人技术层面的认知。</p>
<p>如果你对 Linux 权限有较深的认知和理解，那么完全可以通过查资料去完成具体指令的执行。更重要的是，认知清晰的程序员可以把 Linux 权限管理的知识迁移到其他的系统设计中。而且我认为，能够对某个技术形成认知的人， 同样也会热爱思考，善于总结，这样的程序员是所有团队梦寐以求的。</p>
<p>因此，这次我们就把这道面试题作为引子，开启今天的学习。</p>
<h3>权限抽象</h3>
<p>一个完整的权限管理体系，要有合理的抽象。这里就包括对用户、进程、文件、内存、系统调用等抽象。下面我将带你一一了解。</p>
<p><strong>首先，我们先来说说用户和组</strong>。Linux 是一个多用户平台，允许多个用户同时登录系统工作。Linux 将用户抽象成了账户，账户可以登录系统，比如通过输入登录名 + 密码的方式登录；也可以通过证书的方式登录。</p>
<p>但为了方便分配每个用户的权限，Linux 还支持组 <strong>（Group）账户</strong>。组账户是多个账户的集合，组可以为成员们分配某一类权限。每个用户可以在多个组，这样就可以利用组给用户快速分配权限。</p>
<p>组的概念有点像微信群。一个用户可以在多个群中。比如某个组中分配了 10 个目录的权限，那么新建用户的时候可以将这个用户增加到这个组中，这样新增的用户就不必再去一个个目录分配权限。</p>
<p>而每一个微信群都有一个群主，<strong>Root 账户也叫作超级管理员</strong>，就相当于微信群主，它对系统有着完全的掌控。一个超级管理员可以使用系统提供的全部能力。</p>
<p>此外，Linux 还对<strong>文件</strong>进行了权限抽象（<strong>注意目录也是一种文件</strong>）。Linux 中一个文件可以设置下面 3 种权限：</p>
<ol>
<li>读权限（r）：控制读取文件。</li>
<li>写权限（w）：控制写入文件。</li>
<li>执行权限（x）：控制将文件执行，比如脚本、应用程序等。</li>
</ol>
<p><img src="assets/Ciqc1F91G6qACantAAC4GIUeips460.png" alt="1.png" /></p>
<p>然后每个文件又可以从 3 个维度去配置上述的 3 种权限：</p>
<ol>
<li>用户维度。每个文件可以所属 1 个用户，用户维度配置的 rwx 在用户维度生效；</li>
<li>组维度。每个文件可以所属 1 个分组，组维度配置的 rwx 在组维度生效；</li>
<li>全部用户维度。设置对所有用户的权限。</li>
</ol>
<p><img src="assets/CgqCHl91G9aADTBZAADD7IOpjac809.png" alt="2.png" /></p>
<p>因此 Linux 中文件的权限可以用 9 个字符，3 组<code>rwx</code>描述：第一组是用户权限，第二组是组权限，第三组是所有用户的权限。然后用<code>-</code>代表没有权限。比如<code>rwxrwxrwx</code>代表所有维度可以读写执行。<code>rw--wxr-x</code>代表用户维度不可以执行，组维度不可以读取，所有用户维度不可以写入。</p>
<p>通常情况下，如果用<code>ls -l</code>查看一个文件的权限，会有 10 个字符，这是因为第一个字符代表的是文件类型。我们在 06 课时讲解“几种常见的文件类型”时提到过，有管道文件、目录文件、链接文件等等。<code>-</code>代表普通文件、<code>d</code>代表目录、<code>p</code>代表管道。</p>
<p><strong>学习了这套机制之后，请你跟着我的节奏一起思考以下 4 个问题</strong>。</p>
<ol>
<li>文件被创建后，初始的权限如何设置？</li>
<li>需要全部用户都可以执行的指令，比如<code>ls</code>，它们的权限如何分配？</li>
<li>给一个文本文件分配了可执行权限会怎么样？</li>
<li>可不可以多个用户都登录<code>root</code>，然后只用<code>root</code>账户？</li>
</ol>
<p>你可以把以上 4 个问题作为本课时的小测验，把你的思考或者答案写在留言区，然后再来看我接下来的分析。</p>
<p><strong>问题一：初始权限问题</strong></p>
<p>一个文件创建后，文件的所属用户会被设置成创建文件的用户。谁创建谁拥有，这个逻辑很顺理成章。但是文件的组又是如何分配的呢？</p>
<p>这里 Linux 想到了一个很好的办法，就是为每个用户创建一个同名分组。</p>
<p>比如说<code>zhang</code>这个账户创建时，会创建一个叫作<code>zhang</code>的分组。<code>zhang</code>登录之后，工作分组就会默认使用它的同名分组<code>zhang</code>。如果<code>zhang</code>想要切换工作分组，可以使用<code>newgrp</code>指令切换到另一个工作分组。因此，被创建文件所属的分组是当时用户所在的工作分组，如果没有特别设置，那么就属于用户所在的同名分组。</p>
<p>再说下文件的权限如何？文件被创建后的权限通常是：</p>
<pre><code>rw-rw-r--
</code></pre>
<p>也就是用户、组维度不可以执行，所有用户可读。</p>
<p><strong>问题二：公共执行文件的权限</strong></p>
<p>前面提到过可以用<code>which</code>指令查看<code>ls</code>指令所在的目录，我们发现在<code>/usr/bin</code>中。然后用<code>ls -l</code>查看<code>ls</code>的权限，可以看到下图所示：</p>
<p><img src="assets/Ciqc1F90SRuAAQCEAADdVOthCFw679.png" alt="Drawing 2.png" /></p>
<p>第一个<code>-</code>代表这是一个普通文件，后面的 rwx 代表用户维度可读写和执行；第二个<code>r-x</code>代表组维度不可以写；第三个<code>r-x</code>代表所有用户可以读和执行。后面的两个<code>root</code>，第一个是所属用户，第二个是所属分组。</p>
<p>到这里你可能会有一个疑问：如果一个文件设置为不可读，但是可以执行，那么结果会怎样？</p>
<p>答案当然是不可以执行，无法读取文件内容自然不可以执行。</p>
<p><strong>问题三：执行文件</strong></p>
<p>在 Linux 中，如~~果~~一个文件可以被执行，则可以直接通过输入文件路径（相对路径或绝对路径）的方式执行。如果想执行一个不可以执行的文件，Linux 则会报错。</p>
<p>当用户输入一个文件名，如果没有指定完整路径，Linux 就会在一部分目录中查找这个文件。你可以通过<code>echo $PATH</code>看到 Linux 会在哪些目录中查找可执行文件，<code>PATH</code>是 Linux 的环境变量，关于环境变量，我将在 “12 | 高级技巧之集群部署中”和你详细讨论。</p>
<p><img src="assets/CgqCHl90SSSACa4WAAFIEUypWH4904.png" alt="Drawing 3.png" /></p>
<p><strong>问题四：可不可以都 root</strong></p>
<p>最后一个问题是，可不可以都<code>root</code>？</p>
<p>答案当然是不行！这里先给你留个悬念，具体原因我们会在本课时最后来讨论。</p>
<p><strong>到这里，用户和组相关权限就介绍完了。接下来说说内核和系统调用权限。</strong> 内核是操作系统连接硬件、提供最核心能力的程序。今天我们先简单了解一下，关于内核的详细知识，会在“14 |用户态和内核态：用户态线程和内核态线程有什么区别？”中介绍。</p>
<p>内核提供操作硬件、磁盘、内存分页、进程等最核心的能力，并拥有直接操作全部内存的权限，因此内核不能把自己的全部能力都提供给用户，而且也不能允许用户通过<code>shell</code>指令进行系统调用。Linux 下内核把部分进程需要的系统调用以 C 语言 API 的形式提供出来。部分系统调用会有权限检查，比如说设置系统时间的系统调用。</p>
<p>以上我们看到了 Linux 对系统权限的抽象。接下来我们再说说权限架构的思想。</p>
<h3>权限架构思想</h3>
<p>优秀的权限架构主要目标是让系统安全、稳定且用户、程序之间相互制约、相互隔离。这要求权限系统中的权限划分足够清晰，分配权限的成本足够低。</p>
<p>因此，优秀的架构，应该遵循最小权限原则（Least Privilege)。权限设计需要保证系统的安全和稳定。比如：每一个成员拥有的权限应该足够的小，每一段特权程序执行的过程应该足够的短。对于安全级别较高的时候，还需要成员权限互相牵制。比如金融领域通常登录线上数据库需要两次登录，也就是需要两个密码，分别掌握在两个角色手中。这样即便一个成员出了问题，也可以保证整个系统安全。</p>
<p>同样的，每个程序也应该减少权限，比如说只拥有少量的目录读写权限，只可以进行少量的系统调用。</p>
<h4>权限划分</h4>
<p>此外，权限架构思想还应遵循一个原则，权限划分边界应该足够清晰，尽量做到相互隔离。Linux 提供了用户和分组。当然 Linux 没有强迫你如何划分权限，这是为了应对更多的场景。通常我们服务器上重要的应用，会由不同的账户执行。比如说 Nginx、Web 服务器、数据库不会执行在一个账户下。现在随着容器化技术的发展，我们甚至希望每个应用独享一个虚拟的空间，就好像运行在一个单独的操作系统中一样，让它们互相不用干扰。</p>
<p><strong>到这里，你可能会问：为什么不用 root 账户执行程序？</strong> 下面我们就来说说 root 的危害。</p>
<p>举个例子，你有一个 Mysql 进程执行在 root（最大权限）账户上，如果有黑客攻破了你的 Mysql 服务，获得了在 Mysql 上执行 Sql 的权限，那么，你的整个系统就都暴露在黑客眼前了。这会导致非常严重的后果。</p>
<p>黑客可以利用 Mysql 的 Copy From Prgram 指令为所欲为，比如先备份你的关键文件，然后再删除他们，并要挟你通过指定账户打款。如果执行最小权限原则，那么黑客即便攻破我们的 Mysql 服务，他也只能获得最小的权限。当然，黑客拿到 Mysql 权限也是非常可怕的，但是相比拿到所有权限，这个损失就小多了。</p>
<h4>分级保护</h4>
<p>因为内核可以直接操作内存和 CPU，因此非常危险。驱动程序可以直接控制摄像头、显示屏等核心设备，也需要采取安全措施，比如防止恶意应用开启摄像头盗用隐私。通常操作系统都采取一种环状的保护模式。</p>
<p><img src="assets/CgqCHl91HB2AdNsAAAEpE6rtlHM754.png" alt="3.png" /></p>
<p>如上图所示，内核在最里面，也就是 Ring 0。 应用在最外面也就是Ring 3。驱动在中间，也就是 Ring 1 和 Ring 2。对于相邻的两个 Ring，内层 Ring 会拥有较高的权限，可以改变外层的 Ring；而外层的 Ring 想要使用内层 Ring 的资源时，会有专门的程序（或者硬件）进行保护。</p>
<p>比如说一个 Ring3 的应用需要使用内核，就需要发送一个系统调用给内核。这个系统调用会由内核进行验证，比如验证用户有没有足够的权限，以及这个行为是否安全等等。</p>
<p><strong>权限包围（Privilege Bracking）</strong></p>
<p>之前我们讨论过，当 Mysql 跑在 root 权限时，如果 Mysql 被攻破，整个机器就被攻破了。因此我们所有应用都不要跑在 root 上。如果所有应用都跑在普通账户下，那么就会有临时提升权限的场景。比如说安装程序可能需要临时拥有管理员权限，将应用装到<code>/usr/bin</code>目录下。</p>
<p>Linux 提供了权限包围的能力。比如一个应用，临时需要高级权限，可以利用交互界面（比如让用户输入 root 账户密码）验证身份，然后执行需要高级权限的操作，然后马上恢复到普通权限工作。这样做可以减少应用在高级权限的时间，并做到专权专用，防止被恶意程序利用。</p>
<h3>用户分组指令</h3>
<p>上面我们讨论了 Linux 权限的架构，接下来我们学习一些具体的指令。</p>
<h4>查看</h4>
<p>如果想查看当前用户的分组可以使用<code>groups</code>指令。</p>
<p><img src="assets/CgqCHl90SU6AUJrLAADmRyiiAig313.png" alt="Drawing 5.png" /></p>
<p>上面指令列出当前用户的所有分组。第一个是同名的主要分组，后面从<code>adm</code>开始是次级分组。</p>
<p>我先给你介绍两个分组，其他分组你可以去查资料：</p>
<ul>
<li>adm 分组用于系统监控，比如<code>/var/log</code>中的部分日志就是 adm 分组。</li>
<li>sudo 分组用户可以通过 sudo 指令提升权限。</li>
</ul>
<p>如果想查看当前用户，可以使用<code>id</code>指令，如下所示：</p>
<p><img src="assets/CgqCHl90SVSALssXAAGhSpF-cWY440.png" alt="Drawing 6.png" /></p>
<ul>
<li>uid 是用户 id；</li>
<li>gid 是组 id；</li>
<li>groups 后面是每个分组和分组的 id。</li>
</ul>
<p>如果想查看所有的用户，可以直接看<code>/etc/passwd</code>。</p>
<p><img src="assets/CgqCHl90SVqAIja7AAXBj3lebBQ651.png" alt="Drawing 7.png" /></p>
<p><code>/etc/passwd</code>这个文件存储了所有的用户信息，如下图所示：</p>
<p><img src="assets/CgqCHl91HIGAWXWVAACI9cgafaM295.png" alt="WechatIMG144.png" /></p>
<h4>创建用户</h4>
<p>创建用户用<code>useradd</code>指令。</p>
<pre><code>sudo useradd foo
</code></pre>
<p>sudo 原意是 superuser do，后来演变成用另一个用户的身份去执行某个指令。如果没有指定需要 sudo 的用户，就像上面那样，就是以超级管理员的身份。因为 useradd 需要管理员身份。这句话执行后，会进行权限提升，并弹出输入管理员密码的输入界面。</p>
<h4><strong>创建分组</strong></h4>
<p>创建分组用<code>groupadd</code>指令。下面指令创建一个叫作<code>hello</code>的分组。</p>
<pre><code>sudo groupadd hello
</code></pre>
<h4>为用户增加次级分组</h4>
<p>组分成主要分组（Primary Group）和次级分组（Secondary Group）。主要分组只有 1 个，次级分组可以有多个。如果想为用户添加一个次级分组，可以用<code>usermod</code>指令。下面指令将用户<code>foo</code>添加到<code>sudo</code>分组，从而<code>foo</code>拥有了<code>sudo</code>的权限。</p>
<pre><code>sudo usermod -a -G sudo foo
</code></pre>
<p><code>-a</code>代表append，<code>-G</code>代表一个次级分组的清单， 最后一个<code>foo</code>是账户名。</p>
<h4>修改用户主要分组</h4>
<p>修改主要分组还是使用<code>usermod</code>指令。只不过参数是小写的<code>-g</code>。</p>
<pre><code>sudo usermod -g somegroup foo
</code></pre>
<h3>文件权限管理指令</h3>
<p>接下来我们学习文件管理相关的指令。</p>
<h4>查看</h4>
<p>我们可以用<code>ls -l</code>查看文件的权限，相关内容在本课时前面已经介绍过了。</p>
<h4>修改文件权限</h4>
<p>可以用<code>chmod</code>修改文件权限，<code>chmod</code>（ change file mode bits），也就是我们之前学习的 rwx，只不过 rwx 在 Linux 中是用三个连在一起的二进制位来表示。</p>
<pre><code># 设置foo可以执行

chmod +x ./foo

# 不允许foo执行

chmod -x ./foo

# 也可以同时设置多个权限

chmod +rwx ./foo
</code></pre>
<p>因为<code>rwx</code>在 Linux 中用相邻的 3 个位来表示。比如说<code>111</code>代表<code>rwx</code>，<code>101</code>代表<code>r-x</code>。而<code>rwx</code>总共有三组，分别是用户权限、组权限和全部用户权限。也就是可以用<code>111111111</code>9 个 1 代表<code>rwxrwxrwx</code>。又因为<code>111</code>10 进制是 7，因此当需要一次性设置用户权限、组权限和所有用户权限的时候，我们经常用数字表示。</p>
<pre><code># 设置rwxrwxrwx (111111111 -&gt; 777)

chmod 777 ./foo

# 设置rw-rw-rw-(110110110 -&gt; 666)

chmod 666 ./foo
</code></pre>
<h4>修改文件所属用户</h4>
<p>有时候我们需要修改文件所属用户，这个时候会使用<code>chown</code>指令。 下面指令修改<code>foo</code>文件所属的用户为<code>bar</code>。</p>
<pre><code>chown bar ./foo
</code></pre>
<p>还有一些情况下，我们需要同时修改文件所属的用户和分组，比如我们想修改<code>foo</code>的分组位<code>g</code>，用户为<code>u</code>，可以使用：</p>
<pre><code>chown g.u ./foo
</code></pre>
<h3>总结</h3>
<p>这节课我们学习 Linux 的权限管理的抽象和架构思想。Linux 对用户、组、文件、系统调用等都进行了完善的抽象。之后，我们讨论了最小权限原则。最后我们对用户分组管理和文件权限管理两部分重要的指令进行了系统学习。</p>
<p>那么通过这节课的学习，你现在可以来回答本节关联的面试题目：<strong>请简述 Linux 权限划分的原则？</strong></p>
<p>老规矩，请你先在脑海里构思下给面试官的表述，并把你的思考写在留言区，然后再来看我接下来的分析。</p>
<p><strong>【解析】</strong> Linux 遵循最小权限原则。</p>
<ol>
<li>每个用户掌握的权限应该足够小，每个组掌握的权限也足够小。实际生产过程中，最好管理员权限可以拆分，互相牵制防止问题。</li>
<li>每个应用应当尽可能小的使用权限。最理想的是每个应用单独占用一个容器（比如 Docker），这样就不存在互相影响的问题。即便应用被攻破，也无法攻破 Docker 的保护层。</li>
<li>尽可能少的<code>root</code>。如果一个用户需要<code>root</code>能力，那么应当进行权限包围——马上提升权限（比如 sudo），处理后马上释放权限。</li>
<li>系统层面实现权限分级保护，将系统的权限分成一个个 Ring，外层 Ring 调用内层 Ring 时需要内层 Ring 进行权限校验。</li>
</ol>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="07&#32;&#32;进程、重定向和管道指令：xargs&#32;指令的作用是？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="09&#32;&#32;Linux&#32;中的网络指令：如何查看一个域名有哪些&#32;NS&#32;记录？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435d0248fb645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
