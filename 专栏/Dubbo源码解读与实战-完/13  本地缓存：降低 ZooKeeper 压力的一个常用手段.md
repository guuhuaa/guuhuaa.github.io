<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13  本地缓存：降低 ZooKeeper 压力的一个常用手段.md</title>
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

                    <a class="current-tab" href="13&#32;&#32;本地缓存：降低&#32;ZooKeeper&#32;压力的一个常用手段.md">13  本地缓存：降低 ZooKeeper 压力的一个常用手段.md</a>
                    

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
                        <div><h1>13  本地缓存：降低 ZooKeeper 压力的一个常用手段</h1>
<p>从这一课时开始，我们就进入了第二部分：注册中心。注册中心（Registry）在微服务架构中的作用举足轻重，有了它，<strong>服务提供者（Provider）</strong> 和<strong>消费者（Consumer）</strong> 就能感知彼此。从下面的 Dubbo 架构图中可知：</p>
<p><img src="assets/CgqCHl9W91KABCfoAAB7_C-aKWA893.png" alt="Drawing 0.png" /></p>
<p>Dubbo 架构图</p>
<ul>
<li>Provider 从容器启动后的初始化阶段便会向注册中心完成注册操作；</li>
<li>Consumer 启动初始化阶段会完成对所需 Prov·ider 的订阅操作；</li>
<li>另外，在 Provider 发生变化时，需要通知监听的 Consumer。</li>
</ul>
<p>Registry 只是 Consumer 和 Provider 感知彼此状态变化的一种便捷途径而已，它们彼此的实际通讯交互过程是直接进行的，对于 Registry 来说是透明无感的。Provider 状态发生变化了，会由 Registry 主动推送订阅了该 Provider 的所有 Consumer，这保证了 Consumer 感知 Provider 状态变化的及时性，也将和具体业务需求逻辑交互解耦，提升了系统的稳定性。</p>
<p>Dubbo 中存在很多概念，但有些理解起来就特别费劲，如本文的 Registry，翻译过来的意思是“注册中心”，但它其实是应用本地的注册中心客户端，<strong>真正的“注册中心”服务是其他独立部署的进程，或进程组成的集群，比如 ZooKeeper 集群</strong>。本地的 Registry 通过和 ZooKeeper 等进行实时的信息同步，维持这些内容的一致性，从而实现了注册中心这个特性。另外，就 Registry 而言，Consumer 和 Provider 只是个用户视角的概念，它们被抽象为了一条 URL 。</p>
<p>从本课时开始，我们就真正开始分析 Dubbo 源码了。首先看一下本课程第二部分内容在 Dubbo 架构中所处的位置（如下图红框所示），可以看到这部分内容在整个 Dubbo 体系中还是相对独立的，没有涉及 Protocol、Invoker 等 Dubbo 内部的概念。等介绍完这些概念之后，我们还会回看图中 Registry 红框之外的内容。</p>
<p><img src="assets/CgqCHl9W92uAEdHNAC1YtFrPHGA595.png" alt="Drawing 1.png" /></p>
<p>整个 Dubbo 体系图</p>
<h3>核心接口</h3>
<p>作为“注册中心”部分的第一课时，我们有必要介绍下 dubbo-registry-api 模块中的核心抽象接口，如下图所示：</p>
<p><img src="assets/Ciqc1F9W94aAIB3iAAE7RxqxFDw401.png" alt="Drawing 2.png" /></p>
<p>在 Dubbo 中，一般使用 Node 这个接口来抽象节点的概念。<strong>Node</strong>不仅可以表示 Provider 和 Consumer 节点，还可以表示注册中心节点。Node 接口中定义了三个非常基础的方法（如下图所示）：</p>
<p><img src="assets/Ciqc1F9W942AJdaYAAAlxcqD4vE542.png" alt="Drawing 3.png" /></p>
<ul>
<li>getUrl() 方法返回表示当前节点的 URL；</li>
<li>isAvailable() 检测当前节点是否可用；</li>
<li>destroy() 方法负责销毁当前节点并释放底层资源。</li>
</ul>
<p><strong>RegistryService 接口</strong>抽象了注册服务的基本行为，如下图所示：</p>
<p><img src="assets/CgqCHl9W95SAEiTBAABRqhrI6ig390.png" alt="Drawing 4.png" /></p>
<ul>
<li>register() 方法和 unregister() 方法分别表示<strong>注册</strong>和<strong>取消注册</strong>一个 URL。</li>
<li>subscribe() 方法和 unsubscribe() 方法分别表示<strong>订阅</strong>和<strong>取消订阅</strong>一个 URL。订阅成功之后，当订阅的数据发生变化时，注册中心会主动通知第二个参数指定的 NotifyListener 对象，NotifyListener 接口中定义的 notify() 方法就是用来接收该通知的。</li>
<li>lookup() 方法能够<strong>查询</strong>符合条件的注册数据，它与 subscribe() 方法有一定的区别，subscribe() 方法采用的是 push 模式，lookup() 方法采用的是 pull 模式。</li>
</ul>
<p><strong>Registry 接口</strong>继承了 RegistryService 接口和 Node 接口，如下图所示，它表示的就是一个拥有注册中心能力的节点，其中的 reExportRegister() 和 reExportUnregister() 方法都是委托给 RegistryService 中的相应方法。</p>
<p><img src="assets/Ciqc1F9W952Aesi9AAAjKOjjN0I785.png" alt="Drawing 5.png" /></p>
<p><strong>RegistryFactory 接口</strong>是 Registry 的工厂接口，负责创建 Registry 对象，具体定义如下所示，其中 @SPI 注解指定了默认的扩展名为 dubbo，@Adaptive 注解表示会生成适配器类并根据 URL 参数中的 protocol 参数值选择相应的实现。</p>
<pre><code>@SPI(&quot;dubbo&quot;)

public interface RegistryFactory {

    @Adaptive({&quot;protocol&quot;})

    Registry getRegistry(URL url);

}
</code></pre>
<p>通过下面两张继承关系图可以看出，每个 Registry 实现类都有对应的 RegistryFactory 工厂实现，每个 RegistryFactory 工厂实现只负责创建对应的 Registry 对象。</p>
<p><img src="assets/CgqCHl9W96aAbyVRAAIzHNPLhSM843.png" alt="Drawing 6.png" /></p>
<p>RegistryFactory 继承关系图</p>
<p><img src="assets/Ciqc1F9W97CAdPcXAAG1fsVxaeI019.png" alt="Drawing 7.png" /></p>
<p>Registry 继承关系图</p>
<p>其中，RegistryFactoryWrapper 是 RegistryFactory 接口的 Wrapper 类，它在底层 RegistryFactory 创建的 Registry 对象外层封装了一个 ListenerRegistryWrapper ，ListenerRegistryWrapper 中维护了一个 RegistryServiceListener 集合，会将 register()、subscribe() 等事件通知到 RegistryServiceListener 监听器。</p>
<p>AbstractRegistryFactory 是一个实现了 RegistryFactory 接口的抽象类，提供了规范 URL 的操作以及缓存 Registry 对象的公共能力。其中，缓存 Registry 对象是使用 HashMap&lt;String, Registry&gt; 集合实现的（REGISTRIES 静态字段）。在规范 URL 的实现逻辑中，AbstractRegistryFactory 会将 RegistryService 的类名设置为 URL path 和 interface 参数，同时删除 export 和 refer 参数。</p>
<h3>AbstractRegistry</h3>
<p>AbstractRegistry 实现了 Registry 接口，虽然 AbstractRegistry 本身在内存中实现了注册数据的读写功能，也没有什么抽象方法，但它依然被标记成了抽象类，从前面的Registry 继承关系图中可以看出，<strong>Registry 接口的所有实现类都继承了 AbstractRegistry</strong>。</p>
<p>为了减轻注册中心组件的压力，AbstractRegistry 会把当前节点订阅的 URL 信息缓存到本地的 Properties 文件中，其核心字段如下：</p>
<ul>
<li><strong>registryUrl（URL类型）。</strong> 该 URL 包含了创建该 Registry 对象的全部配置信息，是 AbstractRegistryFactory 修改后的产物。</li>
<li><strong>properties（Properties 类型）、file（File 类型）。</strong> 本地的 Properties 文件缓存，properties 是加载到内存的 Properties 对象，file 是磁盘上对应的文件，两者的数据是同步的。在 AbstractRegistry 初始化时，会根据 registryUrl 中的 file.cache 参数值决定是否开启文件缓存。如果开启文件缓存功能，就会立即将 file 文件中的 KV 缓存加载到 properties 字段中。当 properties 中的注册数据发生变化时，会写入本地的 file 文件进行同步。properties 是一个 KV 结构，其中 Key 是当前节点作为 Consumer 的一个 URL，Value 是对应的 Provider 列表，包含了所有 Category（例如，providers、routes、configurators 等） 下的 URL。properties 中有一个特殊的 Key 值为 registies，对应的 Value 是注册中心列表，其他记录的都是 Provider 列表。</li>
<li><strong>syncSaveFile（boolean 类型）。</strong> 是否同步保存文件的配置，对应的是 registryUrl 中的 save.file 参数。</li>
<li><strong>registryCacheExecutor（ExecutorService 类型）。</strong> 这是一个单线程的线程池，在一个 Provider 的注册数据发生变化的时候，会将该 Provider 的全量数据同步到 properties 字段和缓存文件中，如果 syncSaveFile 配置为 false，就由该线程池异步完成文件写入。</li>
<li><strong>lastCacheChanged（AtomicLong 类型）。</strong> 注册数据的版本号，每次写入 file 文件时，都是全覆盖写入，而不是修改文件，所以需要版本控制，防止旧数据覆盖新数据。</li>
<li><strong>registered（Set 类型）。</strong> 这个比较简单，它是注册的 URL 集合。</li>
<li><strong>subscribed（ConcurrentMap&lt;URL, Set&gt; 类型）。</strong> 表示订阅 URL 的监听器集合，其中 Key 是被监听的 URL， Value 是相应的监听器集合。</li>
<li><strong>notified（ConcurrentMap&lt;URL, Map&lt;String, List&gt;&gt;类型）。</strong> 该集合第一层 Key 是当前节点作为 Consumer 的一个 URL，表示的是该节点的某个 Consumer 角色（一个节点可以同时消费多个 Provider 节点）；Value 是一个 Map 集合，该 Map 集合的 Key 是 Provider URL 的分类（Category），例如 providers、routes、configurators 等，Value 就是相应分类下的 URL 集合。</li>
</ul>
<p>介绍完 AbstractRegistry 的核心字段之后，我们接下来就再看看 AbstractRegistry 依赖这些字段都提供了哪些公共能力。</p>
<h4>1. 本地缓存</h4>
<p>作为一个 RPC 框架，Dubbo 在微服务架构中解决了各个服务间协作的难题；作为 Provider 和 Consumer 的底层依赖，它会与服务一起打包部署。dubbo-registry 也仅仅是其中一个依赖包，负责完成与 ZooKeeper、etcd、Consul 等服务发现组件的交互。</p>
<p>当 Provider 端暴露的 URL 发生变化时，ZooKeeper 等服务发现组件会通知 Consumer 端的 Registry 组件，Registry 组件会调用 notify() 方法，被通知的 Consumer 能匹配到所有 Provider 的 URL 列表并写入 properties 集合中。</p>
<p>下面我们来看 notify() 方法的核心实现：</p>
<pre><code>// 注意入参，第一个URL参数表示的是Consumer，第二个NotifyListener是第一个参数对应的监听器，第三个参数是Provider端暴露的URL的全量数据

protected void notify(URL url, NotifyListener listener,

    List&lt;URL&gt; urls) {

    ... // 省略一系列边界条件的检查

    Map&lt;String, List&lt;URL&gt;&gt; result = new HashMap&lt;&gt;();

    for (URL u : urls) {

        // 需要Consumer URL与Provider URL匹配，具体匹配规则后面详述

        if (UrlUtils.isMatch(url, u)) { 

            // 根据Provider URL中的category参数进行分类

            String category = u.getParameter(&quot;category&quot;, &quot;providers&quot;);

            List&lt;URL&gt; categoryList = result.computeIfAbsent(category, 

                k -&gt; new ArrayList&lt;&gt;());

            categoryList.add(u);

        }

    }

    if (result.size() == 0) {

        return;

    }

    Map&lt;String, List&lt;URL&gt;&gt; categoryNotified = 

      notified.computeIfAbsent(url, u -&gt; new ConcurrentHashMap&lt;&gt;());

    for (Map.Entry&lt;String, List&lt;URL&gt;&gt; entry : result.entrySet()) {

        String category = entry.getKey();

        List&lt;URL&gt; categoryList = entry.getValue();

        categoryNotified.put(category, categoryList); // 更新notified

        listener.notify(categoryList); // 调用NotifyListener

        // 更新properties集合以及底层的文件缓存

        saveProperties(url);

    }

}
</code></pre>
<p>在 saveProperties() 方法中会取出 Consumer 订阅的各个分类的 URL 连接起来（中间以空格分隔），然后以 Consumer 的 ServiceKey 为键值写到 properties 中，同时 lastCacheChanged 版本号会自增。完成 properties 字段的更新之后，会根据 syncSaveFile 字段值来决定是在当前线程同步更新 file 文件，还是向 registryCacheExecutor 线程池提交任务，异步完成 file 文件的同步。本地缓存文件的具体路径是：</p>
<pre><code>/.dubbo/dubbo-registry-[当前应用名]-[当前Registry所在的IP地址].cache
</code></pre>
<p>这里首先关注<strong>第一个细节：UrlUtils.isMatch() 方法</strong>。该方法会完成 Consumer URL 与 Provider URL 的匹配，依次匹配的部分如下所示：</p>
<ul>
<li>匹配 Consumer 和 Provider 的接口（优先取 interface 参数，其次再取 path）。双方接口相同或者其中一方为“*”，则匹配成功，执行下一步。</li>
<li>匹配 Consumer 和 Provider 的 category。</li>
<li>检测 Consumer URL 和 Provider URL 中的 enable 参数是否符合条件。</li>
<li>检测 Consumer 和 Provider 端的 group、version 以及 classifier 是否符合条件。</li>
</ul>
<p><strong>第二个细节是：URL.getServiceKey() 方法</strong>。该方法返回的 ServiceKey 是 properties 集合以及相应缓存文件中的 Key。ServiceKey 的格式如下：</p>
<pre><code>[group]/{interface(或path)}[:version]
</code></pre>
<p><strong>AbstractRegistry 的核心是本地文件缓存的功能。</strong> 在 AbstractRegistry 的构造方法中，会调用 loadProperties() 方法将上面写入的本地缓存文件，加载到 properties 对象中。</p>
<p>在网络抖动等原因而导致订阅失败时，Consumer 端的 Registry 就可以调用 getCacheUrls() 方法获取本地缓存，从而得到最近注册的 Provider URL。可见，<strong>AbstractRegistry 通过本地缓存提供了一种容错机制，保证了服务的可靠性</strong>。</p>
<h4>2. 注册/订阅</h4>
<p>AbstractRegistry 实现了 Registry 接口，它实现的 registry() 方法会将当前节点要注册的 URL 缓存到 registered 集合，而 unregistry() 方法会从 registered 集合删除指定的 URL，例如当前节点下线的时候。</p>
<p>subscribe() 方法会将当前节点作为 Consumer 的 URL 以及相关的 NotifyListener 记录到 subscribed 集合，unsubscribe() 方法会将当前节点的 URL 以及关联的 NotifyListener 从 subscribed 集合删除。</p>
<p>这四个方法都是简单的集合操作，这里我们就不再展示具体代码了。</p>
<p>单看 AbstractRegistry 的实现，上述四个基础的注册、订阅方法都是内存操作，但是 Java 有继承和多态的特性，AbstractRegistry 的子类会覆盖上述四个基础的注册、订阅方法进行增强。</p>
<p><img src="assets/Ciqc1F9W9-eAHUVPAACO6kbGAbU855.png" alt="Drawing 8.png" /></p>
<h4>3. 恢复/销毁</h4>
<p>AbstractRegistry 中还有另外两个需要关注的方法：<strong>recover() 方法</strong>和<strong>destroy() 方法</strong>。</p>
<p>在 Provider 因为网络问题与注册中心断开连接之后，会进行重连，重新连接成功之后，会调用 recover() 方法将 registered 集合中的全部 URL 重新走一遍 register() 方法，恢复注册数据。同样，recover() 方法也会将 subscribed 集合中的 URL 重新走一遍 subscribe() 方法，恢复订阅监听器。recover() 方法的具体实现比较简单，这里就不再展示，你若感兴趣的话，可以参考源码进行学习。</p>
<p>在当前节点下线的时候，会调用 Node.destroy() 方法释放底层资源。AbstractRegistry 实现的 destroy() 方法会调用 unregister() 方法和 unsubscribe() 方法将当前节点注册的 URL 以及订阅的监听全部清理掉，其中不会清理非动态注册的 URL（即 dynamic 参数明确指定为 false）。AbstractRegistry 中 destroy() 方法的实现比较简单，这里我们也不再展示，如果你感兴趣话，同样可以参考源码进行学习。</p>
<h3>总结</h3>
<p>本课时是 Dubbo 注册中心分析的第一个课时，我们首先介绍了注册中心在整个 Dubbo 架构中的位置，以及 Registry、 RegistryService、 RegistryFactory 等核心接口的功能。接下来我们还详细讲解了 AbstractRegistry 这个抽象类提供的公共能力，主要是从本地缓存、注册/订阅、恢复/销毁这三方面进行了分析。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;&#32;简易版&#32;RPC&#32;框架实现（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;&#32;重试机制是网络操作的基本保证.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f2e7d6b70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
