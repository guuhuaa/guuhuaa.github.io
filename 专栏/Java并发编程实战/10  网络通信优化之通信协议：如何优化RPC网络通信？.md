<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10  网络通信优化之通信协议：如何优化RPC网络通信？.md</title>
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

                    
                    <a href="00&#32;开篇词你为什么需要学习并发编程？.md">00 开篇词你为什么需要学习并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;如何制定性能调优标准？.md">01  如何制定性能调优标准？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;如何制定性能调优策略？.md">02  如何制定性能调优策略？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;字符串性能优化不容小觑，百M内存轻松存储几十G数据.md">03  字符串性能优化不容小觑，百M内存轻松存储几十G数据.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;慎重使用正则表达式.md">04  慎重使用正则表达式.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;ArrayList还是LinkedList？使用不当性能差千倍.md">05  ArrayList还是LinkedList？使用不当性能差千倍.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;Stream如何提高遍历集合效率？.md">06  Stream如何提高遍历集合效率？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;深入浅出HashMap的设计与优化.md">07  深入浅出HashMap的设计与优化.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md">08  网络通信优化之IO模型：如何解决高并发下IO瓶颈？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;网络通信优化之序列化：避免使用Java序列化.md">09  网络通信优化之序列化：避免使用Java序列化.md</a>

                </li>
                <li>

                    <a class="current-tab" href="10&#32;&#32;网络通信优化之通信协议：如何优化RPC网络通信？.md">10  网络通信优化之通信协议：如何优化RPC网络通信？.md</a>
                    

                </li>
                <li>

                    
                    <a href="11&#32;&#32;答疑课堂：深入了解NIO的优化实现原理.md">11  答疑课堂：深入了解NIO的优化实现原理.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md">12  多线程之锁优化（上）：深入了解Synchronized同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md">13  多线程之锁优化（中）：深入了解Lock同步锁的优化方法.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;多线程之锁优化（下）：使用乐观锁优化并行操作.md">14  多线程之锁优化（下）：使用乐观锁优化并行操作.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;多线程调优（上）：哪些操作导致了上下文切换？.md">15  多线程调优（上）：哪些操作导致了上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;多线程调优（下）：如何优化多线程上下文切换？.md">16  多线程调优（下）：如何优化多线程上下文切换？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;并发容器的使用：识别不同场景下最优容器.md">17  并发容器的使用：识别不同场景下最优容器.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;如何设置线程池大小？.md">18  如何设置线程池大小？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;如何用协程来优化多线程业务？.md">19  如何用协程来优化多线程业务？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md">20  磨刀不误砍柴工：欲知JVM调优先了解JVM内存模型.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;深入JVM即时编译器JIT，优化Java编译.md">21  深入JVM即时编译器JIT，优化Java编译.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;如何优化垃圾回收机制？.md">22  如何优化垃圾回收机制？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;如何优化JVM内存分配？.md">23  如何优化JVM内存分配？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;内存持续上升，我该如何排查问题？.md">24  内存持续上升，我该如何排查问题？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;答疑课堂：模块四热点问题解答.md">25  答疑课堂：模块四热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;单例模式：如何创建单一对象优化系统性能？.md">26  单例模式：如何创建单一对象优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;原型模式与享元模式：提升系统性能的利器.md">27  原型模式与享元模式：提升系统性能的利器.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;如何使用设计模式优化并发编程？.md">28  如何使用设计模式优化并发编程？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;生产者消费者模式：电商库存设计优化.md">29  生产者消费者模式：电商库存设计优化.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;装饰器模式：如何优化电商系统中复杂的商品价格策略？.md">30  装饰器模式：如何优化电商系统中复杂的商品价格策略？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;答疑课堂：模块五思考题集锦.md">31  答疑课堂：模块五思考题集锦.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;MySQL调优之SQL语句：如何写出高性能SQL语句？.md">32  MySQL调优之SQL语句：如何写出高性能SQL语句？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;MySQL调优之事务：高并发场景下的数据库事务调优.md">33  MySQL调优之事务：高并发场景下的数据库事务调优.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;MySQL调优之索引：索引的失效与优化.md">34  MySQL调优之索引：索引的失效与优化.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;记一次线上SQL死锁事故：如何避免死锁？.md">35  记一次线上SQL死锁事故：如何避免死锁？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;什么时候需要分表分库？.md">36  什么时候需要分表分库？.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;电商系统表设计优化案例分析.md">37  电商系统表设计优化案例分析.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;数据库参数设置优化，失之毫厘差之千里.md">38  数据库参数设置优化，失之毫厘差之千里.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;答疑课堂：MySQL中InnoDB的知识点串讲.md">39  答疑课堂：MySQL中InnoDB的知识点串讲.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;如何设计更优的分布式锁？.md">41  如何设计更优的分布式锁？.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;电商系统的分布式事务调优.md">42  电商系统的分布式事务调优.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;如何使用缓存优化系统性能？.md">43  如何使用缓存优化系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;记一次双十一抢购性能瓶颈调优.md">44  记一次双十一抢购性能瓶颈调优.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;什么是数据的强、弱一致性？.md">加餐  什么是数据的强、弱一致性？.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;推荐几款常用的性能测试工具.md">加餐  推荐几款常用的性能测试工具.md</a>

                </li>
                <li>

                    
                    <a href="答疑课堂：模块三热点问题解答.md">答疑课堂：模块三热点问题解答.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;栉风沐雨，砥砺前行！.md">结束语  栉风沐雨，砥砺前行！.md</a>

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
                        <div><h1>10  网络通信优化之通信协议：如何优化RPC网络通信？</h1>
<p>你好，我是刘超。今天我将带你了解下服务间的网络通信优化。</p>
<p>上一讲中，我提到了微服务框架，其中 SpringCloud 和 Dubbo 的使用最为广泛，行业内也一直存在着对两者的比较，很多技术人会为这两个框架哪个更好而争辩。</p>
<p>我记得我们部门在搭建微服务框架时，也在技术选型上纠结良久，还曾一度有过激烈的讨论。当前 SpringCloud 炙手可热，具备完整的微服务生态，得到了很多同事的票选，但我们最终的选择却是 Dubbo，这是为什么呢？</p>
<h2>RPC 通信是大型服务框架的核心</h2>
<p>我们经常讨论微服务，首要应该了解的就是微服务的核心到底是什么，这样我们在做技术选型时，才能更准确地把握需求。</p>
<p>就我个人理解，我认为微服务的核心是远程通信和服务治理。远程通信提供了服务之间通信的桥梁，服务治理则提供了服务的后勤保障。所以，我们在做技术选型时，更多要考虑的是这两个核心的需求。</p>
<p>我们知道服务的拆分增加了通信的成本，特别是在一些抢购或者促销的业务场景中，如果服务之间存在方法调用，比如，抢购成功之后需要调用订单系统、支付系统、券包系统等，这种远程通信就很容易成为系统的瓶颈。所以，在满足一定的服务治理需求的前提下，对远程通信的性能需求就是技术选型的主要影响因素。</p>
<p>目前，很多微服务框架中的服务通信是基于 RPC 通信实现的，在没有进行组件扩展的前提下，SpringCloud 是基于 Feign 组件实现的 RPC 通信（基于 Http+Json 序列化实现），Dubbo 是基于 SPI 扩展了很多 RPC 通信框架，包括 RMI、Dubbo、Hessian 等 RPC 通信框架（默认是 Dubbo+Hessian 序列化）。不同的业务场景下，RPC 通信的选择和优化标准也不同。</p>
<p>例如，开头我提到的我们部门在选择微服务框架时，选择了 Dubbo。当时的选择标准就是 RPC 通信可以支持抢购类的高并发，在这个业务场景中，请求的特点是瞬时高峰、请求量大和传入、传出参数数据包较小。而 Dubbo 中的 Dubbo 协议就很好地支持了这个请求。</p>
<p>**以下是基于 Dubbo:2.6.4 版本进行的简单的性能测试。**分别测试 Dubbo+Protobuf 序列化以及 Http+Json 序列化的通信性能（这里主要模拟单一 TCP 长连接 +Protobuf 序列化和短连接的 Http+Json 序列化的性能对比）。为了验证在数据量不同的情况下二者的性能表现，我分别准备了小对象和大对象的性能压测，通过这样的方式我们也可以间接地了解下二者在 RPC 通信方面的水平。</p>
<p><img src="assets/dc950f3a5ff15253e101fac90c192f54.jpg" alt="img" /></p>
<p><img src="assets/20814a2a87057fdc03af699454f703b1.jpg" alt="img" /></p>
<p>这个测试是我之前的积累，基于测试环境比较复杂，这里我就直接给出结果了，如果你感兴趣的话，可以留言和我讨论。</p>
<p>通过以上测试结果可以发现：<strong>无论从响应时间还是吞吐量上来看，单一 TCP 长连接 +Protobuf 序列化实现的 RPC 通信框架都有着非常明显的优势。</strong></p>
<p>在高并发场景下，我们选择后端服务框架或者中间件部门自行设计服务框架时，RPC 通信是重点优化的对象。</p>
<p>其实，目前成熟的 RPC 通信框架非常多，如果你们公司没有自己的中间件团队，也可以基于开源的 RPC 通信框架做扩展。在正式进行优化之前，我们不妨简单回顾下 RPC。</p>
<h2>什么是 RPC 通信</h2>
<p>一提到 RPC，你是否还想到 MVC、SOA 这些概念呢？如果你没有经历过这些架构的演变，这些概念就很容易混淆。<strong>你可以通过下面这张图来了解下这些架构的演变史。</strong></p>
<p><img src="assets/e43a8f81d76927948a73a9977643daa5.jpg" alt="img" /></p>
<p>无论是微服务、SOA、还是 RPC 架构，它们都是分布式服务架构，都需要实现服务之间的互相通信，我们通常把这种通信统称为 RPC 通信。</p>
<p>RPC（Remote Process Call），即远程服务调用，是通过网络请求远程计算机程序服务的通信技术。RPC 框架封装好了底层网络通信、序列化等技术，我们只需要在项目中引入各个服务的接口包，就可以实现在代码中调用 RPC 服务同调用本地方法一样。正因为这种方便、透明的远程调用，RPC 被广泛应用于当下企业级以及互联网项目中，是实现分布式系统的核心。</p>
<p>RMI（Remote Method Invocation）是 JDK 中最先实现了 RPC 通信的框架之一，RMI 的实现对建立分布式 Java 应用程序至关重要，是 Java 体系非常重要的底层技术，很多开源的 RPC 通信框架也是基于 RMI 实现原理设计出来的，包括 Dubbo 框架中也接入了 RMI 框架。接下来我们就一起了解下 RMI 的实现原理，看看它存在哪些性能瓶颈有待优化。</p>
<h2>RMI：JDK 自带的 RPC 通信框架</h2>
<p>目前 RMI 已经很成熟地应用在了 EJB 以及 Spring 框架中，是纯 Java 网络分布式应用系统的核心解决方案。RMI 实现了一台虚拟机应用对远程方法的调用可以同对本地方法的调用一样，RMI 帮我们封装好了其中关于远程通信的内容。</p>
<h3>RMI 的实现原理</h3>
<p>RMI 远程代理对象是 RMI 中最核心的组件，除了对象本身所在的虚拟机，其它虚拟机也可以调用此对象的方法。而且这些虚拟机可以不在同一个主机上，通过远程代理对象，远程应用可以用网络协议与服务进行通信。</p>
<p>我们可以通过一张图来详细地了解下整个 RMI 的通信过程：</p>
<p><img src="assets/1113e44dd62591ce68961e017c11ed4f.jpg" alt="img" /></p>
<h3>RMI 在高并发场景下的性能瓶颈</h3>
<ul>
<li>Java 默认序列化</li>
</ul>
<p>RMI 的序列化采用的是 Java 默认的序列化方式，我在 09 讲中详细地介绍过 Java 序列化，我们深知它的性能并不是很好，而且其它语言框架也暂时不支持 Java 序列化。</p>
<ul>
<li>TCP 短连接</li>
</ul>
<p>由于 RMI 是基于 TCP 短连接实现，在高并发情况下，大量请求会带来大量连接的创建和销毁，这对于系统来说无疑是非常消耗性能的。</p>
<ul>
<li>阻塞式网络 I/O</li>
</ul>
<p>在 08 讲中，我提到了网络通信存在 I/O 瓶颈，如果在 Socket 编程中使用传统的 I/O 模型，在高并发场景下基于短连接实现的网络通信就很容易产生 I/O 阻塞，性能将会大打折扣。</p>
<h2>一个高并发场景下的 RPC 通信优化路径</h2>
<p>SpringCloud 的 RPC 通信和 RMI 通信的性能瓶颈就非常相似。SpringCloud 是基于 Http 通信协议（短连接）和 Json 序列化实现的，在高并发场景下并没有优势。 那么，在瞬时高并发的场景下，我们又该如何去优化一个 RPC 通信呢？</p>
<p>RPC 通信包括了建立通信、实现报文、传输协议以及传输数据编解码等操作，接下来我们就从每一层的优化出发，逐步实现整体的性能优化。</p>
<h3>1. 选择合适的通信协议</h3>
<p>要实现不同机器间的网络通信，我们先要了解计算机系统网络通信的基本原理。网络通信是两台设备之间实现数据流交换的过程，是基于网络传输协议和传输数据的编解码来实现的。其中网络传输协议有 TCP、UDP 协议，这两个协议都是基于 Socket 编程接口之上，为某类应用场景而扩展出的传输协议。通过以下两张图，我们可以大概了解到基于 TCP 和 UDP 协议实现的 Socket 网络通信是怎样的一个流程。</p>
<p><img src="assets/2c7c373963196a30e9d4fdc524a92d0b.jpg" alt="img" /></p>
<p>基于 TCP 协议实现的 Socket 通信是有连接的，而传输数据是要通过三次握手来实现数据传输的可靠性，且传输数据是没有边界的，采用的是字节流模式。</p>
<p>基于 UDP 协议实现的 Socket 通信，客户端不需要建立连接，只需要创建一个套接字发送数据报给服务端，这样就不能保证数据报一定会达到服务端，所以在传输数据方面，基于 UDP 协议实现的 Socket 通信具有不可靠性。UDP 发送的数据采用的是数据报模式，每个 UDP 的数据报都有一个长度，该长度将与数据一起发送到服务端。</p>
<p>通过对比，我们可以得出优化方法：为了保证数据传输的可靠性，通常情况下我们会采用 TCP 协议。如果在局域网且对数据传输的可靠性没有要求的情况下，我们也可以考虑使用 UDP 协议，毕竟这种协议的效率要比 TCP 协议高。</p>
<h3>2. 使用单一长连接</h3>
<p>如果是基于 TCP 协议实现 Socket 通信，我们还能做哪些优化呢？</p>
<p>服务之间的通信不同于客户端与服务端之间的通信。客户端与服务端由于客户端数量多，基于短连接实现请求可以避免长时间地占用连接，导致系统资源浪费。</p>
<p>但服务之间的通信，连接的消费端不会像客户端那么多，但消费端向服务端请求的数量却一样多，我们基于长连接实现，就可以省去大量的 TCP 建立和关闭连接的操作，从而减少系统的性能消耗，节省时间。</p>
<h3>3. 优化 Socket 通信</h3>
<p>建立两台机器的网络通信，我们一般使用 Java 的 Socket 编程实现一个 TCP 连接。传统的 Socket 通信主要存在 I/O 阻塞、线程模型缺陷以及内存拷贝等问题。我们可以使用比较成熟的通信框架，比如 Netty。Netty4 对 Socket 通信编程做了很多方面的优化，具体见下方。</p>
<p>**实现非阻塞 I/O：**在 08 讲中，我们提到了多路复用器 Selector 实现了非阻塞 I/O 通信。</p>
<p>**高效的 Reactor 线程模型：**Netty 使用了主从 Reactor 多线程模型，服务端接收客户端请求连接是用了一个主线程，这个主线程用于客户端的连接请求操作，一旦连接建立成功，将会监听 I/O 事件，监听到事件后会创建一个链路请求。</p>
<p>链路请求将会注册到负责 I/O 操作的 I/O 工作线程上，由 I/O 工作线程负责后续的 I/O 操作。利用这种线程模型，可以解决在高负载、高并发的情况下，由于单个 NIO 线程无法监听海量客户端和满足大量 I/O 操作造成的问题。</p>
<p>**串行设计：**服务端在接收消息之后，存在着编码、解码、读取和发送等链路操作。如果这些操作都是基于并行去实现，无疑会导致严重的锁竞争，进而导致系统的性能下降。为了提升性能，Netty 采用了串行无锁化完成链路操作，Netty 提供了 Pipeline 实现链路的各个操作在运行期间不进行线程切换。</p>
<p>**零拷贝：**在 08 讲中，我们提到了一个数据从内存发送到网络中，存在着两次拷贝动作，先是从用户空间拷贝到内核空间，再是从内核空间拷贝到网络 I/O 中。而 NIO 提供的 ByteBuffer 可以使用 Direct Buffers 模式，直接开辟一个非堆物理内存，不需要进行字节缓冲区的二次拷贝，可以直接将数据写入到内核空间。</p>
<p><strong>除了以上这些优化，我们还可以针对套接字编程提供的一些 TCP 参数配置项，提高网络吞吐量，Netty 可以基于 ChannelOption 来设置这些参数。</strong></p>
<p>**TCP_NODELAY：**TCP_NODELAY 选项是用来控制是否开启 Nagle 算法。Nagle 算法通过缓存的方式将小的数据包组成一个大的数据包，从而避免大量的小数据包发送阻塞网络，提高网络传输的效率。我们可以关闭该算法，优化对于时延敏感的应用场景。</p>
<p>**SO_RCVBUF 和 SO_SNDBUF：**可以根据场景调整套接字发送缓冲区和接收缓冲区的大小。</p>
<p>**SO_BACKLOG：**backlog 参数指定了客户端连接请求缓冲队列的大小。服务端处理客户端连接请求是按顺序处理的，所以同一时间只能处理一个客户端连接，当有多个客户端进来的时候，服务端就会将不能处理的客户端连接请求放在队列中等待处理。</p>
<p>**SO_KEEPALIVE：**当设置该选项以后，连接会检查长时间没有发送数据的客户端的连接状态，检测到客户端断开连接后，服务端将回收该连接。我们可以将该时间设置得短一些，来提高回收连接的效率。</p>
<h3>4. 量身定做报文格式</h3>
<p>接下来就是实现报文，我们需要设计一套报文，用于描述具体的校验、操作、传输数据等内容。为了提高传输的效率，我们可以根据自己的业务和架构来考虑设计，尽量实现报体小、满足功能、易解析等特性。我们可以参考下面的数据格式：</p>
<p><img src="assets/6dc21193a6ffbf94a7dd8e5a0d2302c1.jpg" alt="img" />
<img src="assets/f3bb46ed6ece4a8a9bcc3d9e9df84cae.jpg" alt="img" /></p>
<h3>5. 编码、解码</h3>
<p>在 09 讲中，我们分析过序列化编码和解码的过程，对于实现一个好的网络通信协议来说，兼容优秀的序列化框架是非常重要的。如果只是单纯的数据对象传输，我们可以选择性能相对较好的 Protobuf 序列化，有利于提高网络通信的性能。</p>
<h3>6. 调整 Linux 的 TCP 参数设置选项</h3>
<p>如果 RPC 是基于 TCP 短连接实现的，我们可以通过修改 Linux TCP 配置项来优化网络通信。开始 TCP 配置项的优化之前，我们先来了解下建立 TCP 连接的三次握手和关闭 TCP 连接的四次握手，这样有助后面内容的理解。</p>
<ul>
<li>三次握手</li>
</ul>
<p><img src="assets/32381d3314bd982544f69e4d3faba1de.jpg" alt="img" /></p>
<ul>
<li>四次握手</li>
</ul>
<p><img src="assets/df9f4e3f3598a7e160c899f552a59391.jpg" alt="img" /></p>
<p>我们可以通过 sysctl -a | grep net.xxx 命令运行查看 Linux 系统默认的的 TCP 参数设置，如果需要修改某项配置，可以通过编辑 vim/etc/sysctl.conf，加入需要修改的配置项， 并通过 sysctl -p 命令运行生效修改后的配置项设置。通常我们会通过修改以下几个配置项来提高网络吞吐量和降低延时。</p>
<p><img src="assets/9eb01fe017b267367b11170a864bd0bc.jpg" alt="img" /></p>
<p>以上就是我们从不同层次对 RPC 优化的详解，除了最后的 Linux 系统中 TCP 的配置项设置调优，其它的调优更多是从代码编程优化的角度出发，最终实现了一套 RPC 通信框架的优化路径。</p>
<p>弄懂了这些，你就可以根据自己的业务场景去做技术选型了，还能很好地解决过程中出现的一些性能问题。</p>
<h2>总结</h2>
<p>在现在的分布式系统中，特别是系统走向微服务化的今天，服务间的通信就显得尤为频繁，掌握服务间的通信原理和通信协议优化，是你的一项的必备技能。</p>
<p>在一些并发场景比较多的系统中，我更偏向使用 Dubbo 实现的这一套 RPC 通信协议。Dubbo 协议是建立的单一长连接通信，网络 I/O 为 NIO 非阻塞读写操作，更兼容了 Kryo、FST、Protobuf 等性能出众的序列化框架，在高并发、小对象传输的业务场景中非常实用。</p>
<p>在企业级系统中，业务往往要比普通的互联网产品复杂，服务与服务之间可能不仅仅是数据传输，还有图片以及文件的传输，所以 RPC 的通信协议设计考虑更多是功能性需求，在性能方面不追求极致。其它通信框架在功能性、生态以及易用、易入门等方面更具有优势。</p>
<h2>思考题</h2>
<p>目前实现 Java RPC 通信的框架有很多，实现 RPC 通信的协议也有很多，除了 Dubbo 协议以外，你还使用过其它 RPC 通信协议吗？通过这讲的学习，你能对比谈谈各自的优缺点了吗？</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;&#32;网络通信优化之序列化：避免使用Java序列化.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;&#32;答疑课堂：深入了解NIO的优化实现原理.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4343df8f6a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Java%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%E5%AE%9E%E6%88%98/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
