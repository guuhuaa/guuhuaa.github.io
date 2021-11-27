<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  CDN：静态资源如何加速？.md</title>
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

                    <a class="current-tab" href="16&#32;&#32;CDN：静态资源如何加速？.md">16  CDN：静态资源如何加速？.md</a>
                    

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

                    
                    <a href="23&#32;&#32;RPC框架：10万QPS下如何实现毫秒级的服务调用？.md">23  RPC框架：10万QPS下如何实现毫秒级的服务调用？.md</a>

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
                        <div><h1>16  CDN：静态资源如何加速？</h1>
<p>你好，我是唐扬。</p>
<p>前面几节课，我带你了解了缓存的定义以及常用缓存的使用姿势，现在，你应该对包括本地缓存、分布式缓存等缓存组件的适用场景和使用技巧有了一定了解了。结合在14 讲中我提到的客户端高可用方案，你会将单个缓存节点扩展为高可用的缓存集群，现在，你的电商系统架构演变成了下面这样：</p>
<p><img src="assets/1aa34cb9f368727399ba32e2891d48ba.jpg" alt="img" /></p>
<p>在这个架构中我们使用分布式缓存对动态请求数据的读取做了加速，但是在我们的系统中存在着大量的静态资源请求：</p>
<p>\1. 对于移动 APP 来说，这些静态资源主要是图片、视频和流媒体信息。</p>
<p>\2. 对于 Web 网站来说，则包括了 JavaScript 文件，CSS 文件，静态 HTML 文件等等。</p>
<p>具体到你的电商系统来说，商品的图片，介绍商品使用方法的视频等等静态资源，现在都放在了 Nginx 等 Web 服务器上，它们的读请求量极大，并且对访问速度的要求很高，并且占据了很高的带宽，这时会出现访问速度慢，带宽被占满影响动态请求的问题，<strong>那么你就需要考虑如何针对这些静态资源进行读加速了。</strong></p>
<h2>静态资源加速的考虑点</h2>
<p>你可能会问：“我们是否也可以使用分布式缓存来解决这个问题呢？”答案是否定的。一般来说，图片和视频的大小会在几兆到几百兆之间不等，如果我们的应用服务器和分布式缓存都部署在北京的机房里，这时一个杭州的用户要访问缓存中的一个视频，那这个视频文件就需要从北京传输到杭州，期间会经过多个公网骨干网络，延迟很高，会让用户感觉视频打开很慢，严重影响到用户的使用体验。</p>
<p>所以，静态资源访问的关键点是**就近访问，**即北京用户访问北京的数据，杭州用户访问杭州的数据，这样才可以达到性能的最优。</p>
<p>你可能会说：“那我们在杭州也自建一个机房，让用户访问杭州机房的数据就好了呀。”可用户遍布在全国各地，有些应用可能还有国外的用户，我们不可能在每个地域都自建机房，这样成本太高了。</p>
<p>另外，单个视频和图片等静态资源很大，并且访问量又极高，如果使用业务服务器和分布式缓存来承担这些流量，无论是对于内网还是外网的带宽都会是很大的考验。</p>
<p>所以我们考虑在业务服务器的上层，增加一层特殊的缓存，用来承担绝大部分对于静态资源的访问，这一层特殊缓存的节点需要遍布在全国各地，这样可以让用户选择最近的节点访问。缓存的命中率也需要一定的保证，尽量减少访问资源存储源站的请求数量（回源请求）。<strong>这一层缓存就是我们这节课的重点：CDN。</strong></p>
<h2>CDN 的关键技术</h2>
<p>CDN（Content Delivery Network/Content Distribution Network，内容分发网络）。简单来说，CDN 就是将静态的资源分发到，位于多个地理位置机房中的服务器上，因此它能很好地解决数据就近访问的问题，也就加快了静态资源的访问速度。</p>
<p>在大中型公司里面，CDN 的应用非常的普遍，大公司为了提供更稳定的 CDN 服务会选择自建 CDN，而大部分公司基于成本的考虑还是会选择专业的 CDN 厂商，网宿、阿里云、腾讯云、蓝汛等等，其中网宿和蓝汛是老牌的 CDN 厂商，阿里云和腾讯云是云厂商提供的服务，如果你的服务部署在云上可以选择相应云厂商的 CDN 服务，这些 CDN 厂商都是现今行业内比较主流的。</p>
<p>对于 CDN 来说，你可能已经从运维的口中听说过，并且也了解了它的作用。但是当让你来配置 CDN 或者是排查 CDN 方面的问题时，你就有可能因为不了解它的原理而束手无策了。</p>
<p>所以，我先来带你了解一下，要搭建一个 CDN 系统需要考虑哪两点：</p>
<p>\1. 如何将用户的请求映射到 CDN 节点上；</p>
<p>\2. 如何根据用户的地理位置信息选择到比较近的节点。</p>
<p>下面我就带你具体了解一下 CDN 系统是如何实现加速用户对于静态资源的请求的。</p>
<h3>1. 如何让用户的请求到达 CDN 节点</h3>
<p>首先，我们考虑一下如何让用户的请求到达 CDN 节点，你可能会觉得，这很简单啊，只需要告诉用户 CDN 节点的 IP 地址，然后请求这个 IP 地址上面部署的 CDN 服务就可以了啊。**但是这样会有一个问题：**就是我们使用的是第三方厂商的 CDN 服务，CDN 厂商会给我们一个 CDN 的节点 IP，比如说这个 IP 地址是“111.202.34.130”，那么我们的电商系统中的图片的地址很可能是这样的：“http://111.202.34.130/1.jpg”, 这个地址是要存储在数据库中的。</p>
<p>那么如果这个节点 IP 发生了变更怎么办？或者我们如果更改了 CDN 厂商怎么办？是不是要修改所有的商品的 url 域名呢？这就是一个比较大的工作量了。所以，我们要做的事情是将第三方厂商提供的 IP 隐藏起来，给到用户的最好是一个本公司域名的子域名。</p>
<p>**那么如何做到这一点呢？**这就需要依靠 DNS 来帮我们解决域名映射的问题了。</p>
<p>DNS（Domain Name System，域名系统）实际上就是一个存储域名和 IP 地址对应关系的分布式数据库。而域名解析的结果一般有两种，一种叫做“A 记录”，返回的是域名对应的 IP 地址；另一种是“CNAME 记录”，返回的是另一个域名，也就是说当前域名的解析要跳转到另一个域名的解析上，实际上 www.baidu.com 域名的解析结果就是一个 CNAME 记录，域名的解析被跳转到 www.a.shifen.com 上了，我们正是利用 CNAME 记录来解决域名映射问题的，<strong>具体是怎么解决的呢？我给你举个例子。</strong></p>
<p>比如你的公司的一级域名叫做 example.com，那么你可以给你的图片服务的域名定义为“img.example.com”，然后将这个域名的解析结果的 CNAME 配置到 CDN 提供的域名上，比如 uclound 可能会提供一个域名是“80f21f91.cdn.ucloud.com.cn”这个域名。这样你的电商系统使用的图片地址可以是“http://img.example.com/1.jpg”。</p>
<p>用户在请求这个地址时，DNS 服务器会将域名解析到 80f21f91.cdn.ucloud.com.cn 域名上，然后再将这个域名解析为 CDN 的节点 IP，这样就可以得到 CDN 上面的资源数据了。</p>
<p>**不过，这里面有一个问题：**因为域名解析过程是分级的，每一级有专门的域名服务器承担解析的职责，所以，域名的解析过程有可能需要跨越公网做多次 DNS 查询，在性能上是比较差的。</p>
<p><img src="assets/95d3d6081d8e55860bff6ad0df96c396.jpg" alt="img" /></p>
<p>从“ 域名分级解析示意图”中你可以看出 DNS 分为很多种，有根 DNS，顶级 DNS 等等。除此之外还有两种 DNS 需要特别留意：一种是 Local DNS，它是由你的运营商提供的 DNS，一般域名解析的第一站会到这里；另一种是权威 DNS，它的含义是自身数据库中存储了这个域名对应关系的 DNS。</p>
<p>下面我以 www.baidu.com 这个域名为例给你简单介绍一下域名解析的过程：</p>
<p>一开始，域名解析请求先会检查本机的 hosts 文件，查看是否有 www.baidu.com 对应的 IP；</p>
<p>如果没有的话，就请求 Local DNS 是否有域名解析结果的缓存，如果有就返回，标识是从非权威 DNS 返回的结果；</p>
<p>如果没有，就开始 DNS 的迭代查询。先请求根 DNS，根 DNS 返回顶级 DNS（.com）的地址；再请求.com 顶级 DNS，得到 baidu.com 的域名服务器地址；再从 baidu.com 的域名服务器中查询到 www.baidu.com 对应的 IP 地址，返回这个 IP 地址的同时，标记这个结果是来自于权威 DNS 的结果，同时写入 Local DNS 的解析结果缓存，这样下一次的解析同一个域名就不需要做 DNS 的迭代查询了。</p>
<p>经过了向多个 DNS 服务器做查询之后，整个 DNS 的解析的时间有可能会到秒级别，<strong>那么我们如何来解决这个性能问题呢？</strong></p>
<p>**一个解决的思路是：**在 APP 启动时，对需要解析的域名做预先解析，然后把解析的结果缓存到本地的一个 LRU 缓存里面。这样当我们要使用这个域名的时候，只需要从缓存中直接拿到所需要的 IP 地址就好了，如果缓存中不存在才会走整个 DNS 查询的过程。**同时，**为了避免 DNS 解析结果的变更造成缓存内数据失效，我们可以启动一个定时器，定期地更新缓存中的数据。</p>
<p>**我曾经测试过这种方式，**对于 HTTP 请求的响应时间的提升是很明显的，原先 DNS 解析时间经常会超过 1s，使用这种方式后，DNS 解析时间可以控制在 200ms 之内，整个 HTTP 请求的过程也可以减少大概 80ms～100ms。</p>
<p><img src="assets/1a692c89b0bcaa8106a8ba045be835c9.jpg" alt="img" /></p>
<p>**这里总结一下，**将用户的请求映射到 CDN 服务器上，是使用 CDN 时需要解决的一个核心的问题，而 CNAME 记录在 DNS 解析过程中可以充当一个中间代理层的角色，可以把将用户最初使用的域名代理到正确的 IP 地址上。图片:</p>
<p><img src="assets/4c884118fccb7041fdfb4d3e37003f59.jpg" alt="img" /></p>
<p>现在，剩下的一个问题就是如何找到更近的 CDN 节点了，而 GSLB 承担了这个职责。</p>
<h3>2. 如何找到离用户最近的 CDN 节点</h3>
<p>GSLB（Global Server Load Balance，全局负载均衡）, 它的含义是对于部署在不同地域的服务器之间做负载均衡，下面可能管理了很多的本地负载均衡组件。<strong>它有两方面的作用：</strong></p>
<p>一方面，它是一种负载均衡服务器，负载均衡，顾名思义嘛，指的是让流量平均分配使得下面管理的服务器的负载更平均；</p>
<p>另一方面，它还需要保证流量流经的服务器与流量源头在地缘上是比较接近的。</p>
<p>GSLB 可以通过多种策略，来保证返回的 CDN 节点和用户尽量保证在同一地缘区域，比如说可以将用户的 IP 地址按照地理位置划分为若干的区域，然后将 CDN 节点对应到一个区域上，然后根据用户所在区域来返回合适的节点；也可以通过发送数据包测量 RTT 的方式来决定返回哪一个节点。**不过，这些原理不是本节课重点内容，**你了解一下就可以了，我不做详细的介绍。</p>
<p>有了 GSLB 之后，节点的解析过程变成了下图中的样子：</p>
<p><img src="assets/fcc357ff674b4abdc00dc9c33cbf9a01.jpg" alt="img" /></p>
<p>**当然，是否能够从 CDN 节点上获取到资源还取决于 CDN 的同步延时。**一般，我们会通过 CDN 厂商的接口将静态的资源写入到某一个 CDN 节点上，再由 CDN 内部的同步机制将资源分散同步到每个 CDN 节点，即使 CDN 内部网络经过了优化，这个同步的过程是有延时的，一旦我们无法从选定的 CDN 节点上获取到数据，我们就不得不从源站获取数据，而用户网络到源站的网络可能会跨越多个主干网，这样不仅性能上有损耗，也会消耗源站的带宽，带来更高的研发成本。所以，我们在使用 CDN 的时候需要关注 CDN 的命中率和源站的带宽情况。</p>
<h2>课程小结</h2>
<p>本节课，我主要带你了解了 CDN 对静态资源进行加速的原理和使用的核心技术，这里你需要了解的重点有以下几点：</p>
<p>1.DNS 技术是 CDN 实现中使用的核心技术，可以将用户的请求映射到 CDN 节点上；</p>
<p>2.DNS 解析结果需要做本地缓存，降低 DNS 解析过程的响应时间；</p>
<p>3.GSLB 可以给用户返回一个离着他更近的节点，加快静态资源的访问速度。</p>
<p>作为一个服务端开发人员，你可能会忽略 CDN 的重要性，对于偶尔出现的 CDN 问题嗤之以鼻，觉得这个不是我们应该关心的内容，<strong>这种想法是错的。</strong></p>
<p>CDN 是我们系统的门面，其缓存的静态数据，如图片和视频数据的请求量很可能是接口请求数据的几倍甚至更高，一旦发生故障，对于整体系统的影响是巨大的。另外 CDN 的带宽历来是我们研发成本的大头，**尤其是目前处于小视频和直播风口上，**大量的小视频和直播研发团队都在绞尽脑汁地减少 CDN 的成本。由此看出，CDN 是我们整体系统至关重要的组成部分，而它作为一种特殊的缓存，其命中率和可用性也是我们服务端开发人员需要重点关注的指标。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;缓存的使用姿势（三）：缓存穿透了怎么办？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;消息队列：秒杀时如何处理每秒上万次的下单请求？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43619b4f15645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
