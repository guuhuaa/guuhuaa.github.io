<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>34  UDP 协议：UDP 和 TCP 相比快在哪里？.md</title>
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

                    <a class="current-tab" href="34&#32;&#32;UDP&#32;协议：UDP&#32;和&#32;TCP&#32;相比快在哪里？.md">34  UDP 协议：UDP 和 TCP 相比快在哪里？.md</a>
                    

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
                        <div><h1>34  UDP 协议：UDP 和 TCP 相比快在哪里？</h1>
<p>TCP 和 UDP 是目前使用最广泛的两个传输层协议，同时也是面试考察的重点内容。今天我会初步带你认识这两个协议，一起探寻它们之间最大的区别。</p>
<p>在开始本讲的重点内容前，我们先来说说 RFC 文档（Request For Comments，请求评论），互联网的很多基础建设都是以 RFC 的形式文档化，它给用户提供了阅读和学习的权限。在给大家准备《<strong>计算机网络</strong>》专栏的时候，我也经常查阅 RFC 文档。</p>
<p>如果你查阅 TCP 和 UDP 的 RFC 文档，会发现一件非常有趣的事情。TCP 协议的 RFC 很长，我足足读了好几天才把它们全部弄明白。UDP 的 RFC 非常短，只有短短的两页，一个小时就能读明白。这让我不禁感叹，如果能穿越到当时那个年代，我就去发明 UDP 协议，因为实在是太简单了。但即使是这个简单协议，也同样主宰着计算机网络协议的半壁江山。</p>
<p>那么这一讲我们就以 TCP 和 UDP 的区别为引，带你了解这两个在工作中使用频率极高、极为重要的传输层协议。</p>
<h3>可靠性</h3>
<p>首先我们比较一下这两个协议在<strong>可靠性（Reliablility）上的区别。如果一个网络协议是可靠的，那么它能够保证数据被无损</strong>地传送到目的地。当应用的设计者选择一个具有可靠性的协议时，通常意味着这个应用不能容忍数据在传输过程中被损坏。</p>
<p>如果你是初学者，可能会认为所有的应用都需要可靠性。其实不然，比如说一个视频直播服务。如果在传输过程当中，视频图像发生了一定的损坏，用户看到的只是某几个像素、颜色不准确了，或者某几帧视频丢失了——这对用户来说是可以容忍的。但在观看视频的时候，用户最怕的不是实时数据发生一定的损坏，而是吞吐量得不到保证。比如视频看到一半卡住了，要等很久，或者丢失了一大段视频数据，导致错过精彩的内容。</p>
<p><strong>TCP 协议，是一个支持可靠性的协议。UDP 协议，是一个不支持可靠性的协议</strong>。接下来我们讨论几个常见实现可靠性的手段。</p>
<h4>校验和（Checksum）</h4>
<p>首先我们来说说<strong>校验和</strong>。<strong>这是一种非常常见的可靠性检查手段</strong>。</p>
<p>尽管 UDP 不支持可靠性，但是像校验和（Checksum）这一类最基本的数据校验，它还是支持的。<strong>不支持可靠性，并不意味着完全放弃可靠性。TCP 和 UDP 都支持最基本的校验和算法</strong>。</p>
<p>下面我为你举例<strong>一种最简单的校验和算法：纵向冗余检查</strong>。伪代码如下：</p>
<pre><code>byte c = 0;

for(byte x in bytes) {

  c = c xor x;

}
</code></pre>
<p><code>xor</code>是异或运算。上面的程序在计算字节数组 bytes 的校验和。<code>c</code>是最终的结果。你可以看到将所有<code>bytes</code>两两异或，最终的结果就是校验和。假设我们要传输 bytes，如果在传输过程中<code>bytes</code>发生了变化，校验和有<strong>很大概率</strong>也会跟着变化。当然也可能存在<code>bytes</code>发生变化，校验和没有变化的特例，不过校验和可以很大程度上帮助我们识别数据是否损坏了。</p>
<p><img src="assets/CgpVE1_-o5GADgRkAABcTgxXiyw544.png" alt="Lark20210113-153833.png" /></p>
<p>当要传输数据的时候，数据会被分片，我们把每个分片看作一个字节数组。然后在分片中，预留几个字节去存储校验和。校验和随着数据分片一起传输到目的地，目的地会用同样的算法再次计算校验和。如果二者校验和不一致，代表中途数据发生了损坏。</p>
<p><strong>对于 TCP 和 UDP，都实现了校验和算法，但二者的区别是，TCP 如果发现校验核对不上，也就是数据损坏，会主动丢失这个封包并且重发。而 UDP 什么都不会处理，UDP 把处理的权利交给使用它的程序员</strong>。</p>
<h4>请求/应答/连接模型</h4>
<p>另一种保证可靠性的方法是<strong>请求响应和连接的模型</strong>。TCP 实现了请求、响应和连接的模型，UDP 没有实现这个模型。</p>
<p>在通信当中，我们可以把通信双方抽象成两个人用电话通信一样，需要先建立联系（保持连接）。发起会话的人是发送请求，对方需要应答（或者称为响应）。会话双方保持一个连接，直到双方说再见。</p>
<p>在 TCP 协议当中，任何一方向另一方发送信息，另一方都需要给予一个应答。如果发送方在一定的时间内没有获得应答，发送方就会认为自己的信息没有到达目的地，中途发生了损坏或者丢失等，因此发送方会选择重发这条消息。</p>
<p>这样一个模式也造成了 TCP 协议的三次握手和四次挥手，下面我们一起来具体分析一下。</p>
<p><strong>1. TCP 的三次握手</strong></p>
<p>在 TCP 协议当中。我们假设 Alice 和 Bob 是两个通信进程。当 Alice 想要和 Bob 建立连接的时候，Alice 需要发送一个请求建立连接的消息给 Bob。这种请求建立连接的消息在 TCP 协议中称为<strong>同步</strong>（<strong>Synchronization， SYN</strong>）。而 Bob 收到 SYN，必须马上给 Alice 一个响应。这个响应在 TCP 协议当中称为<strong>响应</strong>（<strong>Acknowledgement，ACK</strong>）。请你务必记住这两个单词。不仅是 TCP 在用，其他协议也会复用这样的概念，来描述相同的事情。</p>
<p>当 Alice 给 Bob SYN，Bob 给 Alice ACK，这个时候，对 Alice 而言，连接就建立成功了。但是 TCP 是一个双工协议。所谓双工协议，代表数据可以双向传送。虽然对 Alice 而言，连接建立成功了。但是对 Bob 而言，连接还没有建立。为什么这么说呢？你可以这样思考，如果这个时候，Bob 马上给 Alice 发送信息，信息可能先于 Bob 的 ACK 到达 Alice，但这个时候 Alice 还不知道连接建立成功。 所以解决的办法就是 Bob 再给 Alice 发一次 SYN ，Alice 再给 Bob 一个 ACK。以上就是 TCP 的三次握手内容。</p>
<p>你可能会问，这明明是<strong>四次握手，哪里是三次握手</strong>呢？这是因为，Bob 给 Alice 的 ACK ，可以和 Bob 向 Alice 发起的 SYN 合并，称为一条 SYN-ACK 消息。TCP 协议以此来减少握手的次数，减少数据的传输，于是 TCP 就变成了三次握手。下图中绿色标签状是 Alice 和 Bob 的状态，完整的 TCP 三次握手的过程如下图所示：</p>
<p><img src="assets/CgpVE1_-o7OAHQP4AADkdEFtGfI902.png" alt="Lark20210113-153831.png" /></p>
<p><strong>2. TCP 的四次挥手</strong></p>
<p>四次挥手（TCP 断开连接）的原理类似。中断连接的请求我们称为 Finish（用 FIN 表示）；和三次握手过程一样，需要分析成 4 步：</p>
<ul>
<li>第 1 步是 Alice 发送 FIN</li>
<li>第 2 步是 Bob 给 ACK</li>
<li>第 3 步是 Bob 发送 FIN</li>
<li>第 4 步是 Alice 给 ACK</li>
</ul>
<p>之所以是四次挥手，是因为第 2 步和 第 3 步在挥手的过程中不能合并为 FIN-ACK。原因是在挥手的过程中，Alice 和 Bob 都可能有未完成的工作。比如对 Bob 而言，可能还存在之前发给 Alice 但是还没有收到 ACK 的请求。因此，Bob 收到 Alice 的 FIN 后，就马上给 ACK。但是 Bob 会在自己准备妥当后，再发送 FIN 给 Alice。完整的过程如下图所示：</p>
<p><img src="assets/Ciqc1F_-o7uASykoAAD1Eo7HnP4749.png" alt="Lark20210113-153824.png" /></p>
<p><strong>3. 连接</strong></p>
<p>连接是一个虚拟概念，连接的目的是让连接的双方达成默契，倾尽资源，给对方最快的响应。经历了三次握手，Alice 和 Bob 之间就建立了连接。<strong>连接也是一个很好的编程模型。当连接不稳定的时候，可以中断连接后再重新连接。这种模式极大地增加了两个应用之间的数据传输的可靠性</strong>。</p>
<p>以上就是 TCP 中存在的，而 UDP 中没有的机制，你可以仔细琢磨琢磨。</p>
<h4>封包排序</h4>
<p><strong>可靠性有一个最基本的要求是数据有序发出、无序传输，并且有序组合。TCP 协议保证了这种可靠性，UDP 则没有保证</strong>。</p>
<p>在传输之前，数据被拆分成分块。在 TCP 中叫作一个<strong>TCP Segment</strong>。在 UDP 中叫作一个<strong>UDP Datagram</strong>。Datagram 单词的含义是数据传输的最小单位。在到达目的地之后，尽管所有的数据分块可能是乱序到达的，但为了保证可靠性，乱序到达的数据又需要被重新排序，恢复到原有数据的顺序。</p>
<p><strong>在这个过程当中，TCP 利用了滑动窗口、快速重传等算法，保证了数据的顺序。而 UDP，仅仅是为每个 Datagram 标注了序号，并没有帮助应用程序进行数据的排序</strong>，<strong>这也是 TCP 和 UDP 在保证可靠性上一个非常重要的区别。</strong></p>
<h3>使用场景</h3>
<p>上面的内容中，我们比较了 TCP 和 UDP 在可靠性上的区别，接下来我们看看两个协议的使用场景。</p>
<p><strong>我们先来看一道面试题：如果客户端和服务器之间的单程平均延迟是 30 毫秒，那么客户端 Ping 服务端需要多少毫秒</strong>？</p>
<p>【<strong>分析</strong>】这个问题最核心的点是需要思考 Ping 服务应该由 TCP 实现还是 UDP 实现？请你思考：Ping 需不需要保持连接呢？答案是不需要，Ping 服务器的时候把数据发送过去即可，并不需要特地建立一个连接。</p>
<p>请你再思考，Ping 需不需要保证可靠性呢？答案依然是不需要，如果发生了丢包， Ping 将丢包计入丢包率即可。所以从这个角度来看，Ping 使用 UDP 即可。</p>
<p>所以这道面试题应该是 Round Trip 最快需要在 60 毫秒左右。一个来回的时间，我们也通常称为 Round Trip 时间。</p>
<p>通过分析上面的例子，我想告诉你，TCP 和 UDP 的使用场景是不同的。<strong>TCP 适用于需要可靠性，需要连接的场景</strong>。UDP 因为足够简单，只对数据进行简单加工处理，就调用底层的网络层（IP 协议）传输数据去了。<strong>因此 UDP 更适合对可靠性要求不高的场景</strong>。</p>
<p>另外很多需要定制化的场景，非常需要 UDP。以 HTTP 协议为例，在早期的 HTTP 协议的设计当中就选择了 TCP 协议。因为在 HTTP 的设计当中，请求和返回都是需要可靠性的。但是随着 HTTP 协议的发展，到了 HTTP 3.0 的时候，就开始基于 UDP 进行传输。这是因为，在 HTTP 3.0 协议当中，在 UDP 之上有另一个QUIC 协议在负责可靠性。UDP 足够简单，在其上构建自己的协议就很方便。</p>
<p><strong>你可以再思考一个问题：文件上传应该用 TCP 还是 UDP 呢</strong>？乍一看肯定是 TCP 协议，因为文件上传当然需要可靠性，防止数据损坏。但是如果你愿意在 UDP 上去实现一套专门上传文件的可靠性协议，性能是可以超越 TCP 协议的。因为你只需要解决文件上传一种需求，不用像 TCP 协议那样解决通用需求。</p>
<p>所以时至今日，到底什么情况应该用 TCP，什么情况用 UDP？这个问题边界的确在模糊化。<strong>总体来说，需要可靠性，且不希望花太多心思在网络协议的研发上，就使用 TCP 协议</strong>。</p>
<h3>总结</h3>
<p>最后我们再来总结一下，大而全的协议用起来舒服，比如 TCP；灵活的协议方便定制和扩展，比如 UDP。二者不分伯仲，各有千秋。</p>
<p>这一讲我们深入比较了 TCP 和 UDP 的可靠性及它们的使用场景。关于原理部分，比如具体 TCP 的滑动窗口算法、数据的切割算法、数据重传算法；TCP、UDP 的封包内部究竟有哪些字段，格式如何等。如果你感兴趣，可以来学习我将在拉勾教育推出的《<strong>计算机网络</strong>》专栏。</p>
<p><strong>那么通过这一讲的学习，你现在可以尝试来回答本讲关联的面试题目：UDP 比 TCP 快在哪里</strong>？</p>
<p>【<strong>解析</strong>】使用 UDP 传输数据，不用建立连接，数据直接丢过去即可。至于接收方，有没有在监听？会不会接收？那就是接收方的事情了。UDP 甚至不考虑数据的可靠性。至于发送双方会不会基于 UDP 再去定制研发可靠性协议，那就是开发者的事情了。所以 UDP 快在哪里？UDP 快在它足够简单。因为足够简单，所以 UDP 对计算性能、对网络占用都是比 TCP 少的。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="33&#32;&#32;互联网协议群（TCPIP）：多路复用是怎么回事？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="35&#32;&#32;Linux&#32;的&#32;IO&#32;模式：selectpollepoll&#32;有什么区别？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435dbe0ce7645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
