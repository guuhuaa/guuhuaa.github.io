<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07  ZooKeeper 与 Curator，求你别用 ZkClient 了（下）.md</title>
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

                    <a class="current-tab" href="07&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（下）.md">07  ZooKeeper 与 Curator，求你别用 ZkClient 了（下）.md</a>
                    

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
                        <div><h1>07  ZooKeeper 与 Curator，求你别用 ZkClient 了（下）</h1>
<p>在上一课时我们介绍了 ZooKeeper 的核心概念以及工作原理，这里我们再简单了解一下 ZooKeeper 客户端的相关内容，毕竟在实际工作中，直接使用客户端与 ZooKeeper 进行交互的次数比深入 ZooKeeper 底层进行扩展和二次开发的次数要多得多。从 ZooKeeper 架构的角度看，使用 Dubbo 的业务节点也只是一个 ZooKeeper 客户端罢了。</p>
<p>ZooKeeper 官方提供的客户端支持了一些基本操作，例如，创建会话、创建节点、读取节点、更新数据、删除节点和检查节点是否存在等，但在实际开发中只有这些简单功能是根本不够的。而且，ZooKeeper 本身的一些 API 也存在不足，例如：</p>
<ul>
<li>ZooKeeper 的 Watcher 是一次性的，每次触发之后都需要重新进行注册。</li>
<li>会话超时之后，没有实现自动重连的机制。</li>
<li>ZooKeeper 提供了非常详细的异常，异常处理显得非常烦琐，对开发新手来说，非常不友好。</li>
<li>只提供了简单的 byte[] 数组的接口，没有提供基本类型以及对象级别的序列化。</li>
<li>创建节点时，如果节点存在抛出异常，需要自行检查节点是否存在。</li>
<li>删除节点就无法实现级联删除。</li>
</ul>
<p><strong>常见的第三方开源 ZooKeeper 客户端有 ZkClient 和 Apache Curator</strong>。</p>
<p>ZkClient 是在 ZooKeeper 原生 API 接口的基础上进行了包装，虽然 ZkClient 解决了 ZooKeeper 原生 API 接口的很多问题，提供了非常简洁的 API 接口，实现了会话超时自动重连的机制，解决了 Watcher 反复注册等问题，但其缺陷也非常明显。例如，文档不全、重试机制难用、异常全部转换成了 RuntimeException、没有足够的参考示例等。可见，一个简单易用、高效可靠的 ZooKeeper 客户端是多么重要。</p>
<h3>Apache Curator 基础</h3>
<p><strong>Apache Curator 是 Apache 基金会提供的一款 ZooKeeper 客户端，它提供了一套易用性和可读性非常强的 Fluent 风格的客户端 API ，可以帮助我们快速搭建稳定可靠的 ZooKeeper 客户端程序。</strong></p>
<p>为便于你更全面了解 Curator 的功能，我整理出了如下表格，展示了 Curator 提供的 jar 包：</p>
<p><img src="assets/Ciqc1F87iUKAAAs2AAE2Xaps_KE511.png" alt="1.png" /></p>
<p>下面我们从最基础的使用展开，逐一介绍 Apache Curator 在实践中常用的核心功能，开始我们的 Apache Curator 之旅。</p>
<h4>1. 基本操作</h4>
<p>简单了解了 Apache Curator 各个组件的定位之后，下面我们立刻通过一个示例上手使用 Curator。首先，我们创建一个 Maven 项目，并添加 Apache Curator 的依赖：</p>
<pre><code>&lt;dependency&gt; 

    &lt;groupId&gt;org.apache.curator&lt;/groupId&gt; 

    &lt;artifactId&gt;curator-recipes&lt;/artifactId&gt; 

    &lt;version&gt;4.0.1&lt;/version&gt; 

&lt;/dependency&gt;
</code></pre>
<p>然后写一个 main 方法，其中会说明 Curator 提供的基础 API 的使用：</p>
<pre><code>public class Main { 

    public static void main(String[] args) throws Exception { 

        // Zookeeper集群地址，多个节点地址可以用逗号分隔 

        String zkAddress = &quot;127.0.0.1:2181&quot;; 

        // 重试策略，如果连接不上ZooKeeper集群，会重试三次，重试间隔会递增 

        RetryPolicy retryPolicy =

              new ExponentialBackoffRetry(1000, 3); 

        // 创建Curator Client并启动，启动成功之后，就可以与Zookeeper进行交互了 

        CuratorFramework client =

            CuratorFrameworkFactory.newClient(zkAddress, retryPolicy); 

        client.start(); 

        // 下面简单说明Curator中常用的API 

        // create()方法创建ZNode，可以调用额外方法来设置节点类型、添加Watcher 

        // 下面是创建一个名为&quot;user&quot;的持久节点，其中会存储一个test字符串 

        String path = client.create().withMode(CreateMode.PERSISTENT) 

            .forPath(&quot;/user&quot;, &quot;test&quot;.getBytes()); 

        System.out.println(path); 

        // 输出:/user 

        // checkExists()方法可以检查一个节点是否存在 

        Stat stat = client.checkExists().forPath(&quot;/user&quot;); 

        System.out.println(stat!=null); 

        // 输出:true，返回的Stat不为null，即表示节点存在 

        // getData()方法可以获取一个节点中的数据 

        byte[] data = client.getData().forPath(&quot;/user&quot;); 

        System.out.println(new String(data)); 

        // 输出:test 

        // setData()方法可以设置一个节点中的数据 

        stat = client.setData().forPath(&quot;/user&quot;,&quot;data&quot;.getBytes()); 

        data = client.getData().forPath(&quot;/user&quot;); 

        System.out.println(new String(data)); 

        // 输出:data 

        // 在/user节点下，创建多个临时顺序节点 

        for (int i = 0; i &lt; 3; i++) { 

            client.create().withMode(CreateMode.EPHEMERAL_SEQUENTIAL) 

                .forPath(&quot;/user/child-&quot;; 

        } 

        // 获取所有子节点 

        List&lt;String&gt; children = client.getChildren().forPath(&quot;/user&quot;); 

        System.out.println(children); 

        // 输出：[child-0000000002, child-0000000001, child-0000000000] 

        // delete()方法可以删除指定节点，deletingChildrenIfNeeded()方法 

        // 会级联删除子节点 

        client.delete().deletingChildrenIfNeeded().forPath(&quot;/user&quot;); 

    } 

}
</code></pre>
<h4>2. Background</h4>
<p>上面介绍的创建、删除、更新、读取等方法都是同步的，Curator 提供异步接口，引入了BackgroundCallback 这个回调接口以及 CuratorListener 这个监听器，用于处理 Background 调用之后服务端返回的结果信息。BackgroundCallback 接口和 CuratorListener 监听器中接收一个 CuratorEvent 的参数，里面包含事件类型、响应码、节点路径等详细信息。</p>
<p>下面我们通过一个示例说明 BackgroundCallback 接口以及 CuratorListener 监听器的基本使用：</p>
<pre><code>public class Main2 { 

    public static void main(String[] args) throws Exception { 

        // Zookeeper集群地址，多个节点地址可以用逗号分隔 

        String zkAddress = &quot;127.0.0.1:2181&quot;; 

        // 重试策略，如果连接不上ZooKeeper集群，会重试三次，重试间隔会递增 

        RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000,3); 

        // 创建Curator Client并启动，启动成功之后，就可以与Zookeeper进行交互了 

        CuratorFramework client = CuratorFrameworkFactory 

            .newClient(zkAddress, retryPolicy); 

        client.start(); 

        // 添加CuratorListener监听器，针对不同的事件进行处理 

        client.getCuratorListenable().addListener( 

          new CuratorListener() { 

            public void eventReceived(CuratorFramework client,

                  CuratorEvent event) throws Exception { 

                switch (event.getType()) { 

                    case CREATE: 

                        System.out.println(&quot;CREATE:&quot; +

                              event.getPath()); 

                        break; 

                    case DELETE: 

                        System.out.println(&quot;DELETE:&quot; +

                               event.getPath()); 

                        break; 

                    case EXISTS: 

                        System.out.println(&quot;EXISTS:&quot; +

                                event.getPath()); 

                        break; 

                    case GET_DATA: 

                        System.out.println(&quot;GET_DATA:&quot; +

                          event.getPath() + &quot;,&quot;

                              + new String(event.getData())); 

                        break; 

                    case SET_DATA: 

                        System.out.println(&quot;SET_DATA:&quot; + 

                                 new String(event.getData())); 

                        break; 

                    case CHILDREN: 

                        System.out.println(&quot;CHILDREN:&quot; +

                                event.getPath()); 

                        break; 

                    default: 

                } 

            } 

        }); 

        // 注意:下面所有的操作都添加了inBackground()方法，转换为后台操作 

        client.create().withMode(CreateMode.PERSISTENT) 

            .inBackground().forPath(&quot;/user&quot;, &quot;test&quot;.getBytes()); 

        client.checkExists().inBackground().forPath(&quot;/user&quot;); 

        client.setData().inBackground().forPath(&quot;/user&quot;,

              &quot;setData-Test&quot;.getBytes()); 

        client.getData().inBackground().forPath(&quot;/user&quot;); 

        for (int i = 0; i &lt; 3; i++) { 

            client.create().withMode(CreateMode.EPHEMERAL_SEQUENTIAL) 

                .inBackground().forPath(&quot;/user/child-&quot;); 

        } 

        client.getChildren().inBackground().forPath(&quot;/user&quot;); 

        // 添加BackgroundCallback 

        client.getChildren().inBackground(new BackgroundCallback() { 

            public void processResult(CuratorFramework client,

                CuratorEvent event) throws Exception { 

                System.out.println(&quot;in background:&quot;

                      + event.getType() + &quot;,&quot; + event.getPath()); 

            } 

        }).forPath(&quot;/user&quot;); 

        client.delete().deletingChildrenIfNeeded().inBackground() 

              .forPath(&quot;/user&quot;); 

        System.in.read(); 

    } 

} 

// 输出： 

// CREATE:/user 

// EXISTS:/user 

// GET_DATA:/user,setData-Test 

// CREATE:/user/child- 

// CREATE:/user/child- 

// CREATE:/user/child- 

// CHILDREN:/user 

// DELETE:/user
</code></pre>
<h4>3. 连接状态监听</h4>
<p>除了基础的数据操作，Curator 还提供了<strong>监听连接状态的监听器——ConnectionStateListener</strong>，它主要是处理 Curator 客户端和 ZooKeeper 服务器间连接的异常情况，例如， 短暂或者长时间断开连接。</p>
<p>短暂断开连接时，ZooKeeper 客户端会检测到与服务端的连接已经断开，但是服务端维护的客户端 Session 尚未过期，之后客户端和服务端重新建立了连接；当客户端重新连接后，由于 Session 没有过期，ZooKeeper 能够保证连接恢复后保持正常服务。</p>
<p>而长时间断开连接时，Session 已过期，与先前 Session 相关的 Watcher 和临时节点都会丢失。当 Curator 重新创建了与 ZooKeeper 的连接时，会获取到 Session 过期的相关异常，Curator 会销毁老 Session，并且创建一个新的 Session。由于老 Session 关联的数据不存在了，在 ConnectionStateListener 监听到 LOST 事件时，就可以依靠本地存储的数据恢复 Session 了。</p>
<p><strong>这里 Session 指的是 ZooKeeper 服务器与客户端的会话</strong>。客户端启动的时候会与服务器建立一个 TCP 连接，从第一次连接建立开始，客户端会话的生命周期也开始了。客户端能够通过心跳检测与服务器保持有效的会话，也能够向 ZooKeeper 服务器发送请求并接受响应，同时还能够通过该连接接收来自服务器的 Watch 事件通知。</p>
<p>我们可以设置客户端会话的超时时间（sessionTimeout），当服务器压力太大、网络故障或是客户端主动断开连接等原因导致连接断开时，只要客户端在 sessionTimeout 规定的时间内能够重新连接到 ZooKeeper 集群中任意一个实例，那么之前创建的会话仍然有效。ZooKeeper 通过 sessionID 唯一标识 Session，所以在 ZooKeeper 集群中，sessionID 需要保证全局唯一。 由于 ZooKeeper 会将 Session 信息存放到硬盘中，即使节点重启，之前未过期的 Session 仍然会存在。</p>
<pre><code>public class Main3 { 

    public static void main(String[] args) throws Exception { 

        // Zookeeper集群地址，多个节点地址可以用逗号分隔 

        String zkAddress = &quot;127.0.0.1:2181&quot;; 

        // 重试策略，如果连接不上ZooKeeper集群，会重试三次，重试间隔会递增 

        RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000,3); 

        // 创建Curator Client并启动，启动成功之后，就可以与Zookeeper进行交互了 

        CuratorFramework client = CuratorFrameworkFactory 

            .newClient(zkAddress, retryPolicy); 

        client.start(); 

        // 添加ConnectionStateListener监听器 

        client.getConnectionStateListenable().addListener( 

          new ConnectionStateListener() { 

            public void stateChanged(CuratorFramework client,

                    ConnectionState newState) { 

                // 这里我们可以针对不同的连接状态进行特殊的处理 

                switch (newState) {

                    case CONNECTED: 

                        // 第一次成功连接到ZooKeeper之后会进入该状态。 

                        // 对于每个CuratorFramework对象，此状态仅出现一次 

                        break; 

                    case SUSPENDED: //   ZooKeeper的连接丢失 

                        break; 

                    case RECONNECTED: // 丢失的连接被重新建立 

                        break; 

                    case LOST:

                        // 当Curator认为会话已经过期时，则进入此状态 

                        break; 

                    case READ_ONLY: // 连接进入只读模式 

                        break; 

                } 

            } 

        }); 

   } 

}
</code></pre>
<h4>4. Watcher</h4>
<p>Watcher 监听机制是 ZooKeeper 中非常重要的特性，可以监听某个节点上发生的特定事件，例如，监听节点数据变更、节点删除、子节点状态变更等事件。当相应事件发生时，ZooKeeper 会产生一个 Watcher 事件，并且发送到客户端。通过 Watcher 机制，就可以使用 ZooKeeper 实现分布式锁、集群管理等功能。</p>
<p>在 Curator 客户端中，我们可以使用 usingWatcher() 方法添加 Watcher，前面示例中，能够添加 Watcher 的有 checkExists()、getData()以及 getChildren() 三个方法，下面我们来看一个具体的示例：</p>
<pre><code>public class Main4 { 

    public static void main(String[] args) throws Exception { 

        // Zookeeper集群地址，多个节点地址可以用逗号分隔 

        String zkAddress = &quot;127.0.0.1:2181&quot;; 

        // 重试策略，如果连接不上ZooKeeper集群，会重试三次，重试间隔会递增 

        RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000,3); 

        // 创建Curator Client并启动，启动成功之后，就可以与Zookeeper进行交互了 

        CuratorFramework client = CuratorFrameworkFactory 

              .newClient(zkAddress, retryPolicy); 

        client.start(); 

        try { 

           client.create().withMode(CreateMode.PERSISTENT) 

                 .forPath(&quot;/user&quot;, &quot;test&quot;.getBytes()); 

        } catch (Exception e) { 

        } 

        // 这里通过usingWatcher()方法添加一个Watcher 

        List&lt;String&gt; children = client.getChildren().usingWatcher( 

          new CuratorWatcher() { 

            public void process(WatchedEvent event) throws Exception { 

                System.out.println(event.getType() + &quot;,&quot; +

                    event.getPath()); 

            } 

        }).forPath(&quot;/user&quot;); 

        System.out.println(children); 

        System.in.read(); 

    } 

}
</code></pre>
<p>接下来，我们打开 ZooKeeper 的命令行客户端，在 /user 节点下先后添加两个子节点，如下所示：</p>
<p><img src="assets/Ciqc1F87iXuAQVanAABhI9RRD8M252.png" alt="Drawing 0.png" /></p>
<p>此时我们只得到一行输出：</p>
<pre><code>NodeChildrenChanged,/user
</code></pre>
<p>之所以这样，是因为通过 usingWatcher() 方法添加的 CuratorWatcher 只会触发一次，触发完毕后就会销毁。checkExists() 方法、getData() 方法通过 usingWatcher() 方法添加的 Watcher 也是一样的原理，只不过监听的事件不同，你若感兴趣的话，可以自行尝试一下。</p>
<p>相信你已经感受到，直接通过注册 Watcher 进行事件监听不是特别方便，需要我们自己反复注册 Watcher。<strong>Apache Curator 引入了 Cache 来实现对 ZooKeeper 服务端事件的监听</strong>。Cache 是 Curator 中对事件监听的包装，其对事件的监听其实可以近似看作是一个本地缓存视图和远程ZooKeeper 视图的对比过程。同时，Curator 能够自动为开发人员处理反复注册监听，从而大大简化了代码的复杂程度。</p>
<p>实践中常用的 Cache 有三大类：</p>
<ul>
<li><strong>NodeCache。</strong> 对一个节点进行监听，监听事件包括指定节点的增删改操作。注意哦，NodeCache 不仅可以监听数据节点的内容变更，也能监听指定节点是否存在，如果原本节点不存在，那么 Cache 就会在节点被创建后触发 NodeCacheListener，删除操作亦然。</li>
<li><strong>PathChildrenCache。</strong> 对指定节点的一级子节点进行监听，监听事件包括子节点的增删改操作，但是不对该节点的操作监听。</li>
<li><strong>TreeCache。</strong> 综合 NodeCache 和 PathChildrenCache 的功能，是对指定节点以及其子节点进行监听，同时还可以设置监听的深度。</li>
</ul>
<p>下面通过示例介绍上述三种 Cache 的基本使用：</p>
<pre><code>public class Main5 { 

    public static void main(String[] args) throws Exception { 

        // Zookeeper集群地址，多个节点地址可以用逗号分隔 

        String zkAddress = &quot;127.0.0.1:2181&quot;; 

        // 重试策略，如果连接不上ZooKeeper集群，会重试三次，重试间隔会递增 

        RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000,3); 

        // 创建Curator Client并启动，启动成功之后，就可以与Zookeeper进行交互了 

        CuratorFramework client = CuratorFrameworkFactory 

           .newClient(zkAddress, retryPolicy); 

        client.start(); 

        // 创建NodeCache，监听的是&quot;/user&quot;这个节点 

        NodeCache nodeCache = new NodeCache(client, &quot;/user&quot;); 

        // start()方法有个boolean类型的参数，默认是false。如果设置为true， 

        // 那么NodeCache在第一次启动的时候就会立刻从ZooKeeper上读取对应节点的 

        // 数据内容，并保存在Cache中。 

        nodeCache.start(true); 

        if (nodeCache.getCurrentData() != null) { 

            System.out.println(&quot;NodeCache节点初始化数据为：&quot;

                + new String(nodeCache.getCurrentData().getData())); 

        } else { 

            System.out.println(&quot;NodeCache节点数据为空&quot;); 

        } 

        // 添加监听器 

        nodeCache.getListenable().addListener(() -&gt; { 

            String data = new String(nodeCache.getCurrentData().getData()); 

            System.out.println(&quot;NodeCache节点路径：&quot; + nodeCache.getCurrentData().getPath() 

                    + &quot;，节点数据为：&quot; + data); 

        }); 

        // 创建PathChildrenCache实例，监听的是&quot;user&quot;这个节点 

        PathChildrenCache childrenCache = new PathChildrenCache(client, &quot;/user&quot;, true); 

        // StartMode指定的初始化的模式 

        // NORMAL:普通异步初始化 

        // BUILD_INITIAL_CACHE:同步初始化 

        // POST_INITIALIZED_EVENT:异步初始化，初始化之后会触发事件 

        childrenCache.start(PathChildrenCache.StartMode.BUILD_INITIAL_CACHE); 

        // childrenCache.start(PathChildrenCache.StartMode.POST_INITIALIZED_EVENT); 

        // childrenCache.start(PathChildrenCache.StartMode.NORMAL); 

        List&lt;ChildData&gt; children = childrenCache.getCurrentData(); 

        System.out.println(&quot;获取子节点列表：&quot;); 

        // 如果是BUILD_INITIAL_CACHE可以获取这个数据，如果不是就不行 

        children.forEach(childData -&gt; { 

            System.out.println(new String(childData.getData())); 

        }); 

        childrenCache.getListenable().addListener(((client1, event) -&gt; { 

            System.out.println(LocalDateTime.now() + &quot;  &quot; + event.getType()); 

            if (event.getType().equals(PathChildrenCacheEvent.Type.INITIALIZED)) { 

                System.out.println(&quot;PathChildrenCache:子节点初始化成功...&quot;); 

            } else if (event.getType().equals(PathChildrenCacheEvent.Type.CHILD_ADDED)) { 

                String path = event.getData().getPath(); 

                System.out.println(&quot;PathChildrenCache添加子节点:&quot; + event.getData().getPath()); 

                System.out.println(&quot;PathChildrenCache子节点数据:&quot; + new String(event.getData().getData())); 

            } else if (event.getType().equals(PathChildrenCacheEvent.Type.CHILD_REMOVED)) { 

                System.out.println(&quot;PathChildrenCache删除子节点:&quot; + event.getData().getPath()); 

            } else if (event.getType().equals(PathChildrenCacheEvent.Type.CHILD_UPDATED)) { 

                System.out.println(&quot;PathChildrenCache修改子节点路径:&quot; + event.getData().getPath()); 

                System.out.println(&quot;PathChildrenCache修改子节点数据:&quot; + new String(event.getData().getData())); 

            } 

        })); 

        // 创建TreeCache实例监听&quot;user&quot;节点 

        TreeCache cache = TreeCache.newBuilder(client, &quot;/user&quot;).setCacheData(false).build(); 

        cache.getListenable().addListener((c, event) -&gt; { 

            if (event.getData() != null) { 

                System.out.println(&quot;TreeCache,type=&quot; + event.getType() + &quot; path=&quot; + event.getData().getPath()); 

            } else { 

                System.out.println(&quot;TreeCache,type=&quot; + event.getType()); 

            } 

        }); 

        cache.start(); 

        System.in.read(); 

    } 

}
</code></pre>
<p>此时，ZooKeeper 集群中存在 /user/test1 和 /user/test2 两个节点，启动上述测试代码，得到的输出如下：</p>
<pre><code>NodeCache节点初始化数据为：test //NodeCache的相关输出

获取子节点列表：// PathChildrenCache的相关输出 

xxx 

xxx2 

// TreeCache监听到的事件 

TreeCache,type=NODE_ADDED path=/user 

TreeCache,type=NODE_ADDED path=/user/test1 

TreeCache,type=NODE_ADDED path=/user/test2 

TreeCache,type=INITIALIZED
</code></pre>
<p>接下来，我们在 ZooKeeper 命令行客户端中<strong>更新 /user 节点中的数据</strong>：</p>
<p><img src="assets/Ciqc1F87iY6ACWnvAAA8jA9QVgM875.png" alt="Drawing 1.png" /></p>
<p>得到如下输出：</p>
<pre><code>TreeCache,type=NODE_UPDATED path=/user 

NodeCache节点路径：/user，节点数据为：userData
</code></pre>
<p><strong>创建 /user/test3 节点</strong>：</p>
<p><img src="assets/CgqCHl87iZqAaG93AABwFnQJA7o497.png" alt="Drawing 2.png" /></p>
<p>得到输出：</p>
<pre><code>TreeCache,type=NODE_ADDED path=/user/test3 

2020-06-26T08:35:22.393  CHILD_ADDED 

PathChildrenCache添加子节点:/user/test3 

PathChildrenCache子节点数据:xxx3
</code></pre>
<p><strong>更新 /user/test3 节点的数据</strong>：</p>
<p><img src="assets/Ciqc1F87iaSAFZLpAABDyAm7vuE120.png" alt="Drawing 3.png" /></p>
<p>得到输出：</p>
<pre><code>TreeCache,type=NODE_UPDATED path=/user/test3 

2020-06-26T08:43:54.604  CHILD_UPDATED 

PathChildrenCache修改子节点路径:/user/test3 

PathChildrenCache修改子节点数据:xxx33
</code></pre>
<p><strong>删除 /user/test3 节点</strong>：</p>
<p><img src="assets/CgqCHl87ia6AYvijAABBmFLfzx4213.png" alt="Drawing 4.png" /></p>
<p>得到输出：</p>
<pre><code>TreeCache,type=NODE_REMOVED path=/user/test3 

2020-06-26T08:44:06.329  CHILD_REMOVED 

PathChildrenCache删除子节点:/user/test3
</code></pre>
<h3>curator-x-discovery 扩展库</h3>
<p>为了避免 curator-framework 包过于膨胀，Curator 将很多其他解决方案都拆出来了，作为单独的一个包，例如：curator-recipes、curator-x-discovery、curator-x-rpc 等。</p>
<p>在后面我们会使用到 curator-x-discovery 来完成一个简易 RPC 框架的注册中心模块。<strong>curator-x-discovery 扩展包是一个服务发现的解决方案</strong>。在 ZooKeeper 中，我们可以使用临时节点实现一个服务注册机制。当服务启动后在 ZooKeeper 的指定 Path 下创建临时节点，服务断掉与 ZooKeeper 的会话之后，其相应的临时节点就会被删除。这个 curator-x-discovery 扩展包抽象了这种功能，并提供了一套简单的 API 来实现服务发现机制。curator-x-discovery 扩展包的核心概念如下：</p>
<ul>
<li><strong>ServiceInstance。</strong> 这是 curator-x-discovery 扩展包对服务实例的抽象，由 name、id、address、port 以及一个可选的 payload 属性构成。其存储在 ZooKeeper 中的方式如下图展示的这样。</li>
</ul>
<p><img src="assets/CgqCHl87icOABt59AADHccHcE1Q955.png" alt="Drawing 5.png" /></p>
<ul>
<li><strong>ServiceProvider。</strong> 这是 curator-x-discovery 扩展包的核心组件之一，提供了多种不同策略的服务发现方式，具体策略有轮询调度、随机和黏性（总是选择相同的一个）。得到 ServiceProvider 对象之后，我们可以调用其 getInstance() 方法，按照指定策略获取 ServiceInstance 对象（即发现可用服务实例）；还可以调用 getAllInstances() 方法，获取所有 ServiceInstance 对象（即获取全部可用服务实例）。</li>
<li><strong>ServiceDiscovery。</strong> 这是 curator-x-discovery 扩展包的入口类。开始必须调用 start() 方法，当使用完成应该调用 close() 方法进行销毁。</li>
<li><strong>ServiceCache。</strong> 如果程序中会频繁地查询 ServiceInstance 对象，我们可以添加 ServiceCache 缓存，ServiceCache 会在内存中缓存 ServiceInstance 实例的列表，并且添加相应的 Watcher 来同步更新缓存。查询 ServiceCache 的方式也是 getInstances() 方法。另外，ServiceCache 上还可以添加 Listener 来监听缓存变化。</li>
</ul>
<p>下面通过一个简单示例来说明一下 curator-x-discovery 包的使用，该示例中的 ServerInfo 记录了一个服务的 host、port 以及描述信息。</p>
<pre><code>public class ZookeeperCoordinator { 

    private ServiceDiscovery&lt;ServerInfo&gt; serviceDiscovery; 

    private ServiceCache&lt;ServerInfo&gt; serviceCache; 

    private CuratorFramework client; 

    private String root; 

    // 这里的JsonInstanceSerializer是将ServerInfo序列化成Json 

    private InstanceSerializer serializer =

        new JsonInstanceSerializer&lt;&gt;(ServerInfo.class); 

    ZookeeperCoordinator(Config config) throws Exception { 

        this.root = config.getPath(); 

        // 创建Curator客户端 

        client = CuratorFrameworkFactory.newClient( 

            config.getHostPort(),  new ExponentialBackoffRetry(...)); 

        client.start(); // 启动Curator客户端

        client.blockUntilConnected();  // 阻塞当前线程，等待连接成功 

        // 创建ServiceDiscovery 

        serviceDiscovery = ServiceDiscoveryBuilder 

                .builder(ServerInfo.class) 

                .client(client) // 依赖Curator客户端 

                .basePath(root) // 管理的Zk路径 

                .watchInstances(true) // 当ServiceInstance加载 

                .serializer(serializer) 

                .build(); 

         serviceDiscovery.start(); // 启动ServiceDiscovery 

        // 创建ServiceCache，监Zookeeper相应节点的变化，也方便后续的读取 

        serviceCache = serviceDiscovery.serviceCacheBuilder() 

                .name(root) 

                .build();

         serviceCache.start(); // 启动ServiceCache 

    } 

    public void registerRemote(ServerInfo serverInfo)throws Exception{ 

         // 将ServerInfo对象转换成ServiceInstance对象 

         ServiceInstance&lt;ServerInfo&gt; thisInstance =

            ServiceInstance.&lt;ServerInfo&gt;builder() 

                    .name(root) 

                    .id(UUID.randomUUID().toString()) // 随机生成的UUID 

                    .address(serverInfo.getHost()) // host 

                    .port(serverInfo.getPort()) // port 

                    .payload(serverInfo) // payload 

                    .build(); 

         // 将ServiceInstance写入到Zookeeper中 

         serviceDiscovery.registerService(thisInstance); 

    } 

    public List&lt;ServerInfo&gt; queryRemoteNodes() { 

        List&lt;ServerInfo&gt; ServerInfoDetails = new ArrayList&lt;&gt;(); 

        // 查询 ServiceCache 获取全部的 ServiceInstance 对象 

        List&lt;ServiceInstance&lt;ServerInfo&gt;&gt; serviceInstances =

            serviceCache.getInstances(); 

        serviceInstances.forEach(serviceInstance -&gt; { 

            // 从每个ServiceInstance对象的playload字段中反序列化得 

            // 到ServerInfo实例 

            ServerInfo instance = serviceInstance.getPayload(); 

            ServerInfoDetails.add(instance); 

        }); 

        return ServerInfoDetails; 

    } 

}
</code></pre>
<h3>curator-recipes 简介</h3>
<p>Recipes 是 Curator 对常见分布式场景的解决方案，这里我们只是简单介绍一下，具体的使用和原理，就先不做深入分析了。</p>
<ul>
<li><strong>Queues</strong>。提供了多种的分布式队列解决方法，比如：权重队列、延迟队列等。在生产环境中，很少将 ZooKeeper 用作分布式队列，只适合在压力非常小的情况下，才使用该解决方案，所以建议你要适度使用。</li>
<li><strong>Counters</strong>。全局计数器是分布式系统中很常用的工具，curator-recipes 提供了 SharedCount、DistributedAtomicLong 等组件，帮助开发人员实现分布式计数器功能。</li>
<li><strong>Locks</strong>。java.util.concurrent.locks 中提供的各种锁相信你已经有所了解了，在微服务架构中，分布式锁也是一项非常基础的服务组件，curator-recipes 提供了多种基于 ZooKeeper 实现的分布式锁，满足日常工作中对分布式锁的需求。</li>
<li><strong>Barries</strong>。curator-recipes 提供的分布式栅栏可以实现多个服务之间协同工作，具体实现有 DistributedBarrier 和 DistributedDoubleBarrier。</li>
<li><strong>Elections</strong>。实现的主要功能是在多个参与者中选举出 Leader，然后由 Leader 节点作为操作调度、任务监控或是队列消费的执行者。curator-recipes 给出的实现是 LeaderLatch。</li>
</ul>
<h3>总结</h3>
<p>本课时我们重点介绍了 Apache Curator 相关的内容：</p>
<ul>
<li>首先将 Apache Curator 与其他 ZooKeeper 客户端进行了对比，Apache Curator 的易用性是选择 Apache Curator 的重要原因。</li>
<li>接下来，我们通过示例介绍了 Apache Curator 的基本使用方式以及实际使用过程中的一些注意点。</li>
<li>然后，介绍了 curator-x-discovery 扩展库的基本概念和使用。</li>
<li>最后，简单介绍了 curator-recipes 提供的强大功能。</li>
</ul>
<p>关于 Apache Curator，你有什么其他的见解？欢迎你在评论区给我留言，与我分享。</p>
<p>zk-demo 链接：<a href="https://github.com/xxxlxy2008/zk-demo">https://github.com/xxxlxy2008/zk-demo</a> 。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;&#32;ZooKeeper&#32;与&#32;Curator，求你别用&#32;ZkClient&#32;了（上）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;&#32;代理模式与常见实现.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433eff8fb570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
