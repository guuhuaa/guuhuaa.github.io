<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>34  Nginx：高性能的Web服务器.md</title>
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

                    
                    <a href="00&#32;开篇词｜To&#32;Be&#32;a&#32;HTTP&#32;Hero.md">00 开篇词｜To Be a HTTP Hero.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;时势与英雄：HTTP的前世今生.md">01  时势与英雄：HTTP的前世今生.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;HTTP是什么？HTTP又不是什么？.md">02  HTTP是什么？HTTP又不是什么？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;HTTP世界全览（上）：与HTTP相关的各种概念.md">03  HTTP世界全览（上）：与HTTP相关的各种概念.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;HTTP世界全览（下）：与HTTP相关的各种协议.md">04  HTTP世界全览（下）：与HTTP相关的各种协议.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;常说的“四层”和“七层”到底是什么？“五层”“六层”哪去了？.md">05  常说的“四层”和“七层”到底是什么？“五层”“六层”哪去了？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;域名里有哪些门道？.md">06  域名里有哪些门道？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;自己动手，搭建HTTP实验环境.md">07  自己动手，搭建HTTP实验环境.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;键入网址再按下回车，后面究竟发生了什么？.md">08  键入网址再按下回车，后面究竟发生了什么？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;HTTP报文是什么样子的？.md">09  HTTP报文是什么样子的？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;应该如何理解请求方法？.md">10  应该如何理解请求方法？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;你能写出正确的网址吗？.md">11  你能写出正确的网址吗？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;响应状态码该怎么用？.md">12  响应状态码该怎么用？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;HTTP有哪些特点？.md">13  HTTP有哪些特点？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;HTTP有哪些优点？又有哪些缺点？.md">14  HTTP有哪些优点？又有哪些缺点？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;海纳百川：HTTP的实体数据.md">15  海纳百川：HTTP的实体数据.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;把大象装进冰箱：HTTP传输大文件的方法.md">16  把大象装进冰箱：HTTP传输大文件的方法.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;排队也要讲效率：HTTP的连接管理.md">17  排队也要讲效率：HTTP的连接管理.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;四通八达：HTTP的重定向和跳转.md">18  四通八达：HTTP的重定向和跳转.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;让我知道你是谁：HTTP的Cookie机制.md">19  让我知道你是谁：HTTP的Cookie机制.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;生鲜速递：HTTP的缓存控制.md">20  生鲜速递：HTTP的缓存控制.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;良心中间商：HTTP的代理服务.md">21  良心中间商：HTTP的代理服务.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;冷链周转：HTTP的缓存代理.md">22  冷链周转：HTTP的缓存代理.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;HTTPS是什么？SSLTLS又是什么？.md">23  HTTPS是什么？SSLTLS又是什么？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;固若金汤的根本（上）：对称加密与非对称加密.md">24  固若金汤的根本（上）：对称加密与非对称加密.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;固若金汤的根本（下）：数字签名与证书.md">25  固若金汤的根本（下）：数字签名与证书.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;信任始于握手：TLS1.2连接过程解析.md">26  信任始于握手：TLS1.2连接过程解析.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;更好更快的握手：TLS1.3特性解析.md">27  更好更快的握手：TLS1.3特性解析.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;连接太慢该怎么办：HTTPS的优化.md">28  连接太慢该怎么办：HTTPS的优化.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;我应该迁移到HTTPS吗？.md">29  我应该迁移到HTTPS吗？.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;时代之风（上）：HTTP2特性概览.md">30  时代之风（上）：HTTP2特性概览.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;时代之风（下）：HTTP2内核剖析.md">31  时代之风（下）：HTTP2内核剖析.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;未来之路：HTTP3展望.md">32  未来之路：HTTP3展望.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;我应该迁移到HTTP2吗？.md">33  我应该迁移到HTTP2吗？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="34&#32;&#32;Nginx：高性能的Web服务器.md">34  Nginx：高性能的Web服务器.md</a>
                    

                </li>
                <li>

                    
                    <a href="35&#32;&#32;OpenResty：更灵活的Web服务器.md">35  OpenResty：更灵活的Web服务器.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;WAF：保护我们的网络服务.md">36  WAF：保护我们的网络服务.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;CDN：加速我们的网络服务.md">37  CDN：加速我们的网络服务.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;WebSocket：沙盒里的TCP.md">38  WebSocket：沙盒里的TCP.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;HTTP性能优化面面观（上）.md">39  HTTP性能优化面面观（上）.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;HTTP性能优化面面观（下）.md">40  HTTP性能优化面面观（下）.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;做兴趣使然的Hero.md">结束语  做兴趣使然的Hero.md</a>

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
                        <div><h1>34  Nginx：高性能的Web服务器</h1>
<p>经过前面几大模块的学习，你已经完全掌握了 HTTP 的所有知识，那么接下来请收拾一下行囊，整理一下装备，跟我一起去探索 HTTP 之外的广阔天地。</p>
<p>现在的互联网非常发达，用户越来越多，网速越来越快，HTTPS 的安全加密、HTTP/2 的多路复用等特性都对 Web 服务器提出了非常高的要求。一个好的 Web 服务器必须要具备稳定、快速、易扩展、易维护等特性，才能够让网站“立于不败之地”。</p>
<p>那么，在搭建网站的时候，应该选择什么样的服务器软件呢？</p>
<p>在开头的几讲里我也提到过，Web 服务器就那么几款，目前市面上主流的只有两个：Apache 和 Nginx，两者合计占据了近 90% 的市场份额。</p>
<p>今天我要说的就是其中的 Nginx，它是 Web 服务器的“后起之秀”，虽然比 Apache 小了 10 岁，但增长速度十分迅猛，已经达到了与 Apache“平起平坐”的地位，而在“Top Million”网站中更是超过了 Apache，拥有超过 50% 的用户（<a href="https://w3techs.com/technologies/cross/web_server/ranking">参考数据</a>）。</p>
<p><img src="assets/c5df0592cc8aef91ba961f7fab5a4a0b.png" alt="unpreview" /></p>
<p>在这里必须要说一下 Nginx 的正确发音，它应该读成“Engine X”，但我个人感觉“X”念起来太“拗口”，还是比较倾向于读做“Engine ks”，这也与 UNIX、Linux 的发音一致。</p>
<p>作为一个 Web 服务器，Nginx 的功能非常完善，完美支持 HTTP/1、HTTPS 和 HTTP/2，而且还在不断进步。当前的主线版本已经发展到了 1.17，正在进行 HTTP/3 的研发，或许一年之后就能在 Nginx 上跑 HTTP/3 了。</p>
<p>Nginx 也是我个人的主要研究领域，我也写过相关的书，按理来说今天的课程应该是“手拿把攥”，但真正动笔的时候还是有些犹豫的：很多要点都已经在书里写过了，这次的专栏如果再重复相同的内容就不免有“骗稿费”的嫌疑，应该有些“不一样的东西”。</p>
<p>所以我决定抛开书本，换个角度，结合 HTTP 协议来讲 Nginx，带你窥视一下 HTTP 处理的内幕，看看 Web 服务器的工作原理。</p>
<h2>进程池</h2>
<p>你也许听说过，Nginx 是个“轻量级”的 Web 服务器，那么这个所谓的“轻量级”是什么意思呢？</p>
<p>“轻量级”是相对于“重量级”而言的。“重量级”就是指服务器进程很“重”，占用很多资源，当处理 HTTP 请求时会消耗大量的 CPU 和内存，受到这些资源的限制很难提高性能。</p>
<p>而 Nginx 作为“轻量级”的服务器，它的 CPU、内存占用都非常少，同样的资源配置下就能够为更多的用户提供服务，其奥秘在于它独特的工作模式。</p>
<p><img src="assets/3e94fbd78ed043e88c443f6416f99dc1.png" alt="img" /></p>
<p>在 Nginx 之前，Web 服务器的工作模式大多是“Per-Process”或者“Per-Thread”，对每一个请求使用单独的进程或者线程处理。这就存在创建进程或线程的成本，还会有进程、线程“上下文切换”的额外开销。如果请求数量很多，CPU 就会在多个进程、线程之间切换时“疲于奔命”，平白地浪费了计算时间。</p>
<p>Nginx 则完全不同，“一反惯例”地没有使用多线程，而是使用了“<strong>进程池 + 单线程</strong>”的工作模式。</p>
<p>Nginx 在启动的时候会预先创建好固定数量的 worker 进程，在之后的运行过程中不会再 fork 出新进程，这就是进程池，而且可以自动把进程“绑定”到独立的 CPU 上，这样就完全消除了进程创建和切换的成本，能够充分利用多核 CPU 的计算能力。</p>
<p>在进程池之上，还有一个“master”进程，专门用来管理进程池。它的作用有点像是 supervisor（一个用 Python 编写的进程管理工具），用来监控进程，自动恢复发生异常的 worker，保持进程池的稳定和服务能力。</p>
<p>不过 master 进程完全是 Nginx 自行用 C 语言实现的，这就摆脱了外部的依赖，简化了 Nginx 的部署和配置。</p>
<h2>I/O 多路复用</h2>
<p>如果你用 Java、C 等语言写过程序，一定很熟悉“多线程”的概念，使用多线程能够很容易实现并发处理。</p>
<p>但多线程也有一些缺点，除了刚才说到的“上下文切换”成本，还有编程模型复杂、数据竞争、同步等问题，写出正确、快速的多线程程序并不是一件容易的事情。</p>
<p>所以 Nginx 就选择了单线程的方式，带来的好处就是开发简单，没有互斥锁的成本，减少系统消耗。</p>
<p>那么，疑问也就产生了：为什么单线程的 Nginx，处理能力却能够超越其他多线程的服务器呢？</p>
<p>这要归功于 Nginx 利用了 Linux 内核里的一件“神兵利器”，<strong>I/O 多路复用接口</strong>，“大名鼎鼎”的 epoll。</p>
<p>“多路复用”这个词我们已经在之前的 HTTP/2、HTTP/3 里遇到过好几次，如果你理解了那里的“多路复用”，那么面对 Nginx 的 epoll“多路复用”也就好办了。</p>
<p>Web 服务器从根本上来说是“I/O 密集型”而不是“CPU 密集型”，处理能力的关键在于网络收发而不是 CPU 计算（这里暂时不考虑 HTTPS 的加解密），而网络 I/O 会因为各式各样的原因不得不等待，比如数据还没到达、对端没有响应、缓冲区满发不出去等等。</p>
<p>这种情形就有点像是 HTTP 里的“队头阻塞”。对于一般的单线程来说 CPU 就会“停下来”，造成浪费。而多线程的解决思路有点类似“并发连接”，虽然有的线程可能阻塞，但由于多个线程并行，总体上看阻塞的情况就不会太严重了。</p>
<p>Nginx 里使用的 epoll，就好像是 HTTP/2 里的“多路复用”技术，它把多个 HTTP 请求处理打散成碎片，都“复用”到一个单线程里，不按照先来后到的顺序处理，而是只当连接上真正可读、可写的时候才处理，如果可能发生阻塞就立刻切换出去，处理其他的请求。</p>
<p>通过这种方式，Nginx 就完全消除了 I/O 阻塞，把 CPU 利用得“满满当当”，又因为网络收发并不会消耗太多 CPU 计算能力，也不需要切换进程、线程，所以整体的 CPU 负载是相当低的。</p>
<p>这里我画了一张 Nginx“I/O 多路复用”的示意图，你可以看到，它的形式与 HTTP/2 的流非常相似，每个请求处理单独来看是分散、阻塞的，但因为都复用到了一个线程里，所以资源的利用率非常高。</p>
<p><img src="assets/4c6832cdce34133c9ed89237fb9d5059.png" alt="img" /></p>
<p>epoll 还有一个特点，大量的连接管理工作都是在操作系统内核里做的，这就减轻了应用程序的负担，所以 Nginx 可以为每个连接只分配很小的内存维护状态，即使有几万、几十万的并发连接也只会消耗几百 M 内存，而其他的 Web 服务器这个时候早就“Memory not enough”了。</p>
<h2>多阶段处理</h2>
<p>有了“进程池”和“I/O 多路复用”，Nginx 是如何处理 HTTP 请求的呢？</p>
<p>Nginx 在内部也采用的是“<strong>化整为零</strong>”的思路，把整个 Web 服务器分解成了多个“功能模块”，就好像是乐高积木，可以在配置文件里任意拼接搭建，从而实现了高度的灵活性和扩展性。</p>
<p>Nginx 的 HTTP 处理有四大类模块：</p>
<ol>
<li>handler 模块：直接处理 HTTP 请求；</li>
<li>filter 模块：不直接处理请求，而是加工过滤响应报文；</li>
<li>upstream 模块：实现反向代理功能，转发请求到其他服务器；</li>
<li>balance 模块：实现反向代理时的负载均衡算法。</li>
</ol>
<p>因为 upstream 模块和 balance 模块实现的是代理功能，Nginx 作为“中间人”，运行机制比较复杂，所以我今天只讲 handler 模块和 filter 模块。</p>
<p>不知道你有没有了解过“设计模式”这方面的知识，其中有一个非常有用的模式叫做“<strong>职责链</strong>”。它就好像是工厂里的流水线，原料从一头流入，线上有许多工人会进行各种加工处理，最后从另一头出来的就是完整的产品。</p>
<p>Nginx 里的 handler 模块和 filter 模块就是按照“职责链”模式设计和组织的，HTTP 请求报文就是“原材料”，各种模块就是工厂里的工人，走完模块构成的“流水线”，出来的就是处理完成的响应报文。</p>
<p>下面的这张图显示了 Nginx 的“流水线”，在 Nginx 里的术语叫“阶段式处理”（Phases），一共有 11 个阶段，每个阶段里又有许多各司其职的模块。</p>
<p><img src="assets/41318c867fda8a536d0e3db6f9987030.png" alt="img" /></p>
<p>我简单列几个与我们的课程相关的模块吧：</p>
<ul>
<li>charset 模块实现了字符集编码转换；（[第 15 讲]）</li>
<li>chunked 模块实现了响应数据的分块传输；（[第 16 讲]）</li>
<li>range 模块实现了范围请求，只返回数据的一部分；（[第 16 讲]）</li>
<li>rewrite 模块实现了重定向和跳转，还可以使用内置变量自定义跳转的 URI；（[第 18 讲]）</li>
<li>not_modified 模块检查头字段“if-Modified-Since”和“If-None-Match”，处理条件请求；（[第 20 讲]）</li>
<li>realip 模块处理“X-Real-IP”“X-Forwarded-For”等字段，获取客户端的真实 IP 地址；（[第 21 讲]）</li>
<li>ssl 模块实现了 SSL/TLS 协议支持，读取磁盘上的证书和私钥，实现 TLS 握手和 SNI、ALPN 等扩展功能；（[安全篇]）</li>
<li>http_v2 模块实现了完整的 HTTP/2 协议。（[飞翔篇]）</li>
</ul>
<p>在这张图里，你还可以看到 limit_conn、limit_req、access、log 等其他模块，它们实现的是限流限速、访问控制、日志等功能，不在 HTTP 协议规定之内，但对于运行在现实世界的 Web 服务器却是必备的。</p>
<p>如果你有 C 语言基础，感兴趣的话可以下载 Nginx 的源码，在代码级别仔细看看 HTTP 的处理过程。</p>
<h2>小结</h2>
<ol>
<li>Nginx 是一个高性能的 Web 服务器，它非常的轻量级，消耗的 CPU、内存很少；</li>
<li>Nginx 采用“master/workers”进程池架构，不使用多线程，消除了进程、线程切换的成本；</li>
<li>Nginx 基于 epoll 实现了“I/O 多路复用”，不会阻塞，所以性能很高；</li>
<li>Nginx 使用了“职责链”模式，多个模块分工合作，自由组合，以流水线的方式处理 HTTP 请求。</li>
</ol>
<h2>课下作业</h2>
<ol>
<li>你是怎么理解进程、线程上下文切换时的成本的，为什么 Nginx 要尽量避免？</li>
<li>试着自己描述一下 Nginx 用进程、epoll、模块流水线处理 HTTP 请求的过程。</li>
</ol>
<p>欢迎你把自己的学习体会写在留言区，与我和其他同学一起讨论。如果你觉得有所收获，也欢迎把文章分享给你的朋友。</p>
<p><img src="assets/4c7bceb80a8027389705e9d6ec9eb43d.png" alt="unpreview" /></p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="33&#32;&#32;我应该迁移到HTTP2吗？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="35&#32;&#32;OpenResty：更灵活的Web服务器.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b435c99d9e4645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E9%80%8F%E8%A7%86HTTP%E5%8D%8F%E8%AE%AE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
