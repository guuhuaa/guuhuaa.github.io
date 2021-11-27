<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>26  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（上）.md</title>
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

                    <a class="current-tab" href="26&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（上）.md">26  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（上）.md</a>
                    

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
                        <div><h1>26  加餐：直击 Dubbo “心脏”，带你一起探秘 Invoker（上）</h1>
<p>在前面课时介绍 DubboProtocol 的时候我们看到，上层业务 Bean 会被封装成 Invoker 对象，然后传入 DubboProtocol.export() 方法中，该 Invoker 被封装成 DubboExporter，并保存到 exporterMap 集合中缓存。</p>
<p>在 DubboProtocol 暴露的 ProtocolServer 收到请求时，经过一系列解码处理，最终会到达 DubboProtocol.requestHandler 这个 ExchangeHandler 对象中，该 ExchangeHandler 对象会从 exporterMap 集合中取出请求的 Invoker，并调用其 invoke() 方法处理请求。</p>
<p>DubboProtocol.protocolBindingRefer() 方法则会将底层的 ExchangeClient 集合封装成 DubboInvoker，然后由上层逻辑封装成代理对象，这样业务层就可以像调用本地 Bean 一样，完成远程调用。</p>
<h3>深入 Invoker</h3>
<p>首先，我们来看 AbstractInvoker 这个抽象类，它继承了 Invoker 接口，继承关系如下图所示：</p>
<p><img src="assets/Ciqc1F-Oq-uAdi4nAABRchTw_kQ666.png" alt="Drawing 0.png" /></p>
<p>AbstractInvoker 继承关系示意图</p>
<p>从图中可以看到，最核心的 DubboInvoker 继承自AbstractInvoker 抽象类，AbstractInvoker 的核心字段有如下几个。</p>
<ul>
<li>type（Class<code>&lt;T&gt;</code> 类型）：该 Invoker 对象封装的业务接口类型，例如 Demo 示例中的 DemoService 接口。</li>
<li>url（URL 类型）：与当前 Invoker 关联的 URL 对象，其中包含了全部的配置信息。</li>
<li>attachment（Map&lt;String, Object&gt; 类型）：当前 Invoker 关联的一些附加信息，这些附加信息可以来自关联的 URL。在 AbstractInvoker 的构造函数的某个重载中，会调用 convertAttachment() 方法，其中就会从关联的 URL 对象获取指定的 KV 值记录到 attachment 集合中。</li>
<li>available（volatile boolean类型）、destroyed（AtomicBoolean 类型）：这两个字段用来控制当前 Invoker 的状态。available 默认值为 true，destroyed 默认值为 false。在 destroy() 方法中会将 available 设置为 false，将 destroyed 字段设置为 true。</li>
</ul>
<p>在 AbstractInvoker 中实现了 Invoker 接口中的 invoke() 方法，这里有点模板方法模式的感觉，其中先对 URL 中的配置信息以及 RpcContext 中携带的附加信息进行处理，添加到 Invocation 中作为附加信息，然后调用 doInvoke() 方法发起远程调用（该方法由 AbstractInvoker 的子类具体实现），最后得到 AsyncRpcResult 对象返回。</p>
<pre><code>public Result invoke(Invocation inv) throws RpcException {

    // 首先将传入的Invocation转换为RpcInvocation

    RpcInvocation invocation = (RpcInvocation) inv;

    invocation.setInvoker(this);

    // 将前文介绍的attachment集合添加为Invocation的附加信息

    if (CollectionUtils.isNotEmptyMap(attachment)) {

        invocation.addObjectAttachmentsIfAbsent(attachment);

    }

    // 将RpcContext的附加信息添加为Invocation的附加信息

    Map&lt;String, Object&gt; contextAttachments = RpcContext.getContext().getObjectAttachments();

    if (CollectionUtils.isNotEmptyMap(contextAttachments)) {

        invocation.addObjectAttachments(contextAttachments);

    }

    // 设置此次调用的模式，异步还是同步

    invocation.setInvokeMode(RpcUtils.getInvokeMode(url, invocation));

    // 如果是异步调用，给这次调用添加一个唯一ID

    RpcUtils.attachInvocationIdIfAsync(getUrl(), invocation);

    AsyncRpcResult asyncResult;

    try { // 调用子类实现的doInvoke()方法

        asyncResult = (AsyncRpcResult) doInvoke(invocation);

    } catch (InvocationTargetException e) {// 省略异常处理的逻辑

    } catch (RpcException e) { // 省略异常处理的逻辑

    } catch (Throwable e) {

        asyncResult = AsyncRpcResult.newDefaultAsyncResult(null, e, invocation);

    }

    RpcContext.getContext().setFuture(new FutureAdapter(asyncResult.getResponseFuture()));

    return asyncResult;

}
</code></pre>
<p>接下来，需要深入介绍的第一个类是 RpcContext。</p>
<h3>RpcContext</h3>
<p><strong>RpcContext 是线程级别的上下文信息</strong>，每个线程绑定一个 RpcContext 对象，底层依赖 ThreadLocal 实现。RpcContext 主要用于存储一个线程中一次请求的临时状态，当线程处理新的请求（Provider 端）或是线程发起新的请求（Consumer 端）时，RpcContext 中存储的内容就会更新。</p>
<p>下面来看 RpcContext 中两个<strong>InternalThreadLocal</strong>的核心字段，这两个字段的定义如下所示：</p>
<pre><code>// 在发起请求时，会使用该RpcContext来存储上下文信息

private static final InternalThreadLocal&lt;RpcContext&gt; LOCAL = new InternalThreadLocal&lt;RpcContext&gt;() {

    @Override

    protected RpcContext initialValue() {

        return new RpcContext();

    }

};

// 在接收到响应的时候，会使用该RpcContext来存储上下文信息

private static final InternalThreadLocal&lt;RpcContext&gt; SERVER_LOCAL = ...
</code></pre>
<p>JDK 提供的 ThreadLocal 底层实现大致如下：对于不同线程创建对应的 ThreadLocalMap，用于存放线程绑定信息，当用户调用<strong>ThreadLocal.get() 方法</strong>获取变量时，底层会先获取当前线程 Thread，然后获取绑定到当前线程 Thread 的 ThreadLocalMap，最后将当前 ThreadLocal 对象作为 Key 去 ThreadLocalMap 表中获取线程绑定的数据。<strong>ThreadLocal.set() 方法</strong>的逻辑与之类似，首先会获取绑定到当前线程的 ThreadLocalMap，然后将 ThreadLocal 实例作为 Key、待存储的数据作为 Value 存储到 ThreadLocalMap 中。</p>
<p>Dubbo 的 InternalThreadLocal 与 JDK 提供的 ThreadLocal 功能类似，只是底层实现略有不同，其底层的 InternalThreadLocalMap 采用数组结构存储数据，直接通过 index 获取变量，相较于 Map 方式计算 hash 值的性能更好。</p>
<p>这里我们来介绍一下 dubbo-common 模块中的 InternalThread 这个类，它继承了 Thread 类，Dubbo 的线程工厂 NamedInternalThreadFactory 创建的线程类其实都是 InternalThread 实例对象，你可以回顾前面第 19 课时介绍的 ThreadPool 接口实现，它们都是通过 NamedInternalThreadFactory 这个工厂类来创建线程的。</p>
<p>InternalThread 中主要提供了 setThreadLocalMap() 和 threadLocalMap() 两个方法，用于设置和获取 InternalThreadLocalMap。InternalThreadLocalMap 中的核心字段有如下四个。</p>
<ul>
<li>indexedVariables（Object[] 类型）：用于存储绑定到当前线程的数据。</li>
<li>NEXT_INDEX（AtomicInteger 类型）：自增索引，用于计算下次存储到 indexedVariables 数组中的位置，这是一个静态字段。</li>
<li>slowThreadLocalMap（ThreadLocal<code>&lt;InternalThreadLocalMap&gt;</code> 类型）：当使用原生 Thread 的时候，会使用该 ThreadLocal 存储 InternalThreadLocalMap，这是一个降级策略。</li>
<li>UNSET（Object 类型）：当一个与线程绑定的值被删除之后，会被设置为 UNSET 值。</li>
</ul>
<p>在 InternalThreadLocalMap 中获取当前线程绑定的InternalThreadLocaMap的静态方法，都会与 slowThreadLocalMap 字段配合实现降级，也就是说，如果当前线程为原生 Thread 类型，则根据 slowThreadLocalMap 获取InternalThreadLocalMap。这里我们以 getIfSet() 方法为例：</p>
<pre><code>public static InternalThreadLocalMap getIfSet() {

    Thread thread = Thread.currentThread(); // 获取当前线程

    if (thread instanceof InternalThread) { // 判断当前线程的类型

        // 如果是InternalThread类型，直接获取InternalThreadLocalMap返回

        return ((InternalThread) thread).threadLocalMap();

    }

    // 原生Thread则需要通过ThreadLocal获取InternalThreadLocalMap

    return slowThreadLocalMap.get(); 

}
</code></pre>
<p>InternalThreadLocalMap 中的 get()、remove()、set() 等方法都有类似的降级操作，这里不再一一重复。</p>
<p>在拿到 InternalThreadLocalMap 对象之后，我们就可以调用其 setIndexedVariable() 方法和 indexedVariable() 方法读写，这里我们得结合InternalThreadLocal进行讲解。在 InternalThreadLocal 的构造方法中，会使用 InternalThreadLocalMap.NEXT_INDEX 初始化其 index 字段（int 类型），在 InternalThreadLocal.set() 方法中就会将传入的数据存储到 InternalThreadLocalMap.indexedVariables 集合中，具体的下标位置就是这里的 index 字段值：</p>
<pre><code>public final void set(V value) {

    if (value == null|| value == InternalThreadLocalMap.UNSET）{

        remove(); // 如果要存储的值为null或是UNSERT，则直接清除

    } else {

        // 获取当前线程绑定的InternalThreadLocalMap

        InternalThreadLocalMap threadLocalMap = InternalThreadLocalMap.get();

        // 将value存储到InternalThreadLocalMap.indexedVariables集合中

        if (threadLocalMap.setIndexedVariable(index, value)) {

            // 将当前InternalThreadLocal记录到待删除集合中

            addToVariablesToRemove(threadLocalMap, this);

        }

    }

}
</code></pre>
<p>InternalThreadLocal 的静态变量 VARIABLES_TO_REMOVE_INDEX 是调用InternalThreadLocalMap 的 nextVariableIndex 方法得到的一个索引值，在 InternalThreadLocalMap 数组的对应位置保存的是 Set<code>&lt;InternalThreadLocal&gt;</code> 类型的集合，也就是上面提到的“待删除集合”，即绑定到当前线程所有的 InternalThreadLocal，这样就可以方便管理对象及内存的释放。</p>
<p>接下来我们继续看 InternalThreadLocalMap.setIndexedVariable() 方法的实现：</p>
<pre><code>public boolean setIndexedVariable(int index, Object value) {

    Object[] lookup = indexedVariables;

    if (index &lt; lookup.length) { // 将value存储到index指定的位置

        Object oldValue = lookup[index];

        lookup[index] = value;

        return oldValue == UNSET; 

    } else {

        // 当index超过indexedVariables数组的长度时，需要对indexedVariables数组进行扩容

        expandIndexedVariableTableAndSet(index, value);

        return true;

    }

}
</code></pre>
<p>明确了设置 InternalThreadLocal 变量的流程之后，我们再来分析读取 InternalThreadLocal 变量的流程，入口在 InternalThreadLocal 的 get() 方法。</p>
<pre><code>public final V get() {

    // 获取当前线程绑定的InternalThreadLocalMap

    InternalThreadLocalMap threadLocalMap = InternalThreadLocalMap.get();

    // 根据当前InternalThreadLocal对象的index字段，从InternalThreadLocalMap中读取相应的数据

    Object v = threadLocalMap.indexedVariable(index);

    if (v != InternalThreadLocalMap.UNSET) {

        return (V) v; // 如果非UNSET，则表示读取到了有效数据，直接返回

    }

    // 读取到UNSET值，则会调用initialize()方法进行初始化，其中首先会调用initialValue()方法进行初始化，然后会调用前面介绍的setIndexedVariable()方法和addToVariablesToRemove()方法存储初始化得到的值

    return initialize(threadLocalMap);

}
</code></pre>
<p>我们可以看到，在 RpcContext 中，LOCAL 和 SERVER_LOCAL 两个 InternalThreadLocal 类型的字段都实现了 initialValue() 方法，它们的实现都是创建并返回 RpcContext 对象。</p>
<p>理解了 InternalThreadLocal 的底层原理之后，我们回到 RpcContext 继续分析。RpcContext 作为调用的上下文信息，可以记录非常多的信息，下面介绍其中的一些核心字段。</p>
<ul>
<li>attachments（Map&lt;String, Object&gt; 类型）：可用于记录调用上下文的附加信息，这些信息会被添加到 Invocation 中，并传递到远端节点。</li>
<li>values（Map&lt;String, Object&gt; 类型）：用来记录上下文的键值对信息，但是不会被传递到远端节点。</li>
<li>methodName、parameterTypes、arguments：分别用来记录调用的方法名、参数类型列表以及具体的参数列表，与相关 Invocation 对象中的信息一致。</li>
<li>localAddress、remoteAddress（InetSocketAddress 类型）：记录了自己和远端的地址。</li>
<li>request、response（Object 类型）：可用于记录底层关联的请求和响应。</li>
<li>asyncContext（AsyncContext 类型）：异步Context，其中可以存储异步调用相关的 RpcContext 以及异步请求相关的 Future。</li>
</ul>
<h3>DubboInvoker</h3>
<p>通过前面对 DubboProtocol 的分析我们知道，protocolBindingRefer() 方法会根据调用的业务接口类型以及 URL 创建底层的 ExchangeClient 集合，然后封装成 DubboInvoker 对象返回。DubboInvoker 是 AbstractInvoker 的实现类，在其 doInvoke() 方法中首先会选择此次调用使用 ExchangeClient 对象，然后确定此次调用是否需要返回值，最后调用 ExchangeClient.request() 方法发送请求，对返回的 Future 进行简单封装并返回。</p>
<pre><code>protected Result doInvoke(final Invocation invocation) throws Throwable {

    RpcInvocation inv = (RpcInvocation) invocation;

    // 此次调用的方法名称

    final String methodName = RpcUtils.getMethodName(invocation);

    // 向Invocation中添加附加信息，这里将URL的path和version添加到附加信息中

    inv.setAttachment(PATH_KEY, getUrl().getPath());

    inv.setAttachment(VERSION_KEY, version);

    ExchangeClient currentClient; // 选择一个ExchangeClient实例

    if (clients.length == 1) {

        currentClient = clients[0];

    } else {

        currentClient = clients[index.getAndIncrement() % clients.length];

    }

    boolean isOneway = RpcUtils.isOneway(getUrl(), invocation);

    // 根据调用的方法名称和配置计算此次调用的超时时间

    int timeout = calculateTimeout(invocation, methodName); 

    if (isOneway) { // 不需要关注返回值的请求

        boolean isSent = getUrl().getMethodParameter(methodName, Constants.SENT_KEY, false);

        currentClient.send(inv, isSent);

        return AsyncRpcResult.newDefaultAsyncResult(invocation);

    } else { // 需要关注返回值的请求

        // 获取处理响应的线程池，对于同步请求，会使用ThreadlessExecutor，ThreadlessExecutor的原理前面已经分析过了，这里不再赘述；对于异步请求，则会使用共享的线程池，ExecutorRepository接口的相关设计和实现在前面已经详细分析过了，这里不再重复。

        ExecutorService executor = getCallbackExecutor(getUrl(), inv);

        // 使用上面选出的ExchangeClient执行request()方法，将请求发送出去

        CompletableFuture&lt;AppResponse&gt; appResponseFuture =

                currentClient.request(inv, timeout, executor).thenApply(obj -&gt; (AppResponse) obj);

        // 这里将AppResponse封装成AsyncRpcResult返回

        AsyncRpcResult result = new AsyncRpcResult(appResponseFuture, inv);

        result.setExecutor(executor);

        return result;

    }

}
</code></pre>
<p>在 DubboInvoker.invoke() 方法中有一些细节需要关注一下。首先是根据 URL 以及 Invocation 中的配置，决定此次调用是否为<strong>oneway 调用方式</strong>。</p>
<pre><code>public static boolean isOneway(URL url, Invocation inv) {

    boolean isOneway;

    if (Boolean.FALSE.toString().equals(inv.getAttachment(RETURN_KEY))) {

        isOneway = true; // 首先关注的是Invocation中&quot;return&quot;这个附加属性

    } else {

        isOneway = !url.getMethodParameter(getMethodName(inv), RETURN_KEY, true); // 之后关注URL中，调用方法对应的&quot;return&quot;配置

    }

    return isOneway;

}
</code></pre>
<p>oneway 指的是客户端发送消息后，不需要得到响应。所以，对于那些不关心服务端响应的请求，就比较适合使用 oneway 通信，如下图所示：</p>
<p><img src="assets/CgqCHl-SkLWAaPzTAACgt5rmWHg530.png" alt="Lark20201023-161312.png" /></p>
<p>oneway 和 twoway 通信方式对比图</p>
<p>可以看到发送 oneway 请求的方式是send() 方法，而后面发送 twoway 请求的方式是 request() 方法。通过之前的分析我们知道，request() 方法会相应地创建 DefaultFuture 对象以及检测超时的定时任务，而 send() 方法则不会创建这些东西，它是直接将 Invocation 包装成 oneway 类型的 Request 发送出去。</p>
<p>在服务端的 HeaderExchangeHandler.receive() 方法中，会针对 oneway 请求和 twoway 请求执行不同的分支处理：twoway 请求由 handleRequest() 方法进行处理，其中会关注调用结果并形成 Response 返回给客户端；oneway 请求则直接交给上层的 DubboProtocol.requestHandler，完成方法调用之后，不会返回任何 Response。</p>
<p>我们就结合如下示例代码来简单说明一下 HeaderExchangeHandler.request() 方法中的相关片段。</p>
<pre><code>public void received(Channel channel, Object message) throws RemotingException {

    final ExchangeChannel exchangeChannel = HeaderExchangeChannel.getOrAddChannel(channel);

    if (message instanceof Request) {

        if (request.isTwoWay()) {

            handleRequest(exchangeChannel, request);

        } else {

            handler.received(exchangeChannel, request.getData());

        }

    } else ... // 省略其他分支的展示

}
</code></pre>
<h3>总结</h3>
<p>本课时我们重点介绍了 Dubbo 最核心的接口—— Invoker。首先，我们介绍了 AbstractInvoker 抽象类提供的公共能力；然后分析了 RpcContext 的功能和涉及的组件，例如，InternalThreadLocal、InternalThreadLocalMap 等；最后我们说明了 DubboInvoker 对 doinvoke() 方法的实现，并区分了 oneway 和 twoway 两种类型的请求。</p>
<p>下一课时，我们将继续介绍 DubboInvoker 的实现。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="25&#32;&#32;从&#32;Protocol&#32;起手，看服务暴露和服务引用的全流程（下）.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="27&#32;&#32;加餐：直击&#32;Dubbo&#32;“心脏”，带你一起探秘&#32;Invoker（下）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b433f786bfa70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
