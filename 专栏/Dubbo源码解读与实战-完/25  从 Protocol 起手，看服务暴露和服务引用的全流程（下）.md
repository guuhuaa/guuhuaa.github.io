<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>25  从 Protocol 起手，看服务暴露和服务引用的全流程（下）.md</title>
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

                    <a class="current-tab" href="25&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（下）.md">25  从 Protocol 起手，看服务暴露和服务引用的全流程（下）.md</a>
                    

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

                    
                    <a href="31&#32;&#32;加餐：深潜&#32;Directory&#32;实现，探秘服务目录玄机.md">31  加餐：深潜 Directory 实现，探秘服务目录玄机.md</a>

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
                        <div><h1>25  从 Protocol 起手，看服务暴露和服务引用的全流程（下）</h1>
<p>在上一课时，我们以 DubboProtocol 实现为基础，详细介绍了 Dubbo 服务发布的核心流程。在本课时，我们继续介绍 DubboProtocol 中<strong>服务引用</strong>相关的实现。</p>
<h3>refer 流程</h3>
<p>下面我们开始介绍 DubboProtocol 中引用服务的相关实现，其核心实现在 protocolBindingRefer() 方法中：</p>
<pre><code>public &lt;T&gt; Invoker&lt;T&gt; protocolBindingRefer(Class&lt;T&gt; serviceType, URL url) throws RpcException {

    optimizeSerialization(url); // 进行序列化优化，注册需要优化的类

    // 创建DubboInvoker对象

    DubboInvoker&lt;T&gt; invoker = new DubboInvoker&lt;T&gt;(serviceType, url, getClients(url), invokers);

    // 将上面创建DubboInvoker对象添加到invoker集合之中

    invokers.add(invoker); 

    return invoker;

}
</code></pre>
<p>关于 DubboInvoker 的具体实现，我们先暂时不做深入分析。这里我们需要先关注的是<strong>getClients() 方法</strong>，它创建了底层发送请求和接收响应的 Client 集合，其核心分为了两个部分，一个是针对<strong>共享连接</strong>的处理，另一个是针对<strong>独享连接</strong>的处理，具体实现如下：</p>
<pre><code>private ExchangeClient[] getClients(URL url) {

    // 是否使用共享连接

    boolean useShareConnect = false;

    // CONNECTIONS_KEY参数值决定了后续建立连接的数量

    int connections = url.getParameter(CONNECTIONS_KEY, 0);

    List&lt;ReferenceCountExchangeClient&gt; shareClients = null;

    if (connections == 0) { // 如果没有连接数的相关配置，默认使用共享连接的方式

        useShareConnect = true;

        // 确定建立共享连接的条数，默认只建立一条共享连接

        String shareConnectionsStr = url.getParameter(SHARE_CONNECTIONS_KEY, (String) null);

        connections = Integer.parseInt(StringUtils.isBlank(shareConnectionsStr) ? ConfigUtils.getProperty(SHARE_CONNECTIONS_KEY,

                DEFAULT_SHARE_CONNECTIONS) : shareConnectionsStr);

        // 创建公共ExchangeClient集合

        shareClients = getSharedClient(url, connections);

    }

    // 整理要返回的ExchangeClient集合

    ExchangeClient[] clients = new ExchangeClient[connections];

    for (int i = 0; i &lt; clients.length; i++) {

        if (useShareConnect) {

            clients[i] = shareClients.get(i);

        } else {

            // 不使用公共连接的情况下，会创建单独的ExchangeClient实例

            clients[i] = initClient(url);

        }

    }

    return clients;

}
</code></pre>
<p>当使用独享连接的时候，对每个 Service 建立固定数量的 Client，每个 Client 维护一个底层连接。如下图所示，就是针对每个 Service 都启动了两个独享连接：</p>
<p><img src="assets/CgqCHl-OqnqAD_WFAAGYtk5Nou4688.png" alt="Lark20201020-171207.png" /></p>
<p>Service 独享连接示意图</p>
<p>当使用共享连接的时候，会区分不同的网络地址（host:port），一个地址只建立固定数量的共享连接。如下图所示，Provider 1 暴露了多个服务，Consumer 引用了 Provider 1 中的多个服务，共享连接是说 Consumer 调用 Provider 1 中的多个服务时，是通过固定数量的共享 TCP 长连接进行数据传输，这样就可以达到减少服务端连接数的目的。</p>
<p><img src="assets/Ciqc1F-OqoOAHURKAAF2m0HX5qU972.png" alt="Lark20201020-171159.png" /></p>
<p>Service 共享连接示意图</p>
<p>那怎么去创建共享连接呢？<strong>创建共享连接的实现细节是在 getSharedClient() 方法中</strong>，它首先从 referenceClientMap 缓存（Map&lt;String, List<code>&lt;ReferenceCountExchangeClient&gt;</code>&gt; 类型）中查询 Key（host 和 port 拼接成的字符串）对应的共享 Client 集合，如果查找到的 Client 集合全部可用，则直接使用这些缓存的 Client，否则要创建新的 Client 来补充替换缓存中不可用的 Client。示例代码如下：</p>
<pre><code>private List&lt;ReferenceCountExchangeClient&gt; getSharedClient(URL url, int connectNum) {

    String key = url.getAddress(); // 获取对端的地址(host:port)

    // 从referenceClientMap集合中，获取与该地址连接的ReferenceCountExchangeClient集合

    List&lt;ReferenceCountExchangeClient&gt; clients = referenceClientMap.get(key);

    // checkClientCanUse()方法中会检测clients集合中的客户端是否全部可用

    if (checkClientCanUse(clients)) { 

        batchClientRefIncr(clients); // 客户端全部可用时

        return clients;

    }

    locks.putIfAbsent(key, new Object());

    synchronized (locks.get(key)) { // 针对指定地址的客户端进行加锁，分区加锁可以提高并发度

        clients = referenceClientMap.get(key);

        if (checkClientCanUse(clients)) { // double check，再次检测客户端是否全部可用

            batchClientRefIncr(clients); // 增加应用Client的次数

            return clients;

        }

        connectNum = Math.max(connectNum, 1); // 至少一个共享连接

        // 如果当前Clients集合为空，则直接通过initClient()方法初始化所有共享客户端

        if (CollectionUtils.isEmpty(clients)) {

            clients = buildReferenceCountExchangeClientList(url, connectNum);

            referenceClientMap.put(key, clients);

        } else { // 如果只有部分共享客户端不可用，则只需要处理这些不可用的客户端

            for (int i = 0; i &lt; clients.size(); i++) {

                ReferenceCountExchangeClient referenceCountExchangeClient = clients.get(i);

                if (referenceCountExchangeClient == null || referenceCountExchangeClient.isClosed()) {

                    clients.set(i, buildReferenceCountExchangeClient(url));

                    continue;

                }

                // 增加引用

                referenceCountExchangeClient.incrementAndGetCount();

            }

        }

        // 清理locks集合中的锁对象，防止内存泄漏，如果key对应的服务宕机或是下线，

        // 这里不进行清理的话，这个用于加锁的Object对象是无法被GC的，从而出现内存泄漏

        locks.remove(key); 

        return clients;

    }

}
</code></pre>
<p>这里使用的 ExchangeClient 实现是 ReferenceCountExchangeClient，它是 ExchangeClient 的一个装饰器，在原始 ExchangeClient 对象基础上添加了引用计数的功能。</p>
<p>ReferenceCountExchangeClient 中除了持有被修饰的 ExchangeClient 对象外，还有一个 referenceCount 字段（AtomicInteger 类型），用于记录该 Client 被应用的次数。从下图中我们可以看到，在 ReferenceCountExchangeClient 的构造方法以及 incrementAndGetCount() 方法中会增加引用次数，在 close() 方法中则会减少引用次数。</p>
<p><img src="assets/Ciqc1F-OqqeAHAStAAF3BXy1LnA608.png" alt="Drawing 2.png" /></p>
<p>referenceCount 修改调用栈</p>
<p>这样，对于同一个地址的共享连接，就可以满足两个基本需求：</p>
<ol>
<li>当引用次数减到 0 的时候，ExchangeClient 连接关闭；</li>
<li>当引用次数未减到 0 的时候，底层的 ExchangeClient 不能关闭。</li>
</ol>
<p>还有一个需要注意的细节是 ReferenceCountExchangeClient.close() 方法，在关闭底层 ExchangeClient 对象之后，会立即创建一个 LazyConnectExchangeClient ，也有人称其为“幽灵连接”。具体逻辑如下所示，这里的 LazyConnectExchangeClient 主要用于异常情况的兜底：</p>
<pre><code>public void close(int timeout) {

    // 引用次数减到0，关闭底层的ExchangeClient，具体操作有：停掉心跳任务、重连任务以及关闭底层Channel，这些在前文介绍HeaderExchangeClient的时候已经详细分析过了，这里不再赘述

    if (referenceCount.decrementAndGet() &lt;= 0) { 

        if (timeout == 0) {

            client.close();

        } else {

            client.close(timeout);

        } 

        // 创建LazyConnectExchangeClient，并将client字段指向该对象

        replaceWithLazyClient(); 

    }

}

private void replaceWithLazyClient() {

    // 在原有的URL之上，添加一些LazyConnectExchangeClient特有的参数

    URL lazyUrl = URLBuilder.from(url)

            .addParameter(LAZY_CONNECT_INITIAL_STATE_KEY, Boolean.TRUE)

            .addParameter(RECONNECT_KEY, Boolean.FALSE)

            .addParameter(SEND_RECONNECT_KEY, Boolean.TRUE.toString())

            .addParameter(&quot;warning&quot;, Boolean.TRUE.toString())

            .addParameter(LazyConnectExchangeClient.REQUEST_WITH_WARNING_KEY, true)

            .addParameter(&quot;_client_memo&quot;, &quot;referencecounthandler.replacewithlazyclient&quot;)

            .build();

    // 如果当前client字段已经指向了LazyConnectExchangeClient，则不需要再次创建LazyConnectExchangeClient兜底了

    if (!(client instanceof LazyConnectExchangeClient) || client.isClosed()) {

        // ChannelHandler依旧使用原始ExchangeClient使用的Handler，即DubboProtocol中的requestHandler字段

        client = new LazyConnectExchangeClient(lazyUrl, client.getExchangeHandler());

    }

}
</code></pre>
<p>LazyConnectExchangeClient 也是 ExchangeClient 的装饰器，它会在原有 ExchangeClient 对象的基础上添加懒加载的功能。LazyConnectExchangeClient 在构造方法中不会创建底层持有连接的 Client，而是在需要发送请求的时候，才会调用 initClient() 方法进行 Client 的创建，如下图调用关系所示：</p>
<p><img src="assets/CgqCHl-OqrqAHcvUAAC9KpqKEBQ887.png" alt="Drawing 3.png" /></p>
<p>initClient() 方法的调用位置</p>
<p>initClient() 方法的具体实现如下：</p>
<pre><code>private void initClient() throws RemotingException {

    if (client != null) { // 底层Client已经初始化过了，这里不再初始化

        return;

    }

    connectLock.lock();

    try {

        if (client != null) { return; } // double check

        // 通过Exchangers门面类，创建ExchangeClient对象

        this.client = Exchangers.connect(url, requestHandler);

    } finally {

        connectLock.unlock();

    }

}
</code></pre>
<p>在这些发送请求的方法中，除了通过 initClient() 方法初始化底层 ExchangeClient 外，还会调用warning() 方法，其会根据当前 URL 携带的参数决定是否打印 WARN 级别日志。为了防止瞬间打印大量日志的情况发生，这里有打印的频率限制，默认每发送 5000 次请求打印 1 条日志。你可以看到在前面展示的兜底场景中，我们就开启了打印日志的选项。</p>
<p><strong>分析完 getSharedClient() 方法创建共享 Client 的核心流程之后，我们回到 DubboProtocol 中，继续介绍创建独享 Client 的流程。</strong></p>
<p>创建独享 Client 的入口在<strong>DubboProtocol.initClient() 方法</strong>，它首先会在 URL 中设置一些默认的参数，然后根据 LAZY_CONNECT_KEY 参数决定是否使用 LazyConnectExchangeClient 进行封装，实现懒加载功能，如下代码所示：</p>
<pre><code>private ExchangeClient initClient(URL url) {

    // 获取客户端扩展名并进行检查，省略检测的逻辑

    String str = url.getParameter(CLIENT_KEY, url.getParameter(SERVER_KEY, DEFAULT_REMOTING_CLIENT));

    // 设置Codec2的扩展名

    url = url.addParameter(CODEC_KEY, DubboCodec.NAME);

    // 设置默认的心跳间隔

    url = url.addParameterIfAbsent(HEARTBEAT_KEY, String.valueOf(DEFAULT_HEARTBEAT));

    ExchangeClient client;    

    // 如果配置了延迟创建连接的特性，则创建LazyConnectExchangeClient

    if (url.getParameter(LAZY_CONNECT_KEY, false)) {

        client = new LazyConnectExchangeClient(url, requestHandler);

    } else { // 未使用延迟连接功能，则直接创建HeaderExchangeClient

        client = Exchangers.connect(url, requestHandler);

    }

    return client;

}
</code></pre>
<p>这里涉及的 LazyConnectExchangeClient 装饰器以及 Exchangers 门面类在前面已经深入分析过了，就不再赘述了。</p>
<p>DubboProtocol 中还剩下几个方法没有介绍，这里你只需要简单了解一下它们的实现即可。</p>
<ul>
<li>batchClientRefIncr() 方法：会遍历传入的集合，将其中的每个 ReferenceCountExchangeClient 对象的引用加一。</li>
<li>buildReferenceCountExchangeClient() 方法：会调用上面介绍的 initClient() 创建 Client 对象，然后再包装一层 ReferenceCountExchangeClient 进行修饰，最后返回。该方法主要用于创建共享 Client。</li>
</ul>
<h3>destroy方法</h3>
<p>在 DubboProtocol 销毁的时候，会调用 destroy() 方法释放底层资源，其中就涉及 export 流程中创建的 ProtocolServer 对象以及 refer 流程中创建的 Client。</p>
<p>DubboProtocol.destroy() 方法首先会逐个关闭 serverMap 集合中的 ProtocolServer 对象，相关代码片段如下：</p>
<pre><code>for (String key : new ArrayList&lt;&gt;(serverMap.keySet())) {

    ProtocolServer protocolServer = serverMap.remove(key);

    if (protocolServer == null) { continue;}

    RemotingServer server = protocolServer.getRemotingServer();

    // 在close()方法中，发送ReadOnly请求、阻塞指定时间、关闭底层的定时任务、关闭相关线程池，最终，会断开所有连接，关闭Server。这些逻辑在前文介绍HeaderExchangeServer、NettyServer等实现的时候，已经详细分析过了，这里不再展开

    server.close(ConfigurationUtils.getServerShutdownTimeout());

}
</code></pre>
<p>ConfigurationUtils.getServerShutdownTimeout() 方法返回的阻塞时长默认是 10 秒，我们可以通过 dubbo.service.shutdown.wait 或是 dubbo.service.shutdown.wait.seconds 进行配置。</p>
<p>之后，DubboProtocol.destroy() 方法会逐个关闭 referenceClientMap 集合中的 Client，逻辑与上述关闭ProtocolServer的逻辑相同，这里不再重复。只不过需要注意前面我们提到的 ReferenceCountExchangeClient 的存在，只有引用减到 0，底层的 Client 才会真正销毁。</p>
<p>最后，DubboProtocol.destroy() 方法会调用父类 AbstractProtocol 的 destroy() 方法，销毁全部 Invoker 对象，前面已经介绍过 AbstractProtocol.destroy() 方法的实现，这里也不再重复。</p>
<h3>总结</h3>
<p>本课时我们继续上一课时的话题，以 DubboProtocol 为例，介绍了 Dubbo 在 Protocol 层实现服务引用的核心流程。我们首先介绍了 DubboProtocol 初始化 Client 的核心逻辑，分析了共享连接和独立连接的模型，后续还讲解了ReferenceCountExchangeClient、LazyConnectExchangeClient 等装饰器的功能和实现，最后说明了 destroy() 方法释放底层资源的相关实现。</p>
<p>关于 DubboProtocol，你若还有什么疑问或想法，欢迎你留言跟我分享。下一课时，我们将开始深入介绍 Dubbo 的“心脏”—— Invoker 接口的相关实现，这是我们的一篇加餐文章，记得按时来听课。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="24&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="26&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（上）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f738fa570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
