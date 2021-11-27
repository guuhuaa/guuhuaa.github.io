<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>31  加餐：深潜 Directory 实现，探秘服务目录玄机.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;深入掌握&#32;Dubbo&#32;原理与实现，提升你的职场竞争力.md">00 开篇词  深入掌握 Dubbo 原理与实现，提升你的职场竞争力.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;Dubbo&#32;源码环境搭建：千里之行，始于足下.md">01  Dubbo 源码环境搭建：千里之行，始于足下.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;Dubbo&#32;的配置总线：抓住&#32;URL，就理解了半个&#32;Dubbo.md">02 Dubbo 的配置总线：抓住 URL，就理解了半个 Dubbo.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（上）.md">03  Dubbo SPI 精析，接口实现两极反转（上）.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;Dubbo&#32;SPI&#32;精析，接口实现两极反转（下）.md">04  Dubbo SPI 精析，接口实现两极反转（下）.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;海量定时任务，一个时间轮搞定.md">05  海量定时任务，一个时间轮搞定.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（上）.md">06  ZooKeeper 与 Curator，求你别用 ZkClient 了（上）.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（下）.md">07  ZooKeeper 与 Curator，求你别用 ZkClient 了（下）.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;代理模式与常见实现.md">08  代理模式与常见实现.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;Netty&#32;入门，用它做网络编程都说好（上）.md">09  Netty 入门，用它做网络编程都说好（上）.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;Netty&#32;入门，用它做网络编程都说好（下）.md">10  Netty 入门，用它做网络编程都说好（下）.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;简易版&#32;RPC&#32;框架实现（上）.md">11  简易版 RPC 框架实现（上）.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;简易版&#32;RPC&#32;框架实现（下）.md">12  简易版 RPC 框架实现（下）.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;&#32;本地缓存：降低&#32;ZooKeeper&#32;压力的一个常用手段.md">13  本地缓存：降低 ZooKeeper 压力的一个常用手段.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;重试机制是网络操作的基本保证.md">14  重试机制是网络操作的基本保证.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;ZooKeeper&#32;注册中心实现，官方推荐注册中心实践.md">15  ZooKeeper 注册中心实现，官方推荐注册中心实践.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;Dubbo&#32;Serialize&#32;层：多种序列化算法，总有一款适合你.md">16  Dubbo Serialize 层：多种序列化算法，总有一款适合你.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;Dubbo&#32;Remoting&#32;层核心接口分析：这居然是一套兼容所有&#32;NIO&#32;框架的设计？.md">17  Dubbo Remoting 层核心接口分析：这居然是一套兼容所有 NIO 框架的设计？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;Buffer&#32;缓冲区：我们不生产数据，我们只是数据的搬运工.md">18  Buffer 缓冲区：我们不生产数据，我们只是数据的搬运工.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（上）.md">19  Transporter 层核心实现：编解码与线程模型一文打尽（上）.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（下）.md">20  Transporter 层核心实现：编解码与线程模型一文打尽（下）.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;Exchange&#32;层剖析：彻底搞懂&#32;Request-Response&#32;模型（上）.md">21  Exchange 层剖析：彻底搞懂 Request-Response 模型（上）.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;Exchange&#32;层剖析：彻底搞懂&#32;Request-Response&#32;模型（下）.md">22  Exchange 层剖析：彻底搞懂 Request-Response 模型（下）.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;核心接口介绍，RPC&#32;层骨架梳理.md">23  核心接口介绍，RPC 层骨架梳理.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（上）.md">24  从 Protocol 起手，看服务暴露和服务引用的全流程（上）.md</a>

                </li>
                <li>

                    
                    <a href="25&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（下）.md">25  从 Protocol 起手，看服务暴露和服务引用的全流程（下）.md</a>

                </li>
                <li>

                    
                    <a href="26&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（上）.md">26  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（上）.md</a>

                </li>
                <li>

                    
                    <a href="27&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（下）.md">27  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（下）.md</a>

                </li>
                <li>

                    
                    <a href="28&#32;&#32;复杂问题简单化，代理帮你隐藏了多少底层细节？.md">28  复杂问题简单化，代理帮你隐藏了多少底层细节？.md</a>

                </li>
                <li>

                    
                    <a href="https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Dubbo%E6%BA%90%E7%A0%81%E8%A7%A3%E8%AF%BB%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/29%20%20%E5%8A%A0%E9%A4%90%EF%BC%9AHTTP%20%E5%8D%8F%E8%AE%AE%20+%20JSON-RPC%EF%BC%8CDubbo%20%E8%B7%A8%E8%AF%AD%E8%A8%80%E5%B0%B1%E6%98%AF%E5%A6%82%E6%AD%A4%E7%AE%80%E5%8D%95.md">29  加餐：HTTP 协议 + JSON-RPC，Dubbo 跨语言就是如此简单.md</a>

                </li>
                <li>

                    
                    <a href="30&#32;&#32;Filter&#32;接口，扩展&#32;Dubbo&#32;框架的常用手段指北.md">30  Filter 接口，扩展 Dubbo 框架的常用手段指北.md</a>

                </li>
                <li>

                    <a class="current-tab" href="31&#32;&#32;加餐：深潜&#32;Directory&#32;实现，探秘服务目录玄机.md">31  加餐：深潜 Directory 实现，探秘服务目录玄机.md</a>
                    

                </li>
                <li>

                    
                    <a href="32&#32;&#32;路由机制：请求到底怎么走，它说了算（上）.md">32  路由机制：请求到底怎么走，它说了算（上）.md</a>

                </li>
                <li>

                    
                    <a href="33&#32;&#32;路由机制：请求到底怎么走，它说了算（下）.md">33  路由机制：请求到底怎么走，它说了算（下）.md</a>

                </li>
                <li>

                    
                    <a href="34&#32;&#32;加餐：初探&#32;Dubbo&#32;动态配置的那些事儿.md">34  加餐：初探 Dubbo 动态配置的那些事儿.md</a>

                </li>
                <li>

                    
                    <a href="35&#32;&#32;负载均衡：公平公正物尽其用的负载均衡策略，这里都有（上）.md">35  负载均衡：公平公正物尽其用的负载均衡策略，这里都有（上）.md</a>

                </li>
                <li>

                    
                    <a href="36&#32;&#32;负载均衡：公平公正物尽其用的负载均衡策略，这里都有（下）.md">36  负载均衡：公平公正物尽其用的负载均衡策略，这里都有（下）.md</a>

                </li>
                <li>

                    
                    <a href="37&#32;&#32;集群容错：一个好汉三个帮（上）.md">37  集群容错：一个好汉三个帮（上）.md</a>

                </li>
                <li>

                    
                    <a href="38&#32;&#32;集群容错：一个好汉三个帮（下）.md">38  集群容错：一个好汉三个帮（下）.md</a>

                </li>
                <li>

                    
                    <a href="39&#32;&#32;加餐：多个返回值不用怕，Merger&#32;合并器来帮忙.md">39  加餐：多个返回值不用怕，Merger 合并器来帮忙.md</a>

                </li>
                <li>

                    
                    <a href="40&#32;&#32;加餐：模拟远程调用，Mock&#32;机制帮你搞定.md">40  加餐：模拟远程调用，Mock 机制帮你搞定.md</a>

                </li>
                <li>

                    
                    <a href="41&#32;&#32;加餐：一键通关服务发布全流程.md">41  加餐：一键通关服务发布全流程.md</a>

                </li>
                <li>

                    
                    <a href="42&#32;&#32;加餐：服务引用流程全解析.md">42  加餐：服务引用流程全解析.md</a>

                </li>
                <li>

                    
                    <a href="43&#32;&#32;服务自省设计方案：新版本新方案.md">43  服务自省设计方案：新版本新方案.md</a>

                </li>
                <li>

                    
                    <a href="44&#32;&#32;元数据方案深度剖析，如何避免注册中心数据量膨胀？.md">44  元数据方案深度剖析，如何避免注册中心数据量膨胀？.md</a>

                </li>
                <li>

                    
                    <a href="45&#32;&#32;加餐：深入服务自省方案中的服务发布订阅（上）.md">45  加餐：深入服务自省方案中的服务发布订阅（上）.md</a>

                </li>
                <li>

                    
                    <a href="46&#32;&#32;加餐：深入服务自省方案中的服务发布订阅（下）.md">46  加餐：深入服务自省方案中的服务发布订阅（下）.md</a>

                </li>
                <li>

                    
                    <a href="47&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（上）.md">47  配置中心设计与实现：集中化配置 and 本地化配置，我都要（上）.md</a>

                </li>
                <li>

                    
                    <a href="48&#32;&#32;配置中心设计与实现：集中化配置&#32;and&#32;本地化配置，我都要（下）.md">48  配置中心设计与实现：集中化配置 and 本地化配置，我都要（下）.md</a>

                </li>
                <li>

                    
                    <a href="49&#32;结束语&#32;&#32;认真学习，缩小差距.md">49 结束语  认真学习，缩小差距.md</a>

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
                        <div><h1>31  加餐：深潜 Directory 实现，探秘服务目录玄机</h1>
<p>从这一课时我们就进入“集群”模块了，今天我们分享的是一篇加餐文章，主题是：深潜 Directory 实现，探秘服务目录玄机。</p>
<p>在生产环境中，为了保证服务的可靠性、吞吐量以及容错能力，我们通常会在多个服务器上运行相同的服务端程序，然后以<strong>集群</strong>的形式对外提供服务。根据各项性能指标的要求不同，各个服务端集群中服务实例的个数也不尽相同，从几个实例到几百个实例不等。</p>
<p>对于客户端程序来说，就会出现几个问题：</p>
<ul>
<li>客户端程序是否要感知每个服务端地址？</li>
<li>客户端程序的一次请求，到底调用哪个服务端程序呢？</li>
<li>请求失败之后的处理是重试，还会是抛出异常？</li>
<li>如果是重试，是再次请求该服务实例，还是尝试请求其他服务实例？</li>
<li>服务端集群如何做到负载均衡，负载均衡的标准是什么呢？</li>
<li>……</li>
</ul>
<p>为了解决上述问题，<strong>Dubbo 独立出了一个实现集群功能的模块—— dubbo-cluster</strong>。</p>
<p><img src="assets/Ciqc1F-qN92ADHx8AACiY_cvusQ921.png" alt="Drawing 0.png" /></p>
<p>dubbo-cluster 结构图</p>
<p>作为 dubbo-cluster 模块分析的第一课时，我们就首先来了解一下 dubbo-cluster 模块的架构以及最核心的 Cluster 接口。</p>
<h3>Cluster 架构</h3>
<p>dubbo-cluster 模块的主要功能是将多个 Provider 伪装成一个 Provider 供 Consumer 调用，其中涉及集群的容错处理、路由规则的处理以及负载均衡。下图展示了 dubbo-cluster 的核心组件：</p>
<p><img src="assets/Ciqc1F-qY-CAQ08VAAFAZaC5kyU044.png" alt="Lark20201110-175555.png" /></p>
<p>Cluster 核心接口图</p>
<p>由图我们可以看出，dubbo-cluster 主要包括以下四个核心接口：</p>
<ul>
<li><strong>Cluster 接口</strong>，是集群容错的接口，主要是在某些 Provider 节点发生故障时，让 Consumer 的调用请求能够发送到正常的 Provider 节点，从而保证整个系统的可用性。</li>
<li><strong>Directory 接口</strong>，表示多个 Invoker 的集合，是后续路由规则、负载均衡策略以及集群容错的基础。</li>
<li><strong>Router 接口</strong>，抽象的是路由器，请求经过 Router 的时候，会按照用户指定的规则匹配出符合条件的 Provider。</li>
<li><strong>LoadBalance 接口</strong>，是负载均衡接口，Consumer 会按照指定的负载均衡策略，从 Provider 集合中选出一个最合适的 Provider 节点来处理请求。</li>
</ul>
<p>Cluster 层的核心流程是这样的：当调用进入 Cluster 的时候，Cluster 会创建一个 AbstractClusterInvoker 对象，在这个 AbstractClusterInvoker 中，首先会从 Directory 中获取当前 Invoker 集合；然后按照 Router 集合进行路由，得到符合条件的 Invoker 集合；接下来按照 LoadBalance 指定的负载均衡策略得到最终要调用的 Invoker 对象。</p>
<p>了解了 dubbo-cluster 模块的核心架构和基础组件之后，我们后续将会按照上面架构图的顺序介绍每个接口的定义以及相关实现。</p>
<h3>Directory 接口详解</h3>
<p>Directory 接口表示的是一个集合，该集合由多个 Invoker 构成，后续的路由处理、负载均衡、集群容错等一系列操作都是在 Directory 基础上实现的。</p>
<p>下面我们深入分析一下 Directory 的相关内容，首先是 Directory 接口中定义的方法：</p>
<pre><code>public interface Directory&lt;T&gt; extends Node {

    // 服务接口类型

    Class&lt;T&gt; getInterface();

    // list()方法会根据传入的Invocation请求，过滤自身维护的Invoker集合，返回符合条件的Invoker集合

    List&lt;Invoker&lt;T&gt;&gt; list(Invocation invocation) throws RpcException;

    // getAllInvokers()方法返回当前Directory对象维护的全部Invoker对象

    List&lt;Invoker&lt;T&gt;&gt; getAllInvokers();

    // Consumer端的URL

    URL getConsumerUrl();

}
</code></pre>
<p><strong>AbstractDirectory 是 Directory 接口的抽象实现</strong>，其中除了维护 Consumer 端的 URL 信息，还维护了一个 RouterChain 对象，用于记录当前使用的 Router 对象集合，也就是后面课时要介绍的路由规则。</p>
<p>AbstractDirectory 对 list() 方法的实现也比较简单，就是直接委托给了 doList() 方法，doList() 是个抽象方法，由 AbstractDirectory 的子类具体实现。</p>
<p><strong>Directory 接口有 RegistryDirectory 和 StaticDirectory 两个具体实现</strong>，如下图所示：</p>
<p><img src="assets/Ciqc1F-qN_-AMVHmAAA3C6TAxsA315.png" alt="Drawing 2.png" /></p>
<p>Directory 接口继承关系图</p>
<p>其中，<strong>RegistryDirectory 实现</strong>中维护的 Invoker 集合会随着注册中心中维护的注册信息<strong>动态</strong>发生变化，这就依赖了 ZooKeeper 等注册中心的推送能力；<strong>StaticDirectory 实现</strong>中维护的 Invoker 集合则是<strong>静态</strong>的，在 StaticDirectory 对象创建完成之后，不会再发生变化。</p>
<p>下面我们就来分别介绍 Directory 接口的这两个具体实现。</p>
<h4>1. StaticDirectory</h4>
<p>StaticDirectory 这个 Directory 实现比较简单，在构造方法中，StaticDirectory 会接收一个 Invoker 集合，并赋值到自身的 invokers 字段中，作为底层的 Invoker 集合。在 doList() 方法中，StaticDirectory 会使用 RouterChain 中的 Router 从 invokers 集合中过滤出符合路由规则的 Invoker 对象集合，具体实现如下：</p>
<pre><code>protected List&lt;Invoker&lt;T&gt;&gt; doList(Invocation invocation) throws RpcException {

    List&lt;Invoker&lt;T&gt;&gt; finalInvokers = invokers;

    if (routerChain != null) { // 通过RouterChain过滤出符合条件的Invoker集合

        finalInvokers = routerChain.route(getConsumerUrl(), invocation);

    }

    return finalInvokers == null ? Collections.emptyList() : finalInvokers;

}
</code></pre>
<p>在创建 StaticDirectory 对象的时候，如果没有传入 RouterChain 对象，则会根据 URL 构造一个包含内置 Router 的 RouterChain 对象：</p>
<pre><code>public void buildRouterChain() {

    RouterChain&lt;T&gt; routerChain = RouterChain.buildChain(getUrl()); // 创建内置Router集合

    // 将invokers与RouterChain关联

    routerChain.setInvokers(invokers);

    this.setRouterChain(routerChain); // 设置routerChain字段

}
</code></pre>
<h4>2. RegistryDirectory</h4>
<p>RegistryDirectory 是一个动态的 Directory 实现，<strong>实现了 NotifyListener 接口</strong>，当注册中心的服务配置发生变化时，RegistryDirectory 会收到变更通知，然后RegistryDirectory 会根据注册中心推送的通知，动态增删底层 Invoker 集合。</p>
<p>下面我们先来看一下 RegistryDirectory 中的核心字段。</p>
<ul>
<li>cluster（Cluster 类型）：集群策略适配器，这里通过 Dubbo SPI 方式（即 ExtensionLoader.getAdaptiveExtension() 方法）动态创建适配器实例。</li>
<li>routerFactory（RouterFactory 类型）：路由工厂适配器，也是通过 Dubbo SPI 动态创建的适配器实例。routerFactory 字段和 cluster 字段都是静态字段，多个 RegistryDirectory 对象通用。</li>
<li>serviceKey（String 类型）：服务对应的 ServiceKey，默认是 {interface}:[group]:[version] 三部分构成。</li>
<li>serviceType（Class 类型）：服务接口类型，例如，org.apache.dubbo.demo.DemoService。</li>
<li>queryMap（Map&lt;String, String&gt; 类型）：Consumer URL 中 refer 参数解析后得到的全部 KV。</li>
<li>directoryUrl（URL 类型）：只保留 Consumer 属性的 URL，也就是由 queryMap 集合重新生成的 URL。</li>
<li>multiGroup（boolean类型）：是否引用多个服务组。</li>
<li>protocol（Protocol 类型）：使用的 Protocol 实现。</li>
<li>registry（Registry 类型）：使用的注册中心实现。</li>
<li>invokers（volatile List<Invoker> 类型）：动态更新的 Invoker 集合。</li>
<li>urlInvokerMap（volatile Map&lt; String, Invoker&gt; 类型）：Provider URL 与对应 Invoker 之间的映射，该集合会与 invokers 字段同时动态更新。</li>
<li>cachedInvokerUrls（volatile Set类型）：当前缓存的所有 Provider 的 URL，该集合会与 invokers 字段同时动态更新。</li>
<li>configurators（volatile List&lt; Configurator&gt;类型）：动态更新的配置信息，配置的具体内容在后面的分析中会介绍到。</li>
</ul>
<p>在 RegistryDirectory 的构造方法中，会<strong>根据传入的注册中心 URL 初始化上述核心字段</strong>，具体实现如下：</p>
<pre><code>public RegistryDirectory(Class&lt;T&gt; serviceType, URL url) {

   // 传入的url参数是注册中心的URL，例如，zookeeper://127.0.0.1:2181/org.apache.dubbo.registry.RegistryService?...，其中refer参数包含了Consumer信息，例如，refer=application=dubbo-demo-api-consumer&amp;dubbo=2.0.2&amp;interface=org.apache.dubbo.demo.DemoService&amp;pid=13423&amp;register.ip=192.168.124.3&amp;side=consumer(URLDecode之后的值)

    super(url); 

    shouldRegister = !ANY_VALUE.equals(url.getServiceInterface()) &amp;&amp; url.getParameter(REGISTER_KEY, true);

    shouldSimplified = url.getParameter(SIMPLIFIED_KEY, false);

    this.serviceType = serviceType;

    this.serviceKey = url.getServiceKey();

    // 解析refer参数值，得到其中Consumer的属性信息

    this.queryMap = StringUtils.parseQueryString(url.getParameterAndDecoded(REFER_KEY));

    // 将queryMap中的KV作为参数，重新构造URL，其中的protocol和path部分不变

    this.overrideDirectoryUrl = this.directoryUrl = turnRegistryUrlToConsumerUrl(url);

    String group = directoryUrl.getParameter(GROUP_KEY, &quot;&quot;);

    this.multiGroup = group != null &amp;&amp; (ANY_VALUE.equals(group) || group.contains(&quot;,&quot;));

}
</code></pre>
<p>在完成初始化之后，我们来看 subscribe() 方法，该方法会在 Consumer 进行订阅的时候被调用，其中调用 Registry 的 subscribe() 完成订阅操作，同时还会将当前 RegistryDirectory 对象作为 NotifyListener 监听器添加到 Registry 中，具体实现如下：</p>
<pre><code>public void subscribe(URL url) {

    setConsumerUrl(url);

    // 将当前RegistryDirectory对象作为ConfigurationListener记录到CONSUMER_CONFIGURATION_LISTENER中

    CONSUMER_CONFIGURATION_LISTENER.addNotifyListener(this);

    serviceConfigurationListener = new ReferenceConfigurationListener(this, url);

    // 完成订阅操作，注册中心的相关操作在前文已经介绍过了，这里不再重复

    registry.subscribe(url, this);

}
</code></pre>
<p>我们看到除了作为 NotifyListener 监听器之外，RegistryDirectory 内部还有两个 ConfigurationListener 的内部类（继承关系如下图所示），为了保持连贯，这两个监听器的具体原理我们在后面的课时中会详细介绍，这里先不展开讲述。</p>
<p><img src="assets/CgqCHl-qOBmAbzKkAABZPyC5mIA963.png" alt="Drawing 3.png" /></p>
<p>RegistryDirectory 内部的 ConfigurationListener 实现</p>
<p>通过前面对 Registry 的介绍我们知道，在注册 NotifyListener 的时候，监听的是 providers、configurators 和 routers 三个目录，所以在这三个目录下发生变化的时候，就会触发 RegistryDirectory 的 notify() 方法。</p>
<p>在 RegistryDirectory.notify() 方法中，首先会按照 category 对发生变化的 URL 进行分类，分成 configurators、routers、providers 三类，并分别对不同类型的 URL 进行处理：</p>
<ul>
<li>将 configurators 类型的 URL 转化为 Configurator，保存到 configurators 字段中；</li>
<li>将 router 类型的 URL 转化为 Router，并通过 routerChain.addRouters() 方法添加 routerChain 中保存；</li>
<li>将 provider 类型的 URL 转化为 Invoker 对象，并记录到 invokers 集合和 urlInvokerMap 集合中。</li>
</ul>
<p>notify() 方法的具体实现如下：</p>
<pre><code>public synchronized void notify(List&lt;URL&gt; urls) {

    // 按照category进行分类，分成configurators、routers、providers三类

    Map&lt;String, List&lt;URL&gt;&gt; categoryUrls = urls.stream()

            .filter(Objects::nonNull)

            .filter(this::isValidCategory)

            .filter(this::isNotCompatibleFor26x)

            .collect(Collectors.groupingBy(this::judgeCategory));

    // 获取configurators类型的URL，并转换成Configurator对象

    List&lt;URL&gt; configuratorURLs = categoryUrls.getOrDefault(CONFIGURATORS_CATEGORY, Collections.emptyList());

    this.configurators = Configurator.toConfigurators(configuratorURLs).orElse(this.configurators);

    // 获取routers类型的URL，并转成Router对象，添加到RouterChain中

    List&lt;URL&gt; routerURLs = categoryUrls.getOrDefault(ROUTERS_CATEGORY, Collections.emptyList());

    toRouters(routerURLs).ifPresent(this::addRouters);

    // 获取providers类型的URL，调用refreshOverrideAndInvoker()方法进行处理

    List&lt;URL&gt; providerURLs = categoryUrls.getOrDefault(PROVIDERS_CATEGORY, Collections.emptyList());

    ... // 在Dubbo3.0中会触发AddressListener监听器，但是现在AddressListener接口还没有实现，所以省略这段代码

    refreshOverrideAndInvoker(providerURLs);

}
</code></pre>
<p>我们这里首先来专注<strong>providers 类型 URL 的处理</strong>，具体实现位置在 refreshInvoker() 方法中，具体实现如下：</p>
<pre><code>private void refreshInvoker(List&lt;URL&gt; invokerUrls) {

    // 如果invokerUrls集合不为空，长度为1，并且协议为empty，则表示该服务的所有Provider都下线了，会销毁当前所有Provider对应的Invoker。

    if (invokerUrls.size() == 1 &amp;&amp; invokerUrls.get(0) != null

            &amp;&amp; EMPTY_PROTOCOL.equals(invokerUrls.get(0).getProtocol())) {

        this.forbidden = true; // forbidden标记设置为true，后续请求将直接抛出异常

        this.invokers = Collections.emptyList();

        routerChain.setInvokers(this.invokers); // 清空RouterChain中的Invoker集合

        destroyAllInvokers(); // 关闭所有Invoker对象

    } else {

        this.forbidden = false; // forbidden标记设置为false，RegistryDirectory可以正常处理后续请求

        Map&lt;String, Invoker&lt;T&gt;&gt; oldUrlInvokerMap = this.urlInvokerMap; // 保存本地引用

        if (invokerUrls == Collections.&lt;URL&gt;emptyList()) {

            invokerUrls = new ArrayList&lt;&gt;();

        }

        if (invokerUrls.isEmpty() &amp;&amp; this.cachedInvokerUrls != null) {

            // 如果invokerUrls集合为空，并且cachedInvokerUrls不为空，则将使用cachedInvokerUrls缓存的数据，

            // 也就是说注册中心中的providers目录未发生变化，invokerUrls则为空，表示cachedInvokerUrls集合中缓存的URL为最新的值

            invokerUrls.addAll(this.cachedInvokerUrls);

        } else {

            // 如果invokerUrls集合不为空，则用invokerUrls集合更新cachedInvokerUrls集合

            // 也就是说，providers发生变化，invokerUrls集合中会包含此时注册中心所有的服务提供者

            this.cachedInvokerUrls = new HashSet&lt;&gt;();

            this.cachedInvokerUrls.addAll(invokerUrls);//Cached invoker urls, convenient for comparison

        }

        if (invokerUrls.isEmpty()) { 

            return; // 如果invokerUrls集合为空，即providers目录未发生变更，则无须处理，结束本次更新服务提供者Invoker操作。

        }

        // 将invokerUrls转换为对应的Invoker映射关系

        Map&lt;String, Invoker&lt;T&gt;&gt; newUrlInvokerMap = toInvokers(invokerUrls);

        if (CollectionUtils.isEmptyMap(newUrlInvokerMap)) {

            return;

        }

        // 更新invokers字段和urlInvokerMap集合

        List&lt;Invoker&lt;T&gt;&gt; newInvokers = Collections.unmodifiableList(new ArrayList&lt;&gt;(newUrlInvokerMap.values()));

        routerChain.setInvokers(newInvokers);

        // 针对multiGroup的特殊处理，合并多个group的Invoker

        this.invokers = multiGroup ? toMergeInvokerList(newInvokers) : newInvokers;

        this.urlInvokerMap = newUrlInvokerMap;

        // 比较新旧两组Invoker集合，销毁掉已经下线的Invoker

        destroyUnusedInvokers(oldUrlInvokerMap, newUrlInvokerMap);

    }

}
</code></pre>
<p>通过对 refreshInvoker() 方法的介绍，我们可以看出，其<strong>最核心的逻辑是 Provider URL 转换成 Invoker 对象，也就是 toInvokers() 方法</strong>。下面我们就来深入 toInvokers() 方法内部，看看其具体的转换逻辑：</p>
<pre><code>private Map&lt;String, Invoker&lt;T&gt;&gt; toInvokers(List&lt;URL&gt; urls) {

    ... // urls集合为空时，直接返回空Map

    Set&lt;String&gt; keys = new HashSet&lt;&gt;();

    String queryProtocols = this.queryMap.get(PROTOCOL_KEY); // 获取Consumer端支持的协议，即protocol参数指定的协议

    for (URL providerUrl : urls) {

        if (queryProtocols != null &amp;&amp; queryProtocols.length() &gt; 0) {

            boolean accept = false;

            String[] acceptProtocols = queryProtocols.split(&quot;,&quot;);

            for (String acceptProtocol : acceptProtocols) { // 遍历所有Consumer端支持的协议

                if (providerUrl.getProtocol().equals(acceptProtocol)) {

                    accept = true;

                    break;

                }

            }

            if (!accept) {

                continue; // 如果当前URL不支持Consumer端的协议，也就无法执行后续转换成Invoker的逻辑

            }

        }

        if (EMPTY_PROTOCOL.equals(providerUrl.getProtocol())) {

            continue; // 跳过empty协议的URL

        }

        // 如果Consumer端不支持该URL的协议（这里通过SPI方式检测是否有对应的Protocol扩展实现），也会跳过该URL

        if (!ExtensionLoader.getExtensionLoader(Protocol.class).hasExtension(providerUrl.getProtocol())) {

            logger.error(&quot;...&quot;);

            continue;

        }

        // 合并URL参数，这个合并过程，在本课时后面展开介绍

        URL url = mergeUrl(providerUrl);

        // 获取完整URL对应的字符串，也就是在urlInvokerMap集合中的key

        String key = url.toFullString();

        if (keys.contains(key)) { // 跳过重复的URL

            continue;

        }

        keys.add(key); // 记录key

        // 匹配urlInvokerMap缓存中的Invoker对象，如果命中缓存，直接将Invoker添加到newUrlInvokerMap这个新集合中即可；

        // 如果未命中缓存，则创建新的Invoker对象，然后添加到newUrlInvokerMap这个新集合中

        Map&lt;String, Invoker&lt;T&gt;&gt; localUrlInvokerMap = this.urlInvokerMap;

        Invoker&lt;T&gt; invoker = localUrlInvokerMap == null ? null : localUrlInvokerMap.get(key);

        if (invoker == null) {

            try {

                boolean enabled = true;

                if (url.hasParameter(DISABLED_KEY)) { // 检测URL中的disable和enable参数，决定是否能够创建Invoker对象

                    enabled = !url.getParameter(DISABLED_KEY, false);

                } else {

                    enabled = url.getParameter(ENABLED_KEY, true);

                }

                if (enabled) { // 这里通过Protocol.refer()方法创建对应的Invoker对象

                    invoker = new InvokerDelegate&lt;&gt;(protocol.refer(serviceType, url), url, providerUrl);

                }

            } catch (Throwable t) {

                logger.error(&quot;Failed to refer invoker for interface:&quot; + serviceType + &quot;,url:(&quot; + url + &quot;)&quot; + t.getMessage(), t);

            }

            if (invoker != null) { // 将key和Invoker对象之间的映射关系记录到newUrlInvokerMap中

                newUrlInvokerMap.put(key, invoker);

            }

        } else {// 缓存命中，直接将urlInvokerMap中的Invoker转移到newUrlInvokerMap即可

            newUrlInvokerMap.put(key, invoker);

        }

    }

    keys.clear();

    return newUrlInvokerMap;

}
</code></pre>
<p><strong>toInvokers() 方法的代码虽然有点长，但核心逻辑就是调用 Protocol.refer() 方法创建 Invoker 对象，其他的逻辑都是在判断是否调用该方法。</strong></p>
<p>在 toInvokers() 方法内部，我们可以看到<strong>调用了 mergeUrl() 方法对 URL 参数进行合并</strong>。在 mergeUrl() 方法中，会将注册中心中 configurators 目录下的 URL（override 协议），以及服务治理控制台动态添加的配置与 Provider URL 进行合并，即覆盖 Provider URL 原有的一些信息，具体实现如下：</p>
<pre><code>private URL mergeUrl(URL providerUrl) {

    // 首先，移除Provider URL中只在Provider端生效的属性，例如，threadname、threadpool、corethreads、threads、queues等参数。

    // 然后，用Consumer端的配置覆盖Provider URL的相应配置，其中，version、group、methods、timestamp等参数以Provider端的配置优先

    // 最后，合并Provider端和Consumer端配置的Filter以及Listener

    providerUrl = ClusterUtils.mergeUrl(providerUrl, queryMap); 

    // 合并configurators类型的URL，configurators类型的URL又分为三类：

    // 第一类是注册中心Configurators目录下新增的URL(override协议)

    // 第二类是通过ConsumerConfigurationListener监听器(监听应用级别的配置)得到的动态配置

    // 第三类是通过ReferenceConfigurationListener监听器(监听服务级别的配置)得到的动态配置

    // 这里只需要先了解：除了注册中心的configurators目录下有配置信息之外，还有可以在服务治理控制台动态添加配置，

    // ConsumerConfigurationListener、ReferenceConfigurationListener监听器就是用来监听服务治理控制台的动态配置的

    // 至于服务治理控制台的具体使用，在后面详细介绍

    providerUrl = overrideWithConfigurator(providerUrl);

    // 增加check=false，即只有在调用时，才检查Provider是否可用

    providerUrl = providerUrl.addParameter(Constants.CHECK_KEY, String.valueOf(false));

    // 重新复制overrideDirectoryUrl，providerUrl在经过第一步参数合并后（包含override协议覆盖后的属性）赋值给overrideDirectoryUrl。

    this.overrideDirectoryUrl = this.overrideDirectoryUrl.addParametersIfAbsent(providerUrl.getParameters()); 

    ... // 省略对Dubbo低版本的兼容处理逻辑

    return providerUrl;

}
</code></pre>
<p>完成 URL 到 Invoker 对象的转换（toInvokers() 方法）之后，其实在 refreshInvoker() 方法的最后，还会<strong>根据 multiGroup 的配置决定是否调用 toMergeInvokerList() 方法将每个 group 中的 Invoker 合并成一个 Invoker</strong>。下面我们一起来看 toMergeInvokerList() 方法的具体实现：</p>
<pre><code>private List&lt;Invoker&lt;T&gt;&gt; toMergeInvokerList(List&lt;Invoker&lt;T&gt;&gt; invokers) {

    List&lt;Invoker&lt;T&gt;&gt; mergedInvokers = new ArrayList&lt;&gt;();

    Map&lt;String, List&lt;Invoker&lt;T&gt;&gt;&gt; groupMap = new HashMap&lt;&gt;();

    for (Invoker&lt;T&gt; invoker : invokers) { // 按照group将Invoker分组

        String group = invoker.getUrl().getParameter(GROUP_KEY, &quot;&quot;);

        groupMap.computeIfAbsent(group, k -&gt; new ArrayList&lt;&gt;());

        groupMap.get(group).add(invoker);

    }

    if (groupMap.size() == 1) { // 如果只有一个group，则直接使用该group分组对应的Invoker集合作为mergedInvokers

        mergedInvokers.addAll(groupMap.values().iterator().next());

    } else if (groupMap.size() &gt; 1) { // 将每个group对应的Invoker集合合并成一个Invoker

        for (List&lt;Invoker&lt;T&gt;&gt; groupList : groupMap.values()) {

            // 这里使用到StaticDirectory以及Cluster合并每个group中的Invoker

            StaticDirectory&lt;T&gt; staticDirectory = new StaticDirectory&lt;&gt;(groupList);

            staticDirectory.buildRouterChain();

            mergedInvokers.add(CLUSTER.join(staticDirectory));

        }

    } else {

        mergedInvokers = invokers;

    }

    return mergedInvokers;

}
</code></pre>
<p>这里使用到了 Cluster 接口的相关功能，我们在后面课时还会继续深入分析 Cluster 接口及其实现，你现在可以将 Cluster 理解为一个黑盒，知道其 join() 方法会将多个 Invoker 对象转换成一个 Invoker 对象即可。</p>
<p>到此为止，RegistryDirectory 处理一次完整的动态 Provider 发现流程就介绍完了。</p>
<p>最后，我们再分析下<strong>RegistryDirectory 中另外一个核心方法—— doList() 方法</strong>，该方法是 AbstractDirectory 留给其子类实现的一个方法，也是通过 Directory 接口获取 Invoker 集合的核心所在，具体实现如下：</p>
<pre><code>public List&lt;Invoker&lt;T&gt;&gt; doList(Invocation invocation) {

    if (forbidden) { // 检测forbidden字段，当该字段在refreshInvoker()过程中设置为true时，表示无Provider可用，直接抛出异常

        throw new RpcException(&quot;...&quot;);

    }

    if (multiGroup) {

        // multiGroup为true时的特殊处理，在refreshInvoker()方法中针对multiGroup为true的场景，已经使用Router进行了筛选，所以这里直接返回接口

        return this.invokers == null ? Collections.emptyList() : this.invokers;

    }

    List&lt;Invoker&lt;T&gt;&gt; invokers = null;

    // 通过RouterChain.route()方法筛选Invoker集合，最终得到符合路由条件的Invoker集合

    invokers = routerChain.route(getConsumerUrl(), invocation);

    return invokers == null ? Collections.emptyList() : invokers;

}
</code></pre>
<h3>总结</h3>
<p>在本课时，我们首先介绍了 dubbo-cluster 模块的整体架构，简单说明了 Cluster、Directory、Router、LoadBalance 四个核心接口的功能。接下来我们就深入介绍了 Directory 接口的定义以及 StaticDirectory、RegistryDirectory 两个类的核心实现，其中 RegistryDirectory 涉及动态查找 Provider URL 以及处理动态配置的相关逻辑，显得略微复杂了一点，希望你能耐心学习和理解。关于这部分内容，你若有不懂或不理解的地方，也欢迎你留言和我交流。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="30&#32;&#32;Filter&#32;接口，扩展&#32;Dubbo&#32;框架的常用手段指北.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="32&#32;&#32;路由机制：请求到底怎么走，它说了算（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f977c6a70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Dubbo%E6%BA%90%E7%A0%81%E8%A7%A3%E8%AF%BB%E4%B8%8E%E5%AE%9E%E6%88%98-%E5%AE%8C/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
