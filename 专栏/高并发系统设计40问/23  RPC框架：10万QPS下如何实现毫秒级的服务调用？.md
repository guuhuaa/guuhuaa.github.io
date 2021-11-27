<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>23  RPC框架：10万QPS下如何实现毫秒级的服务调用？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;为什么你要学习高并发系统设计？.md">00 开篇词  为什么你要学习高并发系统设计？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;高并发系统：它的通用设计方法是什么？.md">01  高并发系统：它的通用设计方法是什么？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;架构分层：我们为什么一定要这么做？.md">02  架构分层：我们为什么一定要这么做？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;系统设计目标（一）：如何提升系统性能？.md">03  系统设计目标（一）：如何提升系统性能？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;系统设计目标（二）：系统怎样做到高可用？.md">04  系统设计目标（二）：系统怎样做到高可用？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;系统设计目标（三）：如何让系统易于扩展？.md">05  系统设计目标（三）：如何让系统易于扩展？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;面试现场第一期：当问到组件实现原理时，面试官是在刁难你吗？.md">06  面试现场第一期：当问到组件实现原理时，面试官是在刁难你吗？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;池化技术：如何减少频繁创建数据库连接的性能损耗？.md">07  池化技术：如何减少频繁创建数据库连接的性能损耗？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;数据库优化方案（一）：查询请求增加时，如何做主从分离？.md">08  数据库优化方案（一）：查询请求增加时，如何做主从分离？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;数据库优化方案（二）：写入数据量增加时，如何实现分库分表？.md">09  数据库优化方案（二）：写入数据量增加时，如何实现分库分表？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;发号器：如何保证分库分表后ID的全局唯一性？.md">10  发号器：如何保证分库分表后ID的全局唯一性？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;NoSQL：在高并发场景下，数据库和NoSQL如何做到互补？.md">11  NoSQL：在高并发场景下，数据库和NoSQL如何做到互补？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;缓存：数据库成为瓶颈后，动态数据的查询要如何加速？.md">12  缓存：数据库成为瓶颈后，动态数据的查询要如何加速？.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;缓存的使用姿势（一）：如何选择缓存的读写策略？.md">13  缓存的使用姿势（一）：如何选择缓存的读写策略？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;缓存的使用姿势（二）：缓存如何做到高可用？.md">14  缓存的使用姿势（二）：缓存如何做到高可用？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;缓存的使用姿势（三）：缓存穿透了怎么办？.md">15  缓存的使用姿势（三）：缓存穿透了怎么办？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;CDN：静态资源如何加速？.md">16  CDN：静态资源如何加速？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;消息队列：秒杀时如何处理每秒上万次的下单请求？.md">17  消息队列：秒杀时如何处理每秒上万次的下单请求？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;消息投递：如何保证消息仅仅被消费一次？.md">18  消息投递：如何保证消息仅仅被消费一次？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;消息队列：如何降低消息队列系统中消息的延迟？.md">19  消息队列：如何降低消息队列系统中消息的延迟？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;面试现场第二期：当问到项目经历时，面试官究竟想要了解什么？.md">20  面试现场第二期：当问到项目经历时，面试官究竟想要了解什么？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;系统架构：每秒1万次请求的系统要做服务化拆分吗？.md">21  系统架构：每秒1万次请求的系统要做服务化拆分吗？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;微服务架构：微服务化后，系统架构要如何改造？.md">22  微服务架构：微服务化后，系统架构要如何改造？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="23&#32;&#32;RPC框架：10万QPS下如何实现毫秒级的服务调用？.md">23  RPC框架：10万QPS下如何实现毫秒级的服务调用？.md</a>
                    

                </li>
                <li>

                    
                    <a href="24&#32;&#32;注册中心：分布式系统如何寻址？.md">24  注册中心：分布式系统如何寻址？.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;分布式Trace：横跨几十个分布式组件的慢请求要如何排查？.md">25  分布式Trace：横跨几十个分布式组件的慢请求要如何排查？.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;负载均衡：怎样提升系统的横向扩展能力？.md">26  负载均衡：怎样提升系统的横向扩展能力？.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;API网关：系统的门面要如何做呢？.md">27  API网关：系统的门面要如何做呢？.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;多机房部署：跨地域的分布式系统如何做？.md">28  多机房部署：跨地域的分布式系统如何做？.md</a>

                </li>
                <li>

                    
                    <a href="29&#32;&#32;Service&#32;Mesh：如何屏蔽服务化系统的服务治理细节？.md">29  Service Mesh：如何屏蔽服务化系统的服务治理细节？.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;给系统加上眼睛：服务端监控要怎么做？.md">30  给系统加上眼睛：服务端监控要怎么做？.md</a>

                </li>
                <li>

                    
                    <a href="31&#32;&#32;应用性能管理：用户的使用体验应该如何监控？.md">31  应用性能管理：用户的使用体验应该如何监控？.md</a>

                </li>
                <li>

                    
                    <a href="32&#32;&#32;压力测试：怎样设计全链路压力测试平台？.md">32  压力测试：怎样设计全链路压力测试平台？.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;配置管理：成千上万的配置项要如何管理？.md">33  配置管理：成千上万的配置项要如何管理？.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;降级熔断：如何屏蔽非核心系统故障的影响？.md">34  降级熔断：如何屏蔽非核心系统故障的影响？.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;流量控制：高并发系统中我们如何操纵流量？.md">35  流量控制：高并发系统中我们如何操纵流量？.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;面试现场第三期：你要如何准备一场技术面试呢？.md">36  面试现场第三期：你要如何准备一场技术面试呢？.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;计数系统设计（一）：面对海量数据的计数器要如何做？.md">37  计数系统设计（一）：面对海量数据的计数器要如何做？.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;计数系统设计（二）：50万QPS下如何设计未读数系统？.md">38  计数系统设计（二）：50万QPS下如何设计未读数系统？.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;信息流设计（一）：通用信息流系统的推模式要如何做？.md">39  信息流设计（一）：通用信息流系统的推模式要如何做？.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;信息流设计（二）：通用信息流系统的拉模式要如何做？.md">40  信息流设计（二）：通用信息流系统的拉模式要如何做？.md</a>

                </li>
                <li>

                    
                    <a href="加餐&#32;&#32;数据的迁移应该如何做？.md">加餐  数据的迁移应该如何做？.md</a>

                </li>
                <li>

                    
                    <a href="期中测试&#32;&#32;10道高并发系统设计题目自测.md">期中测试  10道高并发系统设计题目自测.md</a>

                </li>
                <li>

                    
                    <a href="用户故事&#32;&#32;从“心”出发，我还有无数个可能.md">用户故事  从“心”出发，我还有无数个可能.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;学不可以已.md">结束语  学不可以已.md</a>

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
                        <div><h1>23  RPC框架：10万QPS下如何实现毫秒级的服务调用？</h1>
<p>你好，我是唐扬。</p>
<p>在21 讲和22 讲中，你的团队已经决定对垂直电商系统做服务化拆分，以便解决扩展性和研发成本高的问题。与此同时，你们在不断学习的过程中还发现，系统做了服务化拆分之后，会引入一些新的问题，这些问题我在上节课提到过，归纳起来主要是两点：</p>
<p>服务拆分单独部署后，引入的服务跨网络通信的问题；</p>
<p>在拆分成多个小服务之后，服务如何治理的问题。</p>
<p>如果想要解决这两方面问题，你需要了解，微服务化所需要的中间件的基本原理，和使用技巧，那么本节课，我会带你掌握，解决第一点问题的核心组件：<strong>RPC 框架。</strong></p>
<p>**来思考这样一个场景：**你的垂直电商系统的 QPS 已经达到了每秒 2 万次，在做了服务化拆分之后，由于我们把业务逻辑，都拆分到了单独部署的服务中，那么假设你在完成一次完整的请求时，需要调用 4～5 次服务，计算下来，RPC 服务需要承载大概每秒 10 万次的请求。那么，你该如何设计 RPC 框架，来承载如此大的请求量呢？你要做的是：</p>
<p>选择合适的网络模型，有针对性地调整网络参数，以优化网络传输性能；</p>
<p>选择合适的序列化方式，以提升封包、解包的性能。</p>
<p>接下来，我从原理出发，让你对于 RPC 有一个理性的认识，这样你在设计 RPC 框架时，就可以清晰地知道自己的设计目标是什么了。</p>
<h2>你所知道的 RPC</h2>
<p>说到 RPC（Remote Procedure Call，远程过程调用），你不会陌生，它指的是通过网络，调用另一台计算机上部署服务的技术。</p>
<p>而 RPC 框架就封装了网络调用的细节，让你像调用本地服务一样，调用远程部署的服务。你也许觉得只有像 Dubbo、Grpc、Thrift 这些新兴的框架才算是 RPC 框架，<strong>其实严格来说，你很早之前就接触到与 RPC 相关的技术了。</strong></p>
<p>比如，Java 原生就有一套远程调用框架<strong>叫做 RMI（Remote Method Invocation），</strong> 它可以让 Java 程序通过网络，调用另一台机器上的 Java 对象的方法。它是一种远程调用的方法，也是 J2EE 时代大名鼎鼎的 EJB 的实现基础。</p>
<p>时至今日，你仍然可以通过 Spring 的“RmiServiceExporter”将 Spring 管理的 bean 暴露成一个 RMI 的服务，从而继续使用 RMI 来实现跨进程的方法调用。之所以 RMI 没有像 Dubbo，Grpc 一样大火，<strong>是因为它存在着一些缺陷：</strong></p>
<p>RMI 使用专为 Java 远程对象定制的协议 JRMP（Java Remote Messaging Protocol）进行通信，这限制了它的通信双方，只能是 Java 语言的程序，无法实现跨语言通信；</p>
<p>RMI 使用 Java 原生的对象序列化方式，生成的字节数组空间较大，效率很差。</p>
<p>**另一个你可能听过的技术是 Web Service，**它也可以认为是 RPC 的一种实现方式。它的优势是，使用 HTTP+SOAP 协议，保证了调用可以跨语言，跨平台。只要你支持 HTTP 协议，可以解析 XML，那么就能够使用 Web Service。在我来看，它由于使用 XML 封装数据，数据包大，性能还是比较差。</p>
<p>**借上面几个例子，我主要是想告诉你，**RPC 并不是互联网时代的产物，也不是服务化之后才衍生出来的技术，而是一种规范，只要是封装了网络调用的细节，能够实现远程调用其他服务，就可以算作是一种 RPC 技术了。</p>
<p>那么你的垂直电商项目在使用 RPC 框架之后，<strong>会产生什么变化呢？</strong></p>
<p>在我来看，在性能上的变化是不可忽视的，<strong>我给你举个例子。</strong> 比方说，你的电商系统中，商品详情页面需要商品数据、评论数据还有店铺数据，如果在一体化的架构中，你只需要从商品库，评论库和店铺库获取数据就可以了，不考虑缓存的情况下有三次网络请求。</p>
<p>但是，如果独立出商品服务、评论服务和店铺服务之后，那么就需要分别调用这三个服务，而这三个服务又会分别调用各自的数据库，这就是六次网络请求。如果你服务拆分的更细粒度，那么多出的网络调用就会越多，请求的延迟就会更长，而这就是你为了提升系统的扩展性，在性能上所付出的代价。</p>
<p><img src="assets/1dba9b34e2973ec185b353becfc64fce.jpg" alt="img" /></p>
<p>那么，我们要如果优化 RPC 的性能，从而尽量减少网络调用，对于性能的影响呢？在这里，你首先需要了解一次 RPC 的调用都经过了哪些步骤，因为这样，你才可以针对这些步骤中可能存在的性能瓶颈点提出优化方案。<strong>步骤如下：</strong></p>
<p>在一次 RPC 调用过程中，客户端首先会将调用的类名、方法名、参数名、参数值等信息，序列化成二进制流；</p>
<p>然后客户端将二进制流，通过网络发送给服务端；</p>
<p>服务端接收到二进制流之后，将它反序列化，得到需要调用的类名、方法名、参数名和参数值，再通过动态代理的方式，调用对应的方法得到返回值；</p>
<p>服务端将返回值序列化，再通过网络发送给客户端；</p>
<p>客户端对结果反序列化之后，就可以得到调用的结果了。</p>
<p><strong>过程图如下：</strong></p>
<p><img src="assets/f98bd80af8a4e7258251db1084e0383e.jpg" alt="img" /></p>
<p>从这张图中你可以看到，有网络传输的过程，也有将请求序列化和反序列化的过程， 所以，如果要提升 RPC 框架的性能，需要从<strong>网络传输和序列化</strong>两方面来优化。</p>
<h2>如何提升网络传输性能</h2>
<p>在网络传输优化中，你首要做的，是选择一种高性能的 I/O 模型。所谓 I/O 模型，就是我们处理 I/O 的方式。而一般单次 I/O 请求会分为两个阶段，每个阶段对于 I/O 的处理方式是不同的。</p>
<p>**首先，I/O 会经历一个等待资源的阶段，**比方说，等待网络传输数据可用，在这个过程中我们对 I/O 会有两种处理方式：</p>
<p>阻塞。指的是在数据不可用时，I/O 请求一直阻塞，直到数据返回；</p>
<p>非阻塞。指的是数据不可用时，I/O 请求立即返回，直到被通知资源可用为止。</p>
<p>**然后是使用资源的阶段，**比如说从网络上接收到数据，并且拷贝到应用程序的缓冲区里面。在这个阶段我们也会有两种处理方式：</p>
<p>同步处理。指的是 I/O 请求在读取或者写入数据时会阻塞，直到读取或者写入数据完成；</p>
<p>异步处理。指的是 I/O 请求在读取或者写入数据时立即返回，当操作系统处理完成 I/O 请求，并且将数据拷贝到用户提供的缓冲区后，再通知应用 I/O 请求执行完成。</p>
<p>将这两个阶段的四种处理方式，做一些排列组合，再做一些补充，就得到了我们常见的五种 I/O 模型：</p>
<p>同步阻塞 I/O</p>
<p>同步非阻塞 I/O</p>
<p>同步多路 I/O 复用</p>
<p>信号驱动 I/O</p>
<p>异步 I/O</p>
<p>这五种 I/O 模型，你需要理解它们的区别和特点，不过在理解上你可能会有些难度，所以我来做个比喻，方便你理解。</p>
<p>我们来把 I/O 过程比喻成烧水倒水的过程，等待资源（就是烧水的过程），使用资源（就是倒水的过程）：</p>
<p>如果你站在炤台边上一直等着（等待资源）水烧开，然后倒水（使用资源），那么就是同步阻塞 I/O；</p>
<p>如果你偷点儿懒，在烧水的时候躺在沙发上看会儿电视（不再时时刻刻等待资源），但是还是要时不时的去看看水开了没有，一旦水开了，马上去倒水（使用资源），那么这就是同步非阻塞 I/O；</p>
<p>如果你想要洗澡，需要同时烧好多壶水，那你就在看电视的间隙去看看哪壶水开了（等待多个资源），哪一壶开了就先倒哪一壶，这样就加快了烧水的速度，这就是同步多路 I/O 复用；</p>
<p>不过你发现自己总是跑厨房去看水开了没，太累了，于是你考虑给你的水壶加一个报警器（信号），只要水开了就马上去倒水，这就是信号驱动 I/O；</p>
<p>最后一种就高级了，你发明了一个智能水壶，在水烧好后自动就可以把水倒好，这就是异步 I/O。</p>
<p>这五种 I/O 模型中最被广泛使用的是**多路 I/O 复用，**Linux 系统中的 select、epoll 等系统调用都是支持多路 I/O 复用模型的，Java 中的高性能网络框架 Netty 默认也是使用这种模型。所以，我们可以选择它。</p>
<p>那么，选择好了一种高性能的 I/O 模型，是不是就能实现，数据在网络上的高效传输呢？其实并没有那么简单，网络性能的调优涉及很多方面，**其中不可忽视的一项就是网络参数的调优，**接下来，我带你了解其中一个典型例子。当然，你可以结合网络基础知识，以及成熟 RPC 框架（比如 Dubbo）的源码来深入了解，网络参数调优的方方面面。</p>
<p>**在之前的项目中，**我的团队曾经写过一个简单的 RPC 通信框架。在进行测试的时候发现，远程调用一个空业务逻辑的方法时，平均响应时间居然可以到几十毫秒，这明显不符合我们的预期，在我们看来，运行一个空的方法，应该在 1 毫秒之内可以返回。于是，我先在测试的时候使用 tcpdump 抓了包，发现一次请求的 Ack 包竟然要经过 40ms 才返回。在网上 google 了一下原因，发现原因和一个叫做 tcp_nodelay 的参数有关。<strong>这个参数是什么作用呢？</strong></p>
<p>tcp 协议的包头有 20 字节，ip 协议的包头也有 20 字节，如果仅仅传输 1 字节的数据，在网络上传输的就有 20 + 20 + 1 = 41 字节，其中真正有用的数据只有 1 个字节，这对效率和带宽是极大的浪费。所以在 1984 年的时候，John Nagle 提出了以他的名字命名的 Nagle`s 算法，<strong>他期望：</strong></p>
<p>如果是连续的小数据包，大小没有一个 MSS（Maximum Segment</p>
<p>Size，最大分段大小），并且还没有收到之前发送的数据包的 Ack 信息，那么这些小数据包就会在发送端暂存起来，直到小数据包累积到一个 MSS，或者收到一个 Ack 为止。</p>
<p>这原本是为了减少不必要的网络传输，但是如果接收端开启了 DelayedACK（延迟 ACK 的发送，这样可以合并多个 ACK，提升网络传输效率），**那就会发生，**发送端发送第一个数据包后，接收端没有返回 ACK，这时发送端发送了第二个数据包，因为 Nagle`s 算法的存在，并且第一个发送包的 ACK 还没有返回，所以第二个包会暂存起来。而 DelayedACK 的超时时间，默认是 40ms，所以一旦到了 40ms，接收端回给发送端 ACK，那么发送端才会发送第二个包，<strong>这样就增加了延迟。</strong></p>
<p>**解决的方式非常简单：**只要在 socket 上开启 tcp_nodelay 就好了，这个参数关闭了 Nagle`s 算法，这样发送端就不需要等到上一个发送包的 ACK 返回，直接发送新的数据包就好了。这对于强网络交互的场景来说非常的适用，基本上，如果你要自己实现一套网络框架，tcp_nodelay 这个参数最好是要开启的。</p>
<h2>选择合适的序列化方式</h2>
<p>在对网络数据传输完成调优之后，另外一个需要关注的点就是，**数据的序列化和反序列化。**通常所说的序列化，是将传输对象转换成二进制串的过程，而反序列化则是相反的动作，是将二进制串转换成对象的过程。</p>
<p>从上面的 RPC 调用过程中你可以看到，一次 RPC 调用需要经历两次数据序列化的过程，和两次数据反序列化的过程，可见它们对于 RPC 的性能影响是很大的，<strong>那么我们在选择序列化方式的时候需要考虑哪些因素呢？</strong></p>
<p>首先需要考虑的肯定是性能嘛，性能包括时间上的开销和空间上的开销，时间上的开销就是序列化和反序列化的速度，这是显而易见需要重点考虑的，而空间上的开销则是序列化后的二进制串的大小，过大的二进制串也会占据传输带宽，影响传输效率。</p>
<p>除去性能之外，我们需要考虑的是它是否可以跨语言，跨平台，这一点也非常重要，因为一般的公司的技术体系都不是单一的，使用的语言也不是单一的，那么如果你的 RPC 框架中传输的数据只能被一种语言解析，那么这无疑限制了框架的使用。</p>
<p>另外，扩展性也是一个需要考虑的重点问题。你想想，如果对象增加了一个字段就会造成传输协议的不兼容，导致服务调用失败，这会是多么可怕的事情。</p>
<p>综合上面的几个考虑点，在我看来，<strong>我们的序列化备选方案主要有以下几种：</strong></p>
<p>首先是大家熟知的 JSON，它起源于 JavaScript，是一种最广泛使用的序列化协议，它的优势简单易用，人言可读，同时在性能上相比 XML 有比较大的优势。</p>
<p>另外的 Thrift 和 Protobuf 都是需要引入 IDL（Interface description language）的，也就是需要按照约定的语法写一个 IDL 文件，然后通过特定的编译器将它转换成各语言对应的代码，从而实现跨语言的特点。</p>
<p><strong>Thrift</strong> 是 Facebook 开源的高性能的序列化协议，也是一个轻量级的 RPC 框架；<strong>Protobuf</strong> 是谷歌开源的序列化协议。它们的共同特点是，无论在空间上还是时间上都有着很高的性能，缺点就是由于 IDL 存在带来一些使用上的不方便。</p>
<p>那么，你要如何选择这几种序列化协议呢？<strong>这里我给你几点建议：</strong></p>
<p>如果对于性能要求不高，在传输数据占用带宽不大的场景下，可以使用 JSON 作为序列化协议；</p>
<p>如果对于性能要求比较高，那么使用 Thrift 或者 Protobuf 都可以。而 Thrift 提供了配套的 RPC 框架，所以想要一体化的解决方案，你可以优先考虑 Thrift；</p>
<p>在一些存储的场景下，比如说你的缓存中存储的数据占用空间较大，那么你可以考虑使用 Protobuf 替换 JSON，作为存储数据的序列化方式。</p>
<h2>课程小结</h2>
<p>为了优化 RPC 框架的性能，本节课，我带你了解了网络 I/O 模型和序列化方式的选择，它们是实现高并发 RPC 框架的要素，总结起来有三个要点：</p>
<p>\1. 选择高性能的 I/O 模型，这里我推荐使用同步多路 I/O 复用模型；</p>
<p>\2. 调试网络参数，这里面有一些经验值的推荐。比如将 tcp_nodelay 设置为 true，也有一些参数需要在运行中来调试，比如接受缓冲区和发送缓冲区的大小，客户端连接请求缓冲队列的大小（back log）等等；</p>
<p>\3. 序列化协议依据具体业务来选择。如果对性能要求不高，可以选择 JSON，否则可以从 Thrift 和 Protobuf 中选择其一。</p>
<p>在学习本节课的过程中，我建议你阅读一下，成熟的 RPC 框架的源代码。比如，阿里开源的 Dubbo，微博的 Motan 等等，理解它们的实现原理和细节，这样你会更有信心维护好你的微服务系统；同时，你也可以从优秀的代码中，学习到代码设计的技巧，比如说 Dubbo 对于 RPC 的抽象，SPI 扩展点的设计，这样可以有助你提升代码能力。</p>
<p>当然了，本节课我不仅仅想让你了解 RPC 框架实现的一些原理，更想让你了解在做网络编程时，需要考虑哪些关键点，这样你在设计此类型的系统时，就会有一些考虑的方向和思路了。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="22&#32;&#32;微服务架构：微服务化后，系统架构要如何改造？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="24&#32;&#32;注册中心：分布式系统如何寻址？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4361c1e85f645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E9%AB%98%E5%B9%B6%E5%8F%91%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A140%E9%97%AE/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
