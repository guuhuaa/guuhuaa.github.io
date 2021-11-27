<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19  Transporter 层核心实现：编解码与线程模型一文打尽（上）.md</title>
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

                    <a class="current-tab" href="19&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（上）.md">19  Transporter 层核心实现：编解码与线程模型一文打尽（上）.md</a>
                    

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
                        <div><h1>19  Transporter 层核心实现：编解码与线程模型一文打尽（上）</h1>
<p>在第 17 课时中，我们详细介绍了 dubbo-remoting-api 模块中 Transporter 相关的核心抽象接口，本课时将继续介绍 dubbo-remoting-api 模块的其他内容。这里我们依旧从 Transporter 层的 RemotingServer、Client、Channel、ChannelHandler 等核心接口出发，介绍这些核心接口的实现。</p>
<h3>AbstractPeer 抽象类</h3>
<p>首先，我们来看 AbstractPeer 这个抽象类，它同时实现了 Endpoint 接口和 ChannelHandler 接口，如下图所示，它也是 AbstractChannel、AbstractEndpoint 抽象类的父类。</p>
<p><img src="assets/Ciqc1F9wb8eAHyD_AAFkwn8xp18694.png" alt="Drawing 0.png" /></p>
<p>AbstractPeer 继承关系</p>
<blockquote>
<p>Netty 中也有 ChannelHandler、Channel 等接口，但无特殊说明的情况下，这里的接口指的都是 Dubbo 中定义的接口。如果涉及 Netty 中的接口，会进行特殊说明。</p>
</blockquote>
<p>AbstractPeer 中有四个字段：一个是表示该端点自身的 URL 类型的字段，还有两个 Boolean 类型的字段（closing 和 closed）用来记录当前端点的状态，这三个字段都与 Endpoint 接口相关；第四个字段指向了一个 ChannelHandler 对象，AbstractPeer 对 ChannelHandler 接口的所有实现，都是委托给了这个 ChannelHandler 对象。从上面的继承关系图中，我们可以得出这样一个结论：AbstractChannel、AbstractServer、AbstractClient 都是要关联一个 ChannelHandler 对象的。</p>
<h3>AbstractEndpoint 抽象类</h3>
<p>我们顺着上图的继承关系继续向下看，AbstractEndpoint 继承了 AbstractPeer 这个抽象类。AbstractEndpoint 中维护了一个 Codec2 对象（codec 字段）和两个超时时间（timeout 字段和 connectTimeout 字段），在 AbstractEndpoint 的构造方法中会根据传入的 URL 初始化这三个字段：</p>
<pre><code>public AbstractEndpoint(URL url, ChannelHandler handler) {

    super(url, handler); // 调用父类AbstractPeer的构造方法

    // 根据URL中的codec参数值，确定此处具体的Codec2实现类

    this.codec = getChannelCodec(url);

    // 根据URL中的timeout参数确定timeout字段的值，默认1000

    this.timeout = url.getPositiveParameter(TIMEOUT_KEY,

         DEFAULT_TIMEOUT);

    // 根据URL中的connect.timeout参数确定connectTimeout字段的值，默认3000

    this.connectTimeout = url.getPositiveParameter(

    Constants.CONNECT_TIMEOUT_KEY, Constants.DEFAULT_CONNECT_TIMEOUT);

}
</code></pre>
<p>在[第 17 课时]介绍 Codec2 接口的时候提到它是一个 SPI 扩展点，这里的 AbstractEndpoint.getChannelCodec() 方法就是基于 Dubbo SPI 选择其扩展实现的，具体实现如下：</p>
<pre><code>protected static Codec2 getChannelCodec(URL url) {

    // 根据URL的codec参数获取扩展名

    String codecName = url.getParameter(Constants.CODEC_KEY, &quot;telnet&quot;);

    if (ExtensionLoader.getExtensionLoader(Codec2.class).hasExtension(codecName)) { // 通过ExtensionLoader加载并实例化Codec2的具体扩展实现

        return ExtensionLoader.getExtensionLoader(Codec2.class).getExtension(codecName);

    } else { // Codec2接口不存在相应的扩展名，就尝试从Codec这个老接口的扩展名中查找，目前Codec接口已经废弃了，所以省略这部分逻辑

    }

}
</code></pre>
<p>另外，AbstractEndpoint 还实现了 Resetable 接口（只有一个 reset() 方法需要实现），虽然 AbstractEndpoint 中的 reset() 方法比较长，但是逻辑非常简单，就是根据传入的 URL 参数重置 AbstractEndpoint 的三个字段。下面是重置 codec 字段的代码片段，还是调用 getChannelCodec() 方法实现的：</p>
<pre><code>public void reset(URL url) {

    // 检测当前AbstractEndpoint是否已经关闭(略)

    // 省略重置timeout、connectTimeout两个字段的逻辑

    try {

        if (url.hasParameter(Constants.CODEC_KEY)) {

            this.codec = getChannelCodec(url);

        }

    } catch (Throwable t) {

        logger.error(t.getMessage(), t);

    }

}
</code></pre>
<h3>Server 继承路线分析</h3>
<p>AbstractServer 和 AbstractClient 都实现了 AbstractEndpoint 抽象类，我们先来看 AbstractServer 的实现。AbstractServer 在继承了 AbstractEndpoint 的同时，还实现了 RemotingServer 接口，如下图所示：</p>
<p><img src="assets/Ciqc1F9wb-iAMAgtAACJWi59iSc812.png" alt="Drawing 1.png" /></p>
<p>AbstractServer 继承关系图</p>
<p><strong>AbstractServer 是对服务端的抽象，实现了服务端的公共逻辑</strong>。AbstractServer 的核心字段有下面几个。</p>
<ul>
<li>localAddress、bindAddress（InetSocketAddress 类型）：分别对应该 Server 的本地地址和绑定的地址，都是从 URL 中的参数中获取。bindAddress 默认值与 localAddress 一致。</li>
<li>accepts（int 类型）：该 Server 能接收的最大连接数，从 URL 的 accepts 参数中获取，默认值为 0，表示没有限制。</li>
<li>executorRepository（ExecutorRepository 类型）：负责管理线程池，后面我们会深入介绍 ExecutorRepository 的具体实现。</li>
<li>executor（ExecutorService 类型）：当前 Server 关联的线程池，由上面的 ExecutorRepository 创建并管理。</li>
</ul>
<p>在 AbstractServer 的构造方法中会根据传入的 URL初始化上述字段，并调用 doOpen() 这个抽象方法完成该 Server 的启动，具体实现如下：</p>
<pre><code>public AbstractServer(URL url, ChannelHandler handler) {

    super(url, handler); // 调用父类的构造方法

    // 根据传入的URL初始化localAddress和bindAddress

    localAddress = getUrl().toInetSocketAddress();

    String bindIp = getUrl().getParameter(Constants.BIND_IP_KEY, getUrl().getHost());

    int bindPort = getUrl().getParameter(Constants.BIND_PORT_KEY, getUrl().getPort());

    if (url.getParameter(ANYHOST_KEY, false) || NetUtils.isInvalidLocalHost(bindIp)) {

        bindIp = ANYHOST_VALUE;

    }

    bindAddress = new InetSocketAddress(bindIp, bindPort);

    // 初始化accepts等字段

    this.accepts = url.getParameter(ACCEPTS_KEY, DEFAULT_ACCEPTS);

    this.idleTimeout = url.getParameter(IDLE_TIMEOUT_KEY, DEFAULT_IDLE_TIMEOUT);

    try {

        doOpen(); // 调用doOpen()这个抽象方法，启动该Server

    } catch (Throwable t) {

        throw new RemotingException(&quot;...&quot;);

    }

    // 获取该Server关联的线程池

    executor = executorRepository.createExecutorIfAbsent(url);

}
</code></pre>
<h4>ExecutorRepository</h4>
<p>在继续分析 AbstractServer 的具体实现类之前，我们先来了解一下 ExecutorRepository 这个接口。</p>
<p>ExecutorRepository 负责创建并管理 Dubbo 中的线程池，该接口虽然是个 SPI 扩展点，但是只有一个默认实现—— DefaultExecutorRepository。在该默认实现中维护了一个 ConcurrentMap&lt;String, ConcurrentMap&lt;Integer, ExecutorService&gt;&gt; 集合（data 字段）缓存已有的线程池，第一层 Key 值表示线程池属于 Provider 端还是 Consumer 端，第二层 Key 值表示线程池关联服务的端口。</p>
<p>DefaultExecutorRepository.createExecutorIfAbsent() 方法会根据 URL 参数创建相应的线程池并缓存在合适的位置，具体实现如下：</p>
<pre><code>public synchronized ExecutorService createExecutorIfAbsent(URL url) {

    // 根据URL中的side参数值决定第一层key

    String componentKey = EXECUTOR_SERVICE_COMPONENT_KEY;

    if (CONSUMER_SIDE.equalsIgnoreCase(url.getParameter(SIDE_KEY))) {

        componentKey = CONSUMER_SIDE; 

    }

    Map&lt;Integer, ExecutorService&gt; executors = data.computeIfAbsent(componentKey, k -&gt; new ConcurrentHashMap&lt;&gt;());

    // 根据URL中的port值确定第二层key

    Integer portKey = url.getPort();

    ExecutorService executor = executors.computeIfAbsent(portKey, k -&gt; createExecutor(url));

    // 如果缓存中相应的线程池已关闭，则同样需要调用createExecutor()方法

    // 创建新的线程池，并替换掉缓存中已关闭的线程持，这里省略这段逻辑

    return executor;

}
</code></pre>
<p>在 createExecutor() 方法中，会通过 Dubbo SPI 查找 ThreadPool 接口的扩展实现，并调用其 getExecutor() 方法创建线程池。ThreadPool 接口被 @SPI 注解修饰，默认使用 FixedThreadPool 实现，但是 ThreadPool 接口中的 getExecutor() 方法被 @Adaptive 注解修饰，动态生成的适配器类会优先根据 URL 中的 threadpool 参数选择 ThreadPool 的扩展实现。ThreadPool 接口的实现类如下图所示：</p>
<p><img src="assets/CgqCHl9wcBeAYMZ1AABRTGzl5uY627.png" alt="Drawing 2.png" /></p>
<p>ThreadPool 继承关系图</p>
<p>不同实现会根据 URL 参数创建不同特性的线程池，这里以<strong>CacheThreadPool</strong>为例进行分析：</p>
<pre><code>public Executor getExecutor(URL url) {

    String name = url.getParameter(THREAD_NAME_KEY, DEFAULT_THREAD_NAME);

    // 核心线程数量

    int cores = url.getParameter(CORE_THREADS_KEY, DEFAULT_CORE_THREADS);

    // 最大线程数量

    int threads = url.getParameter(THREADS_KEY, Integer.MAX_VALUE);

    // 缓冲队列的最大长度

    int queues = url.getParameter(QUEUES_KEY, DEFAULT_QUEUES);

    // 非核心线程的最大空闲时长，当非核心线程空闲时间超过该值时，会被回收

    int alive = url.getParameter(ALIVE_KEY, DEFAULT_ALIVE);

    // 下面就是依赖JDK的ThreadPoolExecutor创建指定特性的线程池并返回

    return new ThreadPoolExecutor(cores, threads, alive, TimeUnit.MILLISECONDS,

            queues == 0 ? new SynchronousQueue&lt;Runnable&gt;() :

                    (queues &lt; 0 ? new LinkedBlockingQueue&lt;Runnable&gt;()

                            : new LinkedBlockingQueue&lt;Runnable&gt;(queues)),

            new NamedInternalThreadFactory(name, true), new AbortPolicyWithReport(name, url));

}
</code></pre>
<p>再简单说一下其他 ThreadPool 实现创建的线程池。</p>
<ul>
<li><strong>LimitedThreadPool</strong>：与 CacheThreadPool 一样，可以指定核心线程数、最大线程数以及缓冲队列长度。区别在于，LimitedThreadPool 创建的线程池的非核心线程不会被回收。</li>
<li><strong>FixedThreadPool</strong>：核心线程数和最大线程数一致，且不会被回收。</li>
</ul>
<p>上述三种类型的线程池都是基于 JDK ThreadPoolExecutor 线程池，在核心线程全部被占用的时候，会优先将任务放到缓冲队列中缓存，在缓冲队列满了之后，才会尝试创建新线程来处理任务。</p>
<p>EagerThreadPool 创建的线程池是 EagerThreadPoolExecutor（继承了 JDK 提供的 ThreadPoolExecutor），使用的队列是 TaskQueue（继承了LinkedBlockingQueue）。该线程池与 ThreadPoolExecutor 不同的是：在线程数没有达到最大线程数的前提下，EagerThreadPoolExecutor 会优先创建线程来执行任务，而不是放到缓冲队列中；当线程数达到最大值时，EagerThreadPoolExecutor 会将任务放入缓冲队列，等待空闲线程。</p>
<p>EagerThreadPoolExecutor 覆盖了 ThreadPoolExecutor 中的两个方法：execute() 方法和 afterExecute() 方法，具体实现如下，我们可以看到其中维护了一个 submittedTaskCount 字段（AtomicInteger 类型），用来记录当前在线程池中的任务总数（正在线程中执行的任务数+队列中等待的任务数）。</p>
<pre><code>public void execute(Runnable command) {

    // 任务提交之前，递增submittedTaskCount

    submittedTaskCount.incrementAndGet(); 

    try {

        super.execute(command); // 提交任务

    } catch (RejectedExecutionException rx) {

        final TaskQueue queue = (TaskQueue) super.getQueue();

        try {

            // 任务被拒绝之后，会尝试再次放入队列中缓存，等待空闲线程执行

            if (!queue.retryOffer(command, 0, TimeUnit.MILLISECONDS)) {

                // 再次入队被拒绝，则队列已满，无法执行任务

                // 递减submittedTaskCount

                submittedTaskCount.decrementAndGet();

                throw new RejectedExecutionException(&quot;Queue capacity is full.&quot;, rx);

            }

        } catch (InterruptedException x) {

            // 再次入队列异常，递减submittedTaskCount

            submittedTaskCount.decrementAndGet();

            throw new RejectedExecutionException(x);

        }

    } catch (Throwable t) { // 任务提交异常，递减submittedTaskCount

        submittedTaskCount.decrementAndGet();

        throw t;

    }

}

protected void afterExecute(Runnable r, Throwable t) {

    // 任务指定结束，递减submittedTaskCount

    submittedTaskCount.decrementAndGet(); 

}
</code></pre>
<p>看到这里，你可能会有些疑惑：没有看到优先创建线程执行任务的逻辑啊。其实重点在关联的 TaskQueue 实现中，它覆盖了 LinkedBlockingQueue.offer() 方法，会判断线程池的 submittedTaskCount 值是否已经达到最大线程数，如果未超过，则会返回 false，迫使线程池创建新线程来执行任务。示例代码如下：</p>
<pre><code>public boolean offer(Runnable runnable) {

    // 获取当前线程池中的活跃线程数

    int currentPoolThreadSize = executor.getPoolSize();

    // 当前有线程空闲，直接将任务提交到队列中，空闲线程会直接从中获取任务执行

    if (executor.getSubmittedTaskCount() &lt; currentPoolThreadSize) {

        return super.offer(runnable);

    }

    // 当前没有空闲线程，但是还可以创建新线程，则返回false，迫使线程池创建

    // 新线程来执行任务

    if (currentPoolThreadSize &lt; executor.getMaximumPoolSize()) {

        return false;

    }

    // 当前线程数已经达到上限，只能放到队列中缓存了

    return super.offer(runnable);

}
</code></pre>
<p>线程池最后一个相关的小细节是 AbortPolicyWithReport ，它继承了 ThreadPoolExecutor.AbortPolicy，覆盖的 rejectedExecution 方法中会输出包含线程池相关信息的 WARN 级别日志，然后进行 dumpJStack() 方法，最后才会抛出RejectedExecutionException 异常。</p>
<p>我们回到 Server 的继承线上，下面来看基于 Netty 4 实现的 NettyServer，它继承了前文介绍的 AbstractServer，实现了 doOpen() 方法和 doClose() 方法。这里重点看 doOpen() 方法，如下所示：</p>
<pre><code>protected void doOpen() throws Throwable {

    // 创建ServerBootstrap

    bootstrap = new ServerBootstrap(); 

    // 创建boss EventLoopGroup

    bossGroup = NettyEventLoopFactory.eventLoopGroup(1, &quot;NettyServerBoss&quot;);

    // 创建worker EventLoopGroup

    workerGroup = NettyEventLoopFactory.eventLoopGroup(

            getUrl().getPositiveParameter(IO_THREADS_KEY, Constants.DEFAULT_IO_THREADS),

            &quot;NettyServerWorker&quot;);

    // 创建NettyServerHandler，它是一个Netty中的ChannelHandler实现，

    // 不是Dubbo Remoting层的ChannelHandler接口的实现

    final NettyServerHandler nettyServerHandler = new NettyServerHandler(getUrl(), this);

    // 获取当前NettyServer创建的所有Channel，这里的channels集合中的

    // Channel不是Netty中的Channel对象，而是Dubbo Remoting层的Channel对象

    channels = nettyServerHandler.getChannels();

    // 初始化ServerBootstrap，指定boss和worker EventLoopGroup

    bootstrap.group(bossGroup, workerGroup)

            .channel(NettyEventLoopFactory.serverSocketChannelClass())

            .option(ChannelOption.SO_REUSEADDR, Boolean.TRUE)

            .childOption(ChannelOption.TCP_NODELAY, Boolean.TRUE)

            .childOption(ChannelOption.ALLOCATOR, PooledByteBufAllocator.DEFAULT)

            .childHandler(new ChannelInitializer&lt;SocketChannel&gt;() {

                @Override

                protected void initChannel(SocketChannel ch) throws Exception {

                    // 连接空闲超时时间

                    int idleTimeout = UrlUtils.getIdleTimeout(getUrl());

                    // NettyCodecAdapter中会创建Decoder和Encoder

                    NettyCodecAdapter adapter = new NettyCodecAdapter(getCodec(), getUrl(), NettyServer.this);

                    ch.pipeline()

                            // 注册Decoder和Encoder

                            .addLast(&quot;decoder&quot;, adapter.getDecoder())

                            .addLast(&quot;encoder&quot;, adapter.getEncoder())

                            // 注册IdleStateHandler

                            .addLast(&quot;server-idle-handler&quot;, new IdleStateHandler(0, 0, idleTimeout, MILLISECONDS))

                            // 注册NettyServerHandler

                            .addLast(&quot;handler&quot;, nettyServerHandler);

                }

            });

    // 绑定指定的地址和端口

    ChannelFuture channelFuture = bootstrap.bind(getBindAddress());

    channelFuture.syncUninterruptibly(); // 等待bind操作完成

    channel = channelFuture.channel();

}
</code></pre>
<p>看完 NettyServer 实现的 doOpen() 方法之后，你会发现它和简易版 RPC 框架中启动一个 Netty 的 Server 端基本流程类似：初始化 ServerBootstrap、创建 Boss EventLoopGroup 和 Worker EventLoopGroup、创建 ChannelInitializer 指定如何初始化 Channel 上的 ChannelHandler 等一系列 Netty 使用的标准化流程。</p>
<p>其实在 Transporter 这一层看，功能的不同其实就是注册在 Channel 上的 ChannelHandler 不同，通过 doOpen() 方法得到的 Server 端结构如下：</p>
<p><img src="assets/Ciqc1F9y4LaAIHSsAADBytWDQ3U695.png" alt="5.png" /></p>
<p>NettyServer 模型</p>
<h4>核心 ChannelHandler</h4>
<p>下面我们来逐个看看这四个 ChannelHandler 的核心功能。</p>
<p>首先是<strong>decoder 和 encoder</strong>，它们都是 NettyCodecAdapter 的内部类，如下图所示，分别继承了 Netty 中的 ByteToMessageDecoder 和 MessageToByteEncoder：</p>
<p><img src="assets/CgqCHl9wcESANfPCAABDUdzhtNU066.png" alt="Drawing 4.png" /></p>
<p>还记得 AbstractEndpoint 抽象类中的 codec 字段（Codec2 类型）吗？InternalDecoder 和 InternalEncoder 会将真正的编解码功能委托给 NettyServer 关联的这个 Codec2 对象去处理，这里以 InternalDecoder 为例进行分析：</p>
<pre><code>private class InternalDecoder extends ByteToMessageDecoder {

    protected void decode(ChannelHandlerContext ctx, ByteBuf input, List&lt;Object&gt; out) throws Exception {

        // 将ByteBuf封装成统一的ChannelBuffer

        ChannelBuffer message = new NettyBackedChannelBuffer(input);

        // 拿到关联的Channel

        NettyChannel channel = NettyChannel.getOrAddChannel(ctx.channel(), url, handler);

        do {

            // 记录当前readerIndex的位置

            int saveReaderIndex = message.readerIndex();

            // 委托给Codec2进行解码

            Object msg = codec.decode(channel, message);

            // 当前接收到的数据不足一个消息的长度，会返回NEED_MORE_INPUT，

            // 这里会重置readerIndex，继续等待接收更多的数据

            if (msg == Codec2.DecodeResult.NEED_MORE_INPUT) {

                message.readerIndex(saveReaderIndex);

                break;

            } else {

                if (msg != null) { // 将读取到的消息传递给后面的Handler处理

                    out.add(msg);

                }

            }

        } while (message.readable());

    }

}
</code></pre>
<p>你是不是发现 InternalDecoder 的实现与我们简易版 RPC 的 Decoder 实现非常相似呢？</p>
<p>InternalEncoder 的具体实现就不再展开讲解了，你若感兴趣可以翻看源码进行研究和分析。</p>
<p>接下来是<strong>IdleStateHandler</strong>，它是 Netty 提供的一个工具型 ChannelHandler，用于定时心跳请求的功能或是自动关闭长时间空闲连接的功能。它的原理到底是怎样的呢？在 IdleStateHandler 中通过 lastReadTime、lastWriteTime 等几个字段，记录了最近一次读/写事件的时间，IdleStateHandler 初始化的时候，会创建一个定时任务，定时检测当前时间与最后一次读/写时间的差值。如果超过我们设置的阈值（也就是上面 NettyServer 中设置的 idleTimeout），就会触发 IdleStateEvent 事件，并传递给后续的 ChannelHandler 进行处理。后续 ChannelHandler 的 userEventTriggered() 方法会根据接收到的 IdleStateEvent 事件，决定是关闭长时间空闲的连接，还是发送心跳探活。</p>
<p>最后来看<strong>NettyServerHandler</strong>，它继承了 ChannelDuplexHandler，这是 Netty 提供的一个同时处理 Inbound 数据和 Outbound 数据的 ChannelHandler，从下面的继承图就能看出来。</p>
<p><img src="assets/Ciqc1F9wcFKAQQZ3AAB282frbWw282.png" alt="Drawing 5.png" /></p>
<p>NettyServerHandler 继承关系图</p>
<p>在 NettyServerHandler 中有 channels 和 handler 两个核心字段。</p>
<ul>
<li>channels（Map&lt;String,Channel&gt;集合）：记录了当前 Server 创建的所有 Channel，从下图中可以看到，连接创建（触发 channelActive() 方法）、连接断开（触发 channelInactive()方法）会操作 channels 集合进行相应的增删。</li>
</ul>
<p><img src="assets/Ciqc1F9wcFuABJWsAAaIoTwCIA0958.png" alt="Drawing 6.png" /></p>
<ul>
<li>handler（ChannelHandler 类型）：NettyServerHandler 内几乎所有方法都会触发该 Dubbo ChannelHandler 对象（如下图）。</li>
</ul>
<p><img src="assets/CgqCHl9wcGOAE_ykAAFvy5a4X58367.png" alt="Drawing 7.png" /></p>
<p>这里以 write() 方法为例进行简单分析：</p>
<pre><code>public void write(ChannelHandlerContext ctx, Object msg, ChannelPromise promise) throws Exception {

    super.write(ctx, msg, promise); // 将发送的数据继续向下传递

    // 并不影响消息的继续发送，只是触发sent()方法进行相关的处理，这也是方法

    // 名称是动词过去式的原因，可以仔细体会一下。其他方法可能没有那么明显，

    // 这里以write()方法为例进行说明

    NettyChannel channel = NettyChannel.getOrAddChannel(ctx.channel(), url, handler);

    handler.sent(channel, msg);

}
</code></pre>
<p>在 NettyServer 创建 NettyServerHandler 的时候，可以看到下面的这行代码：</p>
<pre><code>final NettyServerHandler nettyServerHandler = new NettyServerHandler(getUrl(), this);
</code></pre>
<p>其中第二个参数传入的是 NettyServer 这个对象，你可以追溯一下 NettyServer 的继承结构，会发现它的最顶层父类 AbstractPeer 实现了 ChannelHandler，并且将所有的方法委托给其中封装的 ChannelHandler 对象，如下图所示：</p>
<p><img src="assets/Ciqc1F9wcGuADQi3AAD6EEURlNU871.png" alt="Drawing 8.png" /></p>
<p>也就是说，NettyServerHandler 会将数据委托给这个 ChannelHandler。</p>
<p>到此为止，Server 这条继承线就介绍完了。你可以回顾一下，从 AbstractPeer 开始往下，一路继承下来，NettyServer 拥有了 Endpoint、ChannelHandler 以及RemotingServer多个接口的能力，关联了一个 ChannelHandler 对象以及 Codec2 对象，并最终将数据委托给这两个对象进行处理。所以，上层调用方只需要实现 ChannelHandler 和 Codec2 这两个接口就可以了。</p>
<p><img src="assets/Ciqc1F9y4MyAR8XLAABTLdOZqrc228.png" alt="6.png" /></p>
<h3>总结</h3>
<p>本课时重点介绍了 Dubbo Transporter 层中 Server 相关的实现。</p>
<p>首先，我们介绍了 AbstractPeer 这个最顶层的抽象类，了解了 Server、Client 和 Channel 的公共属性。接下来，介绍了 AbstractEndpoint 抽象类，它提供了编解码等 Server 和 Client 所需的公共能力。最后，我们深入分析了 AbstractServer 抽象类以及基于 Netty 4 实现的 NettyServer，同时，还深入剖析了涉及的各种组件，例如，ExecutorRepository、NettyServerHandler 等。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;&#32;Buffer&#32;缓冲区：我们不生产数据，我们只是数据的搬运工.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;&#32;Transporter&#32;层核心实现：编解码与线程模型一文打尽（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f50bd3e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
